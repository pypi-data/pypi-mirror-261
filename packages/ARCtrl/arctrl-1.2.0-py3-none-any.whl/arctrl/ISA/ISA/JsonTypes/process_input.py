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
from .material import (Material_reflection, Material, Material_setCharacteristicValues, Material_getUnits_Z42815C11, Material_create_Z31BE6CDD)
from .material_attribute import MaterialAttribute
from .material_attribute_value import MaterialAttributeValue
from .ontology_annotation import OntologyAnnotation
from .sample import (Sample_reflection, Sample, Sample_setCharacteristicValues, Sample_getUnits_Z29207F1E, Sample_create_E50ED22)
from .source import (Source_reflection, Source_get_empty, Source, Source_setCharacteristicValues, Source_getUnits_Z28BE5327, Source_create_7A281ED9)

def _expr351() -> TypeInfo:
    return union_type("ARCtrl.ISA.ProcessInput", [], ProcessInput, lambda: [[("Item", Source_reflection())], [("Item", Sample_reflection())], [("Item", Data_reflection())], [("Item", Material_reflection())]])


class ProcessInput(Union):
    def __init__(self, tag: int, *fields: Any) -> None:
        super().__init__()
        self.tag: int = tag or 0
        self.fields: Array[Any] = list(fields)

    @staticmethod
    def cases() -> list[str]:
        return ["Source", "Sample", "Data", "Material"]

    def Print(self, __unit: None=None) -> str:
        this: ProcessInput = self
        return to_string(this)

    def PrintCompact(self, __unit: None=None) -> str:
        this: ProcessInput = self
        if this.tag == 0:
            arg_1: str = this.fields[0].PrintCompact()
            return to_text(printf("Source {%s}"))(arg_1)

        elif this.tag == 3:
            arg_2: str = this.fields[0].PrintCompact()
            return to_text(printf("Material {%s}"))(arg_2)

        elif this.tag == 2:
            arg_3: str = this.fields[0].PrintCompact()
            return to_text(printf("Data {%s}"))(arg_3)

        else: 
            arg: str = this.fields[0].PrintCompact()
            return to_text(printf("Sample {%s}"))(arg)



ProcessInput_reflection = _expr351

def ProcessInput__get_TryName(this: ProcessInput) -> str | None:
    if this.tag == 0:
        return this.fields[0].Name

    elif this.tag == 3:
        return this.fields[0].Name

    elif this.tag == 2:
        return this.fields[0].Name

    else: 
        return this.fields[0].Name



def ProcessInput__get_Name(this: ProcessInput) -> str:
    return default_arg(ProcessInput__get_TryName(this), "")


def ProcessInput_get_Default(__unit: None=None) -> ProcessInput:
    return ProcessInput(0, Source_get_empty())


def ProcessInput_tryGetName_102B6859(pi: ProcessInput) -> str | None:
    return ProcessInput__get_TryName(pi)


def ProcessInput_getName_102B6859(pi: ProcessInput) -> str:
    return ProcessInput__get_Name(pi)


def ProcessInput_nameEquals(name: str, pi: ProcessInput) -> bool:
    return ProcessInput__get_Name(pi) == name


def ProcessInput_isSample_102B6859(pi: ProcessInput) -> bool:
    if pi.tag == 1:
        return True

    else: 
        return False



def ProcessInput_isSource_102B6859(pi: ProcessInput) -> bool:
    if pi.tag == 0:
        return True

    else: 
        return False



def ProcessInput_isData_102B6859(pi: ProcessInput) -> bool:
    if pi.tag == 2:
        return True

    else: 
        return False



def ProcessInput_isMaterial_102B6859(pi: ProcessInput) -> bool:
    if pi.tag == 3:
        return True

    else: 
        return False



def ProcessInput__isSource(this: ProcessInput) -> bool:
    return ProcessInput_isSource_102B6859(this)


def ProcessInput__isSample(this: ProcessInput) -> bool:
    return ProcessInput_isSample_102B6859(this)


def ProcessInput__isData(this: ProcessInput) -> bool:
    return ProcessInput_isData_102B6859(this)


def ProcessInput__isMaterial(this: ProcessInput) -> bool:
    return ProcessInput_isMaterial_102B6859(this)


def ProcessInput_trySample_102B6859(pi: ProcessInput) -> Sample | None:
    if pi.tag == 1:
        return pi.fields[0]

    else: 
        return None



def ProcessInput_trySource_102B6859(pi: ProcessInput) -> Source | None:
    if pi.tag == 0:
        return pi.fields[0]

    else: 
        return None



def ProcessInput_tryData_102B6859(pi: ProcessInput) -> Data | None:
    if pi.tag == 2:
        return pi.fields[0]

    else: 
        return None



def ProcessInput_tryMaterial_102B6859(pi: ProcessInput) -> Material | None:
    if pi.tag == 3:
        return pi.fields[0]

    else: 
        return None



