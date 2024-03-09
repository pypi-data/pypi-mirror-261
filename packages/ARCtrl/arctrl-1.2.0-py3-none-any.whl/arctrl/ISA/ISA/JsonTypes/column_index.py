from __future__ import annotations
from typing import Any
from ....fable_modules.fable_library.array_ import append
from ....fable_modules.fable_library.int32 import try_parse
from ....fable_modules.fable_library.option import (bind, value as value_1)
from ....fable_modules.fable_library.types import (FSharpRef, Array)
from ....fable_modules.fable_library.util import int32_to_string
from .comment import Comment
from .comment_list import try_item
from .component import (Component, Component_fromString_Z61E08C1)
from .factor import Factor
from .factor_value import FactorValue
from .material_attribute import (MaterialAttribute, MaterialAttribute_fromString_Z2304A83C)
from .material_attribute_value import MaterialAttributeValue
from .ontology_annotation import OntologyAnnotation
from .process_parameter_value import ProcessParameterValue
from .protocol_parameter import ProtocolParameter

def try_int(str_1: str) -> int | None:
    match_value: tuple[bool, int]
    out_arg: int = 0
    def _arrow407(__unit: None=None, str_1: Any=str_1) -> int:
        return out_arg

    def _arrow408(v: int, str_1: Any=str_1) -> None:
        nonlocal out_arg
        out_arg = v or 0

    match_value = (try_parse(str_1, 511, False, 32, FSharpRef(_arrow407, _arrow408)), out_arg)
    if match_value[0]:
        return match_value[1]

    else: 
        return None



order_name: str = "ColumnIndex"

def create_order_comment(index: int) -> Comment:
    value: str = int32_to_string(index)
    return Comment.from_string(order_name, value)


def try_get_index(comments: Array[Comment]) -> int | None:
    def _arrow409(str_1: str, comments: Any=comments) -> int | None:
        return try_int(str_1)

    return bind(_arrow409, try_item(order_name, comments))


def set_ontology_annotation_index(i: int, oa: OntologyAnnotation) -> OntologyAnnotation:
    def _arrow410(__unit: None=None, i: Any=i, oa: Any=oa) -> Array[Comment] | None:
        match_value: Array[Comment] | None = oa.Comments
        if match_value is None:
            return [create_order_comment(i)]

        else: 
            cs: Array[Comment] = match_value
            return append([create_order_comment(i)], cs, None)


    return OntologyAnnotation(oa.ID, oa.Name, oa.TermSourceREF, oa.TermAccessionNumber, _arrow410())


def try_get_ontology_annotation_index(oa: OntologyAnnotation) -> int | None:
    def _arrow411(comments: Array[Comment], oa: Any=oa) -> int | None:
        return try_get_index(comments)

    return bind(_arrow411, oa.Comments)


def try_get_parameter_index(param: ProtocolParameter) -> int | None:
    def binder(oa: OntologyAnnotation, param: Any=param) -> int | None:
        def _arrow412(comments: Array[Comment], oa: Any=oa) -> int | None:
            return try_get_index(comments)

        return bind(_arrow412, oa.Comments)

    return bind(binder, param.ParameterName)


def try_get_parameter_column_index(param_value: ProcessParameterValue) -> int | None:
    def _arrow413(param: ProtocolParameter, param_value: Any=param_value) -> int | None:
        return try_get_parameter_index(param)

    return bind(_arrow413, param_value.Category)


def try_get_factor_index(factor: Factor) -> int | None:
    def binder(oa: OntologyAnnotation, factor: Any=factor) -> int | None:
        def _arrow414(comments: Array[Comment], oa: Any=oa) -> int | None:
            return try_get_index(comments)

        return bind(_arrow414, oa.Comments)

    return bind(binder, factor.FactorType)


def try_get_factor_column_index(factor_value: FactorValue) -> int | None:
    def _arrow415(factor: Factor, factor_value: Any=factor_value) -> int | None:
        return try_get_factor_index(factor)

    return bind(_arrow415, factor_value.Category)


def try_get_characteristic_index(characteristic: MaterialAttribute) -> int | None:
    def binder(oa: OntologyAnnotation, characteristic: Any=characteristic) -> int | None:
        def _arrow416(comments: Array[Comment], oa: Any=oa) -> int | None:
            return try_get_index(comments)

        return bind(_arrow416, oa.Comments)

    return bind(binder, characteristic.CharacteristicType)


