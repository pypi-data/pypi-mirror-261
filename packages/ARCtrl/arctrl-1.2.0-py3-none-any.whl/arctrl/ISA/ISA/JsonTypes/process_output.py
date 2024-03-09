from __future__ import annotations
from typing import Any
from ....fable_modules.fable_library.list import (FSharpList, choose, empty)
from ....fable_modules.fable_library.option import (default_arg, map)
from ....fable_modules.fable_library.reflection import (TypeInfo, union_type)
from ....fable_modules.fable_library.string_ import (to_text, printf)
from ....fable_modules.fable_library.types import (to_string, Array, Union)
from .data import (Data_reflection, Data, Data_create_Z326CF519)
from .data_file import DataFile
from .factor_value import FactorValue
from .material import (Material_reflection, Material, Material_getUnits_Z42815C11, Material_create_Z31BE6CDD)
from .material_attribute import MaterialAttribute
from .material_attribute_value import MaterialAttributeValue
from .ontology_annotation import OntologyAnnotation
from .sample import (Sample_reflection, Sample_get_empty, Sample, Sample_setFactorValues, Sample_getUnits_Z29207F1E, Sample_create_E50ED22)
from .source import Source

def _expr352() -> TypeInfo:
    return union_type("ARCtrl.ISA.ProcessOutput", [], ProcessOutput, lambda: [[("Item", Sample_reflection())], [("Item", Data_reflection())], [("Item", Material_reflection())]])


class ProcessOutput(Union):
    def __init__(self, tag: int, *fields: Any) -> None:
        super().__init__()
        self.tag: int = tag or 0
        self.fields: Array[Any] = list(fields)

    @staticmethod
    def cases() -> list[str]:
        return ["Sample", "Data", "Material"]

    def Print(self, __unit: None=None) -> str:
        this: ProcessOutput = self
        return to_string(this)

    def PrintCompact(self, __unit: None=None) -> str:
        this: ProcessOutput = self
        if this.tag == 2:
            arg_1: str = this.fields[0].PrintCompact()
            return to_text(printf("Material {%s}"))(arg_1)

        elif this.tag == 1:
            arg_2: str = this.fields[0].PrintCompact()
            return to_text(printf("Data {%s}"))(arg_2)

        else: 
            arg: str = this.fields[0].PrintCompact()
            return to_text(printf("Sample {%s}"))(arg)



ProcessOutput_reflection = _expr352

def ProcessOutput__get_TryName(this: ProcessOutput) -> str | None:
    if this.tag == 2:
        return this.fields[0].Name

    elif this.tag == 1:
        return this.fields[0].Name

    else: 
        return this.fields[0].Name



def ProcessOutput__get_Name(this: ProcessOutput) -> str:
    return default_arg(ProcessOutput__get_TryName(this), "")


def ProcessOutput_get_Default(__unit: None=None) -> ProcessOutput:
    return ProcessOutput(0, Sample_get_empty())


def ProcessOutput_tryGetName_11830B70(po: ProcessOutput) -> str | None:
    return ProcessOutput__get_TryName(po)


def ProcessOutput_getName_11830B70(po: ProcessOutput) -> str:
    return ProcessOutput__get_Name(po)


def ProcessOutput_nameEquals(name: str, po: ProcessOutput) -> bool:
    return ProcessOutput__get_Name(po) == name


def ProcessOutput_isSample_11830B70(po: ProcessOutput) -> bool:
    if po.tag == 0:
        return True

    else: 
        return False



def ProcessOutput_isData_11830B70(po: ProcessOutput) -> bool:
    if po.tag == 1:
        return True

    else: 
        return False



def ProcessOutput_isMaterial_11830B70(po: ProcessOutput) -> bool:
    if po.tag == 2:
        return True

    else: 
        return False



def ProcessOutput__isSample(this: ProcessOutput) -> bool:
    return ProcessOutput_isSample_11830B70(this)


def ProcessOutput__isData(this: ProcessOutput) -> bool:
    return ProcessOutput_isData_11830B70(this)


def ProcessOutput__isMaterial(this: ProcessOutput) -> bool:
    return ProcessOutput_isMaterial_11830B70(this)


def ProcessOutput_trySample_11830B70(po: ProcessOutput) -> Sample | None:
    if po.tag == 0:
        return po.fields[0]

    else: 
        return None



def ProcessOutput_tryData_11830B70(po: ProcessOutput) -> Data | None:
    if po.tag == 1:
        return po.fields[0]

    else: 
        return None



