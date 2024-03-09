from __future__ import annotations
from dataclasses import dataclass
from typing import Any
from ....fable_modules.fable_library.list import (length, empty, FSharpList, choose, append)
from ....fable_modules.fable_library.option import default_arg
from ....fable_modules.fable_library.reflection import (TypeInfo, string_type, option_type, list_type, record_type)
from ....fable_modules.fable_library.string_ import (to_text, printf)
from ....fable_modules.fable_library.types import (to_string, Record)
from .factor_value import (FactorValue, FactorValue_reflection)
from .material_attribute_value import (MaterialAttributeValue, MaterialAttributeValue_reflection)
from .ontology_annotation import OntologyAnnotation
from .source import (Source, Source_reflection)

def _expr316() -> TypeInfo:
    return record_type("ARCtrl.ISA.Sample", [], Sample, lambda: [("ID", option_type(string_type)), ("Name", option_type(string_type)), ("Characteristics", option_type(list_type(MaterialAttributeValue_reflection()))), ("FactorValues", option_type(list_type(FactorValue_reflection()))), ("DerivesFrom", option_type(list_type(Source_reflection())))])


@dataclass(eq = False, repr = False, slots = True)
class Sample(Record):
    ID: str | None
    Name: str | None
    Characteristics: FSharpList[MaterialAttributeValue] | None
    FactorValues: FSharpList[FactorValue] | None
    DerivesFrom: FSharpList[Source] | None
    def Print(self, __unit: None=None) -> str:
        this: Sample = self
        return to_string(this)

    def PrintCompact(self, __unit: None=None) -> str:
        this: Sample = self
        chars: int = length(default_arg(this.Characteristics, empty())) or 0
        facts: int = length(default_arg(this.FactorValues, empty())) or 0
        arg: str = Sample__get_NameAsString(this)
        return to_text(printf("%s [%i characteristics; %i factors]"))(arg)(chars)(facts)


Sample_reflection = _expr316

def Sample_make(id: str | None=None, name: str | None=None, characteristics: FSharpList[MaterialAttributeValue] | None=None, factor_values: FSharpList[FactorValue] | None=None, derives_from: FSharpList[Source] | None=None) -> Sample:
    return Sample(id, name, characteristics, factor_values, derives_from)


def Sample_create_E50ED22(Id: str | None=None, Name: str | None=None, Characteristics: FSharpList[MaterialAttributeValue] | None=None, FactorValues: FSharpList[FactorValue] | None=None, DerivesFrom: FSharpList[Source] | None=None) -> Sample:
    return Sample_make(Id, Name, Characteristics, FactorValues, DerivesFrom)


def Sample_get_empty(__unit: None=None) -> Sample:
    return Sample_create_E50ED22()


def Sample__get_NameAsString(this: Sample) -> str:
    return default_arg(this.Name, "")


def Sample_getCharacteristicUnits_Z29207F1E(s: Sample) -> FSharpList[OntologyAnnotation]:
    def chooser(c: MaterialAttributeValue, s: Any=s) -> OntologyAnnotation | None:
        return c.Unit

    return choose(chooser, default_arg(s.Characteristics, empty()))


def Sample_getFactorUnits_Z29207F1E(s: Sample) -> FSharpList[OntologyAnnotation]:
    def chooser(c: FactorValue, s: Any=s) -> OntologyAnnotation | None:
        return c.Unit

    return choose(chooser, default_arg(s.FactorValues, empty()))


def Sample_getUnits_Z29207F1E(s: Sample) -> FSharpList[OntologyAnnotation]:
    return append(Sample_getCharacteristicUnits_Z29207F1E(s), Sample_getFactorUnits_Z29207F1E(s))


def Sample_setCharacteristicValues(values: FSharpList[MaterialAttributeValue], s: Sample) -> Sample:
    return Sample(s.ID, s.Name, values, s.FactorValues, s.DerivesFrom)


def Sample_setFactorValues(values: FSharpList[FactorValue], s: Sample) -> Sample:
    return Sample(s.ID, s.Name, s.Characteristics, values, s.DerivesFrom)


__all__ = ["Sample_reflection", "Sample_make", "Sample_create_E50ED22", "Sample_get_empty", "Sample__get_NameAsString", "Sample_getCharacteristicUnits_Z29207F1E", "Sample_getFactorUnits_Z29207F1E", "Sample_getUnits_Z29207F1E", "Sample_setCharacteristicValues", "Sample_setFactorValues"]