def try_get_characteristic_column_index(characteristic_value: MaterialAttributeValue) -> int | None:
    def _arrow417(characteristic: MaterialAttribute, characteristic_value: Any=characteristic_value) -> int | None:
        return try_get_characteristic_index(characteristic)

    return bind(_arrow417, characteristic_value.Category)


def try_get_component_index(comp: Component) -> int | None:
    def binder(oa: OntologyAnnotation, comp: Any=comp) -> int | None:
        def _arrow418(comments: Array[Comment], oa: Any=oa) -> int | None:
            return try_get_index(comments)

        return bind(_arrow418, oa.Comments)

    return bind(binder, comp.ComponentType)


def ARCtrl_ISA_OntologyAnnotation__OntologyAnnotation_fromStringWithColumnIndex_Static(name: str, term: str, source: str, accession: str, value_index: int) -> Factor:
    return Factor.from_string(name, term, source, accession, [create_order_comment(value_index)])


def ARCtrl_ISA_OntologyAnnotation__OntologyAnnotation_getColumnIndex_Static_Z4C0FE73C(f: OntologyAnnotation) -> int:
    return value_1(try_get_ontology_annotation_index(f))


def ARCtrl_ISA_OntologyAnnotation__OntologyAnnotation_GetColumnIndex(this: OntologyAnnotation) -> int:
    return value_1(try_get_ontology_annotation_index(this))


def ARCtrl_ISA_OntologyAnnotation__OntologyAnnotation_tryGetColumnIndex_Static_Z4C0FE73C(f: OntologyAnnotation) -> int | None:
    return try_get_ontology_annotation_index(f)


def ARCtrl_ISA_OntologyAnnotation__OntologyAnnotation_TryGetColumnIndex(this: OntologyAnnotation) -> int | None:
    return try_get_ontology_annotation_index(this)


def ARCtrl_ISA_OntologyAnnotation__OntologyAnnotation_setColumnIndex_Static(i: int, oa: OntologyAnnotation) -> OntologyAnnotation:
    return set_ontology_annotation_index(i, oa)


def ARCtrl_ISA_OntologyAnnotation__OntologyAnnotation_SetColumnIndex_Z524259A4(this: OntologyAnnotation, i: int) -> OntologyAnnotation:
    return set_ontology_annotation_index(i, this)


def ARCtrl_ISA_Factor__Factor_fromStringWithColumnIndex_Static(name: str, term: str, source: str, accession: str, value_index: int) -> Factor:
    return Factor.from_string(name, term, source, accession, [create_order_comment(value_index)])


def ARCtrl_ISA_Factor__Factor_getColumnIndex_Static_Z55333BD7(f: Factor) -> int:
    return value_1(try_get_factor_index(f))


def ARCtrl_ISA_Factor__Factor_GetColumnIndex(this: Factor) -> int:
    return value_1(try_get_factor_index(this))


def ARCtrl_ISA_Factor__Factor_tryGetColumnIndex_Static_Z55333BD7(f: Factor) -> int | None:
    return try_get_factor_index(f)


def ARCtrl_ISA_Factor__Factor_TryGetColumnIndex(this: Factor) -> int | None:
    return try_get_factor_index(this)


def ARCtrl_ISA_FactorValue__FactorValue_getColumnIndex_Static_Z2623397E(f: FactorValue) -> int:
    return value_1(try_get_factor_column_index(f))


def ARCtrl_ISA_FactorValue__FactorValue_GetColumnIndex(this: FactorValue) -> int:
    return value_1(try_get_factor_column_index(this))


def ARCtrl_ISA_FactorValue__FactorValue_tryGetColumnIndex_Static_Z2623397E(f: FactorValue) -> int | None:
    return try_get_factor_column_index(f)


def ARCtrl_ISA_FactorValue__FactorValue_TryGetColumnIndex(this: FactorValue) -> int | None:
    return try_get_factor_column_index(this)


def ARCtrl_ISA_MaterialAttribute__MaterialAttribute_fromStringWithColumnIndex_Static(term: str, source: str, accession: str, value_index: int) -> MaterialAttribute:
    return MaterialAttribute_fromString_Z2304A83C(term, source, accession, [create_order_comment(value_index)])


def ARCtrl_ISA_MaterialAttribute__MaterialAttribute_getColumnIndex_Static_Z5F39696D(m: MaterialAttribute) -> int:
    return value_1(try_get_characteristic_index(m))


