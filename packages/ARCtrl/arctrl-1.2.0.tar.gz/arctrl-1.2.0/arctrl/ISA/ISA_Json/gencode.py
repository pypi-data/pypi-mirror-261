from __future__ import annotations
from collections.abc import Callable
from typing import (Any, TypeVar)
from ...fable_modules.fable_library.array_ import map as map_1
from ...fable_modules.fable_library.list import (map as map_2, FSharpList)
from ...fable_modules.fable_library.option import value as value_1
from ...fable_modules.fable_library.seq import map
from ...fable_modules.fable_library.types import Array
from ...fable_modules.fable_library.util import IEnumerable_1
from ...fable_modules.thoth_json_core.encode import (seq, list_1 as list_1_1)
from ...fable_modules.thoth_json_core.types import Json

__A = TypeVar("__A")

_VALUE = TypeVar("_VALUE")

def try_include_obj(name: __A, encoder: Callable[[Any], Json], value: Any | None=None) -> tuple[__A, Json]:
    def _arrow973(__unit: None=None, name: Any=name, encoder: Any=encoder, value: Any=value) -> Json:
        os: IEnumerable_1[Any] = value_1(value)
        return seq(map(encoder, os))

    def _arrow974(__unit: None=None, name: Any=name, encoder: Any=encoder, value: Any=value) -> Json:
        o: Any = value_1(value)
        return encoder(o)

    return (name, (_arrow973() if False else _arrow974()) if (value is not None) else Json(3))


def try_include(name: __A, encoder: Callable[[_VALUE], Json], value: _VALUE | None=None) -> tuple[__A, Json]:
    return (name, encoder(value_1(value)) if (value is not None) else Json(3))


def try_include_seq(name: __A, encoder: Callable[[_VALUE], Json], value: Any | None=None) -> tuple[__A, Json]:
    return (name, seq(map(encoder, value_1(value))) if (value is not None) else Json(3))


def try_include_array(name: __A, encoder: Callable[[_VALUE], Json], value: Array[_VALUE] | None=None) -> tuple[__A, Json]:
    return (name, Json(6, map_1(encoder, value, None)) if (value is not None) else Json(3))


def try_include_list(name: __A, encoder: Callable[[_VALUE], Json], value: FSharpList[_VALUE] | None=None) -> tuple[__A, Json]:
    return (name, list_1_1(map_2(encoder, value)) if (value is not None) else Json(3))


__all__ = ["try_include_obj", "try_include", "try_include_seq", "try_include_array", "try_include_list"]

