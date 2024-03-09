from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any
from ....fable_modules.fable_library.array_ import (map2, map as map_2)
from ....fable_modules.fable_library.list import (try_find, FSharpList, exists, append, singleton, map, filter)
from ....fable_modules.fable_library.option import map as map_1
from ....fable_modules.fable_library.reflection import (make_record, get_record_fields, TypeInfo, string_type, option_type, array_type, record_type)
from ....fable_modules.fable_library.types import (Array, Record)
from ....fable_modules.fable_library.util import equals
from ..helper import (Update_updateAppend, Update_updateOnlyByExisting, Update_updateOnlyByExistingAppend)
from ..helper import (Update_UpdateOptions, Option_mapDefault)
from .comment import (Comment, Comment_reflection)

def _expr284() -> TypeInfo:
    return record_type("ARCtrl.ISA.OntologySourceReference", [], OntologySourceReference, lambda: [("Description", option_type(string_type)), ("File", option_type(string_type)), ("Name", option_type(string_type)), ("Version", option_type(string_type)), ("Comments", option_type(array_type(Comment_reflection())))])


@dataclass(eq = False, repr = False, slots = True)
class OntologySourceReference(Record):
    Description: str | None
    File: str | None
    Name: str | None
    Version: str | None
    Comments: Array[Comment] | None
    @staticmethod
    def make(description: str | None=None, file: str | None=None, name: str | None=None, version: str | None=None, comments: Array[Comment] | None=None) -> OntologySourceReference:
        return OntologySourceReference(description, file, name, version, comments)

    @staticmethod
    def create(Description: str | None=None, File: str | None=None, Name: str | None=None, Version: str | None=None, Comments: Array[Comment] | None=None) -> OntologySourceReference:
        return OntologySourceReference.make(Description, File, Name, Version, Comments)

    @staticmethod
    def empty() -> OntologySourceReference:
        return OntologySourceReference.create()

    @staticmethod
    def try_get_by_name(name: str, ontologies: FSharpList[OntologySourceReference]) -> OntologySourceReference | None:
        def _arrow281(t: OntologySourceReference) -> bool:
            return equals(t.Name, name)

        return try_find(_arrow281, ontologies)

    @staticmethod
    def exists_by_name(name: str, ontologies: FSharpList[OntologySourceReference]) -> bool:
        def _arrow282(t: OntologySourceReference) -> bool:
            return equals(t.Name, name)

        return exists(_arrow282, ontologies)

    @staticmethod
    def add(ontology_source_reference: OntologySourceReference, ontologies: FSharpList[OntologySourceReference]) -> FSharpList[OntologySourceReference]:
        return append(ontologies, singleton(ontology_source_reference))

    @staticmethod
    def update_by(predicate: Callable[[OntologySourceReference], bool], update_option: Update_UpdateOptions, ontology_source_reference: OntologySourceReference, ontologies: FSharpList[OntologySourceReference]) -> FSharpList[OntologySourceReference]:
        def mapping_3(t: OntologySourceReference) -> OntologySourceReference:
            if predicate(t):
                this: Update_UpdateOptions = update_option
                record_type_1: OntologySourceReference = t
                record_type_2: OntologySourceReference = ontology_source_reference
                if this.tag == 2:
                    def mapping(old_val: Any=None, new_val: Any=None, t: Any=t) -> Any:
                        return Update_updateAppend(old_val, new_val)

                    return make_record(OntologySourceReference_reflection(), map2(mapping, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                elif this.tag == 1:
                    def mapping_1(old_val_1: Any=None, new_val_1: Any=None, t: Any=t) -> Any:
                        return Update_updateOnlyByExisting(old_val_1, new_val_1)

                    return make_record(OntologySourceReference_reflection(), map2(mapping_1, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                elif this.tag == 3:
                    def mapping_2(old_val_2: Any=None, new_val_2: Any=None, t: Any=t) -> Any:
                        return Update_updateOnlyByExistingAppend(old_val_2, new_val_2)

                    return make_record(OntologySourceReference_reflection(), map2(mapping_2, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                else: 
                    return record_type_2


            else: 
                return t


        return map(mapping_3, ontologies) if exists(predicate, ontologies) else ontologies

    @staticmethod
    def update_by_name(update_option: Update_UpdateOptions, ontology_source_reference: OntologySourceReference, ontologies: FSharpList[OntologySourceReference]) -> FSharpList[OntologySourceReference]:
        def predicate(t: OntologySourceReference) -> bool:
            return equals(t.Name, ontology_source_reference.Name)

        return OntologySourceReference.update_by(predicate, update_option, ontology_source_reference, ontologies)

    @staticmethod
    def remove_by_name(name: str, ontologies: FSharpList[OntologySourceReference]) -> FSharpList[OntologySourceReference]:
        def _arrow283(t: OntologySourceReference) -> bool:
            return not equals(t.Name, name)

        return filter(_arrow283, ontologies)

    @staticmethod
    def get_comments(ontology: OntologySourceReference) -> Array[Comment] | None:
        return ontology.Comments

    @staticmethod
    def map_comments(f: Callable[[Array[Comment]], Array[Comment]], ontology: OntologySourceReference) -> OntologySourceReference:
        return OntologySourceReference(ontology.Description, ontology.File, ontology.Name, ontology.Version, Option_mapDefault([], f, ontology.Comments))

    @staticmethod
    def set_comments(ontology: OntologySourceReference, comments: Array[Comment]) -> OntologySourceReference:
        return OntologySourceReference(ontology.Description, ontology.File, ontology.Name, ontology.Version, comments)

    def Copy(self, __unit: None=None) -> OntologySourceReference:
        this: OntologySourceReference = self
        def mapping_1(array: Array[Comment]) -> Array[Comment]:
            def mapping(c: Comment, array: Any=array) -> Comment:
                return c.Copy()

            return map_2(mapping, array, None)

        comments: Array[Comment] | None = map_1(mapping_1, this.Comments)
        return OntologySourceReference.make(this.Description, this.File, this.Name, this.Version, comments)


OntologySourceReference_reflection = _expr284

__all__ = ["OntologySourceReference_reflection"]