def ARCtrl_ISA_MaterialAttribute__MaterialAttribute_GetColumnIndex(this: MaterialAttribute) -> int:
    return value_1(try_get_characteristic_index(this))


def ARCtrl_ISA_MaterialAttribute__MaterialAttribute_tryGetColumnIndex_Static_Z5F39696D(m: MaterialAttribute) -> int | None:
    return try_get_characteristic_index(m)


def ARCtrl_ISA_MaterialAttribute__MaterialAttribute_TryGetColumnIndex(this: MaterialAttribute) -> int | None:
    return try_get_characteristic_index(this)


def ARCtrl_ISA_MaterialAttributeValue__MaterialAttributeValue_getColumnIndex_Static_43A5B238(m: MaterialAttributeValue) -> int:
    return value_1(try_get_characteristic_column_index(m))


def ARCtrl_ISA_MaterialAttributeValue__MaterialAttributeValue_GetColumnIndex(this: MaterialAttributeValue) -> int:
    return value_1(try_get_characteristic_column_index(this))


def ARCtrl_ISA_MaterialAttributeValue__MaterialAttributeValue_tryGetColumnIndex_Static_43A5B238(m: MaterialAttributeValue) -> int | None:
    return try_get_characteristic_column_index(m)


def ARCtrl_ISA_MaterialAttributeValue__MaterialAttributeValue_TryGetColumnIndex(this: MaterialAttributeValue) -> int | None:
    return try_get_characteristic_column_index(this)


def ARCtrl_ISA_ProtocolParameter__ProtocolParameter_fromStringWithColumnIndex_Static(term: str, source: str, accession: str, value_index: int) -> ProtocolParameter:
    return ProtocolParameter.from_string(term, source, accession, [create_order_comment(value_index)])


def ARCtrl_ISA_ProtocolParameter__ProtocolParameter_getColumnIndex_Static_Z3A4310A5(p: ProtocolParameter) -> int:
    return value_1(try_get_parameter_index(p))


def ARCtrl_ISA_ProtocolParameter__ProtocolParameter_GetColumnIndex(this: ProtocolParameter) -> int:
    return value_1(try_get_parameter_index(this))


def ARCtrl_ISA_ProtocolParameter__ProtocolParameter_tryGetColumnIndex_Static_Z3A4310A5(p: ProtocolParameter) -> int | None:
    return try_get_parameter_index(p)


def ARCtrl_ISA_ProtocolParameter__ProtocolParameter_TryGetColumnIndex(this: ProtocolParameter) -> int | None:
    return try_get_parameter_index(this)


def ARCtrl_ISA_ProcessParameterValue__ProcessParameterValue_getColumnIndex_Static_5FD7232D(p: ProcessParameterValue) -> int:
    return value_1(try_get_parameter_column_index(p))


def ARCtrl_ISA_ProcessParameterValue__ProcessParameterValue_GetColumnIndex(this: ProcessParameterValue) -> int:
    return value_1(try_get_parameter_column_index(this))


def ARCtrl_ISA_ProcessParameterValue__ProcessParameterValue_tryGetColumnIndex_Static_5FD7232D(p: ProcessParameterValue) -> int | None:
    return try_get_parameter_column_index(p)


def ARCtrl_ISA_ProcessParameterValue__ProcessParameterValue_TryGetColumnIndex(this: ProcessParameterValue) -> int | None:
    return try_get_parameter_column_index(this)


def ARCtrl_ISA_Component__Component_fromStringWithColumnIndex_Static(name: str, term: str, source: str, accession: str, value_index: int) -> Component:
    return Component_fromString_Z61E08C1(name, term, source, accession, [create_order_comment(value_index)])


def ARCtrl_ISA_Component__Component_getColumnIndex_Static_Z609B8895(f: Component) -> int:
    return value_1(try_get_component_index(f))


def ARCtrl_ISA_Component__Component_GetColumnIndex(this: Component) -> int:
    return value_1(try_get_component_index(this))


def ARCtrl_ISA_Component__Component_tryGetColumnIndex_Static_Z609B8895(f: Component) -> int | None:
    return try_get_component_index(f)


def ARCtrl_ISA_Component__Component_TryGetColumnIndex(this: Component) -> int | None:
    return try_get_component_index(this)


