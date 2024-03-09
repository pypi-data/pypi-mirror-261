from __future__ import annotations
from collections.abc import Callable
from typing import Any
from ....fable_modules.fable_library.list import (singleton, of_array, FSharpList)
from ....fable_modules.fable_library.option import default_arg
from ....fable_modules.fable_library.result import FSharpResult_2
from ....fable_modules.fable_library.string_ import (to_fail, printf, to_text)
from ....fable_modules.fable_library.types import Array
from ....fable_modules.fable_library.util import to_enumerable
from ....fable_modules.thoth_json_core.decode import (object, IRequiredGetter, string, index, IGetters)
from ....fable_modules.thoth_json_core.encode import list_1
from ....fable_modules.thoth_json_core.types import (Json, Decoder_1)
from ....fable_modules.thoth_json_python.decode import Decode_fromString
from ....fable_modules.thoth_json_python.encode import to_string
from ...ISA.ArcTypes.composite_cell import CompositeCell
from ...ISA.JsonTypes.ontology_annotation import OntologyAnnotation
from ...ISA_Json.converter_options import ConverterOptions__ctor
from ...ISA_Json.ontology import (OntologyAnnotation_encoder, OntologyAnnotation_decoder)
from ...ISA_Json.string_table import (StringTable_encodeString, StringTable_decodeString)
from ...ISA_Json.ArcTypes.oatable import (OATable_encodeOA, OATable_decodeOA)

def CompositeCell_encoder(cc: CompositeCell) -> Json:
    def oa_to_json_string(oa: OntologyAnnotation, cc: Any=cc) -> Json:
        return OntologyAnnotation_encoder(ConverterOptions__ctor(), oa)

    pattern_input: tuple[str, FSharpList[Json]] = (("Term", singleton(oa_to_json_string(cc.fields[0])))) if (cc.tag == 0) else ((("Unitized", of_array([Json(0, cc.fields[0]), oa_to_json_string(cc.fields[1])]))) if (cc.tag == 2) else (("FreeText", singleton(Json(0, cc.fields[0])))))
    return Json(5, to_enumerable([("celltype", Json(0, pattern_input[0])), ("values", list_1(pattern_input[1]))]))


def _arrow1537(get: IGetters) -> CompositeCell:
    match_value: str
    object_arg: IRequiredGetter = get.Required
    match_value = object_arg.Field("celltype", string)
    def _arrow1533(__unit: None=None) -> str:
        arg_3: Decoder_1[str] = index(0, string)
        object_arg_1: IRequiredGetter = get.Required
        return object_arg_1.Field("values", arg_3)

    def _arrow1534(__unit: None=None) -> OntologyAnnotation:
        arg_5: Decoder_1[OntologyAnnotation] = index(0, OntologyAnnotation_decoder(ConverterOptions__ctor()))
        object_arg_2: IRequiredGetter = get.Required
        return object_arg_2.Field("values", arg_5)

    def _arrow1535(__unit: None=None) -> str:
        arg_7: Decoder_1[str] = index(0, string)
        object_arg_3: IRequiredGetter = get.Required
        return object_arg_3.Field("values", arg_7)

    def _arrow1536(__unit: None=None) -> OntologyAnnotation:
        arg_9: Decoder_1[OntologyAnnotation] = index(1, OntologyAnnotation_decoder(ConverterOptions__ctor()))
        object_arg_4: IRequiredGetter = get.Required
        return object_arg_4.Field("values", arg_9)

    return CompositeCell(1, _arrow1533()) if (match_value == "FreeText") else (CompositeCell(0, _arrow1534()) if (match_value == "Term") else (CompositeCell(2, _arrow1535(), _arrow1536()) if (match_value == "Unitized") else to_fail(printf("Error reading CompositeCell from json string: %A"))(match_value)))


CompositeCell_decoder: Decoder_1[CompositeCell] = object(_arrow1537)

