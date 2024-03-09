from __future__ import annotations
from dataclasses import dataclass
from ....fable_modules.fable_library.list import (FSharpList, empty)
from ....fable_modules.fable_library.option import default_arg
from ....fable_modules.fable_library.reflection import (TypeInfo, list_type, option_type, record_type)
from ....fable_modules.fable_library.types import Record
from .material import (Material, Material_reflection)
from .sample import (Sample, Sample_reflection)

def _expr358() -> TypeInfo:
    return record_type("ARCtrl.ISA.AssayMaterials", [], AssayMaterials, lambda: [("Samples", option_type(list_type(Sample_reflection()))), ("OtherMaterials", option_type(list_type(Material_reflection())))])


@dataclass(eq = False, repr = False, slots = True)
class AssayMaterials(Record):
    Samples: FSharpList[Sample] | None
    OtherMaterials: FSharpList[Material] | None

AssayMaterials_reflection = _expr358

def AssayMaterials_make(samples: FSharpList[Sample] | None=None, other_materials: FSharpList[Material] | None=None) -> AssayMaterials:
    return AssayMaterials(samples, other_materials)


def AssayMaterials_create_Z253F0553(Samples: FSharpList[Sample] | None=None, OtherMaterials: FSharpList[Material] | None=None) -> AssayMaterials:
    return AssayMaterials_make(Samples, OtherMaterials)


def AssayMaterials_get_empty(__unit: None=None) -> AssayMaterials:
    return AssayMaterials_create_Z253F0553()


def AssayMaterials_getMaterials_35E61745(am: AssayMaterials) -> FSharpList[Material]:
    return default_arg(am.OtherMaterials, empty())


def AssayMaterials_getSamples_35E61745(am: AssayMaterials) -> FSharpList[Sample]:
    return default_arg(am.Samples, empty())


__all__ = ["AssayMaterials_reflection", "AssayMaterials_make", "AssayMaterials_create_Z253F0553", "AssayMaterials_get_empty", "AssayMaterials_getMaterials_35E61745", "AssayMaterials_getSamples_35E61745"]

