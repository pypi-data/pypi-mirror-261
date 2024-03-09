from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any
from ....fable_modules.fable_library.array_ import (try_find, exists, map, map2, filter, try_pick, append as append_1)
from ....fable_modules.fable_library.list import (append, singleton, FSharpList)
from ....fable_modules.fable_library.option import (value as value_2, default_arg, map as map_1)
from ....fable_modules.fable_library.reflection import (make_record, get_record_fields, TypeInfo, string_type, option_type, array_type, record_type)
from ....fable_modules.fable_library.seq import (to_array, delay, append as append_2, singleton as singleton_1)
from ....fable_modules.fable_library.string_ import ends_with
from ....fable_modules.fable_library.types import (Array, Record)
from ....fable_modules.fable_library.util import (equals, number_hash, IEnumerable_1)
from ..helper import (Update_updateAppend, Update_updateOnlyByExisting, Update_updateOnlyByExistingAppend)
from ..helper import (Update_UpdateOptions, Option_mapDefault, Option_fromValueWithDefault, HashCodes_boxHashArray, HashCodes_boxHashOption, HashCodes_hash)
from .comment import (Comment, Comment_reflection)
from .ontology_annotation import (OntologyAnnotation, OntologyAnnotation_reflection)

def _expr344() -> TypeInfo:
    return record_type("ARCtrl.ISA.Person", [], Person, lambda: [("ID", option_type(string_type)), ("ORCID", option_type(string_type)), ("LastName", option_type(string_type)), ("FirstName", option_type(string_type)), ("MidInitials", option_type(string_type)), ("EMail", option_type(string_type)), ("Phone", option_type(string_type)), ("Fax", option_type(string_type)), ("Address", option_type(string_type)), ("Affiliation", option_type(string_type)), ("Roles", option_type(array_type(OntologyAnnotation_reflection()))), ("Comments", option_type(array_type(Comment_reflection())))])


