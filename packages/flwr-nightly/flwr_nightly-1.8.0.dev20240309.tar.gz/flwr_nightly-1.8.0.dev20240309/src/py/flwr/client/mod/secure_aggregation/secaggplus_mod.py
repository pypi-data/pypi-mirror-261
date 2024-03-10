# Copyright 2024 Flower Labs GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Message handler for the SecAgg+ protocol."""


import os
from dataclasses import dataclass, field
from logging import INFO, WARNING
from typing import Any, Callable, Dict, List, Tuple, cast

from flwr.client.typing import ClientAppCallable
from flwr.common import (
    ConfigsRecord,
    Context,
    Message,
    RecordSet,
    ndarray_to_bytes,
    parameters_to_ndarrays,
)
from flwr.common import recordset_compat as compat
from flwr.common.constant import MessageType
from flwr.common.logger import log
from flwr.common.secure_aggregation.crypto.shamir import create_shares
from flwr.common.secure_aggregation.crypto.symmetric_encryption import (
    bytes_to_private_key,
    bytes_to_public_key,
    decrypt,
    encrypt,
    generate_key_pairs,
    generate_shared_key,
    private_key_to_bytes,
    public_key_to_bytes,
)
from flwr.common.secure_aggregation.ndarrays_arithmetic import (
    factor_combine,
    parameters_addition,
    parameters_mod,
    parameters_multiply,
    parameters_subtraction,
)
from flwr.common.secure_aggregation.quantization import quantize
from flwr.common.secure_aggregation.secaggplus_constants import (
    RECORD_KEY_CONFIGS,
    RECORD_KEY_STATE,
    Key,
    Stage,
)
from flwr.common.secure_aggregation.secaggplus_utils import (
    pseudo_rand_gen,
    share_keys_plaintext_concat,
    share_keys_plaintext_separate,
)
from flwr.common.typing import ConfigsRecordValues, FitRes


@dataclass
# pylint: disable-next=too-many-instance-attributes
class SecAggPlusState:
    """State of the SecAgg+ protocol."""

    current_stage: str = Stage.UNMASK

    sid: int = 0
    sample_num: int = 0
    share_num: int = 0
    threshold: int = 0
    clipping_range: float = 0.0
    target_range: int = 0
    mod_range: int = 0

    # Secret key (sk) and public key (pk)
    sk1: bytes = b""
    pk1: bytes = b""
    sk2: bytes = b""
    pk2: bytes = b""

    # Random seed for generating the private mask
    rd_seed: bytes = b""

    rd_seed_share_dict: Dict[int, bytes] = field(default_factory=dict)
    sk1_share_dict: Dict[int, bytes] = field(default_factory=dict)
    # The dict of the shared secrets from sk2
    ss2_dict: Dict[int, bytes] = field(default_factory=dict)
    public_keys_dict: Dict[int, Tuple[bytes, bytes]] = field(default_factory=dict)

    def __init__(self, **kwargs: ConfigsRecordValues) -> None:
        for k, v in kwargs.items():
            if k.endswith(":V"):
                continue
            new_v: Any = v
            if k.endswith(":K"):
                k = k[:-2]
                keys = cast(List[int], v)
                values = cast(List[bytes], kwargs[f"{k}:V"])
                if len(values) > len(keys):
                    updated_values = [
                        tuple(values[i : i + 2]) for i in range(0, len(values), 2)
                    ]
                    new_v = dict(zip(keys, updated_values))
                else:
                    new_v = dict(zip(keys, values))
            self.__setattr__(k, new_v)

    def to_dict(self) -> Dict[str, ConfigsRecordValues]:
        """Convert the state to a dictionary."""
        ret = vars(self)
        for k in list(ret.keys()):
            if isinstance(ret[k], dict):
                # Replace dict with two lists
                v = cast(Dict[str, Any], ret.pop(k))
                ret[f"{k}:K"] = list(v.keys())
                if k == "public_keys_dict":
                    v_list: List[bytes] = []
                    for b1_b2 in cast(List[Tuple[bytes, bytes]], v.values()):
                        v_list.extend(b1_b2)
                    ret[f"{k}:V"] = v_list
                else:
                    ret[f"{k}:V"] = list(v.values())
        return ret


