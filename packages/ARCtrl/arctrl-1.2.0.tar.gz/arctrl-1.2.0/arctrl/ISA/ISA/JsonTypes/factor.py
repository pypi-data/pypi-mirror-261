from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any
from ....fable_modules.fable_library.array_ import (map2, map as map_2)
from ....fable_modules.fable_library.list import (try_find, FSharpList, exists, append, singleton, map as map_1, filter)
from ....fable_modules.fable_library.option import (default_arg, map)
from ....fable_modules.fable_library.reflection import (make_record, get_record_fields, TypeInfo, string_type, option_type, array_type, record_type)
from ....fable_modules.fable_library.types import (Array, to_string, Record)
from ....fable_modules.fable_library.util import equals
from ..helper import (Update_updateAppend, Update_updateOnlyByExisting, Update_updateOnlyByExistingAppend)
from ..helper import (Option_fromValueWithDefault, Update_UpdateOptions)
from .comment import (Comment, Comment_reflection)
from .ontology_annotation import (OntologyAnnotation, OntologyAnnotation_reflection)

def _expr300() -> TypeInfo:
    return record_type("ARCtrl.ISA.Factor", [], Factor, lambda: [("ID", option_type(string_type)), ("Name", option_type(string_type)), ("FactorType", option_type(OntologyAnnotation_reflection())), ("Comments", option_type(array_type(Comment_reflection())))])


@dataclass(eq = False, repr = False, slots = True)
class Factor(Record):
    ID: str | None
    Name: str | None
    FactorType: OntologyAnnotation | None
    Comments: Array[Comment] | None
    @staticmethod
    def make(id: str | None=None, name: str | None=None, factor_type: OntologyAnnotation | None=None, comments: Array[Comment] | None=None) -> Factor:
        return Factor(id, name, factor_type, comments)

    @staticmethod
    def create(Id: str | None=None, Name: str | None=None, FactorType: OntologyAnnotation | None=None, Comments: Array[Comment] | None=None) -> Factor:
        return Factor.make(Id, Name, FactorType, Comments)

    @staticmethod
    def empty() -> Factor:
        return Factor.create()

    @staticmethod
    def from_string(name: str, term: str, source: str, accession: str, comments: Array[Comment] | None=None) -> Factor:
        oa: OntologyAnnotation = OntologyAnnotation.from_string(term, source, accession, comments)
        name_1: str | None = Option_fromValueWithDefault("", name)
        factor_type: OntologyAnnotation | None = Option_fromValueWithDefault(OntologyAnnotation.empty(), oa)
        return Factor.make(None, name_1, factor_type, None)

    @staticmethod
    def to_string(factor: Factor) -> dict[str, Any]:
        value: dict[str, Any] = {
            "TermAccessionNumber": "",
            "TermName": "",
            "TermSourceREF": ""
        }
        def mapping(oa: OntologyAnnotation) -> dict[str, Any]:
            return OntologyAnnotation.to_string(oa)

        return default_arg(map(mapping, factor.FactorType), value)

    @property
    def NameText(self, __unit: None=None) -> str:
        this: Factor = self
        return default_arg(this.Name, "")

    def MapCategory(self, f: Callable[[OntologyAnnotation], OntologyAnnotation]) -> Factor:
        this: Factor = self
        return Factor(this.ID, this.Name, map(f, this.FactorType), this.Comments)

    def SetCategory(self, c: OntologyAnnotation) -> Factor:
        this: Factor = self
        return Factor(this.ID, this.Name, c, this.Comments)

    @staticmethod
    def try_get_by_name(name: str, factors: FSharpList[Factor]) -> Factor | None:
        def _arrow296(f: Factor) -> bool:
            return equals(f.Name, name)

        return try_find(_arrow296, factors)

    @staticmethod
    def exists_by_name(name: str, factors: FSharpList[Factor]) -> bool:
        def _arrow297(f: Factor) -> bool:
            return equals(f.Name, name)

        return exists(_arrow297, factors)

    @staticmethod
    def add(factors: FSharpList[Factor], factor: Factor) -> FSharpList[Factor]:
        return append(factors, singleton(factor))

    @staticmethod
    def update_by(predicate: Callable[[Factor], bool], update_option: Update_UpdateOptions, factor: Factor, factors: FSharpList[Factor]) -> FSharpList[Factor]:
        def _arrow298(f: Factor) -> Factor:
            if predicate(f):
                this: Update_UpdateOptions = update_option
                record_type_1: Factor = f
                record_type_2: Factor = factor
                if this.tag == 2:
                    return make_record(Factor_reflection(), map2(Update_updateAppend, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                elif this.tag == 1:
                    return make_record(Factor_reflection(), map2(Update_updateOnlyByExisting, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                elif this.tag == 3:
                    return make_record(Factor_reflection(), map2(Update_updateOnlyByExistingAppend, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                else: 
                    return record_type_2


            else: 
                return f


        return map_1(_arrow298, factors) if exists(predicate, factors) else factors

    @staticmethod
    def update_by_name(update_option: Update_UpdateOptions, factor: Factor, factors: FSharpList[Factor]) -> FSharpList[Factor]:
        def predicate(f: Factor) -> bool:
            return equals(f.Name, factor.Name)

        return Factor.update_by(predicate, update_option, factor, factors)

    @staticmethod
    def remove_by_name(name: str, factors: FSharpList[Factor]) -> FSharpList[Factor]:
        def _arrow299(f: Factor) -> bool:
            return not equals(f.Name, name)

        return filter(_arrow299, factors)

    @staticmethod
    def get_comments(factor: Factor) -> Array[Comment] | None:
        return factor.Comments

    @staticmethod
    def map_comments(f: Callable[[Array[Comment]], Array[Comment]], factor: Factor) -> Factor:
        return Factor(factor.ID, factor.Name, factor.FactorType, map(f, factor.Comments))

    @staticmethod
    def set_comments(factor: Factor, comments: Array[Comment]) -> Factor:
        return Factor(factor.ID, factor.Name, factor.FactorType, comments)

    @staticmethod
    def get_factor_type(factor: Factor) -> OntologyAnnotation | None:
        return factor.FactorType

    @staticmethod
    def map_factor_type(f: Callable[[OntologyAnnotation], OntologyAnnotation], factor: Factor) -> Factor:
        return Factor(factor.ID, factor.Name, map(f, factor.FactorType), factor.Comments)

    @staticmethod
    def set_factor_type(factor: Factor, factor_type: OntologyAnnotation) -> Factor:
        return Factor(factor.ID, factor.Name, factor_type, factor.Comments)

    @staticmethod
    def try_get_name(f: Factor) -> str | None:
        return f.Name

    @staticmethod
    def get_name_as_string(f: Factor) -> str:
        return f.NameText

    @staticmethod
    def name_equals_string(name: str, f: Factor) -> bool:
        return f.NameText == name

    def Copy(self, __unit: None=None) -> Factor:
        this: Factor = self
        def mapping_1(array: Array[Comment]) -> Array[Comment]:
            def mapping(c: Comment, array: Any=array) -> Comment:
                return c.Copy()

            return map_2(mapping, array, None)

        comments: Array[Comment] | None = map(mapping_1, this.Comments)
        return Factor.make(this.ID, this.Name, this.FactorType, comments)

    def Print(self, __unit: None=None) -> str:
        this: Factor = self
        return to_string(this)

    def PrintCompact(self, __unit: None=None) -> str:
        this: Factor = self
        return "OA " + this.NameText


Factor_reflection = _expr300

__all__ = ["Factor_reflection"]

