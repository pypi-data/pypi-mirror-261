from __future__ import annotations
from collections.abc import Callable
from typing import Any
from ....fable_modules.fable_library.array_ import map as map_1
from ....fable_modules.fable_library.map_util import add_to_dict
from ....fable_modules.fable_library.seq import (to_array, map, sort_by)
from ....fable_modules.fable_library.types import Array
from ....fable_modules.fable_library.util import compare_primitives
from ....fable_modules.thoth_json_core.decode import (array as array_1, object, int_1, IGetters)
from ....fable_modules.thoth_json_core.types import (Json, Decoder_1)
from ...ISA.helper import Dict_tryFind
from ...ISA.JsonTypes.ontology_annotation import OntologyAnnotation
from ...ISA_Json.converter_options import (ConverterOptions__ctor, ConverterOptions)
from ...ISA_Json.ontology import (OntologyAnnotation_compressedEncoder, OntologyAnnotation_compressedDecoder)

def OATable_arrayFromMap(otm: Any) -> Array[OntologyAnnotation]:
    def mapping(kv_1: Any, otm: Any=otm) -> OntologyAnnotation:
        return kv_1[0]

    def projection(kv: Any, otm: Any=otm) -> int:
        return kv[1]

    class ObjectExpr1420:
        @property
        def Compare(self) -> Callable[[int, int], int]:
            return compare_primitives

    return to_array(map(mapping, sort_by(projection, otm, ObjectExpr1420())))


def OATable_encoder(string_table: Any, ot: Array[OntologyAnnotation]) -> Json:
    def _arrow1422(__unit: None=None, string_table: Any=string_table, ot: Any=ot) -> Callable[[OntologyAnnotation], Json]:
        options: ConverterOptions = ConverterOptions__ctor()
        def _arrow1421(oa: OntologyAnnotation) -> Json:
            return OntologyAnnotation_compressedEncoder(string_table, options, oa)

        return _arrow1421

    return Json(6, map_1(_arrow1422(), ot, None))


def OATable_decoder(string_table: Array[str]) -> Decoder_1[Array[OntologyAnnotation]]:
    return array_1(OntologyAnnotation_compressedDecoder(string_table, ConverterOptions__ctor()))


def OATable_encodeOA(otm: Any, oa: OntologyAnnotation) -> Json:
    match_value: int | None = Dict_tryFind(oa, otm)
    if match_value is None:
        i_1: int = len(otm) or 0
        add_to_dict(otm, oa, i_1)
        return Json(7, int(i_1+0x100000000 if i_1 < 0 else i_1))

    else: 
        i: int = match_value or 0
        return Json(7, int(i+0x100000000 if i < 0 else i))



def OATable_decodeOA(ot: Array[OntologyAnnotation]) -> Decoder_1[OntologyAnnotation]:
    def _arrow1423(get: IGetters, ot: Any=ot) -> OntologyAnnotation:
        i: int = get.Required.Raw(int_1) or 0
        return ot[i]

    return object(_arrow1423)


__all__ = ["OATable_arrayFromMap", "OATable_encoder", "OATable_decoder", "OATable_encodeOA", "OATable_decodeOA"]