__all__ = ["try_int", "order_name", "create_order_comment", "try_get_index", "set_ontology_annotation_index", "try_get_ontology_annotation_index", "try_get_parameter_index", "try_get_parameter_column_index", "try_get_factor_index", "try_get_factor_column_index", "try_get_characteristic_index", "try_get_characteristic_column_index", "try_get_component_index", "ARCtrl_ISA_OntologyAnnotation__OntologyAnnotation_fromStringWithColumnIndex_Static", "ARCtrl_ISA_OntologyAnnotation__OntologyAnnotation_getColumnIndex_Static_Z4C0FE73C", "ARCtrl_ISA_OntologyAnnotation__OntologyAnnotation_GetColumnIndex", "ARCtrl_ISA_OntologyAnnotation__OntologyAnnotation_tryGetColumnIndex_Static_Z4C0FE73C", "ARCtrl_ISA_OntologyAnnotation__OntologyAnnotation_TryGetColumnIndex", "ARCtrl_ISA_OntologyAnnotation__OntologyAnnotation_setColumnIndex_Static", "ARCtrl_ISA_OntologyAnnotation__OntologyAnnotation_SetColumnIndex_Z524259A4", "ARCtrl_ISA_Factor__Factor_fromStringWithColumnIndex_Static", "ARCtrl_ISA_Factor__Factor_getColumnIndex_Static_Z55333BD7", "ARCtrl_ISA_Factor__Factor_GetColumnIndex", "ARCtrl_ISA_Factor__Factor_tryGetColumnIndex_Static_Z55333BD7", "ARCtrl_ISA_Factor__Factor_TryGetColumnIndex", "ARCtrl_ISA_FactorValue__FactorValue_getColumnIndex_Static_Z2623397E", "ARCtrl_ISA_FactorValue__FactorValue_GetColumnIndex", "ARCtrl_ISA_FactorValue__FactorValue_tryGetColumnIndex_Static_Z2623397E", "ARCtrl_ISA_FactorValue__FactorValue_TryGetColumnIndex", "ARCtrl_ISA_MaterialAttribute__MaterialAttribute_fromStringWithColumnIndex_Static", "ARCtrl_ISA_MaterialAttribute__MaterialAttribute_getColumnIndex_Static_Z5F39696D", "ARCtrl_ISA_MaterialAttribute__MaterialAttribute_GetColumnIndex", "ARCtrl_ISA_MaterialAttribute__MaterialAttribute_tryGetColumnIndex_Static_Z5F39696D", "ARCtrl_ISA_MaterialAttribute__MaterialAttribute_TryGetColumnIndex", "ARCtrl_ISA_MaterialAttributeValue__MaterialAttributeValue_getColumnIndex_Static_43A5B238", "ARCtrl_ISA_MaterialAttributeValue__MaterialAttributeValue_GetColumnIndex", "ARCtrl_ISA_MaterialAttributeValue__MaterialAttributeValue_tryGetColumnIndex_Static_43A5B238", "ARCtrl_ISA_MaterialAttributeValue__MaterialAttributeValue_TryGetColumnIndex", "ARCtrl_ISA_ProtocolParameter__ProtocolParameter_fromStringWithColumnIndex_Static", "ARCtrl_ISA_ProtocolParameter__ProtocolParameter_getColumnIndex_Static_Z3A4310A5", "ARCtrl_ISA_ProtocolParameter__ProtocolParameter_GetColumnIndex", "ARCtrl_ISA_ProtocolParameter__ProtocolParameter_tryGetColumnIndex_Static_Z3A4310A5", "ARCtrl_ISA_ProtocolParameter__ProtocolParameter_TryGetColumnIndex", "ARCtrl_ISA_ProcessParameterValue__ProcessParameterValue_getColumnIndex_Static_5FD7232D", "ARCtrl_ISA_ProcessParameterValue__ProcessParameterValue_GetColumnIndex", "ARCtrl_ISA_ProcessParameterValue__ProcessParameterValue_tryGetColumnIndex_Static_5FD7232D", "ARCtrl_ISA_ProcessParameterValue__ProcessParameterValue_TryGetColumnIndex", "ARCtrl_ISA_Component__Component_fromStringWithColumnIndex_Static", "ARCtrl_ISA_Component__Component_getColumnIndex_Static_Z609B8895", "ARCtrl_ISA_Component__Component_GetColumnIndex", "ARCtrl_ISA_Component__Component_tryGetColumnIndex_Static_Z609B8895", "ARCtrl_ISA_Component__Component_TryGetColumnIndex"]