def ProcessInput_setCharacteristicValues(characteristics: FSharpList[MaterialAttributeValue], pi: ProcessInput) -> ProcessInput:
    if pi.tag == 0:
        return ProcessInput(0, Source_setCharacteristicValues(characteristics, pi.fields[0]))

    elif pi.tag == 3:
        return ProcessInput(3, Material_setCharacteristicValues(characteristics, pi.fields[0]))

    elif pi.tag == 2:
        return pi

    else: 
        return ProcessInput(1, Sample_setCharacteristicValues(characteristics, pi.fields[0]))



def ProcessInput_tryGetCharacteristicValues_102B6859(pi: ProcessInput) -> FSharpList[MaterialAttributeValue] | None:
    if pi.tag == 0:
        return pi.fields[0].Characteristics

    elif pi.tag == 3:
        return pi.fields[0].Characteristics

    elif pi.tag == 2:
        return None

    else: 
        return pi.fields[0].Characteristics



def ProcessInput_tryGetCharacteristics_102B6859(pi: ProcessInput) -> FSharpList[MaterialAttribute] | None:
    def mapping(list_1: FSharpList[MaterialAttributeValue], pi: Any=pi) -> FSharpList[MaterialAttribute]:
        def chooser(c: MaterialAttributeValue, list_1: Any=list_1) -> MaterialAttribute | None:
            return c.Category

        return choose(chooser, list_1)

    return map(mapping, ProcessInput_tryGetCharacteristicValues_102B6859(pi))


def ProcessInput_getCharacteristicValues_102B6859(pi: ProcessInput) -> FSharpList[MaterialAttributeValue]:
    return default_arg(ProcessInput_tryGetCharacteristicValues_102B6859(pi), empty())


def ProcessInput_getUnits_102B6859(pi: ProcessInput) -> FSharpList[OntologyAnnotation]:
    if pi.tag == 1:
        return Sample_getUnits_Z29207F1E(pi.fields[0])

    elif pi.tag == 3:
        return Material_getUnits_Z42815C11(pi.fields[0])

    elif pi.tag == 2:
        return empty()

    else: 
        return Source_getUnits_Z28BE5327(pi.fields[0])



def ProcessInput_createSource_7888CE42(name: str, characteristics: FSharpList[MaterialAttributeValue] | None=None) -> ProcessInput:
    return ProcessInput(0, Source_create_7A281ED9(None, name, characteristics))


def ProcessInput_createSample_Z6DF16D07(name: str, characteristics: FSharpList[MaterialAttributeValue] | None=None, factors: FSharpList[FactorValue] | None=None, derives_from: FSharpList[Source] | None=None) -> ProcessInput:
    return ProcessInput(1, Sample_create_E50ED22(None, name, characteristics, factors, derives_from))


def ProcessInput_createMaterial_2363974C(name: str, characteristics: FSharpList[MaterialAttributeValue] | None=None, derives_from: FSharpList[Material] | None=None) -> ProcessInput:
    return ProcessInput(3, Material_create_Z31BE6CDD(None, name, None, characteristics, derives_from))


def ProcessInput_createImageFile_Z721C83C5(name: str) -> ProcessInput:
    return ProcessInput(2, Data_create_Z326CF519(None, name, DataFile(2)))


def ProcessInput_createRawData_Z721C83C5(name: str) -> ProcessInput:
    return ProcessInput(2, Data_create_Z326CF519(None, name, DataFile(0)))


def ProcessInput_createDerivedData_Z721C83C5(name: str) -> ProcessInput:
    return ProcessInput(2, Data_create_Z326CF519(None, name, DataFile(1)))


__all__ = ["ProcessInput_reflection", "ProcessInput__get_TryName", "ProcessInput__get_Name", "ProcessInput_get_Default", "ProcessInput_tryGetName_102B6859", "ProcessInput_getName_102B6859", "ProcessInput_nameEquals", "ProcessInput_isSample_102B6859", "ProcessInput_isSource_102B6859", "ProcessInput_isData_102B6859", "ProcessInput_isMaterial_102B6859", "ProcessInput__isSource", "ProcessInput__isSample", "ProcessInput__isData", "ProcessInput__isMaterial", "ProcessInput_trySample_102B6859", "ProcessInput_trySource_102B6859", "ProcessInput_tryData_102B6859", "ProcessInput_tryMaterial_102B6859", "ProcessInput_setCharacteristicValues", "ProcessInput_tryGetCharacteristicValues_102B6859", "ProcessInput_tryGetCharacteristics_102B6859", "ProcessInput_getCharacteristicValues_102B6859", "ProcessInput_getUnits_102B6859", "ProcessInput_createSource_7888CE42", "ProcessInput_createSample_Z6DF16D07", "ProcessInput_createMaterial_2363974C", "ProcessInput_createImageFile_Z721C83C5", "ProcessInput_createRawData_Z721C83C5", "ProcessInput_createDerivedData_Z721C83C5"]