@dataclass(eq = False, repr = False, slots = True)
class Person(Record):
    ID: str | None
    ORCID: str | None
    LastName: str | None
    FirstName: str | None
    MidInitials: str | None
    EMail: str | None
    Phone: str | None
    Fax: str | None
    Address: str | None
    Affiliation: str | None
    Roles: Array[OntologyAnnotation] | None
    Comments: Array[Comment] | None
    @staticmethod
    def make(id: str | None=None, orcid: str | None=None, last_name: str | None=None, first_name: str | None=None, mid_initials: str | None=None, email: str | None=None, phone: str | None=None, fax: str | None=None, address: str | None=None, affiliation: str | None=None, roles: Array[OntologyAnnotation] | None=None, comments: Array[Comment] | None=None) -> Person:
        return Person(id, orcid, last_name, first_name, mid_initials, email, phone, fax, address, affiliation, roles, comments)

    @staticmethod
    def create(Id: str | None=None, ORCID: str | None=None, LastName: str | None=None, FirstName: str | None=None, MidInitials: str | None=None, Email: str | None=None, Phone: str | None=None, Fax: str | None=None, Address: str | None=None, Affiliation: str | None=None, Roles: Array[OntologyAnnotation] | None=None, Comments: Array[Comment] | None=None) -> Person:
        return Person.make(Id, ORCID, LastName, FirstName, MidInitials, Email, Phone, Fax, Address, Affiliation, Roles, Comments)

    @staticmethod
    def empty() -> Person:
        return Person.create()

    @staticmethod
    def try_get_by_full_name(first_name: str, mid_initials: str, last_name: str, persons: Array[Person]) -> Person | None:
        def _arrow323(p: Person) -> bool:
            return (equals(p.LastName, last_name) if equals(p.FirstName, first_name) else False) if (mid_initials == "") else (equals(p.LastName, last_name) if (equals(p.MidInitials, mid_initials) if equals(p.FirstName, first_name) else False) else False)

        return try_find(_arrow323, persons)

    @staticmethod
    def exists_by_full_name(first_name: str, mid_initials: str, last_name: str, persons: Array[Person]) -> bool:
        def _arrow324(p: Person) -> bool:
            return (equals(p.LastName, last_name) if equals(p.FirstName, first_name) else False) if (mid_initials == "") else (equals(p.LastName, last_name) if (equals(p.MidInitials, mid_initials) if equals(p.FirstName, first_name) else False) else False)

        return exists(_arrow324, persons)

    @staticmethod
    def add(persons: FSharpList[Person], person: Person) -> FSharpList[Person]:
        return append(persons, singleton(person))

    @staticmethod
    def update_by(predicate: Callable[[Person], bool], update_option: Update_UpdateOptions, person: Person, persons: Array[Person]) -> Array[Person]:
        def mapping_3(p: Person) -> Person:
            if predicate(p):
                this: Update_UpdateOptions = update_option
                record_type_1: Person = p
                record_type_2: Person = person
                if this.tag == 2:
                    def mapping(old_val: Any=None, new_val: Any=None, p: Any=p) -> Any:
                        return Update_updateAppend(old_val, new_val)

                    return make_record(Person_reflection(), map2(mapping, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                elif this.tag == 1:
                    def mapping_1(old_val_1: Any=None, new_val_1: Any=None, p: Any=p) -> Any:
                        return Update_updateOnlyByExisting(old_val_1, new_val_1)

                    return make_record(Person_reflection(), map2(mapping_1, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                elif this.tag == 3:
                    def mapping_2(old_val_2: Any=None, new_val_2: Any=None, p: Any=p) -> Any:
                        return Update_updateOnlyByExistingAppend(old_val_2, new_val_2)

                    return make_record(Person_reflection(), map2(mapping_2, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                else: 
                    return record_type_2


            else: 
                return p


        return map(mapping_3, persons, None) if exists(predicate, persons) else persons

    @staticmethod
    def update_by_full_name(update_option: Update_UpdateOptions, person: Person, persons: Array[Person]) -> Array[Person]:
        def predicate(p: Person) -> bool:
            if equals(p.MidInitials, person.MidInitials) if equals(p.FirstName, person.FirstName) else False:
                return equals(p.LastName, person.LastName)

            else: 
                return False


        return Person.update_by(predicate, update_option, person, persons)

    @staticmethod
    def remove_by_full_name(first_name: str, mid_initials: str, last_name: str, persons: Array[Person]) -> Array[Person]:
        def _arrow325(p: Person) -> bool:
            return (not (equals(p.LastName, last_name) if equals(p.FirstName, first_name) else False)) if (mid_initials == "") else (not (equals(p.LastName, last_name) if (equals(p.MidInitials, mid_initials) if equals(p.FirstName, first_name) else False) else False))

        return filter(_arrow325, persons)

    @staticmethod
    def get_roles(person: Person) -> Array[OntologyAnnotation] | None:
        return person.Roles

    @staticmethod
    def map_roles(f: Callable[[Array[OntologyAnnotation]], Array[OntologyAnnotation]], person: Person) -> Person:
        return Person(person.ID, person.ORCID, person.LastName, person.FirstName, person.MidInitials, person.EMail, person.Phone, person.Fax, person.Address, person.Affiliation, Option_mapDefault([], f, person.Roles), person.Comments)

    @staticmethod
    def set_roles(person: Person, roles: Array[OntologyAnnotation]) -> Person:
        return Person(person.ID, person.ORCID, person.LastName, person.FirstName, person.MidInitials, person.EMail, person.Phone, person.Fax, person.Address, person.Affiliation, roles, person.Comments)

    @staticmethod
    def get_comments(person: Person) -> Array[Comment] | None:
        return person.Comments

    @staticmethod
    def map_comments(f: Callable[[Array[Comment]], Array[Comment]], person: Person) -> Person:
        return Person(person.ID, person.ORCID, person.LastName, person.FirstName, person.MidInitials, person.EMail, person.Phone, person.Fax, person.Address, person.Affiliation, person.Roles, Option_mapDefault([], f, person.Comments))

    @staticmethod
    def set_comments(person: Person, comments: Array[Comment]) -> Person:
        return Person(person.ID, person.ORCID, person.LastName, person.FirstName, person.MidInitials, person.EMail, person.Phone, person.Fax, person.Address, person.Affiliation, person.Roles, comments)

    @staticmethod
    def orcid_key() -> str:
        return "ORCID"

    @staticmethod
    def set_orcid_from_comments(person: Person) -> Person:
        def is_orcid_comment(c: Comment) -> bool:
            if c.Name is not None:
                return ends_with(value_2(c.Name).upper(), Person.orcid_key())

            else: 
                return False


        def mapping(comments: Array[Comment]) -> tuple[str | None, Array[Comment] | None]:
            def chooser(c_1: Comment, comments: Any=comments) -> str | None:
                if is_orcid_comment(c_1):
                    return c_1.Value

                else: 
                    return None


            def predicate(arg: Comment, comments: Any=comments) -> bool:
                return not is_orcid_comment(arg)

            return (try_pick(chooser, comments), Option_fromValueWithDefault([], filter(predicate, comments)))

        pattern_input: tuple[str | None, Array[Comment] | None] = default_arg(map_1(mapping, person.Comments), (None, person.Comments))
        return Person(person.ID, pattern_input[0], person.LastName, person.FirstName, person.MidInitials, person.EMail, person.Phone, person.Fax, person.Address, person.Affiliation, person.Roles, pattern_input[1])

    @staticmethod
    def set_comment_from_orcid(person: Person) -> Person:
        def _arrow328(__unit: None=None) -> Array[Comment] | None:
            matchValue: str | None = person.ORCID
            matchValue_1: Array[Comment] | None = person.Comments
            def _arrow326(__unit: None=None) -> Array[Comment] | None:
                orcid_1: str = matchValue
                return [Comment.create(None, Person.orcid_key(), orcid_1)]

            def _arrow327(__unit: None=None) -> Array[Comment] | None:
                comments: Array[Comment] = matchValue_1
                orcid: str = matchValue
                return append_1(comments, [Comment.create(None, Person.orcid_key(), orcid)], None)

            return matchValue_1 if (matchValue is None) else (_arrow326() if (matchValue_1 is None) else _arrow327())

        return Person(person.ID, person.ORCID, person.LastName, person.FirstName, person.MidInitials, person.EMail, person.Phone, person.Fax, person.Address, person.Affiliation, person.Roles, _arrow328())

    def Copy(self, __unit: None=None) -> Person:
        this: Person = self
        def mapping_1(array: Array[Comment]) -> Array[Comment]:
            def mapping(c: Comment, array: Any=array) -> Comment:
                return c.Copy()

            return map(mapping, array, None)

        next_comments: Array[Comment] | None = map_1(mapping_1, this.Comments)
        def mapping_3(array_1: Array[OntologyAnnotation]) -> Array[OntologyAnnotation]:
            def mapping_2(c_1: OntologyAnnotation, array_1: Any=array_1) -> OntologyAnnotation:
                return c_1.Copy()

            return map(mapping_2, array_1, None)

        roles: Array[OntologyAnnotation] | None = map_1(mapping_3, this.Roles)
        return Person.make(this.ID, this.ORCID, this.LastName, this.FirstName, this.MidInitials, this.EMail, this.Phone, this.Fax, this.Address, this.Affiliation, roles, next_comments)

    def __hash__(self, __unit: None=None) -> Any:
        this: Person = self
        def _arrow341(__unit: None=None) -> IEnumerable_1[Any]:
            def _arrow340(__unit: None=None) -> IEnumerable_1[Any]:
                def _arrow339(__unit: None=None) -> IEnumerable_1[Any]:
                    def _arrow338(__unit: None=None) -> IEnumerable_1[Any]:
                        def _arrow337(__unit: None=None) -> IEnumerable_1[Any]:
                            def _arrow336(__unit: None=None) -> IEnumerable_1[Any]:
                                def _arrow335(__unit: None=None) -> IEnumerable_1[Any]:
                                    def _arrow334(__unit: None=None) -> IEnumerable_1[Any]:
                                        def _arrow333(__unit: None=None) -> IEnumerable_1[Any]:
                                            def _arrow332(__unit: None=None) -> IEnumerable_1[Any]:
                                                def _arrow329(__unit: None=None) -> int:
                                                    copy_of_struct: int = 0
                                                    return number_hash(copy_of_struct)

                                                def _arrow331(__unit: None=None) -> IEnumerable_1[Any]:
                                                    def _arrow330(__unit: None=None) -> int:
                                                        copy_of_struct_1: int = 0
                                                        return number_hash(copy_of_struct_1)

                                                    return singleton_1(HashCodes_boxHashArray(value_2(this.Comments))) if (this.Comments is not None) else singleton_1(_arrow330())

                                                return append_2(singleton_1(HashCodes_boxHashArray(value_2(this.Roles))) if (this.Roles is not None) else singleton_1(_arrow329()), delay(_arrow331))

                                            return append_2(singleton_1(HashCodes_boxHashOption(this.Affiliation)), delay(_arrow332))

                                        return append_2(singleton_1(HashCodes_boxHashOption(this.Address)), delay(_arrow333))

                                    return append_2(singleton_1(HashCodes_boxHashOption(this.Fax)), delay(_arrow334))

                                return append_2(singleton_1(HashCodes_boxHashOption(this.Phone)), delay(_arrow335))

                            return append_2(singleton_1(HashCodes_boxHashOption(this.EMail)), delay(_arrow336))

                        return append_2(singleton_1(HashCodes_boxHashOption(this.MidInitials)), delay(_arrow337))

                    return append_2(singleton_1(HashCodes_boxHashOption(this.FirstName)), delay(_arrow338))

                return append_2(singleton_1(HashCodes_boxHashOption(this.LastName)), delay(_arrow339))

            return append_2(singleton_1(HashCodes_boxHashOption(this.ORCID)), delay(_arrow340))

        return HashCodes_boxHashArray(to_array(delay(_arrow341)))

    def __eq__(self, obj: Any=None) -> bool:
        this: Person = self
        return HashCodes_hash(this) == HashCodes_hash(obj)


Person_reflection = _expr344

__all__ = ["Person_reflection"]

