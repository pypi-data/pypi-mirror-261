from __future__ import annotations as annotations_2
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any
from ....fable_modules.fable_library.array_ import (map2, map as map_2)
from ....fable_modules.fable_library.list import (try_find, FSharpList, exists, append, singleton, map, filter)
from ....fable_modules.fable_library.option import (default_arg, value as value_4, map as map_1)
from ....fable_modules.fable_library.reflection import (make_record, get_record_fields, TypeInfo, string_type, option_type, array_type, record_type)
from ....fable_modules.fable_library.types import (Array, to_string, Record)
from ....fable_modules.fable_library.util import (string_hash, equals)
from ..helper import (Update_updateAppend, Update_updateOnlyByExisting, Update_updateOnlyByExistingAppend)
from ..helper import (Update_UpdateOptions, Option_mapDefault)
from ..regex import (try_parse_term_annotation, ActivePatterns__007CRegex_007C__007C, Pattern_TermAnnotationShortPattern)
from .comment import (Comment, Comment_reflection)

def _expr289() -> TypeInfo:
    return record_type("ARCtrl.ISA.OntologyAnnotation", [], OntologyAnnotation, lambda: [("ID", option_type(string_type)), ("Name", option_type(string_type)), ("TermSourceREF", option_type(string_type)), ("TermAccessionNumber", option_type(string_type)), ("Comments", option_type(array_type(Comment_reflection())))])


