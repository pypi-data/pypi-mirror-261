from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any
from ....fable_modules.fable_library.option import (default_arg, map, bind)
from ....fable_modules.fable_library.reflection import (TypeInfo, string_type, option_type, record_type)
from ....fable_modules.fable_library.types import (to_string, Record, Array)
from ..helper import Option_fromValueWithDefault
from .comment import Comment
from .ontology_annotation import (OntologyAnnotation, OntologyAnnotation_reflection)

def _expr306() -> TypeInfo:
    return record_type("ARCtrl.ISA.MaterialAttribute", [], MaterialAttribute, lambda: [("ID", option_type(string_type)), ("CharacteristicType", option_type(OntologyAnnotation_reflection()))])


@dataclass(eq = False, repr = False, slots = True)
class MaterialAttribute(Record):
    ID: str | None
    CharacteristicType: OntologyAnnotation | None
    def Print(self, __unit: None=None) -> str:
        this: MaterialAttribute = self
        return to_string(this)

    def PrintCompact(self, __unit: None=None) -> str:
        this: MaterialAttribute = self
        return "OA " + MaterialAttribute__get_NameText(this)


MaterialAttribute_reflection = _expr306

def MaterialAttribute_make(id: str | None=None, characteristic_type: OntologyAnnotation | None=None) -> MaterialAttribute:
    return MaterialAttribute(id, characteristic_type)


def MaterialAttribute_create_Z6C54B221(Id: str | None=None, CharacteristicType: OntologyAnnotation | None=None) -> MaterialAttribute:
    return MaterialAttribute_make(Id, CharacteristicType)


def MaterialAttribute_get_empty(__unit: None=None) -> MaterialAttribute:
    return MaterialAttribute_create_Z6C54B221()


def MaterialAttribute_fromString_Z2304A83C(term: str, source: str, accession: str, comments: Array[Comment] | None=None) -> MaterialAttribute:
    oa: OntologyAnnotation = OntologyAnnotation.from_string(term, source, accession, comments)
    return MaterialAttribute_make(None, Option_fromValueWithDefault(OntologyAnnotation.empty(), oa))


def MaterialAttribute_toString_Z5F39696D(ma: MaterialAttribute) -> dict[str, Any]:
    value: dict[str, Any] = {
        "TermAccessionNumber": "",
        "TermName": "",
        "TermSourceREF": ""
    }
    def mapping(oa: OntologyAnnotation, ma: Any=ma) -> dict[str, Any]:
        return OntologyAnnotation.to_string(oa)

    return default_arg(map(mapping, ma.CharacteristicType), value)


def MaterialAttribute__get_NameText(this: MaterialAttribute) -> str:
    def mapping(oa: OntologyAnnotation, this: Any=this) -> str:
        return oa.NameText

    return default_arg(map(mapping, this.CharacteristicType), "")


def MaterialAttribute__get_TryNameText(this: MaterialAttribute) -> str | None:
    def binder(oa: OntologyAnnotation, this: Any=this) -> str | None:
        return oa.Name

    return bind(binder, this.CharacteristicType)


def MaterialAttribute__MapCategory_Z69DD836A(this: MaterialAttribute, f: Callable[[OntologyAnnotation], OntologyAnnotation]) -> MaterialAttribute:
    return MaterialAttribute(this.ID, map(f, this.CharacteristicType))


def MaterialAttribute__SetCategory_Z4C0FE73C(this: MaterialAttribute, c: OntologyAnnotation) -> MaterialAttribute:
    return MaterialAttribute(this.ID, c)


def MaterialAttribute_tryGetNameText_Z5F39696D(ma: MaterialAttribute) -> str:
    return MaterialAttribute__get_NameText(ma)


def MaterialAttribute_getNameText_Z5F39696D(ma: MaterialAttribute) -> str | None:
    return MaterialAttribute__get_TryNameText(ma)


def MaterialAttribute_nameEqualsString(name: str, ma: MaterialAttribute) -> bool:
    return MaterialAttribute__get_NameText(ma) == name


__all__ = ["MaterialAttribute_reflection", "MaterialAttribute_make", "MaterialAttribute_create_Z6C54B221", "MaterialAttribute_get_empty", "MaterialAttribute_fromString_Z2304A83C", "MaterialAttribute_toString_Z5F39696D", "MaterialAttribute__get_NameText", "MaterialAttribute__get_TryNameText", "MaterialAttribute__MapCategory_Z69DD836A", "MaterialAttribute__SetCategory_Z4C0FE73C", "MaterialAttribute_tryGetNameText_Z5F39696D", "MaterialAttribute_getNameText_Z5F39696D", "MaterialAttribute_nameEqualsString"]