def _get_fit_fn(
    msg: Message, ctxt: Context, call_next: ClientAppCallable
) -> Callable[[], FitRes]:
    """Get the fit function."""

    def fit() -> FitRes:
        out_msg = call_next(msg, ctxt)
        return compat.recordset_to_fitres(out_msg.content, keep_input=False)

    return fit


def secaggplus_mod(
    msg: Message,
    ctxt: Context,
    call_next: ClientAppCallable,
) -> Message:
    """Handle incoming message and return results, following the SecAgg+ protocol."""
    # Ignore non-fit messages
    if msg.metadata.message_type != MessageType.TRAIN:
        return call_next(msg, ctxt)

    # Retrieve local state
    if RECORD_KEY_STATE not in ctxt.state.configs_records:
        ctxt.state.configs_records[RECORD_KEY_STATE] = ConfigsRecord({})
    state_dict = ctxt.state.configs_records[RECORD_KEY_STATE]
    state = SecAggPlusState(**state_dict)

    # Retrieve incoming configs
    configs = msg.content.configs_records[RECORD_KEY_CONFIGS]

    # Check the validity of the next stage
    check_stage(state.current_stage, configs)

    # Update the current stage
    state.current_stage = cast(str, configs.pop(Key.STAGE))

    # Check the validity of the configs based on the current stage
    check_configs(state.current_stage, configs)

    # Execute
    if state.current_stage == Stage.SETUP:
        res = _setup(state, configs)
    elif state.current_stage == Stage.SHARE_KEYS:
        res = _share_keys(state, configs)
    elif state.current_stage == Stage.COLLECT_MASKED_INPUT:
        fit = _get_fit_fn(msg, ctxt, call_next)
        res = _collect_masked_input(state, configs, fit)
    elif state.current_stage == Stage.UNMASK:
        res = _unmask(state, configs)
    else:
        raise ValueError(f"Unknown secagg stage: {state.current_stage}")

    # Save state
    ctxt.state.configs_records[RECORD_KEY_STATE] = ConfigsRecord(state.to_dict())

    # Return message
    content = RecordSet(configs_records={RECORD_KEY_CONFIGS: ConfigsRecord(res, False)})
    return msg.create_reply(content, ttl="")


def check_stage(current_stage: str, configs: ConfigsRecord) -> None:
    """Check the validity of the next stage."""
    # Check the existence of Config.STAGE
    if Key.STAGE not in configs:
        raise KeyError(
            f"The required key '{Key.STAGE}' is missing from the input `named_values`."
        )

    # Check the value type of the Config.STAGE
    next_stage = configs[Key.STAGE]
    if not isinstance(next_stage, str):
        raise TypeError(
            f"The value for the key '{Key.STAGE}' must be of type {str}, "
            f"but got {type(next_stage)} instead."
        )

    # Check the validity of the next stage
    if next_stage == Stage.SETUP:
        if current_stage != Stage.UNMASK:
            log(WARNING, "Restart from the setup stage")
    # If stage is not "setup",
    # the stage from `named_values` should be the expected next stage
    else:
        stages = Stage.all()
        expected_next_stage = stages[(stages.index(current_stage) + 1) % len(stages)]
        if next_stage != expected_next_stage:
            raise ValueError(
                "Abort secure aggregation: "
                f"expect {expected_next_stage} stage, but receive {next_stage} stage"
            )


