from __future__ import annotations
from collections.abc import Callable
from typing import (Any, TypeVar)
from ...fable_modules.fable_library.list import (FSharpList, is_empty, length, head)
from ...fable_modules.fable_library.result import FSharpResult_2
from ...fable_modules.fable_library.seq import exists
from ...fable_modules.fable_library.set import (contains, of_seq)
from ...fable_modules.fable_library.string_ import (to_text, printf)
from ...fable_modules.fable_library.util import (compare_primitives, IEnumerable_1)
from ...fable_modules.thoth_json_core.decode import (string, Getters_2__ctor_Z4BE6C149, Getters_2, Getters_2__get_Errors, IGetters)
from ...fable_modules.thoth_json_core.types import (IDecoderHelpers_1, Decoder_1, ErrorReason_1)
from ...fable_modules.thoth_json_python.decode import Decode_helpers

__A_ = TypeVar("__A_")

_JSONVALUE = TypeVar("_JSONVALUE")

_VALUE_ = TypeVar("_VALUE_")

_VALUE = TypeVar("_VALUE")

helpers: IDecoderHelpers_1[Any] = Decode_helpers

def is_uri(s: str) -> bool:
    return True


class ObjectExpr970(Decoder_1[str]):
    def Decode(self, s: IDecoderHelpers_1[__A_], json: __A_) -> FSharpResult_2[str, tuple[str, ErrorReason_1[__A_]]]:
        match_value: FSharpResult_2[str, tuple[str, ErrorReason_1[__A_]]] = string.Decode(s, json)
        if match_value.tag == 1:
            return FSharpResult_2(1, match_value.fields[0])

        elif is_uri(match_value.fields[0]):
            return FSharpResult_2(0, match_value.fields[0])

        else: 
            s_3: str = match_value.fields[0]
            return FSharpResult_2(1, (s_3, ErrorReason_1(6, to_text(printf("Expected URI, got %s"))(s_3))))



uri: Decoder_1[str] = ObjectExpr970()

def has_unknown_fields(helpers_1: IDecoderHelpers_1[_JSONVALUE], known_fields: Any, json: _JSONVALUE) -> bool:
    def predicate(x: str, helpers_1: Any=helpers_1, known_fields: Any=known_fields, json: Any=json) -> bool:
        return not contains(x, known_fields)

    return exists(predicate, helpers_1.get_properties(json))


def object(allowed_fields: IEnumerable_1[str], builder: Callable[[IGetters], _VALUE]) -> Decoder_1[_VALUE]:
    class ObjectExpr971:
        @property
        def Compare(self) -> Callable[[str, str], int]:
            return compare_primitives

    allowed_fields_1: Any = of_seq(allowed_fields, ObjectExpr971())
    class ObjectExpr972(Decoder_1[_VALUE_]):
        def Decode(self, helpers_1: IDecoderHelpers_1[__A_], value: __A_, allowed_fields: Any=allowed_fields, builder: Any=builder) -> FSharpResult_2[_VALUE_, tuple[str, ErrorReason_1[__A_]]]:
            getters: Getters_2[__A_, Any] = Getters_2__ctor_Z4BE6C149(helpers_1, value)
            if has_unknown_fields(helpers_1, allowed_fields_1, value):
                return FSharpResult_2(1, ("Unknown fields in object", ErrorReason_1(0, "", value)))

            else: 
                result: _VALUE_ = builder(getters)
                match_value: FSharpList[tuple[str, ErrorReason_1[__A_]]] = Getters_2__get_Errors(getters)
                if not is_empty(match_value):
                    errors: FSharpList[tuple[str, ErrorReason_1[__A_]]] = match_value
                    return FSharpResult_2(1, ("", ErrorReason_1(7, errors))) if (length(errors) > 1) else FSharpResult_2(1, head(match_value))

                else: 
                    return FSharpResult_2(0, result)



    return ObjectExpr972()


__all__ = ["helpers", "is_uri", "uri", "has_unknown_fields", "object"]

