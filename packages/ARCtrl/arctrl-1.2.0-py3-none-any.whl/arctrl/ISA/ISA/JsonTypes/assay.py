from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any
from ....fable_modules.fable_library.array_ import map2 as map2_2
from ....fable_modules.fable_library.list import (FSharpList, try_find, exists, append, singleton, map, filter, empty)
from ....fable_modules.fable_library.option import (default_arg, map as map_1)
from ....fable_modules.fable_library.reflection import (TypeInfo, string_type, option_type, list_type, record_type, make_record, get_record_fields)
from ....fable_modules.fable_library.seq2 import List_distinct
from ....fable_modules.fable_library.string_ import to_fail
from ....fable_modules.fable_library.types import Record
from ....fable_modules.fable_library.util import (equals, structural_hash, safe_hash)
from ..helper import (Update_updateAppend, Update_updateOnlyByExisting, Update_updateOnlyByExistingAppend, Dict_ofSeqWithMerge, Dict_tryFind)
from ..helper import (Update_UpdateOptions, Option_mapDefault, Option_fromValueWithDefault)
from .assay_materials import (AssayMaterials, AssayMaterials_reflection, AssayMaterials_make, AssayMaterials_get_empty)
from .comment import (Comment, Comment_reflection)
from .data import (Data, Data_reflection)
from .factor import Factor
from .factor_value import FactorValue
from .material import (Material, Material_reflection)
from .material_attribute import (MaterialAttribute, MaterialAttribute_reflection)
from .material_attribute_value import MaterialAttributeValue
from .ontology_annotation import (OntologyAnnotation, OntologyAnnotation_reflection)
from .process import (Process, Process_reflection)
from .process_input import ProcessInput
from .process_output import ProcessOutput
from .process_parameter_value import ProcessParameterValue
from .process_sequence import (get_data, get_units, get_characteristics, get_sources, get_samples, get_materials, get_inputs_with_parameter_by, get_outputs_with_parameter_by, get_parameters, get_inputs_with_characteristic_by, get_outputs_with_characteristic_by, get_outputs_with_factor_by, get_factors, get_protocols, update_protocols)
from .protocol import Protocol
from .protocol_parameter import ProtocolParameter
from .sample import (Sample, Sample_reflection)
from .source import Source

def _expr395() -> TypeInfo:
    return record_type("ARCtrl.ISA.Assay", [], Assay, lambda: [("ID", option_type(string_type)), ("FileName", option_type(string_type)), ("MeasurementType", option_type(OntologyAnnotation_reflection())), ("TechnologyType", option_type(OntologyAnnotation_reflection())), ("TechnologyPlatform", option_type(string_type)), ("DataFiles", option_type(list_type(Data_reflection()))), ("Materials", option_type(AssayMaterials_reflection())), ("CharacteristicCategories", option_type(list_type(MaterialAttribute_reflection()))), ("UnitCategories", option_type(list_type(OntologyAnnotation_reflection()))), ("ProcessSequence", option_type(list_type(Process_reflection()))), ("Comments", option_type(list_type(Comment_reflection())))])


@dataclass(eq = False, repr = False, slots = True)
class Assay(Record):
    ID: str | None
    FileName: str | None
    MeasurementType: OntologyAnnotation | None
    TechnologyType: OntologyAnnotation | None
    TechnologyPlatform: str | None
    DataFiles: FSharpList[Data] | None
    Materials: AssayMaterials | None
    CharacteristicCategories: FSharpList[MaterialAttribute] | None
    UnitCategories: FSharpList[OntologyAnnotation] | None
    ProcessSequence: FSharpList[Process] | None
    Comments: FSharpList[Comment] | None

Assay_reflection = _expr395

def Assay_make(id: str | None=None, file_name: str | None=None, measurement_type: OntologyAnnotation | None=None, technology_type: OntologyAnnotation | None=None, technology_platform: str | None=None, data_files: FSharpList[Data] | None=None, materials: AssayMaterials | None=None, characteristic_categories: FSharpList[MaterialAttribute] | None=None, unit_categories: FSharpList[OntologyAnnotation] | None=None, process_sequence: FSharpList[Process] | None=None, comments: FSharpList[Comment] | None=None) -> Assay:
    return Assay(id, file_name, measurement_type, technology_type, technology_platform, data_files, materials, characteristic_categories, unit_categories, process_sequence, comments)


def Assay_create_3D372A24(Id: str | None=None, FileName: str | None=None, MeasurementType: OntologyAnnotation | None=None, TechnologyType: OntologyAnnotation | None=None, TechnologyPlatform: str | None=None, DataFiles: FSharpList[Data] | None=None, Materials: AssayMaterials | None=None, CharacteristicCategories: FSharpList[MaterialAttribute] | None=None, UnitCategories: FSharpList[OntologyAnnotation] | None=None, ProcessSequence: FSharpList[Process] | None=None, Comments: FSharpList[Comment] | None=None) -> Assay:
    return Assay_make(Id, FileName, MeasurementType, TechnologyType, TechnologyPlatform, DataFiles, Materials, CharacteristicCategories, UnitCategories, ProcessSequence, Comments)


