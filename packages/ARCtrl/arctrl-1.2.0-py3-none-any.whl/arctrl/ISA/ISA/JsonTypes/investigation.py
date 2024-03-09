from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any
from ....fable_modules.fable_library.array_ import map2
from ....fable_modules.fable_library.list import (FSharpList, empty, map as map_1)
from ....fable_modules.fable_library.option import (default_arg, map)
from ....fable_modules.fable_library.reflection import (TypeInfo, string_type, option_type, list_type, record_type, make_record, get_record_fields)
from ....fable_modules.fable_library.string_ import to_fail
from ....fable_modules.fable_library.types import Record
from ..helper import (Update_updateAppend, Update_updateOnlyByExisting, Update_updateOnlyByExistingAppend)
from ..helper import (Option_mapDefault, Update_UpdateOptions)
from .comment import (Remark, Comment, Comment_reflection, Remark_reflection)
from .ontology_source_reference import (OntologySourceReference, OntologySourceReference_reflection)
from .person import (Person, Person_reflection)
from .publication import (Publication, Publication_reflection)
from .study import (Study, Study_reflection, Study_update_7312BC8B)

def _expr406() -> TypeInfo:
    return record_type("ARCtrl.ISA.Investigation", [], Investigation, lambda: [("ID", option_type(string_type)), ("FileName", option_type(string_type)), ("Identifier", option_type(string_type)), ("Title", option_type(string_type)), ("Description", option_type(string_type)), ("SubmissionDate", option_type(string_type)), ("PublicReleaseDate", option_type(string_type)), ("OntologySourceReferences", option_type(list_type(OntologySourceReference_reflection()))), ("Publications", option_type(list_type(Publication_reflection()))), ("Contacts", option_type(list_type(Person_reflection()))), ("Studies", option_type(list_type(Study_reflection()))), ("Comments", option_type(list_type(Comment_reflection()))), ("Remarks", list_type(Remark_reflection()))])


@dataclass(eq = False, repr = False, slots = True)
class Investigation(Record):
    ID: str | None
    FileName: str | None
    Identifier: str | None
    Title: str | None
    Description: str | None
    SubmissionDate: str | None
    PublicReleaseDate: str | None
    OntologySourceReferences: FSharpList[OntologySourceReference] | None
    Publications: FSharpList[Publication] | None
    Contacts: FSharpList[Person] | None
    Studies: FSharpList[Study] | None
    Comments: FSharpList[Comment] | None
    Remarks: FSharpList[Remark]

Investigation_reflection = _expr406

def Investigation_make(id: str | None, filename: str | None, identifier: str | None, title: str | None, description: str | None, submission_date: str | None, public_release_date: str | None, ontology_source_reference: FSharpList[OntologySourceReference] | None, publications: FSharpList[Publication] | None, contacts: FSharpList[Person] | None, studies: FSharpList[Study] | None, comments: FSharpList[Comment] | None, remarks: FSharpList[Remark]) -> Investigation:
    return Investigation(id, filename, identifier, title, description, submission_date, public_release_date, ontology_source_reference, publications, contacts, studies, comments, remarks)


def Investigation_create_4AD66BBE(Id: str | None=None, FileName: str | None=None, Identifier: str | None=None, Title: str | None=None, Description: str | None=None, SubmissionDate: str | None=None, PublicReleaseDate: str | None=None, OntologySourceReferences: FSharpList[OntologySourceReference] | None=None, Publications: FSharpList[Publication] | None=None, Contacts: FSharpList[Person] | None=None, Studies: FSharpList[Study] | None=None, Comments: FSharpList[Comment] | None=None, Remarks: FSharpList[Remark] | None=None) -> Investigation:
    return Investigation_make(Id, FileName, Identifier, Title, Description, SubmissionDate, PublicReleaseDate, OntologySourceReferences, Publications, Contacts, Studies, Comments, default_arg(Remarks, empty()))


def Investigation_get_empty(__unit: None=None) -> Investigation:
    return Investigation_create_4AD66BBE()


def Investigation_getContacts_33B81164(investigation: Investigation) -> FSharpList[Person] | None:
    return investigation.Contacts


def Investigation_mapContacts(f: Callable[[FSharpList[Person]], FSharpList[Person]], investigation: Investigation) -> Investigation:
    return Investigation(investigation.ID, investigation.FileName, investigation.Identifier, investigation.Title, investigation.Description, investigation.SubmissionDate, investigation.PublicReleaseDate, investigation.OntologySourceReferences, investigation.Publications, Option_mapDefault(empty(), f, investigation.Contacts), investigation.Studies, investigation.Comments, investigation.Remarks)


