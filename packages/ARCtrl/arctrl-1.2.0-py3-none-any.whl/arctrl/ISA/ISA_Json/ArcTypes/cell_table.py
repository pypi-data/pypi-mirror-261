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
from ...ISA.ArcTypes.composite_cell import CompositeCell
from ...ISA.helper import Dict_tryFind
from ...ISA.JsonTypes.ontology_annotation import OntologyAnnotation
from ...ISA_Json.ArcTypes.composite_cell import (CompositeCell_compressedEncoder, CompositeCell_compressedDecoder)

def CellTable_arrayFromMap(otm: Any) -> Array[CompositeCell]:
    def mapping(kv_1: Any, otm: Any=otm) -> CompositeCell:
        return kv_1[0]

    def projection(kv: Any, otm: Any=otm) -> int:
        return kv[1]

    class ObjectExpr1543:
        @property
        def Compare(self) -> Callable[[int, int], int]:
            return compare_primitives

    return to_array(map(mapping, sort_by(projection, otm, ObjectExpr1543())))


def CellTable_encoder(string_table: Any, oa_table: Any, ot: Array[CompositeCell]) -> Json:
    def mapping(cc: CompositeCell, string_table: Any=string_table, oa_table: Any=oa_table, ot: Any=ot) -> Json:
        return CompositeCell_compressedEncoder(string_table, oa_table, cc)

    return Json(6, map_1(mapping, ot, None))


def CellTable_decoder(string_table: Array[str], oa_table: Array[OntologyAnnotation]) -> Decoder_1[Array[CompositeCell]]:
    return array_1(CompositeCell_compressedDecoder(string_table, oa_table))


def CellTable_encodeCell(otm: Any, cc: CompositeCell) -> Json:
    match_value: int | None = Dict_tryFind(cc, otm)
    if match_value is None:
        i_1: int = len(otm) or 0
        add_to_dict(otm, cc, i_1)
        return Json(7, int(i_1+0x100000000 if i_1 < 0 else i_1))

    else: 
        i: int = match_value or 0
        return Json(7, int(i+0x100000000 if i < 0 else i))



def CellTable_decodeCell(ot: Array[CompositeCell]) -> Decoder_1[CompositeCell]:
    def _arrow1544(get: IGetters, ot: Any=ot) -> CompositeCell:
        i: int = get.Required.Raw(int_1) or 0
        return ot[i]

    return object(_arrow1544)


__all__ = ["CellTable_arrayFromMap", "CellTable_encoder", "CellTable_decoder", "CellTable_encodeCell", "CellTable_decodeCell"]