def Assay_get_empty(__unit: None=None) -> Assay:
    return Assay_create_3D372A24()


def Assay_tryGetByFileName(file_name: str, assays: FSharpList[Assay]) -> Assay | None:
    def _arrow396(a: Assay, file_name: Any=file_name, assays: Any=assays) -> bool:
        return equals(a.FileName, file_name)

    return try_find(_arrow396, assays)


def Assay_existsByFileName(file_name: str, assays: FSharpList[Assay]) -> bool:
    def _arrow397(a: Assay, file_name: Any=file_name, assays: Any=assays) -> bool:
        return equals(a.FileName, file_name)

    return exists(_arrow397, assays)


def Assay_add(assays: FSharpList[Assay], assay: Assay) -> FSharpList[Assay]:
    return append(assays, singleton(assay))


def Assay_updateBy(predicate: Callable[[Assay], bool], update_option: Update_UpdateOptions, assay: Assay, assays: FSharpList[Assay]) -> FSharpList[Assay]:
    if exists(predicate, assays):
        def mapping_3(a: Assay, predicate: Any=predicate, update_option: Any=update_option, assay: Any=assay, assays: Any=assays) -> Assay:
            if predicate(a):
                this: Update_UpdateOptions = update_option
                record_type_1: Assay = a
                record_type_2: Assay = assay
                if this.tag == 2:
                    def mapping(old_val: Any=None, new_val: Any=None, a: Any=a) -> Any:
                        return Update_updateAppend(old_val, new_val)

                    return make_record(Assay_reflection(), map2_2(mapping, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                elif this.tag == 1:
                    def mapping_1(old_val_1: Any=None, new_val_1: Any=None, a: Any=a) -> Any:
                        return Update_updateOnlyByExisting(old_val_1, new_val_1)

                    return make_record(Assay_reflection(), map2_2(mapping_1, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                elif this.tag == 3:
                    def mapping_2(old_val_2: Any=None, new_val_2: Any=None, a: Any=a) -> Any:
                        return Update_updateOnlyByExistingAppend(old_val_2, new_val_2)

                    return make_record(Assay_reflection(), map2_2(mapping_2, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                else: 
                    return record_type_2


            else: 
                return a


        return map(mapping_3, assays)

    else: 
        return assays



def Assay_updateByFileName(update_option: Update_UpdateOptions, assay: Assay, assays: FSharpList[Assay]) -> FSharpList[Assay]:
    def predicate(a: Assay, update_option: Any=update_option, assay: Any=assay, assays: Any=assays) -> bool:
        return equals(a.FileName, assay.FileName)

    return Assay_updateBy(predicate, update_option, assay, assays)


def Assay_removeByFileName(file_name: str, assays: FSharpList[Assay]) -> FSharpList[Assay]:
    def _arrow398(a: Assay, file_name: Any=file_name, assays: Any=assays) -> bool:
        return not equals(a.FileName, file_name)

    return filter(_arrow398, assays)


def Assay_getComments_722A269D(assay: Assay) -> FSharpList[Comment] | None:
    return assay.Comments


def Assay_mapComments(f: Callable[[FSharpList[Comment]], FSharpList[Comment]], assay: Assay) -> Assay:
    return Assay(assay.ID, assay.FileName, assay.MeasurementType, assay.TechnologyType, assay.TechnologyPlatform, assay.DataFiles, assay.Materials, assay.CharacteristicCategories, assay.UnitCategories, assay.ProcessSequence, Option_mapDefault(empty(), f, assay.Comments))


def Assay_setComments(assay: Assay, comments: FSharpList[Comment]) -> Assay:
    return Assay(assay.ID, assay.FileName, assay.MeasurementType, assay.TechnologyType, assay.TechnologyPlatform, assay.DataFiles, assay.Materials, assay.CharacteristicCategories, assay.UnitCategories, assay.ProcessSequence, comments)


def Assay_getData_722A269D(assay: Assay) -> FSharpList[Data]:
    process_sequence_data: FSharpList[Data] = get_data(default_arg(assay.ProcessSequence, empty()))
    update_options: Update_UpdateOptions = Update_UpdateOptions(3)
    def mapping(d: Data, assay: Any=assay) -> str | None:
        return d.Name

    list1: FSharpList[Data] = default_arg(assay.DataFiles, empty())
    list2: FSharpList[Data] = process_sequence_data
    try: 
        def merge(record_type_: Data, record_type__1: Data) -> Data:
            this: Update_UpdateOptions = update_options
            record_type_1: Data = record_type_
            record_type_2: Data = record_type__1
            if this.tag == 2:
                def mapping_2(old_val: Any=None, new_val: Any=None, record_type_: Any=record_type_, record_type__1: Any=record_type__1) -> Any:
                    return Update_updateAppend(old_val, new_val)

                return make_record(Data_reflection(), map2_2(mapping_2, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

            elif this.tag == 1:
                def mapping_1_1(old_val_1: Any=None, new_val_1: Any=None, record_type_: Any=record_type_, record_type__1: Any=record_type__1) -> Any:
                    return Update_updateOnlyByExisting(old_val_1, new_val_1)

                return make_record(Data_reflection(), map2_2(mapping_1_1, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

            elif this.tag == 3:
                def mapping_2_1(old_val_2: Any=None, new_val_2: Any=None, record_type_: Any=record_type_, record_type__1: Any=record_type__1) -> Any:
                    return Update_updateOnlyByExistingAppend(old_val_2, new_val_2)

                return make_record(Data_reflection(), map2_2(mapping_2_1, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

            else: 
                return record_type_2


        def mapping_1(v: Data) -> tuple[str | None, Data]:
            return (mapping(v), v)

        map1: Any = Dict_ofSeqWithMerge(merge, map(mapping_1, list1))
        def merge_1(record_type__2: Data, record_type__3: Data) -> Data:
            this_1: Update_UpdateOptions = update_options
            record_type_1_1: Data = record_type__2
            record_type_2_1: Data = record_type__3
            if this_1.tag == 2:
                def mapping_3(old_val_3: Any=None, new_val_3: Any=None, record_type__2: Any=record_type__2, record_type__3: Any=record_type__3) -> Any:
                    return Update_updateAppend(old_val_3, new_val_3)

                return make_record(Data_reflection(), map2_2(mapping_3, get_record_fields(record_type_1_1), get_record_fields(record_type_2_1), None))

            elif this_1.tag == 1:
                def mapping_1_2(old_val_1_1: Any=None, new_val_1_1: Any=None, record_type__2: Any=record_type__2, record_type__3: Any=record_type__3) -> Any:
                    return Update_updateOnlyByExisting(old_val_1_1, new_val_1_1)

                return make_record(Data_reflection(), map2_2(mapping_1_2, get_record_fields(record_type_1_1), get_record_fields(record_type_2_1), None))

            elif this_1.tag == 3:
                def mapping_2_3(old_val_2_1: Any=None, new_val_2_1: Any=None, record_type__2: Any=record_type__2, record_type__3: Any=record_type__3) -> Any:
                    return Update_updateOnlyByExistingAppend(old_val_2_1, new_val_2_1)

                return make_record(Data_reflection(), map2_2(mapping_2_3, get_record_fields(record_type_1_1), get_record_fields(record_type_2_1), None))

            else: 
                return record_type_2_1


        def mapping_2_2(v_1: Data) -> tuple[str | None, Data]:
            return (mapping(v_1), v_1)

        map2: Any = Dict_ofSeqWithMerge(merge_1, map(mapping_2_2, list2))
        def mapping_3_1(k: str | None=None) -> Data:
            matchValue: Data | None = Dict_tryFind(k, map1)
            matchValue_1: Data | None = Dict_tryFind(k, map2)
            if matchValue is None:
                if matchValue_1 is None:
                    raise Exception("If this fails, then I don\'t know how to program")

                else: 
                    v2_1: Data = matchValue_1
                    return v2_1


            elif matchValue_1 is None:
                v1_1: Data = matchValue
                return v1_1

            else: 
                v1: Data = matchValue
                v2: Data = matchValue_1
                this_2: Update_UpdateOptions = update_options
                record_type_1_2: Data = v1
                record_type_2_2: Data = v2
                if this_2.tag == 2:
                    def mapping_4(old_val_4: Any=None, new_val_4: Any=None, k: Any=k) -> Any:
                        return Update_updateAppend(old_val_4, new_val_4)

                    return make_record(Data_reflection(), map2_2(mapping_4, get_record_fields(record_type_1_2), get_record_fields(record_type_2_2), None))

                elif this_2.tag == 1:
                    def mapping_1_3(old_val_1_2: Any=None, new_val_1_2: Any=None, k: Any=k) -> Any:
                        return Update_updateOnlyByExisting(old_val_1_2, new_val_1_2)

                    return make_record(Data_reflection(), map2_2(mapping_1_3, get_record_fields(record_type_1_2), get_record_fields(record_type_2_2), None))

                elif this_2.tag == 3:
                    def mapping_2_4(old_val_2_2: Any=None, new_val_2_2: Any=None, k: Any=k) -> Any:
                        return Update_updateOnlyByExistingAppend(old_val_2_2, new_val_2_2)

                    return make_record(Data_reflection(), map2_2(mapping_2_4, get_record_fields(record_type_1_2), get_record_fields(record_type_2_2), None))

                else: 
                    return record_type_2_2



        class ObjectExpr399:
            @property
            def Equals(self) -> Callable[[str | None, str | None], bool]:
                return equals

            @property
            def GetHashCode(self) -> Callable[[str | None], int]:
                return structural_hash

        return map(mapping_3_1, List_distinct(append(map(mapping, list1), map(mapping, list2)), ObjectExpr399()))

    except Exception as err:
        raise Exception(((("Could not mergeUpdate " + "Data") + " list: \n") + str(err)) + "")



def Assay_mapData(f: Callable[[FSharpList[Data]], FSharpList[Data]], assay: Assay) -> Assay:
    return Assay(assay.ID, assay.FileName, assay.MeasurementType, assay.TechnologyType, assay.TechnologyPlatform, Option_mapDefault(empty(), f, assay.DataFiles), assay.Materials, assay.CharacteristicCategories, assay.UnitCategories, assay.ProcessSequence, assay.Comments)


def Assay_setData(assay: Assay, data_files: FSharpList[Data]) -> Assay:
    return Assay(assay.ID, assay.FileName, assay.MeasurementType, assay.TechnologyType, assay.TechnologyPlatform, data_files, assay.Materials, assay.CharacteristicCategories, assay.UnitCategories, assay.ProcessSequence, assay.Comments)


def Assay_getUnitCategories_722A269D(assay: Assay) -> FSharpList[OntologyAnnotation]:
    class ObjectExpr400:
        @property
        def Equals(self) -> Callable[[OntologyAnnotation, OntologyAnnotation], bool]:
            return equals

        @property
        def GetHashCode(self) -> Callable[[OntologyAnnotation], int]:
            return safe_hash

    return List_distinct(append(get_units(default_arg(assay.ProcessSequence, empty())), default_arg(assay.UnitCategories, empty())), ObjectExpr400())


def Assay_mapUnitCategories(f: Callable[[FSharpList[OntologyAnnotation]], FSharpList[OntologyAnnotation]], assay: Assay) -> Assay:
    return Assay(assay.ID, assay.FileName, assay.MeasurementType, assay.TechnologyType, assay.TechnologyPlatform, assay.DataFiles, assay.Materials, assay.CharacteristicCategories, Option_mapDefault(empty(), f, assay.UnitCategories), assay.ProcessSequence, assay.Comments)


def Assay_setUnitCategories(assay: Assay, unit_categories: FSharpList[OntologyAnnotation]) -> Assay:
    return Assay(assay.ID, assay.FileName, assay.MeasurementType, assay.TechnologyType, assay.TechnologyPlatform, assay.DataFiles, assay.Materials, assay.CharacteristicCategories, unit_categories, assay.ProcessSequence, assay.Comments)


def Assay_getCharacteristics_722A269D(assay: Assay) -> FSharpList[MaterialAttribute]:
    class ObjectExpr401:
        @property
        def Equals(self) -> Callable[[MaterialAttribute, MaterialAttribute], bool]:
            return equals

        @property
        def GetHashCode(self) -> Callable[[MaterialAttribute], int]:
            return safe_hash

    return List_distinct(append(get_characteristics(default_arg(assay.ProcessSequence, empty())), default_arg(assay.CharacteristicCategories, empty())), ObjectExpr401())


def Assay_mapCharacteristics(f: Callable[[FSharpList[MaterialAttribute]], FSharpList[MaterialAttribute]], assay: Assay) -> Assay:
    return Assay(assay.ID, assay.FileName, assay.MeasurementType, assay.TechnologyType, assay.TechnologyPlatform, assay.DataFiles, assay.Materials, Option_mapDefault(empty(), f, assay.CharacteristicCategories), assay.UnitCategories, assay.ProcessSequence, assay.Comments)


def Assay_setCharacteristics(assay: Assay, characteristics: FSharpList[MaterialAttribute]) -> Assay:
    return Assay(assay.ID, assay.FileName, assay.MeasurementType, assay.TechnologyType, assay.TechnologyPlatform, assay.DataFiles, assay.Materials, characteristics, assay.UnitCategories, assay.ProcessSequence, assay.Comments)


def Assay_getMeasurementType_722A269D(assay: Assay) -> OntologyAnnotation | None:
    return assay.MeasurementType


def Assay_mapMeasurementType(f: Callable[[OntologyAnnotation], OntologyAnnotation], assay: Assay) -> Assay:
    return Assay(assay.ID, assay.FileName, map_1(f, assay.MeasurementType), assay.TechnologyType, assay.TechnologyPlatform, assay.DataFiles, assay.Materials, assay.CharacteristicCategories, assay.UnitCategories, assay.ProcessSequence, assay.Comments)


def Assay_setMeasurementType(assay: Assay, measurement_type: OntologyAnnotation) -> Assay:
    return Assay(assay.ID, assay.FileName, measurement_type, assay.TechnologyType, assay.TechnologyPlatform, assay.DataFiles, assay.Materials, assay.CharacteristicCategories, assay.UnitCategories, assay.ProcessSequence, assay.Comments)


def Assay_getTechnologyType_722A269D(assay: Assay) -> OntologyAnnotation | None:
    return assay.TechnologyType


def Assay_mapTechnologyType(f: Callable[[OntologyAnnotation], OntologyAnnotation], assay: Assay) -> Assay:
    return Assay(assay.ID, assay.FileName, assay.MeasurementType, map_1(f, assay.TechnologyType), assay.TechnologyPlatform, assay.DataFiles, assay.Materials, assay.CharacteristicCategories, assay.UnitCategories, assay.ProcessSequence, assay.Comments)


def Assay_setTechnologyType(assay: Assay, technology_type: OntologyAnnotation) -> Assay:
    return Assay(assay.ID, assay.FileName, assay.MeasurementType, technology_type, assay.TechnologyPlatform, assay.DataFiles, assay.Materials, assay.CharacteristicCategories, assay.UnitCategories, assay.ProcessSequence, assay.Comments)


def Assay_getProcesses_722A269D(assay: Assay) -> FSharpList[Process]:
    return default_arg(assay.ProcessSequence, empty())


def Assay_mapProcesses(f: Callable[[FSharpList[Process]], FSharpList[Process]], assay: Assay) -> Assay:
    return Assay(assay.ID, assay.FileName, assay.MeasurementType, assay.TechnologyType, assay.TechnologyPlatform, assay.DataFiles, assay.Materials, assay.CharacteristicCategories, assay.UnitCategories, Option_mapDefault(empty(), f, assay.ProcessSequence), assay.Comments)


def Assay_setProcesses(assay: Assay, processes: FSharpList[Process]) -> Assay:
    return Assay(assay.ID, assay.FileName, assay.MeasurementType, assay.TechnologyType, assay.TechnologyPlatform, assay.DataFiles, assay.Materials, assay.CharacteristicCategories, assay.UnitCategories, processes, assay.Comments)


def Assay_getSources_722A269D(assay: Assay) -> FSharpList[Source]:
    return get_sources(Assay_getProcesses_722A269D(assay))


def Assay_getSamples_722A269D(assay: Assay) -> FSharpList[Sample]:
    return get_samples(Assay_getProcesses_722A269D(assay))


def Assay_getMaterials_722A269D(assay: Assay) -> AssayMaterials:
    process_sequence_materials: FSharpList[Material] = get_materials(default_arg(assay.ProcessSequence, empty()))
    process_sequence_samples: FSharpList[Sample] = get_samples(default_arg(assay.ProcessSequence, empty()))
    match_value: AssayMaterials | None = assay.Materials
    if match_value is None:
        return AssayMaterials_make(Option_fromValueWithDefault(empty(), process_sequence_samples), Option_fromValueWithDefault(empty(), process_sequence_materials))

    else: 
        mat: AssayMaterials = match_value
        samples: FSharpList[Sample]
        update_options: Update_UpdateOptions = Update_UpdateOptions(3)
        def mapping(s: Sample, assay: Any=assay) -> str | None:
            return s.Name

        list1: FSharpList[Sample] = default_arg(mat.Samples, empty())
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
                    def mapping_1_1(old_val_1: Any=None, new_val_1: Any=None, record_type_: Any=record_type_, record_type__1: Any=record_type__1) -> Any:
                        return Update_updateOnlyByExisting(old_val_1, new_val_1)

                    return make_record(Sample_reflection(), map2_2(mapping_1_1, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                elif this.tag == 3:
                    def mapping_2_1(old_val_2: Any=None, new_val_2: Any=None, record_type_: Any=record_type_, record_type__1: Any=record_type__1) -> Any:
                        return Update_updateOnlyByExistingAppend(old_val_2, new_val_2)

                    return make_record(Sample_reflection(), map2_2(mapping_2_1, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                else: 
                    return record_type_2


            def mapping_1(v: Sample) -> tuple[str | None, Sample]:
                return (mapping(v), v)

            map1: Any = Dict_ofSeqWithMerge(merge, map(mapping_1, list1))
            def merge_1(record_type__2: Sample, record_type__3: Sample) -> Sample:
                this_1: Update_UpdateOptions = update_options
                record_type_1_1: Sample = record_type__2
                record_type_2_1: Sample = record_type__3
                if this_1.tag == 2:
                    def mapping_3(old_val_3: Any=None, new_val_3: Any=None, record_type__2: Any=record_type__2, record_type__3: Any=record_type__3) -> Any:
                        return Update_updateAppend(old_val_3, new_val_3)

                    return make_record(Sample_reflection(), map2_2(mapping_3, get_record_fields(record_type_1_1), get_record_fields(record_type_2_1), None))

                elif this_1.tag == 1:
                    def mapping_1_2(old_val_1_1: Any=None, new_val_1_1: Any=None, record_type__2: Any=record_type__2, record_type__3: Any=record_type__3) -> Any:
                        return Update_updateOnlyByExisting(old_val_1_1, new_val_1_1)

                    return make_record(Sample_reflection(), map2_2(mapping_1_2, get_record_fields(record_type_1_1), get_record_fields(record_type_2_1), None))

                elif this_1.tag == 3:
                    def mapping_2_3(old_val_2_1: Any=None, new_val_2_1: Any=None, record_type__2: Any=record_type__2, record_type__3: Any=record_type__3) -> Any:
                        return Update_updateOnlyByExistingAppend(old_val_2_1, new_val_2_1)

                    return make_record(Sample_reflection(), map2_2(mapping_2_3, get_record_fields(record_type_1_1), get_record_fields(record_type_2_1), None))

                else: 
                    return record_type_2_1


            def mapping_2_2(v_1: Sample) -> tuple[str | None, Sample]:
                return (mapping(v_1), v_1)

            map2: Any = Dict_ofSeqWithMerge(merge_1, map(mapping_2_2, list2))
            def mapping_3_1(k: str | None=None) -> Sample:
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
                        def mapping_1_3(old_val_1_2: Any=None, new_val_1_2: Any=None, k: Any=k) -> Any:
                            return Update_updateOnlyByExisting(old_val_1_2, new_val_1_2)

                        return make_record(Sample_reflection(), map2_2(mapping_1_3, get_record_fields(record_type_1_2), get_record_fields(record_type_2_2), None))

                    elif this_2.tag == 3:
                        def mapping_2_4(old_val_2_2: Any=None, new_val_2_2: Any=None, k: Any=k) -> Any:
                            return Update_updateOnlyByExistingAppend(old_val_2_2, new_val_2_2)

                        return make_record(Sample_reflection(), map2_2(mapping_2_4, get_record_fields(record_type_1_2), get_record_fields(record_type_2_2), None))

                    else: 
                        return record_type_2_2



            class ObjectExpr402:
                @property
                def Equals(self) -> Callable[[str | None, str | None], bool]:
                    return equals

                @property
                def GetHashCode(self) -> Callable[[str | None], int]:
                    return structural_hash

            samples = map(mapping_3_1, List_distinct(append(map(mapping, list1), map(mapping, list2)), ObjectExpr402()))

        except Exception as err:
            raise Exception(((("Could not mergeUpdate " + "Sample") + " list: \n") + str(err)) + "")

        materials: FSharpList[Material]
        update_options_1: Update_UpdateOptions = Update_UpdateOptions(3)
        def mapping_5(m: Material, assay: Any=assay) -> str | None:
            return m.Name

        list1_1: FSharpList[Material] = default_arg(mat.OtherMaterials, empty())
        list2_1: FSharpList[Material] = process_sequence_materials
        try: 
            def merge_2(record_type__6: Material, record_type__1_1: Material) -> Material:
                this_3: Update_UpdateOptions = update_options_1
                record_type_1_3: Material = record_type__6
                record_type_2_3: Material = record_type__1_1
                if this_3.tag == 2:
                    def mapping_6(old_val_5: Any=None, new_val_5: Any=None, record_type__6: Any=record_type__6, record_type__1_1: Any=record_type__1_1) -> Any:
                        return Update_updateAppend(old_val_5, new_val_5)

                    return make_record(Material_reflection(), map2_2(mapping_6, get_record_fields(record_type_1_3), get_record_fields(record_type_2_3), None))

                elif this_3.tag == 1:
                    def mapping_1_5(old_val_1_3: Any=None, new_val_1_3: Any=None, record_type__6: Any=record_type__6, record_type__1_1: Any=record_type__1_1) -> Any:
                        return Update_updateOnlyByExisting(old_val_1_3, new_val_1_3)

                    return make_record(Material_reflection(), map2_2(mapping_1_5, get_record_fields(record_type_1_3), get_record_fields(record_type_2_3), None))

                elif this_3.tag == 3:
                    def mapping_2_5(old_val_2_3: Any=None, new_val_2_3: Any=None, record_type__6: Any=record_type__6, record_type__1_1: Any=record_type__1_1) -> Any:
                        return Update_updateOnlyByExistingAppend(old_val_2_3, new_val_2_3)

                    return make_record(Material_reflection(), map2_2(mapping_2_5, get_record_fields(record_type_1_3), get_record_fields(record_type_2_3), None))

                else: 
                    return record_type_2_3


            def mapping_1_4(v_2: Material) -> tuple[str | None, Material]:
                return (mapping_5(v_2), v_2)

            map1_1: Any = Dict_ofSeqWithMerge(merge_2, map(mapping_1_4, list1_1))
            def merge_1_1(record_type__2_1: Material, record_type__3_1: Material) -> Material:
                this_4: Update_UpdateOptions = update_options_1
                record_type_1_4: Material = record_type__2_1
                record_type_2_4: Material = record_type__3_1
                if this_4.tag == 2:
                    def mapping_7(old_val_6: Any=None, new_val_6: Any=None, record_type__2_1: Any=record_type__2_1, record_type__3_1: Any=record_type__3_1) -> Any:
                        return Update_updateAppend(old_val_6, new_val_6)

                    return make_record(Material_reflection(), map2_2(mapping_7, get_record_fields(record_type_1_4), get_record_fields(record_type_2_4), None))

                elif this_4.tag == 1:
                    def mapping_1_6(old_val_1_4: Any=None, new_val_1_4: Any=None, record_type__2_1: Any=record_type__2_1, record_type__3_1: Any=record_type__3_1) -> Any:
                        return Update_updateOnlyByExisting(old_val_1_4, new_val_1_4)

                    return make_record(Material_reflection(), map2_2(mapping_1_6, get_record_fields(record_type_1_4), get_record_fields(record_type_2_4), None))

                elif this_4.tag == 3:
                    def mapping_2_7(old_val_2_4: Any=None, new_val_2_4: Any=None, record_type__2_1: Any=record_type__2_1, record_type__3_1: Any=record_type__3_1) -> Any:
                        return Update_updateOnlyByExistingAppend(old_val_2_4, new_val_2_4)

                    return make_record(Material_reflection(), map2_2(mapping_2_7, get_record_fields(record_type_1_4), get_record_fields(record_type_2_4), None))

                else: 
                    return record_type_2_4


            def mapping_2_6(v_1_1: Material) -> tuple[str | None, Material]:
                return (mapping_5(v_1_1), v_1_1)

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
                    this_5: Update_UpdateOptions = update_options_1
                    record_type_1_5: Material = v1_2
                    record_type_2_5: Material = v2_2
                    if this_5.tag == 2:
                        def mapping_8(old_val_7: Any=None, new_val_7: Any=None, k_1: Any=k_1) -> Any:
                            return Update_updateAppend(old_val_7, new_val_7)

                        return make_record(Material_reflection(), map2_2(mapping_8, get_record_fields(record_type_1_5), get_record_fields(record_type_2_5), None))

                    elif this_5.tag == 1:
                        def mapping_1_7(old_val_1_5: Any=None, new_val_1_5: Any=None, k_1: Any=k_1) -> Any:
                            return Update_updateOnlyByExisting(old_val_1_5, new_val_1_5)

                        return make_record(Material_reflection(), map2_2(mapping_1_7, get_record_fields(record_type_1_5), get_record_fields(record_type_2_5), None))

                    elif this_5.tag == 3:
                        def mapping_2_8(old_val_2_5: Any=None, new_val_2_5: Any=None, k_1: Any=k_1) -> Any:
                            return Update_updateOnlyByExistingAppend(old_val_2_5, new_val_2_5)

                        return make_record(Material_reflection(), map2_2(mapping_2_8, get_record_fields(record_type_1_5), get_record_fields(record_type_2_5), None))

                    else: 
                        return record_type_2_5



            class ObjectExpr403:
                @property
                def Equals(self) -> Callable[[str | None, str | None], bool]:
                    return equals

                @property
                def GetHashCode(self) -> Callable[[str | None], int]:
                    return structural_hash

            materials = map(mapping_3_2, List_distinct(append(map(mapping_5, list1_1), map(mapping_5, list2_1)), ObjectExpr403()))

        except Exception as err_1:
            raise Exception(((("Could not mergeUpdate " + "Material") + " list: \n") + str(err_1)) + "")

        return AssayMaterials_make(Option_fromValueWithDefault(empty(), samples), Option_fromValueWithDefault(empty(), materials))



def Assay_mapMaterials(f: Callable[[AssayMaterials], AssayMaterials], assay: Assay) -> Assay:
    return Assay(assay.ID, assay.FileName, assay.MeasurementType, assay.TechnologyType, assay.TechnologyPlatform, assay.DataFiles, map_1(f, assay.Materials), assay.CharacteristicCategories, assay.UnitCategories, assay.ProcessSequence, assay.Comments)


def Assay_setMaterials(assay: Assay, materials: AssayMaterials) -> Assay:
    return Assay(assay.ID, assay.FileName, assay.MeasurementType, assay.TechnologyType, assay.TechnologyPlatform, assay.DataFiles, materials, assay.CharacteristicCategories, assay.UnitCategories, assay.ProcessSequence, assay.Comments)


def Assay_getInputsWithParameterBy(predicate: Callable[[ProtocolParameter], bool], assay: Assay) -> FSharpList[tuple[ProcessInput, ProcessParameterValue]] | None:
    def mapping(process_sequence: FSharpList[Process], predicate: Any=predicate, assay: Any=assay) -> FSharpList[tuple[ProcessInput, ProcessParameterValue]]:
        return get_inputs_with_parameter_by(predicate, process_sequence)

    return map_1(mapping, assay.ProcessSequence)


def Assay_getOutputsWithParameterBy(predicate: Callable[[ProtocolParameter], bool], assay: Assay) -> FSharpList[tuple[ProcessOutput, ProcessParameterValue]] | None:
    def mapping(process_sequence: FSharpList[Process], predicate: Any=predicate, assay: Any=assay) -> FSharpList[tuple[ProcessOutput, ProcessParameterValue]]:
        return get_outputs_with_parameter_by(predicate, process_sequence)

    return map_1(mapping, assay.ProcessSequence)


def Assay_getParameters_722A269D(assay: Assay) -> FSharpList[ProtocolParameter] | None:
    def _arrow404(process_sequence: FSharpList[Process], assay: Any=assay) -> FSharpList[ProtocolParameter]:
        return get_parameters(process_sequence)

    return map_1(_arrow404, assay.ProcessSequence)


def Assay_getInputsWithCharacteristicBy(predicate: Callable[[MaterialAttribute], bool], assay: Assay) -> FSharpList[tuple[ProcessInput, MaterialAttributeValue]] | None:
    def mapping(process_sequence: FSharpList[Process], predicate: Any=predicate, assay: Any=assay) -> FSharpList[tuple[ProcessInput, MaterialAttributeValue]]:
        return get_inputs_with_characteristic_by(predicate, process_sequence)

    return map_1(mapping, assay.ProcessSequence)


def Assay_getOutputsWithCharacteristicBy(predicate: Callable[[MaterialAttribute], bool], assay: Assay) -> FSharpList[tuple[ProcessOutput, MaterialAttributeValue]] | None:
    def mapping(process_sequence: FSharpList[Process], predicate: Any=predicate, assay: Any=assay) -> FSharpList[tuple[ProcessOutput, MaterialAttributeValue]]:
        return get_outputs_with_characteristic_by(predicate, process_sequence)

    return map_1(mapping, assay.ProcessSequence)


def Assay_getOutputsWithFactorBy(predicate: Callable[[Factor], bool], assay: Assay) -> FSharpList[tuple[ProcessOutput, FactorValue]] | None:
    def mapping(process_sequence: FSharpList[Process], predicate: Any=predicate, assay: Any=assay) -> FSharpList[tuple[ProcessOutput, FactorValue]]:
        return get_outputs_with_factor_by(predicate, process_sequence)

    return map_1(mapping, assay.ProcessSequence)


def Assay_getFactors_722A269D(assay: Assay) -> FSharpList[Factor]:
    return get_factors(default_arg(assay.ProcessSequence, empty()))


def Assay_getProtocols_722A269D(assay: Assay) -> FSharpList[Protocol]:
    return get_protocols(default_arg(assay.ProcessSequence, empty()))


def Assay_update_722A269D(assay: Assay) -> Assay:
    try: 
        def _arrow405(__unit: None=None) -> AssayMaterials | None:
            v_1: AssayMaterials = Assay_getMaterials_722A269D(assay)
            return Option_fromValueWithDefault(AssayMaterials_get_empty(), v_1)

        return Assay(assay.ID, assay.FileName, assay.MeasurementType, assay.TechnologyType, assay.TechnologyPlatform, Option_fromValueWithDefault(empty(), Assay_getData_722A269D(assay)), _arrow405(), Option_fromValueWithDefault(empty(), Assay_getCharacteristics_722A269D(assay)), Option_fromValueWithDefault(empty(), Assay_getUnitCategories_722A269D(assay)), assay.ProcessSequence, assay.Comments)

    except Exception as err:
        return to_fail(((("Could not update assay " + str(assay.FileName)) + ": \n") + str(err)) + "")



def Assay_updateProtocols(protocols: FSharpList[Protocol], assay: Assay) -> Assay:
    try: 
        def f(process_sequence: FSharpList[Process]) -> FSharpList[Process]:
            return update_protocols(protocols, process_sequence)

        return Assay_mapProcesses(f, assay)

    except Exception as err:
        return to_fail(((("Could not update assay protocols " + str(assay.FileName)) + ": \n") + str(err)) + "")



__all__ = ["Assay_reflection", "Assay_make", "Assay_create_3D372A24", "Assay_get_empty", "Assay_tryGetByFileName", "Assay_existsByFileName", "Assay_add", "Assay_updateBy", "Assay_updateByFileName", "Assay_removeByFileName", "Assay_getComments_722A269D", "Assay_mapComments", "Assay_setComments", "Assay_getData_722A269D", "Assay_mapData", "Assay_setData", "Assay_getUnitCategories_722A269D", "Assay_mapUnitCategories", "Assay_setUnitCategories", "Assay_getCharacteristics_722A269D", "Assay_mapCharacteristics", "Assay_setCharacteristics", "Assay_getMeasurementType_722A269D", "Assay_mapMeasurementType", "Assay_setMeasurementType", "Assay_getTechnologyType_722A269D", "Assay_mapTechnologyType", "Assay_setTechnologyType", "Assay_getProcesses_722A269D", "Assay_mapProcesses", "Assay_setProcesses", "Assay_getSources_722A269D", "Assay_getSamples_722A269D", "Assay_getMaterials_722A269D", "Assay_mapMaterials", "Assay_setMaterials", "Assay_getInputsWithParameterBy", "Assay_getOutputsWithParameterBy", "Assay_getParameters_722A269D", "Assay_getInputsWithCharacteristicBy", "Assay_getOutputsWithCharacteristicBy", "Assay_getOutputsWithFactorBy", "Assay_getFactors_722A269D", "Assay_getProtocols_722A269D", "Assay_update_722A269D", "Assay_updateProtocols"]

