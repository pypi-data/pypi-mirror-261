from __future__ import annotations
from collections.abc import Callable
from typing import (Any, TypeVar)
from ...fable_modules.fable_library.array_ import (contains, fold, partition, exactly_one)
from ...fable_modules.fable_library.list import (is_empty, tail, FSharpList, head, append, singleton, empty)
from ...fable_modules.fable_library.map_util import (add_to_dict, try_get_value, remove_from_dict)
from ...fable_modules.fable_library.mutable_map import Dictionary
from ...fable_modules.fable_library.option import (value as value_1, some)
from ...fable_modules.fable_library.reflection import (obj_type, name, get_union_cases, make_generic_type, option_type as option_type_1, make_union, TypeInfo, union_type)
from ...fable_modules.fable_library.seq import (fold as fold_1, iterate, is_empty as is_empty_1)
from ...fable_modules.fable_library.types import (Array, FSharpRef, to_string, Union)
from ...fable_modules.fable_library.util import (get_enumerator, dispose, equals, structural_hash, identity_hash, number_hash, IEnumerable_1, ignore, is_iterable)
from .fable import (is_map_generic, is_list_generic, distinct_generic, append_generic, is_none_generic)

__B = TypeVar("__B")

__A = TypeVar("__A")

__C = TypeVar("__C")

__A_ = TypeVar("__A_")

_A = TypeVar("_A")

_T = TypeVar("_T")

_U = TypeVar("_U")

_KEY_ = TypeVar("_KEY_")

_KEY = TypeVar("_KEY")

def ResizeArray_map(f: Callable[[__A], __B], a: Array[__A]) -> Array[__B]:
    b: Array[__B] = []
    enumerator: Any = get_enumerator(a)
    try: 
        while enumerator.System_Collections_IEnumerator_MoveNext():
            i: __A = enumerator.System_Collections_Generic_IEnumerator_1_get_Current()
            (b.append(f(i)))

    finally: 
        dispose(enumerator)

    return b


def ResizeArray_choose(f: Callable[[__A], __B | None], a: Array[__A]) -> Array[__B]:
    b: Array[__B] = []
    enumerator: Any = get_enumerator(a)
    try: 
        while enumerator.System_Collections_IEnumerator_MoveNext():
            match_value: __B | None = f(enumerator.System_Collections_Generic_IEnumerator_1_get_Current())
            if match_value is None:
                pass

            else: 
                x: __B = value_1(match_value)
                (b.append(x))


    finally: 
        dispose(enumerator)

    return b


def ResizeArray_filter(f: Callable[[__A], bool], a: Array[__A]) -> Array[__A]:
    b: Array[__A] = []
    enumerator: Any = get_enumerator(a)
    try: 
        while enumerator.System_Collections_IEnumerator_MoveNext():
            i: __A = enumerator.System_Collections_Generic_IEnumerator_1_get_Current()
            if f(i):
                (b.append(i))


    finally: 
        dispose(enumerator)

    return b


def ResizeArray_fold(f: Callable[[__A, __B], __A], s: __A, a: Array[__B]) -> __A:
    state: __A = s
    enumerator: Any = get_enumerator(a)
    try: 
        while enumerator.System_Collections_IEnumerator_MoveNext():
            i: __B = enumerator.System_Collections_Generic_IEnumerator_1_get_Current()
            state = f(state, i)

    finally: 
        dispose(enumerator)

    return state


def ResizeArray_foldBack(f: Callable[[__A, __B], __B], a: Array[__A], s: __B) -> __B:
    state: __B = s
    enumerator: Any = get_enumerator(a)
    try: 
        while enumerator.System_Collections_IEnumerator_MoveNext():
            i: __A = enumerator.System_Collections_Generic_IEnumerator_1_get_Current()
            state = f(i, state)

    finally: 
        dispose(enumerator)

    return state


def ResizeArray_iter(f: Callable[[__A], None], a: Array[__A]) -> None:
    enumerator: Any = get_enumerator(a)
    try: 
        while enumerator.System_Collections_IEnumerator_MoveNext():
            f(enumerator.System_Collections_Generic_IEnumerator_1_get_Current())

    finally: 
        dispose(enumerator)



def ResizeArray_reduce(f: Callable[[__A, __A], __A], a: Array[__A]) -> __A:
    if len(a) == 0:
        raise Exception("ResizeArray.reduce: empty array")

    elif len(a) == 1:
        return a[0]

    else: 
        a_5: Array[__A] = a
        state: __A = a_5[0]
        for i in range(1, (len(a_5) - 1) + 1, 1):
            state = f(state, a_5[i])
        return state



