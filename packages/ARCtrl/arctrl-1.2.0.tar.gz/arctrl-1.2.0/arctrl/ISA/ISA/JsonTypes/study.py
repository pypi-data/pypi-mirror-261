from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any
from ....fable_modules.fable_library.array_ import map2 as map2_2
from ....fable_modules.fable_library.list import (FSharpList, exists, append, singleton, map, filter, empty, collect)
from ....fable_modules.fable_library.option import (default_arg, map as map_1)
from ....fable_modules.fable_library.reflection import (TypeInfo, string_type, option_type, list_type, record_type, make_record, get_record_fields)
from ....fable_modules.fable_library.seq2 import List_distinct
from ....fable_modules.fable_library.string_ import to_fail
from ....fable_modules.fable_library.types import Record
from ....fable_modules.fable_library.util import (equals, structural_hash, safe_hash, string_hash)
from ..helper import (Update_updateAppend, Update_updateOnlyByExisting, Update_updateOnlyByExistingAppend, Dict_ofSeqWithMerge, Dict_tryFind)
from ..helper import (Update_UpdateOptions, Option_mapDefault, Option_fromValueWithDefault)
from .assay import (Assay, Assay_reflection, Assay_getProtocols_722A269D, Assay_getCharacteristics_722A269D, Assay_getFactors_722A269D, Assay_getUnitCategories_722A269D, Assay_getSources_722A269D, Assay_getSamples_722A269D, Assay_getMaterials_722A269D, Assay_updateProtocols, Assay_update_722A269D)
from .assay_materials import AssayMaterials_getMaterials_35E61745
from .comment import (Comment, Comment_reflection)
from .factor import (Factor, Factor_reflection)
from .material import (Material, Material_reflection)
from .material_attribute import (MaterialAttribute, MaterialAttribute_reflection)
from .ontology_annotation import (OntologyAnnotation, OntologyAnnotation_reflection)
from .person import (Person, Person_reflection)
from .process import (Process, Process_reflection)
from .process_sequence import (get_protocols, get_characteristics, get_factors, get_units, get_sources, get_samples, get_materials, update_protocols)
from .protocol import (Protocol, Protocol_reflection)
from .publication import (Publication, Publication_reflection)
from .sample import (Sample, Sample_reflection)
from .source import (Source, Source_reflection)
from .study_materials import (StudyMaterials, StudyMaterials_reflection, StudyMaterials_make, StudyMaterials_get_empty)

def _expr419() -> TypeInfo:
    return record_type("ARCtrl.ISA.Study", [], Study, lambda: [("ID", option_type(string_type)), ("FileName", option_type(string_type)), ("Identifier", option_type(string_type)), ("Title", option_type(string_type)), ("Description", option_type(string_type)), ("SubmissionDate", option_type(string_type)), ("PublicReleaseDate", option_type(string_type)), ("Publications", option_type(list_type(Publication_reflection()))), ("Contacts", option_type(list_type(Person_reflection()))), ("StudyDesignDescriptors", option_type(list_type(OntologyAnnotation_reflection()))), ("Protocols", option_type(list_type(Protocol_reflection()))), ("Materials", option_type(StudyMaterials_reflection())), ("ProcessSequence", option_type(list_type(Process_reflection()))), ("Assays", option_type(list_type(Assay_reflection()))), ("Factors", option_type(list_type(Factor_reflection()))), ("CharacteristicCategories", option_type(list_type(MaterialAttribute_reflection()))), ("UnitCategories", option_type(list_type(OntologyAnnotation_reflection()))), ("Comments", option_type(list_type(Comment_reflection())))])


@dataclass(eq = False, repr = False, slots = True)
class Study(Record):
    ID: str | None
    FileName: str | None
    Identifier: str | None
    Title: str | None
    Description: str | None
    SubmissionDate: str | None
    PublicReleaseDate: str | None
    Publications: FSharpList[Publication] | None
    Contacts: FSharpList[Person] | None
    StudyDesignDescriptors: FSharpList[OntologyAnnotation] | None
    Protocols: FSharpList[Protocol] | None
    Materials: StudyMaterials | None
    ProcessSequence: FSharpList[Process] | None
    Assays: FSharpList[Assay] | None
    Factors: FSharpList[Factor] | None
    CharacteristicCategories: FSharpList[MaterialAttribute] | None
    UnitCategories: FSharpList[OntologyAnnotation] | None
    Comments: FSharpList[Comment] | None

Study_reflection = _expr419

def Study_make(id: str | None=None, filename: str | None=None, identifier: str | None=None, title: str | None=None, description: str | None=None, submission_date: str | None=None, public_release_date: str | None=None, publications: FSharpList[Publication] | None=None, contacts: FSharpList[Person] | None=None, study_design_descriptors: FSharpList[OntologyAnnotation] | None=None, protocols: FSharpList[Protocol] | None=None, materials: StudyMaterials | None=None, process_sequence: FSharpList[Process] | None=None, assays: FSharpList[Assay] | None=None, factors: FSharpList[Factor] | None=None, characteristic_categories: FSharpList[MaterialAttribute] | None=None, unit_categories: FSharpList[OntologyAnnotation] | None=None, comments: FSharpList[Comment] | None=None) -> Study:
    return Study(id, filename, identifier, title, description, submission_date, public_release_date, publications, contacts, study_design_descriptors, protocols, materials, process_sequence, assays, factors, characteristic_categories, unit_categories, comments)


def Study_create_Z2D28E954(Id: str | None=None, FileName: str | None=None, Identifier: str | None=None, Title: str | None=None, Description: str | None=None, SubmissionDate: str | None=None, PublicReleaseDate: str | None=None, Publications: FSharpList[Publication] | None=None, Contacts: FSharpList[Person] | None=None, StudyDesignDescriptors: FSharpList[OntologyAnnotation] | None=None, Protocols: FSharpList[Protocol] | None=None, Materials: StudyMaterials | None=None, ProcessSequence: FSharpList[Process] | None=None, Assays: FSharpList[Assay] | None=None, Factors: FSharpList[Factor] | None=None, CharacteristicCategories: FSharpList[MaterialAttribute] | None=None, UnitCategories: FSharpList[OntologyAnnotation] | None=None, Comments: FSharpList[Comment] | None=None) -> Study:
    return Study_make(Id, FileName, Identifier, Title, Description, SubmissionDate, PublicReleaseDate, Publications, Contacts, StudyDesignDescriptors, Protocols, Materials, ProcessSequence, Assays, Factors, CharacteristicCategories, UnitCategories, Comments)


def Study_get_empty(__unit: None=None) -> Study:
    return Study_create_Z2D28E954()


def Study_existsByIdentifier(identifier: str, studies: FSharpList[Study]) -> bool:
    def _arrow420(s: Study, identifier: Any=identifier, studies: Any=studies) -> bool:
        return equals(s.Identifier, identifier)

    return exists(_arrow420, studies)


def Study_add(studies: FSharpList[Study], study: Study) -> FSharpList[Study]:
    return append(studies, singleton(study))


