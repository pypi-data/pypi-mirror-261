from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any
from ....fable_modules.fable_library.option import (map, default_arg)
from ....fable_modules.fable_library.reflection import (TypeInfo, string_type, option_type, record_type)
from ....fable_modules.fable_library.string_ import (to_text, printf)
from ....fable_modules.fable_library.types import (to_string, Record)
from ....fable_modules.fable_library.util import int32_to_string
from .factor import (Factor, Factor_reflection)
from .ontology_annotation import (OntologyAnnotation, OntologyAnnotation_reflection)
from .value import (Value as Value_1, Value_reflection)

def _expr304() -> TypeInfo:
    return record_type("ARCtrl.ISA.FactorValue", [], FactorValue, lambda: [("ID", option_type(string_type)), ("Category", option_type(Factor_reflection())), ("Value", option_type(Value_reflection())), ("Unit", option_type(OntologyAnnotation_reflection()))])


@dataclass(eq = False, repr = False, slots = True)
class FactorValue(Record):
    ID: str | None
    Category: Factor | None
    Value: Value_1 | None
    Unit: OntologyAnnotation | None
    def Print(self, __unit: None=None) -> str:
        this: FactorValue = self
        return to_string(this)

    def PrintCompact(self, __unit: None=None) -> str:
        this: FactorValue = self
        def mapping(f: Factor) -> str:
            return f.NameText

        category: str | None = map(mapping, this.Category)
        def mapping_1(oa: OntologyAnnotation) -> str:
            return oa.NameText

        unit: str | None = map(mapping_1, this.Unit)
        def mapping_2(v: Value_1) -> str:
            s: str = v.PrintCompact()
            if unit is None:
                return s

            else: 
                return (s + " ") + unit


        value: str | None = map(mapping_2, this.Value)
        def _arrow301(__unit: None=None) -> str:
            value_2: str = value
            return value_2

        def _arrow302(__unit: None=None) -> str:
            category_2: str = category
            return (category_2 + ":") + "No Value"

        def _arrow303(__unit: None=None) -> str:
            category_1: str = category
            value_1: str = value
            return (category_1 + ":") + value_1

        return ("" if (value is None) else _arrow301()) if (category is None) else (_arrow302() if (value is None) else _arrow303())


FactorValue_reflection = _expr304

def FactorValue_make(id: str | None=None, category: Factor | None=None, value: Value_1 | None=None, unit: OntologyAnnotation | None=None) -> FactorValue:
    return FactorValue(id, category, value, unit)


def FactorValue_create_18335379(Id: str | None=None, Category: Factor | None=None, Value: Value_1 | None=None, Unit: OntologyAnnotation | None=None) -> FactorValue:
    return FactorValue_make(Id, Category, Value, Unit)


def FactorValue_get_empty(__unit: None=None) -> FactorValue:
    return FactorValue_create_18335379()


def FactorValue__get_ValueText(this: FactorValue) -> str:
    def mapping(oa: Value_1, this: Any=this) -> str:
        if oa.tag == 2:
            return to_string(oa.fields[0])

        elif oa.tag == 1:
            return int32_to_string(oa.fields[0])

        elif oa.tag == 3:
            return oa.fields[0]

        else: 
            return oa.fields[0].NameText


    return default_arg(map(mapping, this.Value), "")


def FactorValue__get_ValueWithUnitText(this: FactorValue) -> str:
    def mapping(oa: OntologyAnnotation, this: Any=this) -> str:
        return oa.NameText

    unit: str | None = map(mapping, this.Unit)
    v: str = FactorValue__get_ValueText(this)
    if unit is None:
        return v

    else: 
        u: str = unit
        return to_text(printf("%s %s"))(v)(u)



def FactorValue__get_NameText(this: FactorValue) -> str:
    def mapping(factor: Factor, this: Any=this) -> str:
        return factor.NameText

    return default_arg(map(mapping, this.Category), "")


def FactorValue__MapCategory_Z69DD836A(this: FactorValue, f: Callable[[OntologyAnnotation], OntologyAnnotation]) -> FactorValue:
    def mapping(p: Factor, this: Any=this, f: Any=f) -> Factor:
        return p.MapCategory(f)

    return FactorValue(this.ID, map(mapping, this.Category), this.Value, this.Unit)


def FactorValue__SetCategory_Z4C0FE73C(this: FactorValue, c: OntologyAnnotation) -> FactorValue:
    def _arrow305(__unit: None=None, this: Any=this, c: Any=c) -> Factor | None:
        match_value: Factor | None = this.Category
        if match_value is None:
            return Factor.create(None, None, c)

        else: 
            p: Factor = match_value
            return p.SetCategory(c)


    return FactorValue(this.ID, _arrow305(), this.Value, this.Unit)


def FactorValue_getNameAsString_Z2623397E(fv: FactorValue) -> str:
    return FactorValue__get_NameText(fv)


def FactorValue_nameEqualsString(name: str, fv: FactorValue) -> bool:
    return FactorValue__get_NameText(fv) == name


__all__ = ["FactorValue_reflection", "FactorValue_make", "FactorValue_create_18335379", "FactorValue_get_empty", "FactorValue__get_ValueText", "FactorValue__get_ValueWithUnitText", "FactorValue__get_NameText", "FactorValue__MapCategory_Z69DD836A", "FactorValue__SetCategory_Z4C0FE73C", "FactorValue_getNameAsString_Z2623397E", "FactorValue_nameEqualsString"]