def ResizeArray_collect(f: Callable[[__A], __B], a: Array[__A]) -> Array[Any]:
    b: Array[__C] = []
    enumerator: Any = get_enumerator(a)
    try: 
        while enumerator.System_Collections_IEnumerator_MoveNext():
            with get_enumerator(f(enumerator.System_Collections_Generic_IEnumerator_1_get_Current())) as enumerator_1:
                while enumerator_1.System_Collections_IEnumerator_MoveNext():
                    j: __C = enumerator_1.System_Collections_Generic_IEnumerator_1_get_Current()
                    (b.append(j))

    finally: 
        dispose(enumerator)

    return b


def ResizeArray_distinct(a: Array[__A]) -> Array[__A]:
    b: Array[__A] = []
    enumerator: Any = get_enumerator(a)
    try: 
        while enumerator.System_Collections_IEnumerator_MoveNext():
            i: __A = enumerator.System_Collections_Generic_IEnumerator_1_get_Current()
            class ObjectExpr272:
                @property
                def Equals(self) -> Callable[[__A_, __A_], bool]:
                    return equals

                @property
                def GetHashCode(self) -> Callable[[__A_], int]:
                    return structural_hash

            if not contains(i, b, ObjectExpr272()):
                (b.append(i))


    finally: 
        dispose(enumerator)

    return b


def ResizeArray_isEmpty(a: Array[Any]) -> bool:
    return len(a) == 0


def HashCodes_hash(obj: Any | None=None) -> int:
    if hasattr(obj,"__hash__"):
        return obj.__hash__()

    else: 
        copy_of_struct: __A = obj
        return identity_hash(copy_of_struct)



def HashCodes_boxHashOption(a: Any | None=None) -> Any:
    def _arrow273(__unit: None=None, a: Any=a) -> int:
        copy_of_struct: _A = value_1(a)
        return identity_hash(copy_of_struct)

    def _arrow274(__unit: None=None, a: Any=a) -> int:
        copy_of_struct_1: int = 0
        return number_hash(copy_of_struct_1)

    return _arrow273() if (a is not None) else _arrow274()


def HashCodes_boxHashArray(a: Array[Any]) -> Any:
    def folder(acc: int, o: _A, a: Any=a) -> int:
        return ((-1640531527 + HashCodes_hash(o)) + (acc << 6)) + (acc >> 2)

    return fold(folder, 0, a)


def HashCodes_boxHashSeq(a: IEnumerable_1[Any]) -> Any:
    def folder(acc: int, o: _A, a: Any=a) -> int:
        def _arrow275(__unit: None=None, acc: Any=acc, o: Any=o) -> int:
            copy_of_struct: _A = o
            return identity_hash(copy_of_struct)

        return ((-1640531527 + _arrow275()) + (acc << 6)) + (acc >> 2)

    return fold_1(folder, 0, a)


def Option_fromValueWithDefault(d: __A, v: __A) -> __A | None:
    if equals(d, v):
        return None

    else: 
        return some(v)



def Option_mapDefault(d: _T, f: Callable[[_T], _T], o: _T | None=None) -> _T | None:
    return Option_fromValueWithDefault(d, f(d) if (o is None) else f(value_1(o)))


def Option_mapOrDefault(d: _T | None, f: Callable[[_U], _T], o: _U | None=None) -> _T | None:
    if o is None:
        return d

    else: 
        return some(f(value_1(o)))



def List_tryPickAndRemove(f: Callable[[_T], _U | None], lst: FSharpList[_T]) -> tuple[_U | None, FSharpList[_T]]:
    def loop(new_list_mut: FSharpList[_T], remaining_list_mut: FSharpList[_T], f: Any=f, lst: Any=lst) -> tuple[_U | None, FSharpList[_T]]:
        while True:
            (new_list, remaining_list) = (new_list_mut, remaining_list_mut)
            if not is_empty(remaining_list):
                t: FSharpList[_T] = tail(remaining_list)
                h: _T = head(remaining_list)
                match_value: _U | None = f(h)
                if match_value is None:
                    new_list_mut = append(new_list, singleton(h))
                    remaining_list_mut = t
                    continue

                else: 
                    return (some(value_1(match_value)), append(new_list, t))


            else: 
                return (None, new_list)

            break

    return loop(empty(), lst)


