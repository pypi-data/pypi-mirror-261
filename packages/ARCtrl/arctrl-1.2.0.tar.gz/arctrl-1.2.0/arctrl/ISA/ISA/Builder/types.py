from __future__ import annotations
from typing import Any
from ....fable_modules.fable_library.list import (append, empty, singleton, FSharpList, fold, exists, map as map_1)
from ....fable_modules.fable_library.option import (default_arg, value as value_4, map)
from ....fable_modules.fable_library.reflection import (TypeInfo, string_type, union_type, list_type)
from ....fable_modules.fable_library.string_ import (to_fail, printf)
from ....fable_modules.fable_library.types import (Array, Union)
from ..JsonTypes.assay import (Assay, Assay_get_empty)
from ..JsonTypes.factor_value import FactorValue_reflection
from ..JsonTypes.material_attribute_value import MaterialAttributeValue_reflection
from ..JsonTypes.ontology_annotation import OntologyAnnotation_reflection
from ..JsonTypes.process import (Process, Process_get_empty)
from ..JsonTypes.process_input import ProcessInput
from ..JsonTypes.process_output import ProcessOutput
from ..JsonTypes.process_parameter_value import (ProcessParameterValue_reflection, ProcessParameterValue)
from ..JsonTypes.protocol import (Protocol, Protocol_get_empty)
from ..JsonTypes.study import Study

def _expr600() -> TypeInfo:
    return union_type("ARCtrl.ISA.Builder.ProtocolTransformation", [], ProtocolTransformation, lambda: [[("Item", string_type)], [("Item", OntologyAnnotation_reflection())], [("Item", string_type)]])


class ProtocolTransformation(Union):
    def __init__(self, tag: int, *fields: Any) -> None:
        super().__init__()
        self.tag: int = tag or 0
        self.fields: Array[Any] = list(fields)

    @staticmethod
    def cases() -> list[str]:
        return ["AddName", "AddProtocolType", "AddDescription"]


ProtocolTransformation_reflection = _expr600

def ProtocolTransformation__Transform_Z5F51792E(this: ProtocolTransformation, p: Protocol) -> Protocol:
    if this.tag == 1:
        return Protocol(p.ID, p.Name, this.fields[0], p.Description, p.Uri, p.Version, p.Parameters, p.Components, p.Comments)

    elif this.tag == 2:
        return Protocol(p.ID, p.Name, p.ProtocolType, this.fields[0], p.Uri, p.Version, p.Parameters, p.Components, p.Comments)

    else: 
        return Protocol(p.ID, this.fields[0], p.ProtocolType, p.Description, p.Uri, p.Version, p.Parameters, p.Components, p.Comments)



def ProtocolTransformation__Equals_Z5F51792E(this: ProtocolTransformation, p: Protocol) -> bool:
    matchValue: str | None = p.Name
    (pattern_matching_result,) = (None,)
    if this.tag == 0:
        if matchValue is not None:
            if this.fields[0] == matchValue:
                pattern_matching_result = 0

            else: 
                pattern_matching_result = 1


        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        return True

    elif pattern_matching_result == 1:
        return False



def _expr601() -> TypeInfo:
    return union_type("ARCtrl.ISA.Builder.ProcessTransformation", [], ProcessTransformation, lambda: [[("Item", string_type)], [("Item", ProcessParameterValue_reflection())], [("Item", MaterialAttributeValue_reflection())], [("Item", FactorValue_reflection())], [("Item", list_type(ProtocolTransformation_reflection()))]])


class ProcessTransformation(Union):
    def __init__(self, tag: int, *fields: Any) -> None:
        super().__init__()
        self.tag: int = tag or 0
        self.fields: Array[Any] = list(fields)

    @staticmethod
    def cases() -> list[str]:
        return ["AddName", "AddParameter", "AddCharacteristic", "AddFactor", "AddProtocol"]


ProcessTransformation_reflection = _expr601

