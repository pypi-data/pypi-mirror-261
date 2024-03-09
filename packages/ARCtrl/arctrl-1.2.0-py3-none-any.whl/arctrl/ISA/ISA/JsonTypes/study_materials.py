from __future__ import annotations
from dataclasses import dataclass
from ....fable_modules.fable_library.list import (FSharpList, empty)
from ....fable_modules.fable_library.option import default_arg
from ....fable_modules.fable_library.reflection import (TypeInfo, list_type, option_type, record_type)
from ....fable_modules.fable_library.types import Record
from .material import (Material, Material_reflection)
from .sample import (Sample, Sample_reflection)
from .source import (Source, Source_reflection)

def _expr394() -> TypeInfo:
    return record_type("ARCtrl.ISA.StudyMaterials", [], StudyMaterials, lambda: [("Sources", option_type(list_type(Source_reflection()))), ("Samples", option_type(list_type(Sample_reflection()))), ("OtherMaterials", option_type(list_type(Material_reflection())))])


@dataclass(eq = False, repr = False, slots = True)
class StudyMaterials(Record):
    Sources: FSharpList[Source] | None
    Samples: FSharpList[Sample] | None
    OtherMaterials: FSharpList[Material] | None

StudyMaterials_reflection = _expr394

def StudyMaterials_make(sources: FSharpList[Source] | None=None, samples: FSharpList[Sample] | None=None, other_materials: FSharpList[Material] | None=None) -> StudyMaterials:
    return StudyMaterials(sources, samples, other_materials)


def StudyMaterials_create_1BE9FA55(Sources: FSharpList[Source] | None=None, Samples: FSharpList[Sample] | None=None, OtherMaterials: FSharpList[Material] | None=None) -> StudyMaterials:
    return StudyMaterials_make(Sources, Samples, OtherMaterials)


def StudyMaterials_get_empty(__unit: None=None) -> StudyMaterials:
    return StudyMaterials_create_1BE9FA55()


def StudyMaterials_getMaterials_Z34D4FD6D(am: StudyMaterials) -> FSharpList[Material]:
    return default_arg(am.OtherMaterials, empty())


def StudyMaterials_getSamples_Z34D4FD6D(am: StudyMaterials) -> FSharpList[Sample]:
    return default_arg(am.Samples, empty())


def StudyMaterials_getSources_Z34D4FD6D(am: StudyMaterials) -> FSharpList[Source]:
    return default_arg(am.Sources, empty())


__all__ = ["StudyMaterials_reflection", "StudyMaterials_make", "StudyMaterials_create_1BE9FA55", "StudyMaterials_get_empty", "StudyMaterials_getMaterials_Z34D4FD6D", "StudyMaterials_getSamples_Z34D4FD6D", "StudyMaterials_getSources_Z34D4FD6D"]