def Dict_ofSeq(s: IEnumerable_1[tuple[_KEY, _T]]) -> Any:
    class ObjectExpr276:
        @property
        def Equals(self) -> Callable[[_KEY_, _KEY_], bool]:
            return equals

        @property
        def GetHashCode(self) -> Callable[[_KEY_], int]:
            return structural_hash

    dict_1: Any = Dictionary([], ObjectExpr276())
    def action(tupled_arg: tuple[_KEY, _T], s: Any=s) -> None:
        add_to_dict(dict_1, tupled_arg[0], tupled_arg[1])

    iterate(action, s)
    return dict_1


def Dict_tryFind(key: _KEY, dict_1: Any) -> _T | None:
    pattern_input: tuple[bool, _T]
    out_arg: _T = None
    def _arrow277(__unit: None=None, key: Any=key, dict_1: Any=dict_1) -> _T:
        return out_arg

    def _arrow278(v: _T | None=None, key: Any=key, dict_1: Any=dict_1) -> None:
        nonlocal out_arg
        out_arg = v

    pattern_input = (try_get_value(dict_1, key, FSharpRef(_arrow277, _arrow278)), out_arg)
    if pattern_input[0]:
        return some(pattern_input[1])

    else: 
        return None



def Dict_ofSeqWithMerge(merge: Callable[[_T, _T], _T], s: IEnumerable_1[tuple[_KEY, _T]]) -> Any:
    class ObjectExpr279:
        @property
        def Equals(self) -> Callable[[_KEY_, _KEY_], bool]:
            return equals

        @property
        def GetHashCode(self) -> Callable[[_KEY_], int]:
            return structural_hash

    dict_1: Any = Dictionary([], ObjectExpr279())
    def action(tupled_arg: tuple[_KEY, _T], merge: Any=merge, s: Any=s) -> None:
        k: _KEY = tupled_arg[0]
        v: _T = tupled_arg[1]
        match_value: _T | None = Dict_tryFind(k, dict_1)
        if match_value is None:
            add_to_dict(dict_1, k, v)

        else: 
            v_0027: _T = value_1(match_value)
            ignore(remove_from_dict(dict_1, k))
            add_to_dict(dict_1, k, merge(v_0027, v))


    iterate(action, s)
    return dict_1


def Update_isMapType(v: Any=None) -> bool:
    return is_map_generic(v)


def Update_isListType(v: Any=None) -> bool:
    return is_list_generic(v)


def Update_enumGetInnerType(v: Any=None) -> Any:
    return obj_type


def Update_updateAppend(old_val: Any=None, new_val: Any=None) -> Any:
    (pattern_matching_result, old_internal) = (None, None)
    if str(type(old_val)) == "<class \'str\'>":
        pattern_matching_result = 0

    elif is_iterable(old_val):
        active_pattern_result: Any | None
        a: Any = old_val
        active_pattern_result = None if (a is None) else (None)
        if active_pattern_result is not None:
            pattern_matching_result = 1
            old_internal = value_1(active_pattern_result)

        else: 
            pattern_matching_result = 2


    else: 
        active_pattern_result_1: Any | None
        a_1: Any = old_val
        active_pattern_result_1 = None if (a_1 is None) else (None)
        if active_pattern_result_1 is not None:
            pattern_matching_result = 1
            old_internal = value_1(active_pattern_result_1)

        else: 
            pattern_matching_result = 3


    if pattern_matching_result == 0:
        return new_val

    elif pattern_matching_result == 1:
        if str(type(old_internal)) == "<class \'str\'>":
            return new_val

        elif is_iterable(old_internal):
            active_pattern_result_2: Any | None
            a_2: Any = new_val
            active_pattern_result_2 = None if (a_2 is None) else (None)
            if active_pattern_result_2 is not None:
                new_internal: Any = value_1(active_pattern_result_2)
                v: Any = Update_updateAppend(old_internal, new_internal)
                def predicate(x: Any, old_val: Any=old_val, new_val: Any=new_val) -> bool:
                    return name(x) == "Some"

                cases_1: tuple[Array[Any], Array[Any]] = partition(predicate, get_union_cases(make_generic_type(option_type_1(obj_type), [obj_type])), None)
                pattern_input: tuple[Any, Array[Any]] = (exactly_one(cases_1[0]), [v])
                return make_union(pattern_input[0], pattern_input[1])

            else: 
                return old_val


        else: 
            return new_val


    elif pattern_matching_result == 2:
        inner_type: Any = Update_enumGetInnerType(old_val)
        if Update_isMapType(old_val):
            return new_val

        else: 
            return distinct_generic(append_generic(old_val, new_val))


    elif pattern_matching_result == 3:
        return new_val