def CompositeCell_compressedEncoder(string_table: Any, oa_table: Any, cc: CompositeCell) -> Json:
    pattern_input: tuple[str, FSharpList[Json]] = (("Term", singleton(OATable_encodeOA(oa_table, cc.fields[0])))) if (cc.tag == 0) else ((("Unitized", of_array([StringTable_encodeString(string_table, cc.fields[0]), OATable_encodeOA(oa_table, cc.fields[1])]))) if (cc.tag == 2) else (("FreeText", singleton(StringTable_encodeString(string_table, cc.fields[0])))))
    return Json(5, to_enumerable([("t", StringTable_encodeString(string_table, pattern_input[0])), ("v", list_1(pattern_input[1]))]))


def CompositeCell_compressedDecoder(string_table: Array[str], oa_table: Array[OntologyAnnotation]) -> Decoder_1[CompositeCell]:
    def _arrow1542(get: IGetters, string_table: Any=string_table, oa_table: Any=oa_table) -> CompositeCell:
        match_value: str
        arg_1: Decoder_1[str] = StringTable_decodeString(string_table)
        object_arg: IRequiredGetter = get.Required
        match_value = object_arg.Field("t", arg_1)
        def _arrow1538(__unit: None=None) -> str:
            arg_3: Decoder_1[str] = index(0, StringTable_decodeString(string_table))
            object_arg_1: IRequiredGetter = get.Required
            return object_arg_1.Field("v", arg_3)

        def _arrow1539(__unit: None=None) -> OntologyAnnotation:
            arg_5: Decoder_1[OntologyAnnotation] = index(0, OATable_decodeOA(oa_table))
            object_arg_2: IRequiredGetter = get.Required
            return object_arg_2.Field("v", arg_5)

        def _arrow1540(__unit: None=None) -> str:
            arg_7: Decoder_1[str] = index(0, StringTable_decodeString(string_table))
            object_arg_3: IRequiredGetter = get.Required
            return object_arg_3.Field("v", arg_7)

        def _arrow1541(__unit: None=None) -> OntologyAnnotation:
            arg_9: Decoder_1[OntologyAnnotation] = index(1, OATable_decodeOA(oa_table))
            object_arg_4: IRequiredGetter = get.Required
            return object_arg_4.Field("v", arg_9)

        return CompositeCell(1, _arrow1538()) if (match_value == "FreeText") else (CompositeCell(0, _arrow1539()) if (match_value == "Term") else (CompositeCell(2, _arrow1540(), _arrow1541()) if (match_value == "Unitized") else to_fail(printf("Error reading CompositeCell from json string: %A"))(match_value)))

    return object(_arrow1542)


def ARCtrl_ISA_CompositeCell__CompositeCell_fromJsonString_Static_Z721C83C5(json_string: str) -> CompositeCell:
    match_value: FSharpResult_2[CompositeCell, str] = Decode_fromString(CompositeCell_decoder, json_string)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def ARCtrl_ISA_CompositeCell__CompositeCell_ToJsonString_71136F3F(this: CompositeCell, spaces: int | None=None) -> str:
    return to_string(default_arg(spaces, 0), CompositeCell_encoder(this))


def ARCtrl_ISA_CompositeCell__CompositeCell_toJsonString_Static_1B703D57(a: CompositeCell) -> str:
    return ARCtrl_ISA_CompositeCell__CompositeCell_ToJsonString_71136F3F(a)


__all__ = ["CompositeCell_encoder", "CompositeCell_decoder", "CompositeCell_compressedEncoder", "CompositeCell_compressedDecoder", "ARCtrl_ISA_CompositeCell__CompositeCell_fromJsonString_Static_Z721C83C5", "ARCtrl_ISA_CompositeCell__CompositeCell_ToJsonString_71136F3F", "ARCtrl_ISA_CompositeCell__CompositeCell_toJsonString_Static_1B703D57"]