# pylint: disable-next=too-many-branches
def check_configs(stage: str, configs: ConfigsRecord) -> None:
    """Check the validity of the configs."""
    # Check `named_values` for the setup stage
    if stage == Stage.SETUP:
        key_type_pairs = [
            (Key.SAMPLE_NUMBER, int),
            (Key.SECURE_ID, int),
            (Key.SHARE_NUMBER, int),
            (Key.THRESHOLD, int),
            (Key.CLIPPING_RANGE, float),
            (Key.TARGET_RANGE, int),
            (Key.MOD_RANGE, int),
        ]
        for key, expected_type in key_type_pairs:
            if key not in configs:
                raise KeyError(
                    f"Stage {Stage.SETUP}: the required key '{key}' is "
                    "missing from the input `named_values`."
                )
            # Bool is a subclass of int in Python,
            # so `isinstance(v, int)` will return True even if v is a boolean.
            # pylint: disable-next=unidiomatic-typecheck
            if type(configs[key]) is not expected_type:
                raise TypeError(
                    f"Stage {Stage.SETUP}: The value for the key '{key}' "
                    f"must be of type {expected_type}, "
                    f"but got {type(configs[key])} instead."
                )
    elif stage == Stage.SHARE_KEYS:
        for key, value in configs.items():
            if (
                not isinstance(value, list)
                or len(value) != 2
                or not isinstance(value[0], bytes)
                or not isinstance(value[1], bytes)
            ):
                raise TypeError(
                    f"Stage {Stage.SHARE_KEYS}: "
                    f"the value for the key '{key}' must be a list of two bytes."
                )
    elif stage == Stage.COLLECT_MASKED_INPUT:
        key_type_pairs = [
            (Key.CIPHERTEXT_LIST, bytes),
            (Key.SOURCE_LIST, int),
        ]
        for key, expected_type in key_type_pairs:
            if key not in configs:
                raise KeyError(
                    f"Stage {Stage.COLLECT_MASKED_INPUT}: "
                    f"the required key '{key}' is "
                    "missing from the input `named_values`."
                )
            if not isinstance(configs[key], list) or any(
                elm
                for elm in cast(List[Any], configs[key])
                # pylint: disable-next=unidiomatic-typecheck
                if type(elm) is not expected_type
            ):
                raise TypeError(
                    f"Stage {Stage.COLLECT_MASKED_INPUT}: "
                    f"the value for the key '{key}' "
                    f"must be of type List[{expected_type.__name__}]"
                )
    elif stage == Stage.UNMASK:
        key_type_pairs = [
            (Key.ACTIVE_SECURE_ID_LIST, int),
            (Key.DEAD_SECURE_ID_LIST, int),
        ]
        for key, expected_type in key_type_pairs:
            if key not in configs:
                raise KeyError(
                    f"Stage {Stage.UNMASK}: "
                    f"the required key '{key}' is "
                    "missing from the input `named_values`."
                )
            if not isinstance(configs[key], list) or any(
                elm
                for elm in cast(List[Any], configs[key])
                # pylint: disable-next=unidiomatic-typecheck
                if type(elm) is not expected_type
            ):
                raise TypeError(
                    f"Stage {Stage.UNMASK}: "
                    f"the value for the key '{key}' "
                    f"must be of type List[{expected_type.__name__}]"
                )
    else:
        raise ValueError(f"Unknown secagg stage: {stage}")


