from __future__ import annotations
from ....fable_modules.fable_library.option import default_arg
from ....fable_modules.fable_library.result import FSharpResult_2
from ....fable_modules.fable_library.string_ import (to_text, printf)
from ....fable_modules.fable_library.types import to_string
from ....fable_modules.thoth_json_core.decode import (and_then, succeed, string)
from ....fable_modules.thoth_json_core.types import (Json, Decoder_1)
from ....fable_modules.thoth_json_python.decode import Decode_fromString
from ....fable_modules.thoth_json_python.encode import to_string as to_string_1
from ...ISA.ArcTypes.composite_header import IOType

def IOType_encoder(io: IOType) -> Json:
    return Json(0, to_string(io))


def cb(s: str) -> Decoder_1[IOType]:
    return succeed(IOType.of_string(s))


IOType_decoder: Decoder_1[IOType] = and_then(cb, string)

def ARCtrl_ISA_IOType__IOType_fromJsonString_Static_Z721C83C5(json_string: str) -> IOType:
    match_value: FSharpResult_2[IOType, str] = Decode_fromString(IOType_decoder, json_string)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def ARCtrl_ISA_IOType__IOType_ToJsonString_71136F3F(this: IOType, spaces: int | None=None) -> str:
    return to_string_1(default_arg(spaces, 0), IOType_encoder(this))


def ARCtrl_ISA_IOType__IOType_toJsonString_Static_Z359DBB26(a: IOType) -> str:
    return ARCtrl_ISA_IOType__IOType_ToJsonString_71136F3F(a)


__all__ = ["IOType_encoder", "IOType_decoder", "ARCtrl_ISA_IOType__IOType_fromJsonString_Static_Z721C83C5", "ARCtrl_ISA_IOType__IOType_ToJsonString_71136F3F", "ARCtrl_ISA_IOType__IOType_toJsonString_Static_Z359DBB26"]