def Investigation_setContacts(investigation: Investigation, persons: FSharpList[Person]) -> Investigation:
    return Investigation(investigation.ID, investigation.FileName, investigation.Identifier, investigation.Title, investigation.Description, investigation.SubmissionDate, investigation.PublicReleaseDate, investigation.OntologySourceReferences, investigation.Publications, persons, investigation.Studies, investigation.Comments, investigation.Remarks)


def Investigation_getPublications_33B81164(investigation: Investigation) -> FSharpList[Publication] | None:
    return investigation.Publications


def Investigation_mapPublications(f: Callable[[FSharpList[Publication]], FSharpList[Publication]], investigation: Investigation) -> Investigation:
    return Investigation(investigation.ID, investigation.FileName, investigation.Identifier, investigation.Title, investigation.Description, investigation.SubmissionDate, investigation.PublicReleaseDate, investigation.OntologySourceReferences, Option_mapDefault(empty(), f, investigation.Publications), investigation.Contacts, investigation.Studies, investigation.Comments, investigation.Remarks)


def Investigation_setPublications(investigation: Investigation, publications: FSharpList[Publication]) -> Investigation:
    return Investigation(investigation.ID, investigation.FileName, investigation.Identifier, investigation.Title, investigation.Description, investigation.SubmissionDate, investigation.PublicReleaseDate, investigation.OntologySourceReferences, publications, investigation.Contacts, investigation.Studies, investigation.Comments, investigation.Remarks)


def Investigation_getOntologies_33B81164(investigation: Investigation) -> FSharpList[OntologySourceReference] | None:
    return investigation.OntologySourceReferences


def Investigation_mapOntologies(f: Callable[[FSharpList[OntologySourceReference]], FSharpList[OntologySourceReference]], investigation: Investigation) -> Investigation:
    return Investigation(investigation.ID, investigation.FileName, investigation.Identifier, investigation.Title, investigation.Description, investigation.SubmissionDate, investigation.PublicReleaseDate, Option_mapDefault(empty(), f, investigation.OntologySourceReferences), investigation.Publications, investigation.Contacts, investigation.Studies, investigation.Comments, investigation.Remarks)


def Investigation_setOntologies(investigation: Investigation, ontologies: FSharpList[OntologySourceReference]) -> Investigation:
    return Investigation(investigation.ID, investigation.FileName, investigation.Identifier, investigation.Title, investigation.Description, investigation.SubmissionDate, investigation.PublicReleaseDate, ontologies, investigation.Publications, investigation.Contacts, investigation.Studies, investigation.Comments, investigation.Remarks)


def Investigation_getStudies_33B81164(investigation: Investigation) -> FSharpList[Study]:
    return default_arg(investigation.Studies, empty())


def Investigation_mapStudies(f: Callable[[FSharpList[Study]], FSharpList[Study]], investigation: Investigation) -> Investigation:
    return Investigation(investigation.ID, investigation.FileName, investigation.Identifier, investigation.Title, investigation.Description, investigation.SubmissionDate, investigation.PublicReleaseDate, investigation.OntologySourceReferences, investigation.Publications, investigation.Contacts, Option_mapDefault(empty(), f, investigation.Studies), investigation.Comments, investigation.Remarks)


def Investigation_setStudies(investigation: Investigation, studies: FSharpList[Study]) -> Investigation:
    return Investigation(investigation.ID, investigation.FileName, investigation.Identifier, investigation.Title, investigation.Description, investigation.SubmissionDate, investigation.PublicReleaseDate, investigation.OntologySourceReferences, investigation.Publications, investigation.Contacts, studies, investigation.Comments, investigation.Remarks)


def Investigation_getComments_33B81164(investigation: Investigation) -> FSharpList[Comment] | None:
    return investigation.Comments


def Investigation_mapComments(f: Callable[[FSharpList[Comment]], FSharpList[Comment]], investigation: Investigation) -> Investigation:
    return Investigation(investigation.ID, investigation.FileName, investigation.Identifier, investigation.Title, investigation.Description, investigation.SubmissionDate, investigation.PublicReleaseDate, investigation.OntologySourceReferences, investigation.Publications, investigation.Contacts, investigation.Studies, Option_mapDefault(empty(), f, investigation.Comments), investigation.Remarks)


