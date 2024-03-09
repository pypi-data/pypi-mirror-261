from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any
from ....fable_modules.fable_library.option import (default_arg, map)
from ....fable_modules.fable_library.reflection import (TypeInfo, string_type, option_type, record_type)
from ....fable_modules.fable_library.reg_exp import (get_item, groups)
from ....fable_modules.fable_library.string_ import (to_text, printf)
from ....fable_modules.fable_library.types import (Record, Array)
from ..helper import Option_fromValueWithDefault
from ..regex import ActivePatterns__007CRegex_007C__007C
from .comment import Comment
from .ontology_annotation import (OntologyAnnotation, OntologyAnnotation_reflection)
from .value import (Value as Value_1, Value_reflection)

def _expr343() -> TypeInfo:
    return record_type("ARCtrl.ISA.Component", [], Component, lambda: [("ComponentName", option_type(string_type)), ("ComponentValue", option_type(Value_reflection())), ("ComponentUnit", option_type(OntologyAnnotation_reflection())), ("ComponentType", option_type(OntologyAnnotation_reflection()))])


@dataclass(eq = False, repr = False, slots = True)
class Component(Record):
    ComponentName: str | None
    ComponentValue: Value_1 | None
    ComponentUnit: OntologyAnnotation | None
    ComponentType: OntologyAnnotation | None

Component_reflection = _expr343

def Component_make(name: str | None=None, value: Value_1 | None=None, unit: OntologyAnnotation | None=None, component_type: OntologyAnnotation | None=None) -> Component:
    return Component(name, value, unit, component_type)


def Component_create_61502994(Name: str | None=None, Value: Value_1 | None=None, Unit: OntologyAnnotation | None=None, ComponentType: OntologyAnnotation | None=None) -> Component:
    return Component_make(Name, Value, Unit, ComponentType)


def Component_get_empty(__unit: None=None) -> Component:
    return Component_create_61502994()


def Component_composeName(value: Value_1 | None=None, unit: OntologyAnnotation | None=None) -> str:
    if value is None:
        return ""

    elif value.tag == 0:
        oa: OntologyAnnotation = value.fields[0]
        return ((("" + oa.NameText) + " (") + oa.TermAccessionShort) + ")"

    elif unit is not None:
        u: OntologyAnnotation = unit
        v_1: Value_1 = value
        return ((((("" + v_1.Text) + " ") + u.NameText) + " (") + u.TermAccessionShort) + ")"

    else: 
        v: Value_1 = value
        return ("" + v.Text) + ""



def Component_decomposeName_Z721C83C5(name: str) -> tuple[Value_1, OntologyAnnotation | None]:
    active_pattern_result: Any | None = ActivePatterns__007CRegex_007C__007C("(?<value>[\\d\\.]+) (?<unit>.+) \\((?<ontology>[^(]*:[^)]*)\\)", name)
    if active_pattern_result is not None:
        unitr: Any = active_pattern_result
        oa: OntologyAnnotation
        term_annotation: str = get_item(groups(unitr), "ontology") or ""
        oa = OntologyAnnotation.from_term_annotation(term_annotation)
        def _arrow345(__unit: None=None, name: Any=name) -> Value_1:
            value: str = get_item(groups(unitr), "value") or ""
            return Value_1.from_string(value)

        return (_arrow345(), OntologyAnnotation(oa.ID, get_item(groups(unitr), "unit") or "", oa.TermSourceREF, oa.TermAccessionNumber, oa.Comments))

    else: 
        active_pattern_result_1: Any | None = ActivePatterns__007CRegex_007C__007C("(?<value>[^\\(]+) \\((?<ontology>[^(]*:[^)]*)\\)", name)
        if active_pattern_result_1 is not None:
            r: Any = active_pattern_result_1
            oa_1: OntologyAnnotation
            term_annotation_1: str = get_item(groups(r), "ontology") or ""
            oa_1 = OntologyAnnotation.from_term_annotation(term_annotation_1)
            v_1: Value_1
            value_1: str = get_item(groups(r), "value") or ""
            v_1 = Value_1.from_string(value_1)
            return (Value_1(0, OntologyAnnotation(oa_1.ID, v_1.Text, oa_1.TermSourceREF, oa_1.TermAccessionNumber, oa_1.Comments)), None)

        else: 
            return (Value_1(3, name), None)