def _setup(
    state: SecAggPlusState, configs: ConfigsRecord
) -> Dict[str, ConfigsRecordValues]:
    # Assigning parameter values to object fields
    sec_agg_param_dict = configs
    state.sample_num = cast(int, sec_agg_param_dict[Key.SAMPLE_NUMBER])
    state.sid = cast(int, sec_agg_param_dict[Key.SECURE_ID])
    log(INFO, "Client %d: starting stage 0...", state.sid)

    state.share_num = cast(int, sec_agg_param_dict[Key.SHARE_NUMBER])
    state.threshold = cast(int, sec_agg_param_dict[Key.THRESHOLD])
    state.clipping_range = cast(float, sec_agg_param_dict[Key.CLIPPING_RANGE])
    state.target_range = cast(int, sec_agg_param_dict[Key.TARGET_RANGE])
    state.mod_range = cast(int, sec_agg_param_dict[Key.MOD_RANGE])

    # Dictionaries containing client secure IDs as keys
    # and their respective secret shares as values.
    state.rd_seed_share_dict = {}
    state.sk1_share_dict = {}
    # Dictionary containing client secure IDs as keys
    # and their respective shared secrets (with this client) as values.
    state.ss2_dict = {}

    # Create 2 sets private public key pairs
    # One for creating pairwise masks
    # One for encrypting message to distribute shares
    sk1, pk1 = generate_key_pairs()
    sk2, pk2 = generate_key_pairs()

    state.sk1, state.pk1 = private_key_to_bytes(sk1), public_key_to_bytes(pk1)
    state.sk2, state.pk2 = private_key_to_bytes(sk2), public_key_to_bytes(pk2)
    log(INFO, "Client %d: stage 0 completes. uploading public keys...", state.sid)
    return {Key.PUBLIC_KEY_1: state.pk1, Key.PUBLIC_KEY_2: state.pk2}


# pylint: disable-next=too-many-locals
def _share_keys(
    state: SecAggPlusState, configs: ConfigsRecord
) -> Dict[str, ConfigsRecordValues]:
    named_bytes_tuples = cast(Dict[str, Tuple[bytes, bytes]], configs)
    key_dict = {int(sid): (pk1, pk2) for sid, (pk1, pk2) in named_bytes_tuples.items()}
    log(INFO, "Client %d: starting stage 1...", state.sid)
    state.public_keys_dict = key_dict

    # Check if the size is larger than threshold
    if len(state.public_keys_dict) < state.threshold:
        raise ValueError("Available neighbours number smaller than threshold")

    # Check if all public keys are unique
    pk_list: List[bytes] = []
    for pk1, pk2 in state.public_keys_dict.values():
        pk_list.append(pk1)
        pk_list.append(pk2)
    if len(set(pk_list)) != len(pk_list):
        raise ValueError("Some public keys are identical")

    # Check if public keys of this client are correct in the dictionary
    if (
        state.public_keys_dict[state.sid][0] != state.pk1
        or state.public_keys_dict[state.sid][1] != state.pk2
    ):
        raise ValueError(
            "Own public keys are displayed in dict incorrectly, should not happen!"
        )

    # Generate the private mask seed
    state.rd_seed = os.urandom(32)

    # Create shares for the private mask seed and the first private key
    b_shares = create_shares(state.rd_seed, state.threshold, state.share_num)
    sk1_shares = create_shares(state.sk1, state.threshold, state.share_num)

    srcs, dsts, ciphertexts = [], [], []

    # Distribute shares
    for idx, (sid, (_, pk2)) in enumerate(state.public_keys_dict.items()):
        if sid == state.sid:
            state.rd_seed_share_dict[state.sid] = b_shares[idx]
            state.sk1_share_dict[state.sid] = sk1_shares[idx]
        else:
            shared_key = generate_shared_key(
                bytes_to_private_key(state.sk2),
                bytes_to_public_key(pk2),
            )
            state.ss2_dict[sid] = shared_key
            plaintext = share_keys_plaintext_concat(
                state.sid, sid, b_shares[idx], sk1_shares[idx]
            )
            ciphertext = encrypt(shared_key, plaintext)
            srcs.append(state.sid)
            dsts.append(sid)
            ciphertexts.append(ciphertext)

    log(INFO, "Client %d: stage 1 completes. uploading key shares...", state.sid)
    return {Key.DESTINATION_LIST: dsts, Key.CIPHERTEXT_LIST: ciphertexts}


