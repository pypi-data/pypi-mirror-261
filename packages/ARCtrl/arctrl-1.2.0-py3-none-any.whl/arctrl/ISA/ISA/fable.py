from collections.abc import Callable
from typing import (Any, TypeVar)
from ...fable_modules.fable_library.array_ import append as append_2
from ...fable_modules.fable_library.list import append as append_1
from ...fable_modules.fable_library.seq import (append, reduce, map)
from ...fable_modules.fable_library.seq2 import (distinct, List_distinct, Array_distinct)
from ...fable_modules.fable_library.types import to_string
from ...fable_modules.fable_library.util import (equals, structural_hash, IEnumerable_1, identity_hash)

__A = TypeVar("__A")

_A = TypeVar("_A")

def is_list_python(l1: Any | None=None) -> bool:
    return to_string(type(l1)).find("FSharpList") >= 0


def is_seq_python(l1: Any | None=None) -> bool:
    t: str = to_string(type(l1))
    if t.find("Enumerator_Seq") >= 0:
        return True

    else: 
        return t.find("Enumerable") >= 0



def is_array_python(l1: Any | None=None) -> bool:
    return to_string(type(l1)).find("list") >= 0


def is_map_python(l1: Any | None=None) -> bool:
    return to_string(type(l1)).find("FSharpMap") >= 0


def is_none_python(l1: Any | None=None) -> bool:
    def _arrow259(__unit: None=None, l1: Any=l1) -> str:
        copy_of_struct: __A = l1
        return to_string(copy_of_struct)

    return _arrow259() == "None"


def is_map_json(l1: Any | None=None) -> bool:
    def _arrow260(__unit: None=None, l1: Any=l1) -> str:
        copy_of_struct: __A = l1
        return to_string(copy_of_struct)

    return _arrow260().find("map [") == 0


def is_seq_json(l1: Any | None=None) -> bool:
    def _arrow261(__unit: None=None, l1: Any=l1) -> str:
        copy_of_struct: __A = l1
        return to_string(copy_of_struct)

    return _arrow261().find("seq [") == 0


def is_list_json(l1: Any | None=None) -> bool:
    s: str
    copy_of_struct: __A = l1
    s = to_string(copy_of_struct)
    if s.find("[") == 0:
        return not (s.find("seq [") == 0)

    else: 
        return False



def is_none_json(l1: Any | None=None) -> bool:
    return l1 is None


def is_list_generic(l1: Any | None=None) -> bool:
    return is_list_python(l1)


def is_seq_generic(l1: Any | None=None) -> bool:
    return is_seq_python(l1)


def is_array_generic(l1: Any | None=None) -> bool:
    return is_array_python(l1)


def is_map_generic(l1: Any | None=None) -> bool:
    return is_map_python(l1)


def is_none_generic(l1: Any | None=None) -> Any:
    is_none_python(l1)
    return is_none_json(l1)


def append_generic(l1: __A, l2: Any) -> __A:
    if is_none_generic(l2):
        return l1

    elif is_seq_generic(l1):
        return append(l1, l2)

    elif is_list_generic(l1):
        return append_1(l1, l2)

    else: 
        return append_2(l1, l2, None)



def distinct_generic(l1: Any | None=None) -> IEnumerable_1[Any]:
    if is_seq_generic(l1):
        class ObjectExpr264:
            @property
            def Equals(self) -> Callable[[Any, Any], bool]:
                return equals

            @property
            def GetHashCode(self) -> Callable[[Any], int]:
                return structural_hash

        return distinct(l1, ObjectExpr264())

    elif is_list_generic(l1):
        class ObjectExpr265:
            @property
            def Equals(self) -> Callable[[Any, Any], bool]:
                return equals

            @property
            def GetHashCode(self) -> Callable[[Any], int]:
                return structural_hash

        return List_distinct(l1, ObjectExpr265())

    else: 
        class ObjectExpr266:
            @property
            def Equals(self) -> Callable[[Any, Any], bool]:
                return equals

            @property
            def GetHashCode(self) -> Callable[[Any], int]:
                return structural_hash

        return Array_distinct(l1, ObjectExpr266())



def hash_seq(s: IEnumerable_1[Any]) -> int:
    def reduction(a: int, b: int, s: Any=s) -> int:
        return a + b

    def mapping(x: _A | None=None, s: Any=s) -> int:
        copy_of_struct: _A = x
        return identity_hash(copy_of_struct)

    return reduce(reduction, map(mapping, s))


__all__ = ["is_list_python", "is_seq_python", "is_array_python", "is_map_python", "is_none_python", "is_map_json", "is_seq_json", "is_list_json", "is_none_json", "is_list_generic", "is_seq_generic", "is_array_generic", "is_map_generic", "is_none_generic", "append_generic", "distinct_generic", "hash_seq"]