def Component_fromString_Z61E08C1(name: str | None=None, term: str | None=None, source: str | None=None, accession: str | None=None, comments: Array[Comment] | None=None) -> Component:
    c_type: OntologyAnnotation | None
    v: OntologyAnnotation = OntologyAnnotation.from_string(term, source, accession, comments)
    c_type = Option_fromValueWithDefault(OntologyAnnotation.empty(), v)
    if name is None:
        return Component_make(None, None, None, c_type)

    else: 
        pattern_input: tuple[Value_1, OntologyAnnotation | None] = Component_decomposeName_Z721C83C5(name)
        return Component_make(name, Option_fromValueWithDefault(Value_1(3, ""), pattern_input[0]), pattern_input[1], c_type)



def Component_fromOptions(value: Value_1 | None=None, unit: OntologyAnnotation | None=None, header: OntologyAnnotation | None=None) -> Component:
    return Component_make(Option_fromValueWithDefault("", Component_composeName(value, unit)), value, unit, header)


def Component_toString_Z609B8895(c: Component) -> tuple[str, dict[str, Any]]:
    oa_1: dict[str, Any]
    value: dict[str, Any] = {
        "TermAccessionNumber": "",
        "TermName": "",
        "TermSourceREF": ""
    }
    def mapping(oa: OntologyAnnotation, c: Any=c) -> dict[str, Any]:
        return OntologyAnnotation.to_string(oa)

    oa_1 = default_arg(map(mapping, c.ComponentType), value)
    return (default_arg(c.ComponentName, ""), oa_1)


def Component__get_NameText(this: Component) -> str:
    def mapping(c: OntologyAnnotation, this: Any=this) -> str:
        return c.NameText

    return default_arg(map(mapping, this.ComponentType), "")


def Component__get_UnitText(this: Component) -> str:
    def mapping(c: OntologyAnnotation, this: Any=this) -> str:
        return c.NameText

    return default_arg(map(mapping, this.ComponentUnit), "")


def Component__get_ValueText(this: Component) -> str:
    def mapping(c: Value_1, this: Any=this) -> str:
        return c.Text

    return default_arg(map(mapping, this.ComponentValue), "")


def Component__get_ValueWithUnitText(this: Component) -> str:
    def mapping(oa: OntologyAnnotation, this: Any=this) -> str:
        return oa.NameText

    unit: str | None = map(mapping, this.ComponentUnit)
    v: str = Component__get_ValueText(this)
    if unit is None:
        return v

    else: 
        u: str = unit
        return to_text(printf("%s %s"))(v)(u)



def Component__MapCategory_Z69DD836A(this: Component, f: Callable[[OntologyAnnotation], OntologyAnnotation]) -> Component:
    return Component(this.ComponentName, this.ComponentValue, this.ComponentUnit, map(f, this.ComponentType))


def Component__SetCategory_Z4C0FE73C(this: Component, c: OntologyAnnotation) -> Component:
    return Component(this.ComponentName, this.ComponentValue, this.ComponentUnit, c)


__all__ = ["Component_reflection", "Component_make", "Component_create_61502994", "Component_get_empty", "Component_composeName", "Component_decomposeName_Z721C83C5", "Component_fromString_Z61E08C1", "Component_fromOptions", "Component_toString_Z609B8895", "Component__get_NameText", "Component__get_UnitText", "Component__get_ValueText", "Component__get_ValueWithUnitText", "Component__MapCategory_Z69DD836A", "Component__SetCategory_Z4C0FE73C"]