# pylint: disable-next=too-many-locals
def _collect_masked_input(
    state: SecAggPlusState,
    configs: ConfigsRecord,
    fit: Callable[[], FitRes],
) -> Dict[str, ConfigsRecordValues]:
    log(INFO, "Client %d: starting stage 2...", state.sid)
    available_clients: List[int] = []
    ciphertexts = cast(List[bytes], configs[Key.CIPHERTEXT_LIST])
    srcs = cast(List[int], configs[Key.SOURCE_LIST])
    if len(ciphertexts) + 1 < state.threshold:
        raise ValueError("Not enough available neighbour clients.")

    # Decrypt ciphertexts, verify their sources, and store shares.
    for src, ciphertext in zip(srcs, ciphertexts):
        shared_key = state.ss2_dict[src]
        plaintext = decrypt(shared_key, ciphertext)
        actual_src, dst, rd_seed_share, sk1_share = share_keys_plaintext_separate(
            plaintext
        )
        available_clients.append(src)
        if src != actual_src:
            raise ValueError(
                f"Client {state.sid}: received ciphertext "
                f"from {actual_src} instead of {src}."
            )
        if dst != state.sid:
            raise ValueError(
                f"Client {state.sid}: received an encrypted message"
                f"for Client {dst} from Client {src}."
            )
        state.rd_seed_share_dict[src] = rd_seed_share
        state.sk1_share_dict[src] = sk1_share

    # Fit client
    fit_res = fit()
    parameters_factor = fit_res.num_examples
    parameters = parameters_to_ndarrays(fit_res.parameters)

    # Quantize parameter update (vector)
    quantized_parameters = quantize(
        parameters, state.clipping_range, state.target_range
    )

    quantized_parameters = parameters_multiply(quantized_parameters, parameters_factor)
    quantized_parameters = factor_combine(parameters_factor, quantized_parameters)

    dimensions_list: List[Tuple[int, ...]] = [a.shape for a in quantized_parameters]

    # Add private mask
    private_mask = pseudo_rand_gen(state.rd_seed, state.mod_range, dimensions_list)
    quantized_parameters = parameters_addition(quantized_parameters, private_mask)

    for client_id in available_clients:
        # Add pairwise masks
        shared_key = generate_shared_key(
            bytes_to_private_key(state.sk1),
            bytes_to_public_key(state.public_keys_dict[client_id][0]),
        )
        pairwise_mask = pseudo_rand_gen(shared_key, state.mod_range, dimensions_list)
        if state.sid > client_id:
            quantized_parameters = parameters_addition(
                quantized_parameters, pairwise_mask
            )
        else:
            quantized_parameters = parameters_subtraction(
                quantized_parameters, pairwise_mask
            )

    # Take mod of final weight update vector and return to server
    quantized_parameters = parameters_mod(quantized_parameters, state.mod_range)
    log(INFO, "Client %d: stage 2 completes. uploading masked parameters...", state.sid)
    return {
        Key.MASKED_PARAMETERS: [ndarray_to_bytes(arr) for arr in quantized_parameters]
    }


def _unmask(
    state: SecAggPlusState, configs: ConfigsRecord
) -> Dict[str, ConfigsRecordValues]:
    log(INFO, "Client %d: starting stage 3...", state.sid)

    active_sids = cast(List[int], configs[Key.ACTIVE_SECURE_ID_LIST])
    dead_sids = cast(List[int], configs[Key.DEAD_SECURE_ID_LIST])
    # Send private mask seed share for every avaliable client (including itclient)
    # Send first private key share for building pairwise mask for every dropped client
    if len(active_sids) < state.threshold:
        raise ValueError("Available neighbours number smaller than threshold")

    sids, shares = [], []
    sids += active_sids
    shares += [state.rd_seed_share_dict[sid] for sid in active_sids]
    sids += dead_sids
    shares += [state.sk1_share_dict[sid] for sid in dead_sids]

    log(INFO, "Client %d: stage 3 completes. uploading key shares...", state.sid)
    return {Key.SECURE_ID_LIST: sids, Key.SHARE_LIST: shares}