def ProcessTransformation__Transform_716E708F(this: ProcessTransformation, p: Process) -> Process:
    if this.tag == 1:
        pv: ProcessParameterValue = this.fields[0]
        parameter_values: FSharpList[ProcessParameterValue] = append(default_arg(p.ParameterValues, empty()), singleton(pv))
        def _arrow602(__unit: None=None, this: Any=this, p: Any=p) -> Protocol:
            pro: Protocol = default_arg(p.ExecutesProtocol, Protocol_get_empty())
            return Protocol(pro.ID, pro.Name, pro.ProtocolType, pro.Description, pro.Uri, pro.Version, append(default_arg(pro.Parameters, empty()), singleton(value_4(pv.Category))), pro.Components, pro.Comments)

        return Process(p.ID, p.Name, _arrow602(), parameter_values, p.Performer, p.Date, p.PreviousProcess, p.NextProcess, p.Inputs, p.Outputs, p.Comments)

    elif this.tag == 2:
        def mapping(i: FSharpList[ProcessInput], this: Any=this, p: Any=p) -> FSharpList[ProcessInput]:
            return i

        return Process(p.ID, p.Name, p.ExecutesProtocol, p.ParameterValues, p.Performer, p.Date, p.PreviousProcess, p.NextProcess, map(mapping, p.Inputs), p.Outputs, p.Comments)

    elif this.tag == 3:
        def mapping_1(i_1: FSharpList[ProcessOutput], this: Any=this, p: Any=p) -> FSharpList[ProcessOutput]:
            return i_1

        return Process(p.ID, p.Name, p.ExecutesProtocol, p.ParameterValues, p.Performer, p.Date, p.PreviousProcess, p.NextProcess, p.Inputs, map(mapping_1, p.Outputs), p.Comments)

    elif this.tag == 4:
        def folder(pro_2: Protocol, trans: ProtocolTransformation, this: Any=this, p: Any=p) -> Protocol:
            return ProtocolTransformation__Transform_Z5F51792E(trans, pro_2)

        return Process(p.ID, p.Name, fold(folder, default_arg(p.ExecutesProtocol, Protocol_get_empty()), this.fields[0]), p.ParameterValues, p.Performer, p.Date, p.PreviousProcess, p.NextProcess, p.Inputs, p.Outputs, p.Comments)

    else: 
        return Process(p.ID, this.fields[0], p.ExecutesProtocol, p.ParameterValues, p.Performer, p.Date, p.PreviousProcess, p.NextProcess, p.Inputs, p.Outputs, p.Comments)



def ProcessTransformation__Equals_716E708F(this: ProcessTransformation, p: Process) -> bool:
    matchValue: str | None = p.Name
    (pattern_matching_result,) = (None,)
    if this.tag == 0:
        if matchValue is not None:
            if this.fields[0] == matchValue:
                pattern_matching_result = 0

            else: 
                pattern_matching_result = 1


        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        return True

    elif pattern_matching_result == 1:
        return False



def _expr608() -> TypeInfo:
    return union_type("ARCtrl.ISA.Builder.AssayTransformation", [], AssayTransformation, lambda: [[("Item", string_type)], [("Item", ProcessParameterValue_reflection())], [("Item", MaterialAttributeValue_reflection())], [("Item", FactorValue_reflection())], [("Item", list_type(ProcessTransformation_reflection()))]])


class AssayTransformation(Union):
    def __init__(self, tag: int, *fields: Any) -> None:
        super().__init__()
        self.tag: int = tag or 0
        self.fields: Array[Any] = list(fields)

    @staticmethod
    def cases() -> list[str]:
        return ["AddFileName", "AddParameter", "AddCharacteristic", "AddFactor", "AddProcess"]


AssayTransformation_reflection = _expr608

def AssayTransformation__Transform_722A269D(this: AssayTransformation, a: Assay) -> Assay:
    if this.tag == 4:
        pts: FSharpList[ProcessTransformation] = this.fields[0]
        processes: FSharpList[Process] = default_arg(a.ProcessSequence, empty())
        def predicate_1(p: Process, this: Any=this, a: Any=a) -> bool:
            def predicate(trans: ProcessTransformation, p: Any=p) -> bool:
                return ProcessTransformation__Equals_716E708F(trans, p)

            return exists(predicate, pts)

        def mapping(p_1: Process, this: Any=this, a: Any=a) -> Process:
            def predicate_2(trans_1: ProcessTransformation, p_1: Any=p_1) -> bool:
                return ProcessTransformation__Equals_716E708F(trans_1, p_1)

            if exists(predicate_2, pts):
                def folder(p_2: Process, trans_2: ProcessTransformation, p_1: Any=p_1) -> Process:
                    return ProcessTransformation__Transform_716E708F(trans_2, p_2)

                return fold(folder, p_1, pts)

            else: 
                return p_1


        def folder_1(p_3: Process, trans_3: ProcessTransformation, this: Any=this, a: Any=a) -> Process:
            return ProcessTransformation__Transform_716E708F(trans_3, p_3)

        return Assay(a.ID, a.FileName, a.MeasurementType, a.TechnologyType, a.TechnologyPlatform, a.DataFiles, a.Materials, a.CharacteristicCategories, a.UnitCategories, map_1(mapping, processes) if exists(predicate_1, processes) else append(processes, singleton(fold(folder_1, Process_get_empty(), pts))), a.Comments)

    elif this.tag == 0:
        return Assay(a.ID, this.fields[0], a.MeasurementType, a.TechnologyType, a.TechnologyPlatform, a.DataFiles, a.Materials, a.CharacteristicCategories, a.UnitCategories, a.ProcessSequence, a.Comments)

    else: 
        return to_fail(printf("Builder failed: Case %O Not implemented"))(this)



def AssayTransformation__Equals_722A269D(this: AssayTransformation, a: Assay) -> bool:
    matchValue: str | None = a.FileName
    (pattern_matching_result,) = (None,)
    if this.tag == 0:
        if matchValue is not None:
            if this.fields[0] == matchValue:
                pattern_matching_result = 0

            else: 
                pattern_matching_result = 1


        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        return True

    elif pattern_matching_result == 1:
        return False