def Study_updateBy(predicate: Callable[[Study], bool], update_option: Update_UpdateOptions, study: Study, studies: FSharpList[Study]) -> FSharpList[Study]:
    if exists(predicate, studies):
        def _arrow421(a: Study, predicate: Any=predicate, update_option: Any=update_option, study: Any=study, studies: Any=studies) -> Study:
            if predicate(a):
                this: Update_UpdateOptions = update_option
                record_type_1: Study = a
                record_type_2: Study = study
                if this.tag == 2:
                    return make_record(Study_reflection(), map2_2(Update_updateAppend, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                elif this.tag == 1:
                    return make_record(Study_reflection(), map2_2(Update_updateOnlyByExisting, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                elif this.tag == 3:
                    return make_record(Study_reflection(), map2_2(Update_updateOnlyByExistingAppend, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                else: 
                    return record_type_2


            else: 
                return a


        return map(_arrow421, studies)

    else: 
        return studies



def Study_updateByIdentifier(update_option: Update_UpdateOptions, study: Study, studies: FSharpList[Study]) -> FSharpList[Study]:
    def predicate(s: Study, update_option: Any=update_option, study: Any=study, studies: Any=studies) -> bool:
        return equals(s.Identifier, study.Identifier)

    return Study_updateBy(predicate, update_option, study, studies)


def Study_removeByIdentifier(identifier: str, studies: FSharpList[Study]) -> FSharpList[Study]:
    def _arrow422(s: Study, identifier: Any=identifier, studies: Any=studies) -> bool:
        return not equals(s.Identifier, identifier)

    return filter(_arrow422, studies)


def Study_getAssays_7312BC8B(study: Study) -> FSharpList[Assay]:
    return default_arg(study.Assays, empty())


def Study_mapAssays(f: Callable[[FSharpList[Assay]], FSharpList[Assay]], study: Study) -> Study:
    return Study(study.ID, study.FileName, study.Identifier, study.Title, study.Description, study.SubmissionDate, study.PublicReleaseDate, study.Publications, study.Contacts, study.StudyDesignDescriptors, study.Protocols, study.Materials, study.ProcessSequence, Option_mapDefault(empty(), f, study.Assays), study.Factors, study.CharacteristicCategories, study.UnitCategories, study.Comments)


def Study_setAssays(study: Study, assays: FSharpList[Assay]) -> Study:
    return Study(study.ID, study.FileName, study.Identifier, study.Title, study.Description, study.SubmissionDate, study.PublicReleaseDate, study.Publications, study.Contacts, study.StudyDesignDescriptors, study.Protocols, study.Materials, study.ProcessSequence, assays, study.Factors, study.CharacteristicCategories, study.UnitCategories, study.Comments)


def Study_mapFactors(f: Callable[[FSharpList[Factor]], FSharpList[Factor]], study: Study) -> Study:
    return Study(study.ID, study.FileName, study.Identifier, study.Title, study.Description, study.SubmissionDate, study.PublicReleaseDate, study.Publications, study.Contacts, study.StudyDesignDescriptors, study.Protocols, study.Materials, study.ProcessSequence, study.Assays, Option_mapDefault(empty(), f, study.Factors), study.CharacteristicCategories, study.UnitCategories, study.Comments)


def Study_setFactors(study: Study, factors: FSharpList[Factor]) -> Study:
    return Study(study.ID, study.FileName, study.Identifier, study.Title, study.Description, study.SubmissionDate, study.PublicReleaseDate, study.Publications, study.Contacts, study.StudyDesignDescriptors, study.Protocols, study.Materials, study.ProcessSequence, study.Assays, factors, study.CharacteristicCategories, study.UnitCategories, study.Comments)


def Study_mapProtocols(f: Callable[[FSharpList[Protocol]], FSharpList[Protocol]], study: Study) -> Study:
    return Study(study.ID, study.FileName, study.Identifier, study.Title, study.Description, study.SubmissionDate, study.PublicReleaseDate, study.Publications, study.Contacts, study.StudyDesignDescriptors, Option_mapDefault(empty(), f, study.Protocols), study.Materials, study.ProcessSequence, study.Assays, study.Factors, study.CharacteristicCategories, study.UnitCategories, study.Comments)


def Study_setProtocols(study: Study, protocols: FSharpList[Protocol]) -> Study:
    return Study(study.ID, study.FileName, study.Identifier, study.Title, study.Description, study.SubmissionDate, study.PublicReleaseDate, study.Publications, study.Contacts, study.StudyDesignDescriptors, protocols, study.Materials, study.ProcessSequence, study.Assays, study.Factors, study.CharacteristicCategories, study.UnitCategories, study.Comments)


def Study_getContacts_7312BC8B(study: Study) -> FSharpList[Person]:
    return default_arg(study.Contacts, empty())


def Study_mapContacts(f: Callable[[FSharpList[Person]], FSharpList[Person]], study: Study) -> Study:
    return Study(study.ID, study.FileName, study.Identifier, study.Title, study.Description, study.SubmissionDate, study.PublicReleaseDate, study.Publications, Option_mapDefault(empty(), f, study.Contacts), study.StudyDesignDescriptors, study.Protocols, study.Materials, study.ProcessSequence, study.Assays, study.Factors, study.CharacteristicCategories, study.UnitCategories, study.Comments)


def Study_setContacts(study: Study, persons: FSharpList[Person]) -> Study:
    return Study(study.ID, study.FileName, study.Identifier, study.Title, study.Description, study.SubmissionDate, study.PublicReleaseDate, study.Publications, persons, study.StudyDesignDescriptors, study.Protocols, study.Materials, study.ProcessSequence, study.Assays, study.Factors, study.CharacteristicCategories, study.UnitCategories, study.Comments)


def Study_getPublications_7312BC8B(study: Study) -> FSharpList[Publication]:
    return default_arg(study.Publications, empty())


def Study_mapPublications(f: Callable[[FSharpList[Publication]], FSharpList[Publication]], study: Study) -> Study:
    return Study(study.ID, study.FileName, study.Identifier, study.Title, study.Description, study.SubmissionDate, study.PublicReleaseDate, Option_mapDefault(empty(), f, study.Publications), study.Contacts, study.StudyDesignDescriptors, study.Protocols, study.Materials, study.ProcessSequence, study.Assays, study.Factors, study.CharacteristicCategories, study.UnitCategories, study.Comments)


def Study_setPublications(study: Study, publications: FSharpList[Publication]) -> Study:
    return Study(study.ID, study.FileName, study.Identifier, study.Title, study.Description, study.SubmissionDate, study.PublicReleaseDate, publications, study.Contacts, study.StudyDesignDescriptors, study.Protocols, study.Materials, study.ProcessSequence, study.Assays, study.Factors, study.CharacteristicCategories, study.UnitCategories, study.Comments)


def Study_getDescriptors_7312BC8B(study: Study) -> FSharpList[OntologyAnnotation]:
    return default_arg(study.StudyDesignDescriptors, empty())


def Study_mapDescriptors(f: Callable[[FSharpList[OntologyAnnotation]], FSharpList[OntologyAnnotation]], study: Study) -> Study:
    return Study(study.ID, study.FileName, study.Identifier, study.Title, study.Description, study.SubmissionDate, study.PublicReleaseDate, study.Publications, study.Contacts, Option_mapDefault(empty(), f, study.StudyDesignDescriptors), study.Protocols, study.Materials, study.ProcessSequence, study.Assays, study.Factors, study.CharacteristicCategories, study.UnitCategories, study.Comments)


def Study_setDescriptors(study: Study, descriptors: FSharpList[OntologyAnnotation]) -> Study:
    return Study(study.ID, study.FileName, study.Identifier, study.Title, study.Description, study.SubmissionDate, study.PublicReleaseDate, study.Publications, study.Contacts, descriptors, study.Protocols, study.Materials, study.ProcessSequence, study.Assays, study.Factors, study.CharacteristicCategories, study.UnitCategories, study.Comments)


def Study_getProcesses_7312BC8B(study: Study) -> FSharpList[Process]:
    return default_arg(study.ProcessSequence, empty())


def Study_getProtocols_7312BC8B(study: Study) -> FSharpList[Protocol]:
    process_sequence_protocols: FSharpList[Protocol] = get_protocols(Study_getProcesses_7312BC8B(study))
    def mapping(assay: Assay, study: Any=study) -> FSharpList[Protocol]:
        return Assay_getProtocols_722A269D(assay)

    assays_protocols: FSharpList[Protocol] = collect(mapping, Study_getAssays_7312BC8B(study))
    update_options_2: Update_UpdateOptions = Update_UpdateOptions(3)
    def mapping_6(p_1: Protocol, study: Any=study) -> str | None:
        return p_1.Name

    list1_1: FSharpList[Protocol] = default_arg(study.Protocols, empty())
    list2_1: FSharpList[Protocol]
    update_options: Update_UpdateOptions = Update_UpdateOptions(3)
    def mapping_1(p: Protocol, study: Any=study) -> str | None:
        return p.Name

    list1: FSharpList[Protocol] = assays_protocols
    list2: FSharpList[Protocol] = process_sequence_protocols
    try: 
        def merge(record_type_: Protocol, record_type__1: Protocol) -> Protocol:
            this: Update_UpdateOptions = update_options
            record_type_1: Protocol = record_type_
            record_type_2: Protocol = record_type__1
            if this.tag == 2:
                def mapping_2(old_val: Any=None, new_val: Any=None, record_type_: Any=record_type_, record_type__1: Any=record_type__1) -> Any:
                    return Update_updateAppend(old_val, new_val)

                return make_record(Protocol_reflection(), map2_2(mapping_2, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

            elif this.tag == 1:
                def mapping_1_2(old_val_1: Any=None, new_val_1: Any=None, record_type_: Any=record_type_, record_type__1: Any=record_type__1) -> Any:
                    return Update_updateOnlyByExisting(old_val_1, new_val_1)

                return make_record(Protocol_reflection(), map2_2(mapping_1_2, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

            elif this.tag == 3:
                def mapping_2_1(old_val_2: Any=None, new_val_2: Any=None, record_type_: Any=record_type_, record_type__1: Any=record_type__1) -> Any:
                    return Update_updateOnlyByExistingAppend(old_val_2, new_val_2)

                return make_record(Protocol_reflection(), map2_2(mapping_2_1, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

            else: 
                return record_type_2


        def mapping_1_1(v: Protocol) -> tuple[str | None, Protocol]:
            return (mapping_1(v), v)

        map1: Any = Dict_ofSeqWithMerge(merge, map(mapping_1_1, list1))
        def merge_1(record_type__2: Protocol, record_type__3: Protocol) -> Protocol:
            this_1: Update_UpdateOptions = update_options
            record_type_1_1: Protocol = record_type__2
            record_type_2_1: Protocol = record_type__3
            if this_1.tag == 2:
                def mapping_3(old_val_3: Any=None, new_val_3: Any=None, record_type__2: Any=record_type__2, record_type__3: Any=record_type__3) -> Any:
                    return Update_updateAppend(old_val_3, new_val_3)

                return make_record(Protocol_reflection(), map2_2(mapping_3, get_record_fields(record_type_1_1), get_record_fields(record_type_2_1), None))

            elif this_1.tag == 1:
                def mapping_1_3(old_val_1_1: Any=None, new_val_1_1: Any=None, record_type__2: Any=record_type__2, record_type__3: Any=record_type__3) -> Any:
                    return Update_updateOnlyByExisting(old_val_1_1, new_val_1_1)

                return make_record(Protocol_reflection(), map2_2(mapping_1_3, get_record_fields(record_type_1_1), get_record_fields(record_type_2_1), None))

            elif this_1.tag == 3:
                def mapping_2_3(old_val_2_1: Any=None, new_val_2_1: Any=None, record_type__2: Any=record_type__2, record_type__3: Any=record_type__3) -> Any:
                    return Update_updateOnlyByExistingAppend(old_val_2_1, new_val_2_1)

                return make_record(Protocol_reflection(), map2_2(mapping_2_3, get_record_fields(record_type_1_1), get_record_fields(record_type_2_1), None))

            else: 
                return record_type_2_1


        def mapping_2_2(v_1: Protocol) -> tuple[str | None, Protocol]:
            return (mapping_1(v_1), v_1)

        map2: Any = Dict_ofSeqWithMerge(merge_1, map(mapping_2_2, list2))
        def mapping_3_1(k: str | None=None) -> Protocol:
            matchValue: Protocol | None = Dict_tryFind(k, map1)
            matchValue_1: Protocol | None = Dict_tryFind(k, map2)
            if matchValue is None:
                if matchValue_1 is None:
                    raise Exception("If this fails, then I don\'t know how to program")

                else: 
                    v2_1: Protocol = matchValue_1
                    return v2_1


            elif matchValue_1 is None:
                v1_1: Protocol = matchValue
                return v1_1

            else: 
                v1: Protocol = matchValue
                v2: Protocol = matchValue_1
                this_2: Update_UpdateOptions = update_options
                record_type_1_2: Protocol = v1
                record_type_2_2: Protocol = v2
                if this_2.tag == 2:
                    def mapping_4(old_val_4: Any=None, new_val_4: Any=None, k: Any=k) -> Any:
                        return Update_updateAppend(old_val_4, new_val_4)

                    return make_record(Protocol_reflection(), map2_2(mapping_4, get_record_fields(record_type_1_2), get_record_fields(record_type_2_2), None))

                elif this_2.tag == 1:
                    def mapping_1_4(old_val_1_2: Any=None, new_val_1_2: Any=None, k: Any=k) -> Any:
                        return Update_updateOnlyByExisting(old_val_1_2, new_val_1_2)

                    return make_record(Protocol_reflection(), map2_2(mapping_1_4, get_record_fields(record_type_1_2), get_record_fields(record_type_2_2), None))

                elif this_2.tag == 3:
                    def mapping_2_4(old_val_2_2: Any=None, new_val_2_2: Any=None, k: Any=k) -> Any:
                        return Update_updateOnlyByExistingAppend(old_val_2_2, new_val_2_2)

                    return make_record(Protocol_reflection(), map2_2(mapping_2_4, get_record_fields(record_type_1_2), get_record_fields(record_type_2_2), None))

                else: 
                    return record_type_2_2



        class ObjectExpr423:
            @property
            def Equals(self) -> Callable[[str | None, str | None], bool]:
                return equals

            @property
            def GetHashCode(self) -> Callable[[str | None], int]:
                return structural_hash

        list2_1 = map(mapping_3_1, List_distinct(append(map(mapping_1, list1), map(mapping_1, list2)), ObjectExpr423()))

    except Exception as err:
        raise Exception(((("Could not mergeUpdate " + "Protocol") + " list: \n") + str(err)) + "")

    try: 
        def merge_2(record_type__6: Protocol, record_type__1_1: Protocol) -> Protocol:
            this_3: Update_UpdateOptions = update_options_2
            record_type_1_3: Protocol = record_type__6
            record_type_2_3: Protocol = record_type__1_1
            if this_3.tag == 2:
                def mapping_7(old_val_5: Any=None, new_val_5: Any=None, record_type__6: Any=record_type__6, record_type__1_1: Any=record_type__1_1) -> Any:
                    return Update_updateAppend(old_val_5, new_val_5)

                return make_record(Protocol_reflection(), map2_2(mapping_7, get_record_fields(record_type_1_3), get_record_fields(record_type_2_3), None))

            elif this_3.tag == 1:
                def mapping_1_6(old_val_1_3: Any=None, new_val_1_3: Any=None, record_type__6: Any=record_type__6, record_type__1_1: Any=record_type__1_1) -> Any:
                    return Update_updateOnlyByExisting(old_val_1_3, new_val_1_3)

                return make_record(Protocol_reflection(), map2_2(mapping_1_6, get_record_fields(record_type_1_3), get_record_fields(record_type_2_3), None))

            elif this_3.tag == 3:
                def mapping_2_5(old_val_2_3: Any=None, new_val_2_3: Any=None, record_type__6: Any=record_type__6, record_type__1_1: Any=record_type__1_1) -> Any:
                    return Update_updateOnlyByExistingAppend(old_val_2_3, new_val_2_3)

                return make_record(Protocol_reflection(), map2_2(mapping_2_5, get_record_fields(record_type_1_3), get_record_fields(record_type_2_3), None))

            else: 
                return record_type_2_3


        def mapping_1_5(v_2: Protocol) -> tuple[str | None, Protocol]:
            return (mapping_6(v_2), v_2)

        map1_1: Any = Dict_ofSeqWithMerge(merge_2, map(mapping_1_5, list1_1))
        def merge_1_1(record_type__2_1: Protocol, record_type__3_1: Protocol) -> Protocol:
            this_4: Update_UpdateOptions = update_options_2
            record_type_1_4: Protocol = record_type__2_1
            record_type_2_4: Protocol = record_type__3_1
            if this_4.tag == 2:
                def mapping_8(old_val_6: Any=None, new_val_6: Any=None, record_type__2_1: Any=record_type__2_1, record_type__3_1: Any=record_type__3_1) -> Any:
                    return Update_updateAppend(old_val_6, new_val_6)

                return make_record(Protocol_reflection(), map2_2(mapping_8, get_record_fields(record_type_1_4), get_record_fields(record_type_2_4), None))

            elif this_4.tag == 1:
                def mapping_1_7(old_val_1_4: Any=None, new_val_1_4: Any=None, record_type__2_1: Any=record_type__2_1, record_type__3_1: Any=record_type__3_1) -> Any:
                    return Update_updateOnlyByExisting(old_val_1_4, new_val_1_4)

                return make_record(Protocol_reflection(), map2_2(mapping_1_7, get_record_fields(record_type_1_4), get_record_fields(record_type_2_4), None))

            elif this_4.tag == 3:
                def mapping_2_7(old_val_2_4: Any=None, new_val_2_4: Any=None, record_type__2_1: Any=record_type__2_1, record_type__3_1: Any=record_type__3_1) -> Any:
                    return Update_updateOnlyByExistingAppend(old_val_2_4, new_val_2_4)

                return make_record(Protocol_reflection(), map2_2(mapping_2_7, get_record_fields(record_type_1_4), get_record_fields(record_type_2_4), None))

            else: 
                return record_type_2_4


        def mapping_2_6(v_1_1: Protocol) -> tuple[str | None, Protocol]:
            return (mapping_6(v_1_1), v_1_1)

        map2_1: Any = Dict_ofSeqWithMerge(merge_1_1, map(mapping_2_6, list2_1))
        def mapping_3_2(k_1: str | None=None) -> Protocol:
            matchValue_2: Protocol | None = Dict_tryFind(k_1, map1_1)
            matchValue_1_1: Protocol | None = Dict_tryFind(k_1, map2_1)
            if matchValue_2 is None:
                if matchValue_1_1 is None:
                    raise Exception("If this fails, then I don\'t know how to program")

                else: 
                    v2_1_1: Protocol = matchValue_1_1
                    return v2_1_1


            elif matchValue_1_1 is None:
                v1_1_1: Protocol = matchValue_2
                return v1_1_1

            else: 
                v1_2: Protocol = matchValue_2
                v2_2: Protocol = matchValue_1_1
                this_5: Update_UpdateOptions = update_options_2
                record_type_1_5: Protocol = v1_2
                record_type_2_5: Protocol = v2_2
                if this_5.tag == 2:
                    def mapping_9(old_val_7: Any=None, new_val_7: Any=None, k_1: Any=k_1) -> Any:
                        return Update_updateAppend(old_val_7, new_val_7)

                    return make_record(Protocol_reflection(), map2_2(mapping_9, get_record_fields(record_type_1_5), get_record_fields(record_type_2_5), None))

                elif this_5.tag == 1:
                    def mapping_1_8(old_val_1_5: Any=None, new_val_1_5: Any=None, k_1: Any=k_1) -> Any:
                        return Update_updateOnlyByExisting(old_val_1_5, new_val_1_5)

                    return make_record(Protocol_reflection(), map2_2(mapping_1_8, get_record_fields(record_type_1_5), get_record_fields(record_type_2_5), None))

                elif this_5.tag == 3:
                    def mapping_2_8(old_val_2_5: Any=None, new_val_2_5: Any=None, k_1: Any=k_1) -> Any:
                        return Update_updateOnlyByExistingAppend(old_val_2_5, new_val_2_5)

                    return make_record(Protocol_reflection(), map2_2(mapping_2_8, get_record_fields(record_type_1_5), get_record_fields(record_type_2_5), None))

                else: 
                    return record_type_2_5



        class ObjectExpr424:
            @property
            def Equals(self) -> Callable[[str | None, str | None], bool]:
                return equals

            @property
            def GetHashCode(self) -> Callable[[str | None], int]:
                return structural_hash

        return map(mapping_3_2, List_distinct(append(map(mapping_6, list1_1), map(mapping_6, list2_1)), ObjectExpr424()))

    except Exception as err_1:
        raise Exception(((("Could not mergeUpdate " + "Protocol") + " list: \n") + str(err_1)) + "")



def Study_getCharacteristics_7312BC8B(study: Study) -> FSharpList[MaterialAttribute]:
    def mapping(assay: Assay, study: Any=study) -> FSharpList[MaterialAttribute]:
        return Assay_getCharacteristics_722A269D(assay)

    class ObjectExpr425:
        @property
        def Equals(self) -> Callable[[MaterialAttribute, MaterialAttribute], bool]:
            return equals

        @property
        def GetHashCode(self) -> Callable[[MaterialAttribute], int]:
            return safe_hash

    return List_distinct(append(get_characteristics(Study_getProcesses_7312BC8B(study)), append(collect(mapping, Study_getAssays_7312BC8B(study)), default_arg(study.CharacteristicCategories, empty()))), ObjectExpr425())


def Study_getFactors_7312BC8B(study: Study) -> FSharpList[Factor]:
    def mapping(assay: Assay, study: Any=study) -> FSharpList[Factor]:
        return Assay_getFactors_722A269D(assay)

    class ObjectExpr426:
        @property
        def Equals(self) -> Callable[[Factor, Factor], bool]:
            return equals

        @property
        def GetHashCode(self) -> Callable[[Factor], int]:
            return safe_hash

    return List_distinct(append(get_factors(Study_getProcesses_7312BC8B(study)), append(collect(mapping, Study_getAssays_7312BC8B(study)), default_arg(study.Factors, empty()))), ObjectExpr426())


def Study_getUnitCategories_7312BC8B(study: Study) -> FSharpList[OntologyAnnotation]:
    def mapping(assay: Assay, study: Any=study) -> FSharpList[OntologyAnnotation]:
        return Assay_getUnitCategories_722A269D(assay)

    class ObjectExpr427:
        @property
        def Equals(self) -> Callable[[OntologyAnnotation, OntologyAnnotation], bool]:
            return equals

        @property
        def GetHashCode(self) -> Callable[[OntologyAnnotation], int]:
            return safe_hash

    return List_distinct(append(get_units(Study_getProcesses_7312BC8B(study)), append(collect(mapping, Study_getAssays_7312BC8B(study)), default_arg(study.UnitCategories, empty()))), ObjectExpr427())


def Study_getSources_7312BC8B(study: Study) -> FSharpList[Source]:
    process_sequence_sources: FSharpList[Source] = get_sources(Study_getProcesses_7312BC8B(study))
    def mapping(assay: Assay, study: Any=study) -> FSharpList[Source]:
        return Assay_getSources_722A269D(assay)

    assays_sources: FSharpList[Source] = collect(mapping, Study_getAssays_7312BC8B(study))
    update_options_2: Update_UpdateOptions = Update_UpdateOptions(3)
    def mapping_6(s_2: Source, study: Any=study) -> str:
        return default_arg(s_2.Name, "")

    list1_1: FSharpList[Source]
    match_value: StudyMaterials | None = study.Materials
    list1_1 = empty() if (match_value is None) else default_arg(match_value.Sources, empty())
    list2_1: FSharpList[Source]
    update_options: Update_UpdateOptions = Update_UpdateOptions(3)
    def mapping_1(s: Source, study: Any=study) -> str:
        return default_arg(s.Name, "")

    list1: FSharpList[Source] = assays_sources
    list2: FSharpList[Source] = process_sequence_sources
    try: 
        def merge(record_type_: Source, record_type__1: Source) -> Source:
            this: Update_UpdateOptions = update_options
            record_type_1: Source = record_type_
            record_type_2: Source = record_type__1
            if this.tag == 2:
                def mapping_2(old_val: Any=None, new_val: Any=None, record_type_: Any=record_type_, record_type__1: Any=record_type__1) -> Any:
                    return Update_updateAppend(old_val, new_val)

                return make_record(Source_reflection(), map2_2(mapping_2, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

            elif this.tag == 1:
                def mapping_1_2(old_val_1: Any=None, new_val_1: Any=None, record_type_: Any=record_type_, record_type__1: Any=record_type__1) -> Any:
                    return Update_updateOnlyByExisting(old_val_1, new_val_1)

                return make_record(Source_reflection(), map2_2(mapping_1_2, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

            elif this.tag == 3:
                def mapping_2_1(old_val_2: Any=None, new_val_2: Any=None, record_type_: Any=record_type_, record_type__1: Any=record_type__1) -> Any:
                    return Update_updateOnlyByExistingAppend(old_val_2, new_val_2)

                return make_record(Source_reflection(), map2_2(mapping_2_1, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

            else: 
                return record_type_2


        def mapping_1_1(v: Source) -> tuple[str, Source]:
            return (mapping_1(v), v)

        map1: Any = Dict_ofSeqWithMerge(merge, map(mapping_1_1, list1))
        def merge_1(record_type__2: Source, record_type__3: Source) -> Source:
            this_1: Update_UpdateOptions = update_options
            record_type_1_1: Source = record_type__2
            record_type_2_1: Source = record_type__3
            if this_1.tag == 2:
                def mapping_3(old_val_3: Any=None, new_val_3: Any=None, record_type__2: Any=record_type__2, record_type__3: Any=record_type__3) -> Any:
                    return Update_updateAppend(old_val_3, new_val_3)

                return make_record(Source_reflection(), map2_2(mapping_3, get_record_fields(record_type_1_1), get_record_fields(record_type_2_1), None))

            elif this_1.tag == 1:
                def mapping_1_3(old_val_1_1: Any=None, new_val_1_1: Any=None, record_type__2: Any=record_type__2, record_type__3: Any=record_type__3) -> Any:
                    return Update_updateOnlyByExisting(old_val_1_1, new_val_1_1)

                return make_record(Source_reflection(), map2_2(mapping_1_3, get_record_fields(record_type_1_1), get_record_fields(record_type_2_1), None))

            elif this_1.tag == 3:
                def mapping_2_3(old_val_2_1: Any=None, new_val_2_1: Any=None, record_type__2: Any=record_type__2, record_type__3: Any=record_type__3) -> Any:
                    return Update_updateOnlyByExistingAppend(old_val_2_1, new_val_2_1)

                return make_record(Source_reflection(), map2_2(mapping_2_3, get_record_fields(record_type_1_1), get_record_fields(record_type_2_1), None))

            else: 
                return record_type_2_1


        def mapping_2_2(v_1: Source) -> tuple[str, Source]:
            return (mapping_1(v_1), v_1)

        map2: Any = Dict_ofSeqWithMerge(merge_1, map(mapping_2_2, list2))
        def mapping_3_1(k: str) -> Source:
            matchValue: Source | None = Dict_tryFind(k, map1)
            matchValue_1: Source | None = Dict_tryFind(k, map2)
            if matchValue is None:
                if matchValue_1 is None:
                    raise Exception("If this fails, then I don\'t know how to program")

                else: 
                    v2_1: Source = matchValue_1
                    return v2_1


            elif matchValue_1 is None:
                v1_1: Source = matchValue
                return v1_1

            else: 
                v1: Source = matchValue
                v2: Source = matchValue_1
                this_2: Update_UpdateOptions = update_options
                record_type_1_2: Source = v1
                record_type_2_2: Source = v2
                if this_2.tag == 2:
                    def mapping_4(old_val_4: Any=None, new_val_4: Any=None, k: Any=k) -> Any:
                        return Update_updateAppend(old_val_4, new_val_4)

                    return make_record(Source_reflection(), map2_2(mapping_4, get_record_fields(record_type_1_2), get_record_fields(record_type_2_2), None))

                elif this_2.tag == 1:
                    def mapping_1_4(old_val_1_2: Any=None, new_val_1_2: Any=None, k: Any=k) -> Any:
                        return Update_updateOnlyByExisting(old_val_1_2, new_val_1_2)

                    return make_record(Source_reflection(), map2_2(mapping_1_4, get_record_fields(record_type_1_2), get_record_fields(record_type_2_2), None))

                elif this_2.tag == 3:
                    def mapping_2_4(old_val_2_2: Any=None, new_val_2_2: Any=None, k: Any=k) -> Any:
                        return Update_updateOnlyByExistingAppend(old_val_2_2, new_val_2_2)

                    return make_record(Source_reflection(), map2_2(mapping_2_4, get_record_fields(record_type_1_2), get_record_fields(record_type_2_2), None))

                else: 
                    return record_type_2_2



        class ObjectExpr429:
            @property
            def Equals(self) -> Callable[[str, str], bool]:
                def _arrow428(x: str, y: str) -> bool:
                    return x == y

                return _arrow428

            @property
            def GetHashCode(self) -> Callable[[str], int]:
                return string_hash

        list2_1 = map(mapping_3_1, List_distinct(append(map(mapping_1, list1), map(mapping_1, list2)), ObjectExpr429()))

    except Exception as err:
        raise Exception(((("Could not mergeUpdate " + "Source") + " list: \n") + str(err)) + "")

    try: 
        def merge_2(record_type__6: Source, record_type__1_1: Source) -> Source:
            this_3: Update_UpdateOptions = update_options_2
            record_type_1_3: Source = record_type__6
            record_type_2_3: Source = record_type__1_1
            if this_3.tag == 2:
                def mapping_7(old_val_5: Any=None, new_val_5: Any=None, record_type__6: Any=record_type__6, record_type__1_1: Any=record_type__1_1) -> Any:
                    return Update_updateAppend(old_val_5, new_val_5)

                return make_record(Source_reflection(), map2_2(mapping_7, get_record_fields(record_type_1_3), get_record_fields(record_type_2_3), None))

            elif this_3.tag == 1:
                def mapping_1_6(old_val_1_3: Any=None, new_val_1_3: Any=None, record_type__6: Any=record_type__6, record_type__1_1: Any=record_type__1_1) -> Any:
                    return Update_updateOnlyByExisting(old_val_1_3, new_val_1_3)

                return make_record(Source_reflection(), map2_2(mapping_1_6, get_record_fields(record_type_1_3), get_record_fields(record_type_2_3), None))

            elif this_3.tag == 3:
                def mapping_2_5(old_val_2_3: Any=None, new_val_2_3: Any=None, record_type__6: Any=record_type__6, record_type__1_1: Any=record_type__1_1) -> Any:
                    return Update_updateOnlyByExistingAppend(old_val_2_3, new_val_2_3)

                return make_record(Source_reflection(), map2_2(mapping_2_5, get_record_fields(record_type_1_3), get_record_fields(record_type_2_3), None))

            else: 
                return record_type_2_3


        def mapping_1_5(v_2: Source) -> tuple[str, Source]:
            return (mapping_6(v_2), v_2)

        map1_1: Any = Dict_ofSeqWithMerge(merge_2, map(mapping_1_5, list1_1))
        def merge_1_1(record_type__2_1: Source, record_type__3_1: Source) -> Source:
            this_4: Update_UpdateOptions = update_options_2
            record_type_1_4: Source = record_type__2_1
            record_type_2_4: Source = record_type__3_1
            if this_4.tag == 2:
                def mapping_8(old_val_6: Any=None, new_val_6: Any=None, record_type__2_1: Any=record_type__2_1, record_type__3_1: Any=record_type__3_1) -> Any:
                    return Update_updateAppend(old_val_6, new_val_6)

                return make_record(Source_reflection(), map2_2(mapping_8, get_record_fields(record_type_1_4), get_record_fields(record_type_2_4), None))

            elif this_4.tag == 1:
                def mapping_1_7(old_val_1_4: Any=None, new_val_1_4: Any=None, record_type__2_1: Any=record_type__2_1, record_type__3_1: Any=record_type__3_1) -> Any:
                    return Update_updateOnlyByExisting(old_val_1_4, new_val_1_4)

                return make_record(Source_reflection(), map2_2(mapping_1_7, get_record_fields(record_type_1_4), get_record_fields(record_type_2_4), None))

            elif this_4.tag == 3:
                def mapping_2_7(old_val_2_4: Any=None, new_val_2_4: Any=None, record_type__2_1: Any=record_type__2_1, record_type__3_1: Any=record_type__3_1) -> Any:
                    return Update_updateOnlyByExistingAppend(old_val_2_4, new_val_2_4)

                return make_record(Source_reflection(), map2_2(mapping_2_7, get_record_fields(record_type_1_4), get_record_fields(record_type_2_4), None))

            else: 
                return record_type_2_4


        def mapping_2_6(v_1_1: Source) -> tuple[str, Source]:
            return (mapping_6(v_1_1), v_1_1)

        map2_1: Any = Dict_ofSeqWithMerge(merge_1_1, map(mapping_2_6, list2_1))
        def mapping_3_2(k_1: str) -> Source:
            matchValue_2: Source | None = Dict_tryFind(k_1, map1_1)
            matchValue_1_1: Source | None = Dict_tryFind(k_1, map2_1)
            if matchValue_2 is None:
                if matchValue_1_1 is None:
                    raise Exception("If this fails, then I don\'t know how to program")

                else: 
                    v2_1_1: Source = matchValue_1_1
                    return v2_1_1


            elif matchValue_1_1 is None:
                v1_1_1: Source = matchValue_2
                return v1_1_1

            else: 
                v1_2: Source = matchValue_2
                v2_2: Source = matchValue_1_1
                this_5: Update_UpdateOptions = update_options_2
                record_type_1_5: Source = v1_2
                record_type_2_5: Source = v2_2
                if this_5.tag == 2:
                    def mapping_9(old_val_7: Any=None, new_val_7: Any=None, k_1: Any=k_1) -> Any:
                        return Update_updateAppend(old_val_7, new_val_7)

                    return make_record(Source_reflection(), map2_2(mapping_9, get_record_fields(record_type_1_5), get_record_fields(record_type_2_5), None))

                elif this_5.tag == 1:
                    def mapping_1_8(old_val_1_5: Any=None, new_val_1_5: Any=None, k_1: Any=k_1) -> Any:
                        return Update_updateOnlyByExisting(old_val_1_5, new_val_1_5)

                    return make_record(Source_reflection(), map2_2(mapping_1_8, get_record_fields(record_type_1_5), get_record_fields(record_type_2_5), None))

                elif this_5.tag == 3:
                    def mapping_2_8(old_val_2_5: Any=None, new_val_2_5: Any=None, k_1: Any=k_1) -> Any:
                        return Update_updateOnlyByExistingAppend(old_val_2_5, new_val_2_5)

                    return make_record(Source_reflection(), map2_2(mapping_2_8, get_record_fields(record_type_1_5), get_record_fields(record_type_2_5), None))

                else: 
                    return record_type_2_5



        class ObjectExpr431:
            @property
            def Equals(self) -> Callable[[str, str], bool]:
                def _arrow430(x_1: str, y_1: str) -> bool:
                    return x_1 == y_1

                return _arrow430

            @property
            def GetHashCode(self) -> Callable[[str], int]:
                return string_hash

        return map(mapping_3_2, List_distinct(append(map(mapping_6, list1_1), map(mapping_6, list2_1)), ObjectExpr431()))

    except Exception as err_1:
        raise Exception(((("Could not mergeUpdate " + "Source") + " list: \n") + str(err_1)) + "")



def Study_getSamples_7312BC8B(study: Study) -> FSharpList[Sample]:
    process_sequence_samples: FSharpList[Sample] = get_samples(Study_getProcesses_7312BC8B(study))
    def mapping(assay: Assay, study: Any=study) -> FSharpList[Sample]:
        return Assay_getSamples_722A269D(assay)

    assays_samples: FSharpList[Sample] = collect(mapping, Study_getAssays_7312BC8B(study))
    update_options_2: Update_UpdateOptions = Update_UpdateOptions(3)
    def mapping_6(s_2: Sample, study: Any=study) -> str:
        return default_arg(s_2.Name, "")

    list1_1: FSharpList[Sample]
    match_value: StudyMaterials | None = study.Materials
    list1_1 = empty() if (match_value is None) else default_arg(match_value.Samples, empty())
    list2_1: FSharpList[Sample]
    update_options: Update_UpdateOptions = Update_UpdateOptions(3)
    def mapping_1(s: Sample, study: Any=study) -> str:
        return default_arg(s.Name, "")

    list1: FSharpList[Sample] = assays_samples
    list2: FSharpList[Sample] = process_sequence_samples
    try: 
        def merge(record_type_: Sample, record_type__1: Sample) -> Sample:
            this: Update_UpdateOptions = update_options
            record_type_1: Sample = record_type_
            record_type_2: Sample = record_type__1
            if this.tag == 2:
                def mapping_2(old_val: Any=None, new_val: Any=None, record_type_: Any=record_type_, record_type__1: Any=record_type__1) -> Any:
                    return Update_updateAppend(old_val, new_val)

                return make_record(Sample_reflection(), map2_2(mapping_2, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

            elif this.tag == 1:
                def mapping_1_2(old_val_1: Any=None, new_val_1: Any=None, record_type_: Any=record_type_, record_type__1: Any=record_type__1) -> Any:
                    return Update_updateOnlyByExisting(old_val_1, new_val_1)

                return make_record(Sample_reflection(), map2_2(mapping_1_2, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

            elif this.tag == 3:
                def mapping_2_1(old_val_2: Any=None, new_val_2: Any=None, record_type_: Any=record_type_, record_type__1: Any=record_type__1) -> Any:
                    return Update_updateOnlyByExistingAppend(old_val_2, new_val_2)

                return make_record(Sample_reflection(), map2_2(mapping_2_1, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

            else: 
                return record_type_2


        def mapping_1_1(v: Sample) -> tuple[str, Sample]:
            return (mapping_1(v), v)

        map1: Any = Dict_ofSeqWithMerge(merge, map(mapping_1_1, list1))
        def merge_1(record_type__2: Sample, record_type__3: Sample) -> Sample:
            this_1: Update_UpdateOptions = update_options
            record_type_1_1: Sample = record_type__2
            record_type_2_1: Sample = record_type__3
            if this_1.tag == 2:
                def mapping_3(old_val_3: Any=None, new_val_3: Any=None, record_type__2: Any=record_type__2, record_type__3: Any=record_type__3) -> Any:
                    return Update_updateAppend(old_val_3, new_val_3)

                return make_record(Sample_reflection(), map2_2(mapping_3, get_record_fields(record_type_1_1), get_record_fields(record_type_2_1), None))

            elif this_1.tag == 1:
                def mapping_1_3(old_val_1_1: Any=None, new_val_1_1: Any=None, record_type__2: Any=record_type__2, record_type__3: Any=record_type__3) -> Any:
                    return Update_updateOnlyByExisting(old_val_1_1, new_val_1_1)

                return make_record(Sample_reflection(), map2_2(mapping_1_3, get_record_fields(record_type_1_1), get_record_fields(record_type_2_1), None))

            elif this_1.tag == 3:
                def mapping_2_3(old_val_2_1: Any=None, new_val_2_1: Any=None, record_type__2: Any=record_type__2, record_type__3: Any=record_type__3) -> Any:
                    return Update_updateOnlyByExistingAppend(old_val_2_1, new_val_2_1)

                return make_record(Sample_reflection(), map2_2(mapping_2_3, get_record_fields(record_type_1_1), get_record_fields(record_type_2_1), None))

            else: 
                return record_type_2_1


        def mapping_2_2(v_1: Sample) -> tuple[str, Sample]:
            return (mapping_1(v_1), v_1)

        map2: Any = Dict_ofSeqWithMerge(merge_1, map(mapping_2_2, list2))
        def mapping_3_1(k: str) -> Sample:
            matchValue: Sample | None = Dict_tryFind(k, map1)
            matchValue_1: Sample | None = Dict_tryFind(k, map2)
            if matchValue is None:
                if matchValue_1 is None:
                    raise Exception("If this fails, then I don\'t know how to program")

                else: 
                    v2_1: Sample = matchValue_1
                    return v2_1


            elif matchValue_1 is None:
                v1_1: Sample = matchValue
                return v1_1

            else: 
                v1: Sample = matchValue
                v2: Sample = matchValue_1
                this_2: Update_UpdateOptions = update_options
                record_type_1_2: Sample = v1
                record_type_2_2: Sample = v2
                if this_2.tag == 2:
                    def mapping_4(old_val_4: Any=None, new_val_4: Any=None, k: Any=k) -> Any:
                        return Update_updateAppend(old_val_4, new_val_4)

                    return make_record(Sample_reflection(), map2_2(mapping_4, get_record_fields(record_type_1_2), get_record_fields(record_type_2_2), None))

                elif this_2.tag == 1:
                    def mapping_1_4(old_val_1_2: Any=None, new_val_1_2: Any=None, k: Any=k) -> Any:
                        return Update_updateOnlyByExisting(old_val_1_2, new_val_1_2)

                    return make_record(Sample_reflection(), map2_2(mapping_1_4, get_record_fields(record_type_1_2), get_record_fields(record_type_2_2), None))

                elif this_2.tag == 3:
                    def mapping_2_4(old_val_2_2: Any=None, new_val_2_2: Any=None, k: Any=k) -> Any:
                        return Update_updateOnlyByExistingAppend(old_val_2_2, new_val_2_2)

                    return make_record(Sample_reflection(), map2_2(mapping_2_4, get_record_fields(record_type_1_2), get_record_fields(record_type_2_2), None))

                else: 
                    return record_type_2_2



        class ObjectExpr433:
            @property
            def Equals(self) -> Callable[[str, str], bool]:
                def _arrow432(x: str, y: str) -> bool:
                    return x == y

                return _arrow432

            @property
            def GetHashCode(self) -> Callable[[str], int]:
                return string_hash

        list2_1 = map(mapping_3_1, List_distinct(append(map(mapping_1, list1), map(mapping_1, list2)), ObjectExpr433()))

    except Exception as err:
        raise Exception(((("Could not mergeUpdate " + "Sample") + " list: \n") + str(err)) + "")

    try: 
        def merge_2(record_type__6: Sample, record_type__1_1: Sample) -> Sample:
            this_3: Update_UpdateOptions = update_options_2
            record_type_1_3: Sample = record_type__6
            record_type_2_3: Sample = record_type__1_1
            if this_3.tag == 2:
                def mapping_7(old_val_5: Any=None, new_val_5: Any=None, record_type__6: Any=record_type__6, record_type__1_1: Any=record_type__1_1) -> Any:
                    return Update_updateAppend(old_val_5, new_val_5)

                return make_record(Sample_reflection(), map2_2(mapping_7, get_record_fields(record_type_1_3), get_record_fields(record_type_2_3), None))

            elif this_3.tag == 1:
                def mapping_1_6(old_val_1_3: Any=None, new_val_1_3: Any=None, record_type__6: Any=record_type__6, record_type__1_1: Any=record_type__1_1) -> Any:
                    return Update_updateOnlyByExisting(old_val_1_3, new_val_1_3)

                return make_record(Sample_reflection(), map2_2(mapping_1_6, get_record_fields(record_type_1_3), get_record_fields(record_type_2_3), None))

            elif this_3.tag == 3:
                def mapping_2_5(old_val_2_3: Any=None, new_val_2_3: Any=None, record_type__6: Any=record_type__6, record_type__1_1: Any=record_type__1_1) -> Any:
                    return Update_updateOnlyByExistingAppend(old_val_2_3, new_val_2_3)

                return make_record(Sample_reflection(), map2_2(mapping_2_5, get_record_fields(record_type_1_3), get_record_fields(record_type_2_3), None))

            else: 
                return record_type_2_3


        def mapping_1_5(v_2: Sample) -> tuple[str, Sample]:
            return (mapping_6(v_2), v_2)

        map1_1: Any = Dict_ofSeqWithMerge(merge_2, map(mapping_1_5, list1_1))
        def merge_1_1(record_type__2_1: Sample, record_type__3_1: Sample) -> Sample:
            this_4: Update_UpdateOptions = update_options_2
            record_type_1_4: Sample = record_type__2_1
            record_type_2_4: Sample = record_type__3_1
            if this_4.tag == 2:
                def mapping_8(old_val_6: Any=None, new_val_6: Any=None, record_type__2_1: Any=record_type__2_1, record_type__3_1: Any=record_type__3_1) -> Any:
                    return Update_updateAppend(old_val_6, new_val_6)

                return make_record(Sample_reflection(), map2_2(mapping_8, get_record_fields(record_type_1_4), get_record_fields(record_type_2_4), None))

            elif this_4.tag == 1:
                def mapping_1_7(old_val_1_4: Any=None, new_val_1_4: Any=None, record_type__2_1: Any=record_type__2_1, record_type__3_1: Any=record_type__3_1) -> Any:
                    return Update_updateOnlyByExisting(old_val_1_4, new_val_1_4)

                return make_record(Sample_reflection(), map2_2(mapping_1_7, get_record_fields(record_type_1_4), get_record_fields(record_type_2_4), None))

            elif this_4.tag == 3:
                def mapping_2_7(old_val_2_4: Any=None, new_val_2_4: Any=None, record_type__2_1: Any=record_type__2_1, record_type__3_1: Any=record_type__3_1) -> Any:
                    return Update_updateOnlyByExistingAppend(old_val_2_4, new_val_2_4)

                return make_record(Sample_reflection(), map2_2(mapping_2_7, get_record_fields(record_type_1_4), get_record_fields(record_type_2_4), None))

            else: 
                return record_type_2_4


        def mapping_2_6(v_1_1: Sample) -> tuple[str, Sample]:
            return (mapping_6(v_1_1), v_1_1)

        map2_1: Any = Dict_ofSeqWithMerge(merge_1_1, map(mapping_2_6, list2_1))
        def mapping_3_2(k_1: str) -> Sample:
            matchValue_2: Sample | None = Dict_tryFind(k_1, map1_1)
            matchValue_1_1: Sample | None = Dict_tryFind(k_1, map2_1)
            if matchValue_2 is None:
                if matchValue_1_1 is None:
                    raise Exception("If this fails, then I don\'t know how to program")

                else: 
                    v2_1_1: Sample = matchValue_1_1
                    return v2_1_1


            elif matchValue_1_1 is None:
                v1_1_1: Sample = matchValue_2
                return v1_1_1

            else: 
                v1_2: Sample = matchValue_2
                v2_2: Sample = matchValue_1_1
                this_5: Update_UpdateOptions = update_options_2
                record_type_1_5: Sample = v1_2
                record_type_2_5: Sample = v2_2
                if this_5.tag == 2:
                    def mapping_9(old_val_7: Any=None, new_val_7: Any=None, k_1: Any=k_1) -> Any:
                        return Update_updateAppend(old_val_7, new_val_7)

                    return make_record(Sample_reflection(), map2_2(mapping_9, get_record_fields(record_type_1_5), get_record_fields(record_type_2_5), None))

                elif this_5.tag == 1:
                    def mapping_1_8(old_val_1_5: Any=None, new_val_1_5: Any=None, k_1: Any=k_1) -> Any:
                        return Update_updateOnlyByExisting(old_val_1_5, new_val_1_5)

                    return make_record(Sample_reflection(), map2_2(mapping_1_8, get_record_fields(record_type_1_5), get_record_fields(record_type_2_5), None))

                elif this_5.tag == 3:
                    def mapping_2_8(old_val_2_5: Any=None, new_val_2_5: Any=None, k_1: Any=k_1) -> Any:
                        return Update_updateOnlyByExistingAppend(old_val_2_5, new_val_2_5)

                    return make_record(Sample_reflection(), map2_2(mapping_2_8, get_record_fields(record_type_1_5), get_record_fields(record_type_2_5), None))

                else: 
                    return record_type_2_5



        class ObjectExpr435:
            @property
            def Equals(self) -> Callable[[str, str], bool]:
                def _arrow434(x_1: str, y_1: str) -> bool:
                    return x_1 == y_1

                return _arrow434

            @property
            def GetHashCode(self) -> Callable[[str], int]:
                return string_hash

        return map(mapping_3_2, List_distinct(append(map(mapping_6, list1_1), map(mapping_6, list2_1)), ObjectExpr435()))

    except Exception as err_1:
        raise Exception(((("Could not mergeUpdate " + "Sample") + " list: \n") + str(err_1)) + "")



def Study_getMaterials_7312BC8B(study: Study) -> StudyMaterials:
    process_sequence_materials: FSharpList[Material] = get_materials(Study_getProcesses_7312BC8B(study))
    def mapping(arg: Assay, study: Any=study) -> FSharpList[Material]:
        return AssayMaterials_getMaterials_35E61745(Assay_getMaterials_722A269D(arg))

    assays_materials: FSharpList[Material] = collect(mapping, Study_getAssays_7312BC8B(study))
    materials: FSharpList[Material]
    update_options_2: Update_UpdateOptions = Update_UpdateOptions(3)
    def mapping_6(s_2: Material, study: Any=study) -> str | None:
        return s_2.Name

    list1_1: FSharpList[Material]
    match_value: StudyMaterials | None = study.Materials
    list1_1 = empty() if (match_value is None) else default_arg(match_value.OtherMaterials, empty())
    list2_1: FSharpList[Material]
    update_options: Update_UpdateOptions = Update_UpdateOptions(3)
    def mapping_1(s: Material, study: Any=study) -> str | None:
        return s.Name

    list1: FSharpList[Material] = assays_materials
    list2: FSharpList[Material] = process_sequence_materials
    try: 
        def merge(record_type_: Material, record_type__1: Material) -> Material:
            this: Update_UpdateOptions = update_options
            record_type_1: Material = record_type_
            record_type_2: Material = record_type__1
            if this.tag == 2:
                def mapping_2(old_val: Any=None, new_val: Any=None, record_type_: Any=record_type_, record_type__1: Any=record_type__1) -> Any:
                    return Update_updateAppend(old_val, new_val)

                return make_record(Material_reflection(), map2_2(mapping_2, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

            elif this.tag == 1:
                def mapping_1_2(old_val_1: Any=None, new_val_1: Any=None, record_type_: Any=record_type_, record_type__1: Any=record_type__1) -> Any:
                    return Update_updateOnlyByExisting(old_val_1, new_val_1)

                return make_record(Material_reflection(), map2_2(mapping_1_2, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

            elif this.tag == 3:
                def mapping_2_1(old_val_2: Any=None, new_val_2: Any=None, record_type_: Any=record_type_, record_type__1: Any=record_type__1) -> Any:
                    return Update_updateOnlyByExistingAppend(old_val_2, new_val_2)

                return make_record(Material_reflection(), map2_2(mapping_2_1, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

            else: 
                return record_type_2


        def mapping_1_1(v: Material) -> tuple[str | None, Material]:
            return (mapping_1(v), v)

        map1: Any = Dict_ofSeqWithMerge(merge, map(mapping_1_1, list1))
        def merge_1(record_type__2: Material, record_type__3: Material) -> Material:
            this_1: Update_UpdateOptions = update_options
            record_type_1_1: Material = record_type__2
            record_type_2_1: Material = record_type__3
            if this_1.tag == 2:
                def mapping_3(old_val_3: Any=None, new_val_3: Any=None, record_type__2: Any=record_type__2, record_type__3: Any=record_type__3) -> Any:
                    return Update_updateAppend(old_val_3, new_val_3)

                return make_record(Material_reflection(), map2_2(mapping_3, get_record_fields(record_type_1_1), get_record_fields(record_type_2_1), None))

            elif this_1.tag == 1:
                def mapping_1_3(old_val_1_1: Any=None, new_val_1_1: Any=None, record_type__2: Any=record_type__2, record_type__3: Any=record_type__3) -> Any:
                    return Update_updateOnlyByExisting(old_val_1_1, new_val_1_1)

                return make_record(Material_reflection(), map2_2(mapping_1_3, get_record_fields(record_type_1_1), get_record_fields(record_type_2_1), None))

            elif this_1.tag == 3:
                def mapping_2_3(old_val_2_1: Any=None, new_val_2_1: Any=None, record_type__2: Any=record_type__2, record_type__3: Any=record_type__3) -> Any:
                    return Update_updateOnlyByExistingAppend(old_val_2_1, new_val_2_1)

                return make_record(Material_reflection(), map2_2(mapping_2_3, get_record_fields(record_type_1_1), get_record_fields(record_type_2_1), None))

            else: 
                return record_type_2_1


        def mapping_2_2(v_1: Material) -> tuple[str | None, Material]:
            return (mapping_1(v_1), v_1)

        map2: Any = Dict_ofSeqWithMerge(merge_1, map(mapping_2_2, list2))
        def mapping_3_1(k: str | None=None) -> Material:
            matchValue: Material | None = Dict_tryFind(k, map1)
            matchValue_1: Material | None = Dict_tryFind(k, map2)
            if matchValue is None:
                if matchValue_1 is None:
                    raise Exception("If this fails, then I don\'t know how to program")

                else: 
                    v2_1: Material = matchValue_1
                    return v2_1


            elif matchValue_1 is None:
                v1_1: Material = matchValue
                return v1_1

            else: 
                v1: Material = matchValue
                v2: Material = matchValue_1
                this_2: Update_UpdateOptions = update_options
                record_type_1_2: Material = v1
                record_type_2_2: Material = v2
                if this_2.tag == 2:
                    def mapping_4(old_val_4: Any=None, new_val_4: Any=None, k: Any=k) -> Any:
                        return Update_updateAppend(old_val_4, new_val_4)

                    return make_record(Material_reflection(), map2_2(mapping_4, get_record_fields(record_type_1_2), get_record_fields(record_type_2_2), None))

                elif this_2.tag == 1:
                    def mapping_1_4(old_val_1_2: Any=None, new_val_1_2: Any=None, k: Any=k) -> Any:
                        return Update_updateOnlyByExisting(old_val_1_2, new_val_1_2)

                    return make_record(Material_reflection(), map2_2(mapping_1_4, get_record_fields(record_type_1_2), get_record_fields(record_type_2_2), None))

                elif this_2.tag == 3:
                    def mapping_2_4(old_val_2_2: Any=None, new_val_2_2: Any=None, k: Any=k) -> Any:
                        return Update_updateOnlyByExistingAppend(old_val_2_2, new_val_2_2)

                    return make_record(Material_reflection(), map2_2(mapping_2_4, get_record_fields(record_type_1_2), get_record_fields(record_type_2_2), None))

                else: 
                    return record_type_2_2



        class ObjectExpr436:
            @property
            def Equals(self) -> Callable[[str | None, str | None], bool]:
                return equals

            @property
            def GetHashCode(self) -> Callable[[str | None], int]:
                return structural_hash

        list2_1 = map(mapping_3_1, List_distinct(append(map(mapping_1, list1), map(mapping_1, list2)), ObjectExpr436()))

    except Exception as err:
        raise Exception(((("Could not mergeUpdate " + "Material") + " list: \n") + str(err)) + "")

    try: 
        def merge_2(record_type__6: Material, record_type__1_1: Material) -> Material:
            this_3: Update_UpdateOptions = update_options_2
            record_type_1_3: Material = record_type__6
            record_type_2_3: Material = record_type__1_1
            if this_3.tag == 2:
                def mapping_7(old_val_5: Any=None, new_val_5: Any=None, record_type__6: Any=record_type__6, record_type__1_1: Any=record_type__1_1) -> Any:
                    return Update_updateAppend(old_val_5, new_val_5)

                return make_record(Material_reflection(), map2_2(mapping_7, get_record_fields(record_type_1_3), get_record_fields(record_type_2_3), None))

            elif this_3.tag == 1:
                def mapping_1_6(old_val_1_3: Any=None, new_val_1_3: Any=None, record_type__6: Any=record_type__6, record_type__1_1: Any=record_type__1_1) -> Any:
                    return Update_updateOnlyByExisting(old_val_1_3, new_val_1_3)

                return make_record(Material_reflection(), map2_2(mapping_1_6, get_record_fields(record_type_1_3), get_record_fields(record_type_2_3), None))

            elif this_3.tag == 3:
                def mapping_2_5(old_val_2_3: Any=None, new_val_2_3: Any=None, record_type__6: Any=record_type__6, record_type__1_1: Any=record_type__1_1) -> Any:
                    return Update_updateOnlyByExistingAppend(old_val_2_3, new_val_2_3)

                return make_record(Material_reflection(), map2_2(mapping_2_5, get_record_fields(record_type_1_3), get_record_fields(record_type_2_3), None))

            else: 
                return record_type_2_3


        def mapping_1_5(v_2: Material) -> tuple[str | None, Material]:
            return (mapping_6(v_2), v_2)

        map1_1: Any = Dict_ofSeqWithMerge(merge_2, map(mapping_1_5, list1_1))
        def merge_1_1(record_type__2_1: Material, record_type__3_1: Material) -> Material:
            this_4: Update_UpdateOptions = update_options_2
            record_type_1_4: Material = record_type__2_1
            record_type_2_4: Material = record_type__3_1
            if this_4.tag == 2:
                def mapping_8(old_val_6: Any=None, new_val_6: Any=None, record_type__2_1: Any=record_type__2_1, record_type__3_1: Any=record_type__3_1) -> Any:
                    return Update_updateAppend(old_val_6, new_val_6)

                return make_record(Material_reflection(), map2_2(mapping_8, get_record_fields(record_type_1_4), get_record_fields(record_type_2_4), None))

            elif this_4.tag == 1:
                def mapping_1_7(old_val_1_4: Any=None, new_val_1_4: Any=None, record_type__2_1: Any=record_type__2_1, record_type__3_1: Any=record_type__3_1) -> Any:
                    return Update_updateOnlyByExisting(old_val_1_4, new_val_1_4)

                return make_record(Material_reflection(), map2_2(mapping_1_7, get_record_fields(record_type_1_4), get_record_fields(record_type_2_4), None))

            elif this_4.tag == 3:
                def mapping_2_7(old_val_2_4: Any=None, new_val_2_4: Any=None, record_type__2_1: Any=record_type__2_1, record_type__3_1: Any=record_type__3_1) -> Any:
                    return Update_updateOnlyByExistingAppend(old_val_2_4, new_val_2_4)

                return make_record(Material_reflection(), map2_2(mapping_2_7, get_record_fields(record_type_1_4), get_record_fields(record_type_2_4), None))

            else: 
                return record_type_2_4


        def mapping_2_6(v_1_1: Material) -> tuple[str | None, Material]:
            return (mapping_6(v_1_1), v_1_1)

        map2_1: Any = Dict_ofSeqWithMerge(merge_1_1, map(mapping_2_6, list2_1))
        def mapping_3_2(k_1: str | None=None) -> Material:
            matchValue_2: Material | None = Dict_tryFind(k_1, map1_1)
            matchValue_1_1: Material | None = Dict_tryFind(k_1, map2_1)
            if matchValue_2 is None:
                if matchValue_1_1 is None:
                    raise Exception("If this fails, then I don\'t know how to program")

                else: 
                    v2_1_1: Material = matchValue_1_1
                    return v2_1_1


            elif matchValue_1_1 is None:
                v1_1_1: Material = matchValue_2
                return v1_1_1

            else: 
                v1_2: Material = matchValue_2
                v2_2: Material = matchValue_1_1
                this_5: Update_UpdateOptions = update_options_2
                record_type_1_5: Material = v1_2
                record_type_2_5: Material = v2_2
                if this_5.tag == 2:
                    def mapping_9(old_val_7: Any=None, new_val_7: Any=None, k_1: Any=k_1) -> Any:
                        return Update_updateAppend(old_val_7, new_val_7)

                    return make_record(Material_reflection(), map2_2(mapping_9, get_record_fields(record_type_1_5), get_record_fields(record_type_2_5), None))

                elif this_5.tag == 1:
                    def mapping_1_8(old_val_1_5: Any=None, new_val_1_5: Any=None, k_1: Any=k_1) -> Any:
                        return Update_updateOnlyByExisting(old_val_1_5, new_val_1_5)

                    return make_record(Material_reflection(), map2_2(mapping_1_8, get_record_fields(record_type_1_5), get_record_fields(record_type_2_5), None))

                elif this_5.tag == 3:
                    def mapping_2_8(old_val_2_5: Any=None, new_val_2_5: Any=None, k_1: Any=k_1) -> Any:
                        return Update_updateOnlyByExistingAppend(old_val_2_5, new_val_2_5)

                    return make_record(Material_reflection(), map2_2(mapping_2_8, get_record_fields(record_type_1_5), get_record_fields(record_type_2_5), None))

                else: 
                    return record_type_2_5



        class ObjectExpr437:
            @property
            def Equals(self) -> Callable[[str | None, str | None], bool]:
                return equals

            @property
            def GetHashCode(self) -> Callable[[str | None], int]:
                return structural_hash

        materials = map(mapping_3_2, List_distinct(append(map(mapping_6, list1_1), map(mapping_6, list2_1)), ObjectExpr437()))

    except Exception as err_1:
        raise Exception(((("Could not mergeUpdate " + "Material") + " list: \n") + str(err_1)) + "")

    sources: FSharpList[Source] = Study_getSources_7312BC8B(study)
    samples: FSharpList[Sample] = Study_getSamples_7312BC8B(study)
    return StudyMaterials_make(Option_fromValueWithDefault(empty(), sources), Option_fromValueWithDefault(empty(), samples), Option_fromValueWithDefault(empty(), materials))


def Study_update_7312BC8B(study: Study) -> Study:
    try: 
        protocols: FSharpList[Protocol] = Study_getProtocols_7312BC8B(study)
        Materials: StudyMaterials | None
        v: StudyMaterials = Study_getMaterials_7312BC8B(study)
        Materials = Option_fromValueWithDefault(StudyMaterials_get_empty(), v)
        def mapping_1(list_1: FSharpList[Assay]) -> FSharpList[Assay]:
            def mapping(arg: Assay, list_1: Any=list_1) -> Assay:
                def f2(assay_1: Assay, arg: Any=arg) -> Assay:
                    return Assay_updateProtocols(protocols, assay_1)

                return f2(Assay_update_722A269D(arg))

            return map(mapping, list_1)

        Assays: FSharpList[Assay] | None = map_1(mapping_1, study.Assays)
        Protocols: FSharpList[Protocol] | None = Option_fromValueWithDefault(empty(), protocols)
        Factors: FSharpList[Factor] | None = Option_fromValueWithDefault(empty(), Study_getFactors_7312BC8B(study))
        CharacteristicCategories: FSharpList[MaterialAttribute] | None = Option_fromValueWithDefault(empty(), Study_getCharacteristics_7312BC8B(study))
        UnitCategories: FSharpList[OntologyAnnotation] | None = Option_fromValueWithDefault(empty(), Study_getUnitCategories_7312BC8B(study))
        def mapping_2(process_sequence: FSharpList[Process]) -> FSharpList[Process]:
            return update_protocols(protocols, process_sequence)

        return Study(study.ID, study.FileName, study.Identifier, study.Title, study.Description, study.SubmissionDate, study.PublicReleaseDate, study.Publications, study.Contacts, study.StudyDesignDescriptors, Protocols, Materials, map_1(mapping_2, study.ProcessSequence), Assays, Factors, CharacteristicCategories, UnitCategories, study.Comments)

    except Exception as err:
        return to_fail(((("Could not update study " + str(study.Identifier)) + ": \n") + str(err)) + "")



__all__ = ["Study_reflection", "Study_make", "Study_create_Z2D28E954", "Study_get_empty", "Study_existsByIdentifier", "Study_add", "Study_updateBy", "Study_updateByIdentifier", "Study_removeByIdentifier", "Study_getAssays_7312BC8B", "Study_mapAssays", "Study_setAssays", "Study_mapFactors", "Study_setFactors", "Study_mapProtocols", "Study_setProtocols", "Study_getContacts_7312BC8B", "Study_mapContacts", "Study_setContacts", "Study_getPublications_7312BC8B", "Study_mapPublications", "Study_setPublications", "Study_getDescriptors_7312BC8B", "Study_mapDescriptors", "Study_setDescriptors", "Study_getProcesses_7312BC8B", "Study_getProtocols_7312BC8B", "Study_getCharacteristics_7312BC8B", "Study_getFactors_7312BC8B", "Study_getUnitCategories_7312BC8B", "Study_getSources_7312BC8B", "Study_getSamples_7312BC8B", "Study_getMaterials_7312BC8B", "Study_update_7312BC8B"]

