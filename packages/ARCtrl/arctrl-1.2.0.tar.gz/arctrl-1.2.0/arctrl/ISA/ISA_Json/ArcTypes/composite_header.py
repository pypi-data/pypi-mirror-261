from __future__ import annotations
from collections.abc import Callable
from typing import Any
from ....fable_modules.fable_library.list import (singleton, empty, FSharpList)
from ....fable_modules.fable_library.option import default_arg
from ....fable_modules.fable_library.result import FSharpResult_2
from ....fable_modules.fable_library.string_ import (to_text, printf)
from ....fable_modules.fable_library.util import to_enumerable
from ....fable_modules.thoth_json_core.decode import (object, IRequiredGetter, string, index, IGetters)
from ....fable_modules.thoth_json_core.encode import list_1
from ....fable_modules.thoth_json_core.types import (Json, Decoder_1)
from ....fable_modules.thoth_json_python.decode import Decode_fromString
from ....fable_modules.thoth_json_python.encode import to_string
from ...ISA.ArcTypes.composite_header import (CompositeHeader, IOType)
from ...ISA.JsonTypes.ontology_annotation import OntologyAnnotation
from ...ISA_Json.converter_options import ConverterOptions__ctor
from ...ISA_Json.ontology import (OntologyAnnotation_encoder, OntologyAnnotation_decoder)
from ...ISA_Json.ArcTypes.iotype import (IOType_encoder, IOType_decoder)

def CompositeHeader_encoder(ch: CompositeHeader) -> Json:
    def oa_to_json_string(oa: OntologyAnnotation, ch: Any=ch) -> Json:
        return OntologyAnnotation_encoder(ConverterOptions__ctor(), oa)

    pattern_input: tuple[str, FSharpList[Json]] = (("Parameter", singleton(oa_to_json_string(ch.fields[0])))) if (ch.tag == 3) else ((("Factor", singleton(oa_to_json_string(ch.fields[0])))) if (ch.tag == 2) else ((("Characteristic", singleton(oa_to_json_string(ch.fields[0])))) if (ch.tag == 1) else ((("Component", singleton(oa_to_json_string(ch.fields[0])))) if (ch.tag == 0) else ((("ProtocolType", empty())) if (ch.tag == 4) else ((("ProtocolREF", empty())) if (ch.tag == 8) else ((("ProtocolDescription", empty())) if (ch.tag == 5) else ((("ProtocolUri", empty())) if (ch.tag == 6) else ((("ProtocolVersion", empty())) if (ch.tag == 7) else ((("Performer", empty())) if (ch.tag == 9) else ((("Date", empty())) if (ch.tag == 10) else ((("Input", singleton(IOType_encoder(ch.fields[0])))) if (ch.tag == 11) else ((("Output", singleton(IOType_encoder(ch.fields[0])))) if (ch.tag == 12) else ((ch.fields[0], empty()))))))))))))))
    return Json(5, to_enumerable([("headertype", Json(0, pattern_input[0])), ("values", list_1(pattern_input[1]))]))


def _arrow1545(get: IGetters) -> CompositeHeader:
    header_type: str
    object_arg: IRequiredGetter = get.Required
    header_type = object_arg.Field("headertype", string)
    def oa(__unit: None=None) -> OntologyAnnotation:
        arg_3: Decoder_1[OntologyAnnotation] = index(0, OntologyAnnotation_decoder(ConverterOptions__ctor()))
        object_arg_1: IRequiredGetter = get.Required
        return object_arg_1.Field("values", arg_3)

    def io(__unit: None=None) -> IOType:
        arg_5: Decoder_1[IOType] = index(0, IOType_decoder)
        object_arg_2: IRequiredGetter = get.Required
        return object_arg_2.Field("values", arg_5)

    return CompositeHeader(1, oa(None)) if (header_type == "Characteristic") else (CompositeHeader(3, oa(None)) if (header_type == "Parameter") else (CompositeHeader(0, oa(None)) if (header_type == "Component") else (CompositeHeader(2, oa(None)) if (header_type == "Factor") else (CompositeHeader(11, io(None)) if (header_type == "Input") else (CompositeHeader(12, io(None)) if (header_type == "Output") else (CompositeHeader(4) if (header_type == "ProtocolType") else (CompositeHeader(8) if (header_type == "ProtocolREF") else (CompositeHeader(5) if (header_type == "ProtocolDescription") else (CompositeHeader(6) if (header_type == "ProtocolUri") else (CompositeHeader(7) if (header_type == "ProtocolVersion") else (CompositeHeader(9) if (header_type == "Performer") else (CompositeHeader(10) if (header_type == "Date") else CompositeHeader(13, header_type)))))))))))))


CompositeHeader_decoder: Decoder_1[CompositeHeader] = object(_arrow1545)

def ARCtrl_ISA_CompositeHeader__CompositeHeader_fromJsonString_Static_Z721C83C5(json_string: str) -> CompositeHeader:
    match_value: FSharpResult_2[CompositeHeader, str] = Decode_fromString(CompositeHeader_decoder, json_string)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def ARCtrl_ISA_CompositeHeader__CompositeHeader_ToJsonString_71136F3F(this: CompositeHeader, spaces: int | None=None) -> str:
    return to_string(default_arg(spaces, 0), CompositeHeader_encoder(this))


def ARCtrl_ISA_CompositeHeader__CompositeHeader_toJsonString_Static_Z331CE692(a: CompositeHeader) -> str:
    return ARCtrl_ISA_CompositeHeader__CompositeHeader_ToJsonString_71136F3F(a)


__all__ = ["CompositeHeader_encoder", "CompositeHeader_decoder", "ARCtrl_ISA_CompositeHeader__CompositeHeader_fromJsonString_Static_Z721C83C5", "ARCtrl_ISA_CompositeHeader__CompositeHeader_ToJsonString_71136F3F", "ARCtrl_ISA_CompositeHeader__CompositeHeader_toJsonString_Static_Z331CE692"]

