from __future__ import annotations
from typing import Any
from ....fable_modules.fable_library.seq import fold
from ....fable_modules.fable_library.util import IEnumerable_1
from ..JsonTypes.component import Component_create_61502994
from ..JsonTypes.protocol import (Protocol_setProtocolType, Protocol_setVersion, Protocol_setUri, Protocol_setDescription, Protocol_setName, Protocol_addParameter, Protocol_addComponent, Protocol, Protocol_create_Z7DFD6E67)
from ..JsonTypes.protocol_parameter import ProtocolParameter
from ..JsonTypes.value import Value
from .composite_cell import CompositeCell
from .composite_header import CompositeHeader

def to_protocol(table_name: str, row: IEnumerable_1[tuple[CompositeHeader, CompositeCell]]) -> Protocol:
    def folder(p: Protocol, hc: tuple[CompositeHeader, CompositeCell], table_name: Any=table_name, row: Any=row) -> Protocol:
        (pattern_matching_result, oa, v, v_1, v_2, v_3, oa_1, oa_2, unit, v_4, oa_3, t) = (None, None, None, None, None, None, None, None, None, None, None, None)
        if hc[0].tag == 4:
            if hc[1].tag == 0:
                pattern_matching_result = 0
                oa = hc[1].fields[0]

            else: 
                pattern_matching_result = 8


        elif hc[0].tag == 7:
            if hc[1].tag == 1:
                pattern_matching_result = 1
                v = hc[1].fields[0]

            else: 
                pattern_matching_result = 8


        elif hc[0].tag == 6:
            if hc[1].tag == 1:
                pattern_matching_result = 2
                v_1 = hc[1].fields[0]

            else: 
                pattern_matching_result = 8


        elif hc[0].tag == 5:
            if hc[1].tag == 1:
                pattern_matching_result = 3
                v_2 = hc[1].fields[0]

            else: 
                pattern_matching_result = 8


        elif hc[0].tag == 8:
            if hc[1].tag == 1:
                pattern_matching_result = 4
                v_3 = hc[1].fields[0]

            else: 
                pattern_matching_result = 8


        elif hc[0].tag == 3:
            pattern_matching_result = 5
            oa_1 = hc[0].fields[0]

        elif hc[0].tag == 0:
            if hc[1].tag == 2:
                pattern_matching_result = 6
                oa_2 = hc[0].fields[0]
                unit = hc[1].fields[1]
                v_4 = hc[1].fields[0]

            elif hc[1].tag == 0:
                pattern_matching_result = 7
                oa_3 = hc[0].fields[0]
                t = hc[1].fields[0]

            else: 
                pattern_matching_result = 8


        else: 
            pattern_matching_result = 8

        if pattern_matching_result == 0:
            return Protocol_setProtocolType(p, oa)

        elif pattern_matching_result == 1:
            return Protocol_setVersion(p, v)

        elif pattern_matching_result == 2:
            return Protocol_setUri(p, v_1)

        elif pattern_matching_result == 3:
            return Protocol_setDescription(p, v_2)

        elif pattern_matching_result == 4:
            return Protocol_setName(p, v_3)

        elif pattern_matching_result == 5:
            return Protocol_addParameter(ProtocolParameter.create(None, oa_1), p)

        elif pattern_matching_result == 6:
            return Protocol_addComponent(Component_create_61502994(None, Value.from_string(v_4), unit, oa_2), p)

        elif pattern_matching_result == 7:
            return Protocol_addComponent(Component_create_61502994(None, Value(0, t), None, oa_3), p)

        elif pattern_matching_result == 8:
            return p


    return fold(folder, Protocol_create_Z7DFD6E67(None, table_name), row)


__all__ = ["to_protocol"]