def ProcessOutput_tryMaterial_11830B70(po: ProcessOutput) -> Material | None:
    if po.tag == 2:
        return po.fields[0]

    else: 
        return None



def ProcessOutput_tryGetCharacteristicValues_11830B70(po: ProcessOutput) -> FSharpList[MaterialAttributeValue] | None:
    if po.tag == 2:
        return po.fields[0].Characteristics

    elif po.tag == 1:
        return None

    else: 
        return po.fields[0].Characteristics



def ProcessOutput_tryGetCharacteristics_11830B70(po: ProcessOutput) -> FSharpList[MaterialAttribute] | None:
    def mapping(list_1: FSharpList[MaterialAttributeValue], po: Any=po) -> FSharpList[MaterialAttribute]:
        def chooser(c: MaterialAttributeValue, list_1: Any=list_1) -> MaterialAttribute | None:
            return c.Category

        return choose(chooser, list_1)

    return map(mapping, ProcessOutput_tryGetCharacteristicValues_11830B70(po))


def ProcessOutput_tryGetFactorValues_11830B70(po: ProcessOutput) -> FSharpList[FactorValue] | None:
    if po.tag == 2:
        return None

    elif po.tag == 1:
        return None

    else: 
        return po.fields[0].FactorValues



def ProcessOutput_setFactorValues(values: FSharpList[FactorValue], po: ProcessOutput) -> ProcessOutput:
    if po.tag == 2:
        return po

    elif po.tag == 1:
        return po

    else: 
        return ProcessOutput(0, Sample_setFactorValues(values, po.fields[0]))



def ProcessOutput_getFactorValues_11830B70(po: ProcessOutput) -> FSharpList[FactorValue]:
    return default_arg(ProcessOutput_tryGetFactorValues_11830B70(po), empty())


def ProcessOutput_getUnits_11830B70(po: ProcessOutput) -> FSharpList[OntologyAnnotation]:
    if po.tag == 2:
        return Material_getUnits_Z42815C11(po.fields[0])

    elif po.tag == 1:
        return empty()

    else: 
        return Sample_getUnits_Z29207F1E(po.fields[0])



def ProcessOutput_createSample_Z6DF16D07(name: str, characteristics: FSharpList[MaterialAttributeValue] | None=None, factors: FSharpList[FactorValue] | None=None, derives_from: FSharpList[Source] | None=None) -> ProcessOutput:
    return ProcessOutput(0, Sample_create_E50ED22(None, name, characteristics, factors, derives_from))


def ProcessOutput_createMaterial_2363974C(name: str, characteristics: FSharpList[MaterialAttributeValue] | None=None, derives_from: FSharpList[Material] | None=None) -> ProcessOutput:
    return ProcessOutput(2, Material_create_Z31BE6CDD(None, name, None, characteristics, derives_from))


def ProcessOutput_createImageFile_Z721C83C5(name: str) -> ProcessOutput:
    return ProcessOutput(1, Data_create_Z326CF519(None, name, DataFile(2)))


def ProcessOutput_createRawData_Z721C83C5(name: str) -> ProcessOutput:
    return ProcessOutput(1, Data_create_Z326CF519(None, name, DataFile(0)))


def ProcessOutput_createDerivedData_Z721C83C5(name: str) -> ProcessOutput:
    return ProcessOutput(1, Data_create_Z326CF519(None, name, DataFile(1)))


__all__ = ["ProcessOutput_reflection", "ProcessOutput__get_TryName", "ProcessOutput__get_Name", "ProcessOutput_get_Default", "ProcessOutput_tryGetName_11830B70", "ProcessOutput_getName_11830B70", "ProcessOutput_nameEquals", "ProcessOutput_isSample_11830B70", "ProcessOutput_isData_11830B70", "ProcessOutput_isMaterial_11830B70", "ProcessOutput__isSample", "ProcessOutput__isData", "ProcessOutput__isMaterial", "ProcessOutput_trySample_11830B70", "ProcessOutput_tryData_11830B70", "ProcessOutput_tryMaterial_11830B70", "ProcessOutput_tryGetCharacteristicValues_11830B70", "ProcessOutput_tryGetCharacteristics_11830B70", "ProcessOutput_tryGetFactorValues_11830B70", "ProcessOutput_setFactorValues", "ProcessOutput_getFactorValues_11830B70", "ProcessOutput_getUnits_11830B70", "ProcessOutput_createSample_Z6DF16D07", "ProcessOutput_createMaterial_2363974C", "ProcessOutput_createImageFile_Z721C83C5", "ProcessOutput_createRawData_Z721C83C5", "ProcessOutput_createDerivedData_Z721C83C5"]