def Update_updateOnlyByExisting(old_val: Any=None, new_val: Any=None) -> Any:
    if is_none_generic(new_val):
        return old_val

    else: 
        active_pattern_result: Any | None
        a: Any = old_val
        active_pattern_result = None if (a is None) else (None)
        if active_pattern_result is not None:
            old_internal: Any = value_1(active_pattern_result)
            active_pattern_result_1: Any | None
            a_1: Any = new_val
            active_pattern_result_1 = None if (a_1 is None) else (None)
            if active_pattern_result_1 is not None:
                new_internal: Any = value_1(active_pattern_result_1)
                v: Any = Update_updateOnlyByExisting(old_internal, new_internal)
                def predicate(x: Any, old_val: Any=old_val, new_val: Any=new_val) -> bool:
                    return name(x) == "Some"

                cases_1: tuple[Array[Any], Array[Any]] = partition(predicate, get_union_cases(make_generic_type(option_type_1(obj_type), [obj_type])), None)
                pattern_input: tuple[Any, Array[Any]] = (exactly_one(cases_1[0]), [v])
                return make_union(pattern_input[0], pattern_input[1])

            else: 
                return old_val


        elif str(type(old_val)) == "<class \'str\'>":
            new_str: Any = new_val
            if to_string(new_str) == "":
                return old_val

            else: 
                return new_str


        elif is_iterable(old_val):
            new_seq: Any = new_val
            if is_empty_1(new_seq):
                return old_val

            else: 
                return new_seq


        else: 
            return new_val




def Update_updateOnlyByExistingAppend(old_val: Any=None, new_val: Any=None) -> Any:
    if is_none_generic(new_val):
        return old_val

    else: 
        active_pattern_result: Any | None
        a: Any = old_val
        active_pattern_result = None if (a is None) else (None)
        if active_pattern_result is not None:
            old_internal: Any = value_1(active_pattern_result)
            active_pattern_result_1: Any | None
            a_1: Any = new_val
            active_pattern_result_1 = None if (a_1 is None) else (None)
            if active_pattern_result_1 is not None:
                new_internal: Any = value_1(active_pattern_result_1)
                v: Any = Update_updateOnlyByExistingAppend(old_internal, new_internal)
                def predicate(x: Any, old_val: Any=old_val, new_val: Any=new_val) -> bool:
                    return name(x) == "Some"

                cases_1: tuple[Array[Any], Array[Any]] = partition(predicate, get_union_cases(make_generic_type(option_type_1(obj_type), [obj_type])), None)
                pattern_input: tuple[Any, Array[Any]] = (exactly_one(cases_1[0]), [v])
                return make_union(pattern_input[0], pattern_input[1])

            else: 
                return old_val


        elif str(type(old_val)) == "<class \'str\'>":
            new_str: Any = new_val
            if to_string(new_str) == "":
                return old_val

            else: 
                return new_str


        elif is_iterable(old_val):
            inner_type: Any = Update_enumGetInnerType(old_val)
            if Update_isMapType(old_val):
                return new_val

            else: 
                return distinct_generic(append_generic(old_val, new_val))


        else: 
            return new_val




def _expr280() -> TypeInfo:
    return union_type("ARCtrl.ISA.Aux.Update.UpdateOptions", [], Update_UpdateOptions, lambda: [[], [], [], []])


class Update_UpdateOptions(Union):
    def __init__(self, tag: int, *fields: Any) -> None:
        super().__init__()
        self.tag: int = tag or 0
        self.fields: Array[Any] = list(fields)

    @staticmethod
    def cases() -> list[str]:
        return ["UpdateAll", "UpdateByExisting", "UpdateAllAppendLists", "UpdateByExistingAppendLists"]


Update_UpdateOptions_reflection = _expr280

__all__ = ["ResizeArray_map", "ResizeArray_choose", "ResizeArray_filter", "ResizeArray_fold", "ResizeArray_foldBack", "ResizeArray_iter", "ResizeArray_reduce", "ResizeArray_collect", "ResizeArray_distinct", "ResizeArray_isEmpty", "HashCodes_hash", "HashCodes_boxHashOption", "HashCodes_boxHashArray", "HashCodes_boxHashSeq", "Option_fromValueWithDefault", "Option_mapDefault", "Option_mapOrDefault", "List_tryPickAndRemove", "Dict_ofSeq", "Dict_tryFind", "Dict_ofSeqWithMerge", "Update_isMapType", "Update_isListType", "Update_enumGetInnerType", "Update_updateAppend", "Update_updateOnlyByExisting", "Update_updateOnlyByExistingAppend", "Update_UpdateOptions_reflection"]