@dataclass(eq = False, repr = False, slots = True)
class OntologyAnnotation(Record):
    ID: str | None
    Name: str | None
    TermSourceREF: str | None
    TermAccessionNumber: str | None
    Comments: Array[Comment] | None
    @staticmethod
    def make(id: str | None=None, name: str | None=None, term_source_ref: str | None=None, term_accession_number: str | None=None, comments: Array[Comment] | None=None) -> OntologyAnnotation:
        return OntologyAnnotation(id, name, term_source_ref, term_accession_number, comments)

    @staticmethod
    def create(Id: str | None=None, Name: str | None=None, TermSourceREF: str | None=None, TermAccessionNumber: str | None=None, Comments: Array[Comment] | None=None) -> OntologyAnnotation:
        return OntologyAnnotation.make(Id, Name, TermSourceREF, TermAccessionNumber, Comments)

    @staticmethod
    def empty() -> OntologyAnnotation:
        return OntologyAnnotation.create()

    @property
    def TANInfo(self, __unit: None=None) -> dict[str, Any] | None:
        this: OntologyAnnotation = self
        match_value: str | None = this.TermAccessionNumber
        return None if (match_value is None) else try_parse_term_annotation(match_value)

    @property
    def NameText(self, __unit: None=None) -> str:
        this: OntologyAnnotation = self
        return default_arg(this.Name, "")

    @property
    def TermSourceREFString(self, __unit: None=None) -> str:
        this: OntologyAnnotation = self
        return default_arg(this.TermSourceREF, "")

    @property
    def TermAccessionString(self, __unit: None=None) -> str:
        this: OntologyAnnotation = self
        return default_arg(this.TermAccessionNumber, "")

    @staticmethod
    def create_uri_annotation(term_source_ref: str, local_tan: str) -> str:
        return ((((("" + "http://purl.obolibrary.org/obo/") + "") + term_source_ref) + "_") + local_tan) + ""

    @staticmethod
    def from_string(term_name: str | None=None, tsr: str | None=None, tan: str | None=None, comments: Array[Comment] | None=None) -> OntologyAnnotation:
        return OntologyAnnotation.make(None, term_name, tsr, tan, comments)

    @staticmethod
    def from_term_annotation(term_annotation: str) -> OntologyAnnotation:
        r: dict[str, Any] = value_4(try_parse_term_annotation(term_annotation))
        accession: str = (r["IDSpace"] + ":") + r["LocalID"]
        return OntologyAnnotation.from_string("", r["IDSpace"], accession)

    @property
    def TermAccessionShort(self, __unit: None=None) -> str:
        this: OntologyAnnotation = self
        match_value: dict[str, Any] | None = this.TANInfo
        if match_value is not None:
            id: dict[str, Any] = match_value
            return ((("" + id["IDSpace"]) + ":") + id["LocalID"]) + ""

        else: 
            return ""


    @property
    def TermAccessionOntobeeUrl(self, __unit: None=None) -> str:
        this: OntologyAnnotation = self
        match_value: dict[str, Any] | None = this.TANInfo
        if match_value is not None:
            id: dict[str, Any] = match_value
            return OntologyAnnotation.create_uri_annotation(id["IDSpace"], id["LocalID"])

        else: 
            return ""


    @property
    def TermAccessionAndOntobeeUrlIfShort(self, __unit: None=None) -> str:
        this: OntologyAnnotation = self
        match_value: str | None = this.TermAccessionNumber
        if match_value is not None:
            tan: str = match_value
            return this.TermAccessionOntobeeUrl if (ActivePatterns__007CRegex_007C__007C(Pattern_TermAnnotationShortPattern, tan) is not None) else tan

        else: 
            return ""


    @staticmethod
    def to_string(oa: OntologyAnnotation, as_ontobee_purl_url_if_short: bool | None=None) -> dict[str, Any]:
        as_ontobee_purl_url_if_short_1: bool = default_arg(as_ontobee_purl_url_if_short, False)
        TermName: str = default_arg(oa.Name, "")
        TermSourceREF: str = default_arg(oa.TermSourceREF, "")
        def _arrow285(__unit: None=None) -> str:
            url: str = oa.TermAccessionAndOntobeeUrlIfShort
            return default_arg(oa.TermAccessionNumber, "") if (url == "") else url

        return {
            "TermAccessionNumber": _arrow285() if as_ontobee_purl_url_if_short_1 else default_arg(oa.TermAccessionNumber, ""),
            "TermName": TermName,
            "TermSourceREF": TermSourceREF
        }

    def __eq__(self, other: Any=None) -> bool:
        this: OntologyAnnotation = self
        if isinstance(other, OntologyAnnotation):
            return this.System_IEquatable_1_Equals2B595(other)

        elif str(type(other)) == "<class \'str\'>":
            s: str = other
            return True if (True if (this.NameText == s) else (this.TermAccessionShort == s)) else (this.TermAccessionOntobeeUrl == s)

        else: 
            return False


    def __hash__(self, __unit: None=None) -> int:
        this: OntologyAnnotation = self
        return string_hash(this.NameText + this.TermAccessionShort)

    @staticmethod
    def try_get_name(oa: OntologyAnnotation) -> str | None:
        return oa.Name

    @staticmethod
    def get_name_text(oa: OntologyAnnotation) -> str:
        return oa.NameText

    @staticmethod
    def name_equals_string(name: str, oa: OntologyAnnotation) -> bool:
        return oa.NameText == name

    @staticmethod
    def try_get_by_name(name: str, annotations: FSharpList[OntologyAnnotation]) -> OntologyAnnotation | None:
        def _arrow286(d: OntologyAnnotation) -> bool:
            return equals(d.Name, name)

        return try_find(_arrow286, annotations)

    @staticmethod
    def exists_by_name(name: str, annotations: FSharpList[OntologyAnnotation]) -> bool:
        def _arrow287(d: OntologyAnnotation) -> bool:
            return equals(d.Name, name)

        return exists(_arrow287, annotations)

    @staticmethod
    def add(onotolgy_annotations: FSharpList[OntologyAnnotation], onotolgy_annotation: OntologyAnnotation) -> FSharpList[OntologyAnnotation]:
        return append(onotolgy_annotations, singleton(onotolgy_annotation))

    @staticmethod
    def update_by(predicate: Callable[[OntologyAnnotation], bool], update_option: Update_UpdateOptions, design: OntologyAnnotation, annotations: FSharpList[OntologyAnnotation]) -> FSharpList[OntologyAnnotation]:
        def mapping_3(d: OntologyAnnotation) -> OntologyAnnotation:
            if predicate(d):
                this: Update_UpdateOptions = update_option
                record_type_1: OntologyAnnotation = d
                record_type_2: OntologyAnnotation = design
                if this.tag == 2:
                    def mapping(old_val: Any=None, new_val: Any=None, d: Any=d) -> Any:
                        return Update_updateAppend(old_val, new_val)

                    return make_record(OntologyAnnotation_reflection(), map2(mapping, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                elif this.tag == 1:
                    def mapping_1(old_val_1: Any=None, new_val_1: Any=None, d: Any=d) -> Any:
                        return Update_updateOnlyByExisting(old_val_1, new_val_1)

                    return make_record(OntologyAnnotation_reflection(), map2(mapping_1, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                elif this.tag == 3:
                    def mapping_2(old_val_2: Any=None, new_val_2: Any=None, d: Any=d) -> Any:
                        return Update_updateOnlyByExistingAppend(old_val_2, new_val_2)

                    return make_record(OntologyAnnotation_reflection(), map2(mapping_2, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                else: 
                    return record_type_2


            else: 
                return d


        return map(mapping_3, annotations) if exists(predicate, annotations) else annotations

    @staticmethod
    def update_by_name(update_option: Update_UpdateOptions, design: OntologyAnnotation, annotations: FSharpList[OntologyAnnotation]) -> FSharpList[OntologyAnnotation]:
        def predicate(f: OntologyAnnotation) -> bool:
            return equals(f.Name, design.Name)

        return OntologyAnnotation.update_by(predicate, update_option, design, annotations)

    @staticmethod
    def remove_by_name(name: str, annotations: FSharpList[OntologyAnnotation]) -> FSharpList[OntologyAnnotation]:
        def _arrow288(d: OntologyAnnotation) -> bool:
            return not equals(d.Name, name)

        return filter(_arrow288, annotations)

    @staticmethod
    def get_comments(annotation: OntologyAnnotation) -> Array[Comment] | None:
        return annotation.Comments

    @staticmethod
    def map_comments(f: Callable[[Array[Comment]], Array[Comment]], annotation: OntologyAnnotation) -> OntologyAnnotation:
        return OntologyAnnotation(annotation.ID, annotation.Name, annotation.TermSourceREF, annotation.TermAccessionNumber, Option_mapDefault([], f, annotation.Comments))

    @staticmethod
    def set_comments(annotation: OntologyAnnotation, comments: Array[Comment]) -> OntologyAnnotation:
        return OntologyAnnotation(annotation.ID, annotation.Name, annotation.TermSourceREF, annotation.TermAccessionNumber, comments)

    def Copy(self, __unit: None=None) -> OntologyAnnotation:
        this: OntologyAnnotation = self
        def mapping_1(array: Array[Comment]) -> Array[Comment]:
            def mapping(c: Comment, array: Any=array) -> Comment:
                return c.Copy()

            return map_2(mapping, array, None)

        comments: Array[Comment] | None = map_1(mapping_1, this.Comments)
        return OntologyAnnotation.make(this.ID, this.Name, this.TermSourceREF, this.TermAccessionNumber, comments)

    def Print(self, __unit: None=None) -> str:
        this: OntologyAnnotation = self
        return to_string(this)

    def PrintCompact(self, __unit: None=None) -> str:
        this: OntologyAnnotation = self
        return "OA " + this.NameText

    def System_IEquatable_1_Equals2B595(self, other: OntologyAnnotation) -> bool:
        this: OntologyAnnotation = self
        return (True if (other.TermAccessionShort == this.TermAccessionShort) else (other.TermAccessionOntobeeUrl == this.TermAccessionOntobeeUrl)) if ((other.TermAccessionNumber is not None) if (this.TermAccessionNumber is not None) else False) else ((other.NameText == this.NameText) if ((other.Name is not None) if (this.Name is not None) else False) else (True if ((other.Name is None) if ((this.Name is None) if ((other.TermAccessionNumber is None) if (this.TermAccessionNumber is None) else False) else False) else False) else False))


OntologyAnnotation_reflection = _expr289

__all__ = ["OntologyAnnotation_reflection"]

