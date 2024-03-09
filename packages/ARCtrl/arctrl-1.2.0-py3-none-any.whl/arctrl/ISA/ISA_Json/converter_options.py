from __future__ import annotations
from ...fable_modules.fable_library.reflection import (TypeInfo, class_type)

def _expr969() -> TypeInfo:
    return class_type("ARCtrl.ISA.Json.ConverterOptions", None, ConverterOptions)


class ConverterOptions:
    def __init__(self, __unit: None=None) -> None:
        self.set_id: bool = False
        self.include_type: bool = False
        self.include_context: bool = False
        self.is_ro_crate: bool = False


ConverterOptions_reflection = _expr969

def ConverterOptions__ctor(__unit: None=None) -> ConverterOptions:
    return ConverterOptions(__unit)


def ConverterOptions__get_SetID(this: ConverterOptions) -> bool:
    return this.set_id


def ConverterOptions__set_SetID_Z1FBCCD16(this: ConverterOptions, set_id: bool) -> None:
    this.set_id = set_id


def ConverterOptions__get_IncludeType(this: ConverterOptions) -> bool:
    return this.include_type


def ConverterOptions__set_IncludeType_Z1FBCCD16(this: ConverterOptions, i_t: bool) -> None:
    this.include_type = i_t


def ConverterOptions__get_IncludeContext(this: ConverterOptions) -> bool:
    return this.include_context


def ConverterOptions__set_IncludeContext_Z1FBCCD16(this: ConverterOptions, i_c: bool) -> None:
    this.include_context = i_c


def ConverterOptions__get_IsRoCrate(this: ConverterOptions) -> bool:
    return this.is_ro_crate


def ConverterOptions__set_IsRoCrate_Z1FBCCD16(this: ConverterOptions, i_r: bool) -> None:
    this.is_ro_crate = i_r


__all__ = ["ConverterOptions_reflection", "ConverterOptions__get_SetID", "ConverterOptions__set_SetID_Z1FBCCD16", "ConverterOptions__get_IncludeType", "ConverterOptions__set_IncludeType_Z1FBCCD16", "ConverterOptions__get_IncludeContext", "ConverterOptions__set_IncludeContext_Z1FBCCD16", "ConverterOptions__get_IsRoCrate", "ConverterOptions__set_IsRoCrate_Z1FBCCD16"]