def _expr613() -> TypeInfo:
    return union_type("ARCtrl.ISA.Builder.StudyTransformation", [], StudyTransformation, lambda: [[("Item", ProcessParameterValue_reflection())], [("Item", MaterialAttributeValue_reflection())], [("Item", FactorValue_reflection())], [("Item", list_type(ProcessTransformation_reflection()))], [("Item", list_type(AssayTransformation_reflection()))]])


class StudyTransformation(Union):
    def __init__(self, tag: int, *fields: Any) -> None:
        super().__init__()
        self.tag: int = tag or 0
        self.fields: Array[Any] = list(fields)

    @staticmethod
    def cases() -> list[str]:
        return ["AddParameter", "AddCharacteristic", "AddFactor", "AddProcess", "AddAssay"]


StudyTransformation_reflection = _expr613

def StudyTransformation__Transform_7312BC8B(this: StudyTransformation, s: Study) -> Study:
    if this.tag == 3:
        pts: FSharpList[ProcessTransformation] = this.fields[0]
        processes: FSharpList[Process] = default_arg(s.ProcessSequence, empty())
        def predicate_1(p: Process, this: Any=this, s: Any=s) -> bool:
            def predicate(trans: ProcessTransformation, p: Any=p) -> bool:
                return ProcessTransformation__Equals_716E708F(trans, p)

            return exists(predicate, pts)

        def mapping(p_1: Process, this: Any=this, s: Any=s) -> Process:
            def predicate_2(trans_1: ProcessTransformation, p_1: Any=p_1) -> bool:
                return ProcessTransformation__Equals_716E708F(trans_1, p_1)

            if exists(predicate_2, pts):
                def folder(p_2: Process, trans_2: ProcessTransformation, p_1: Any=p_1) -> Process:
                    return ProcessTransformation__Transform_716E708F(trans_2, p_2)

                return fold(folder, p_1, pts)

            else: 
                return p_1


        def folder_1(p_3: Process, trans_3: ProcessTransformation, this: Any=this, s: Any=s) -> Process:
            return ProcessTransformation__Transform_716E708F(trans_3, p_3)

        return Study(s.ID, s.FileName, s.Identifier, s.Title, s.Description, s.SubmissionDate, s.PublicReleaseDate, s.Publications, s.Contacts, s.StudyDesignDescriptors, s.Protocols, s.Materials, map_1(mapping, processes) if exists(predicate_1, processes) else append(processes, singleton(fold(folder_1, Process_get_empty(), pts))), s.Assays, s.Factors, s.CharacteristicCategories, s.UnitCategories, s.Comments)

    elif this.tag == 4:
        ats: FSharpList[AssayTransformation] = this.fields[0]
        assays: FSharpList[Assay] = default_arg(s.Assays, empty())
        def predicate_4(a: Assay, this: Any=this, s: Any=s) -> bool:
            def predicate_3(trans_4: AssayTransformation, a: Any=a) -> bool:
                return AssayTransformation__Equals_722A269D(trans_4, a)

            return exists(predicate_3, ats)

        def mapping_1(a_1: Assay, this: Any=this, s: Any=s) -> Assay:
            def predicate_5(trans_5: AssayTransformation, a_1: Any=a_1) -> bool:
                return AssayTransformation__Equals_722A269D(trans_5, a_1)

            if exists(predicate_5, ats):
                def folder_2(a_2: Assay, trans_6: AssayTransformation, a_1: Any=a_1) -> Assay:
                    return AssayTransformation__Transform_722A269D(trans_6, a_2)

                return fold(folder_2, a_1, ats)

            else: 
                return a_1


        def folder_3(a_3: Assay, trans_7: AssayTransformation, this: Any=this, s: Any=s) -> Assay:
            return AssayTransformation__Transform_722A269D(trans_7, a_3)

        return Study(s.ID, s.FileName, s.Identifier, s.Title, s.Description, s.SubmissionDate, s.PublicReleaseDate, s.Publications, s.Contacts, s.StudyDesignDescriptors, s.Protocols, s.Materials, s.ProcessSequence, map_1(mapping_1, assays) if exists(predicate_4, assays) else append(assays, singleton(fold(folder_3, Assay_get_empty(), ats))), s.Factors, s.CharacteristicCategories, s.UnitCategories, s.Comments)

    else: 
        return to_fail(printf("Builder failed: Case %O Not implemented"))(this)



__all__ = ["ProtocolTransformation_reflection", "ProtocolTransformation__Transform_Z5F51792E", "ProtocolTransformation__Equals_Z5F51792E", "ProcessTransformation_reflection", "ProcessTransformation__Transform_716E708F", "ProcessTransformation__Equals_716E708F", "AssayTransformation_reflection", "AssayTransformation__Transform_722A269D", "AssayTransformation__Equals_722A269D", "StudyTransformation_reflection", "StudyTransformation__Transform_7312BC8B"]