def Investigation_setComments(investigation: Investigation, comments: FSharpList[Comment]) -> Investigation:
    return Investigation(investigation.ID, investigation.FileName, investigation.Identifier, investigation.Title, investigation.Description, investigation.SubmissionDate, investigation.PublicReleaseDate, investigation.OntologySourceReferences, investigation.Publications, investigation.Contacts, investigation.Studies, comments, investigation.Remarks)


def Investigation_getRemarks_33B81164(investigation: Investigation) -> FSharpList[Remark]:
    return investigation.Remarks


def Investigation_mapRemarks(f: Callable[[FSharpList[Remark]], FSharpList[Remark]], investigation: Investigation) -> Investigation:
    return Investigation(investigation.ID, investigation.FileName, investigation.Identifier, investigation.Title, investigation.Description, investigation.SubmissionDate, investigation.PublicReleaseDate, investigation.OntologySourceReferences, investigation.Publications, investigation.Contacts, investigation.Studies, investigation.Comments, f(investigation.Remarks))


def Investigation_setRemarks(investigation: Investigation, remarks: FSharpList[Remark]) -> Investigation:
    return Investigation(investigation.ID, investigation.FileName, investigation.Identifier, investigation.Title, investigation.Description, investigation.SubmissionDate, investigation.PublicReleaseDate, investigation.OntologySourceReferences, investigation.Publications, investigation.Contacts, investigation.Studies, investigation.Comments, remarks)


def Investigation_updateBy(update_option: Update_UpdateOptions, investigation: Investigation, new_investigation: Investigation) -> Investigation:
    this: Update_UpdateOptions = update_option
    record_type_1: Investigation = investigation
    record_type_2: Investigation = new_investigation
    if this.tag == 2:
        def mapping(old_val: Any=None, new_val: Any=None, update_option: Any=update_option, investigation: Any=investigation, new_investigation: Any=new_investigation) -> Any:
            return Update_updateAppend(old_val, new_val)

        return make_record(Investigation_reflection(), map2(mapping, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

    elif this.tag == 1:
        def mapping_1(old_val_1: Any=None, new_val_1: Any=None, update_option: Any=update_option, investigation: Any=investigation, new_investigation: Any=new_investigation) -> Any:
            return Update_updateOnlyByExisting(old_val_1, new_val_1)

        return make_record(Investigation_reflection(), map2(mapping_1, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

    elif this.tag == 3:
        def mapping_2(old_val_2: Any=None, new_val_2: Any=None, update_option: Any=update_option, investigation: Any=investigation, new_investigation: Any=new_investigation) -> Any:
            return Update_updateOnlyByExistingAppend(old_val_2, new_val_2)

        return make_record(Investigation_reflection(), map2(mapping_2, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

    else: 
        return record_type_2



def Investigation_update_33B81164(investigation: Investigation) -> Investigation:
    try: 
        def mapping_1(list_1: FSharpList[Study]) -> FSharpList[Study]:
            def mapping(study: Study, list_1: Any=list_1) -> Study:
                return Study_update_7312BC8B(study)

            return map_1(mapping, list_1)

        return Investigation(investigation.ID, investigation.FileName, investigation.Identifier, investigation.Title, investigation.Description, investigation.SubmissionDate, investigation.PublicReleaseDate, investigation.OntologySourceReferences, investigation.Publications, investigation.Contacts, map(mapping_1, investigation.Studies), investigation.Comments, investigation.Remarks)

    except Exception as err:
        return to_fail(((("Could not update investigation " + str(investigation.Identifier)) + ": \n") + str(err)) + "")



__all__ = ["Investigation_reflection", "Investigation_make", "Investigation_create_4AD66BBE", "Investigation_get_empty", "Investigation_getContacts_33B81164", "Investigation_mapContacts", "Investigation_setContacts", "Investigation_getPublications_33B81164", "Investigation_mapPublications", "Investigation_setPublications", "Investigation_getOntologies_33B81164", "Investigation_mapOntologies", "Investigation_setOntologies", "Investigation_getStudies_33B81164", "Investigation_mapStudies", "Investigation_setStudies", "Investigation_getComments_33B81164", "Investigation_mapComments", "Investigation_setComments", "Investigation_getRemarks_33B81164", "Investigation_mapRemarks", "Investigation_setRemarks", "Investigation_updateBy", "Investigation_update_33B81164"]

