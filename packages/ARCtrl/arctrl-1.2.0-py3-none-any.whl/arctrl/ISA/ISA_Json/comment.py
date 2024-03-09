from __future__ import annotations
from typing import Any
from ...fable_modules.fable_library.list import choose
from ...fable_modules.fable_library.option import value as value_8
from ...fable_modules.fable_library.result import FSharpResult_2
from ...fable_modules.fable_library.seq import (to_list, delay, append, singleton, empty)
from ...fable_modules.fable_library.string_ import (replace, to_text, printf)
from ...fable_modules.fable_library.util import (equals, IEnumerable_1)
from ...fable_modules.thoth_json_core.decode import (object, IOptionalGetter, string, IGetters)
from ...fable_modules.thoth_json_core.types import (Json, Decoder_1)
from ...fable_modules.thoth_json_python.decode import Decode_fromString
from ...fable_modules.thoth_json_python.encode import to_string
from ..ISA.JsonTypes.comment import Comment
from ..ISA.JsonTypes.uri import URIModule_toString
from ..ISA_Json.context.rocrate.isa_comment_context import context_jsonvalue
from ..ISA_Json.converter_options import (ConverterOptions__get_SetID, ConverterOptions__get_IncludeType, ConverterOptions__get_IncludeContext, ConverterOptions, ConverterOptions__ctor, ConverterOptions__set_SetID_Z1FBCCD16, ConverterOptions__set_IncludeType_Z1FBCCD16, ConverterOptions__set_IncludeContext_Z1FBCCD16)
from ..ISA_Json.decode import uri
from ..ISA_Json.gencode import try_include

def gen_id(c: Comment) -> str:
    match_value: str | None = c.ID
    if match_value is None:
        match_value_1: str | None = c.Name
        if match_value_1 is None:
            return "#EmptyComment"

        else: 
            n: str = match_value_1
            v: str = ("_" + replace(value_8(c.Value), " ", "_")) if (c.Value is not None) else ""
            return ("#Comment_" + replace(n, " ", "_")) + v


    else: 
        return URIModule_toString(match_value)



def encoder(options: ConverterOptions, comment: Comment) -> Json:
    def chooser(tupled_arg: tuple[str, Json], options: Any=options, comment: Any=comment) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow982(__unit: None=None, options: Any=options, comment: Any=comment) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow975(value_1: str) -> Json:
            return Json(0, value_1)

        def _arrow981(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow980(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow976(value_4: str) -> Json:
                    return Json(0, value_4)

                def _arrow979(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow977(value_6: str) -> Json:
                        return Json(0, value_6)

                    def _arrow978(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        return singleton(("@context", context_jsonvalue)) if ConverterOptions__get_IncludeContext(options) else empty()

                    return append(singleton(try_include("value", _arrow977, comment.Value)), delay(_arrow978))

                return append(singleton(try_include("name", _arrow976, comment.Name)), delay(_arrow979))

            return append(singleton(("@type", Json(0, "Comment"))) if ConverterOptions__get_IncludeType(options) else empty(), delay(_arrow980))

        return append(singleton(("@id", Json(0, gen_id(comment)))) if ConverterOptions__get_SetID(options) else singleton(try_include("@id", _arrow975, comment.ID)), delay(_arrow981))

    return Json(5, choose(chooser, to_list(delay(_arrow982))))


def decoder(options: ConverterOptions) -> Decoder_1[Comment]:
    def _arrow986(get: IGetters, options: Any=options) -> Comment:
        def _arrow983(__unit: None=None) -> str | None:
            object_arg: IOptionalGetter = get.Optional
            return object_arg.Field("@id", uri)

        def _arrow984(__unit: None=None) -> str | None:
            object_arg_1: IOptionalGetter = get.Optional
            return object_arg_1.Field("name", string)

        def _arrow985(__unit: None=None) -> str | None:
            object_arg_2: IOptionalGetter = get.Optional
            return object_arg_2.Field("value", string)

        return Comment(_arrow983(), _arrow984(), _arrow985())

    return object(_arrow986)


def from_json_string(s: str) -> Comment:
    match_value: FSharpResult_2[Comment, str] = Decode_fromString(decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def to_json_string(c: Comment) -> str:
    return to_string(2, encoder(ConverterOptions__ctor(), c))


def to_jsonld_string(c: Comment) -> str:
    def _arrow987(__unit: None=None, c: Any=c) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, encoder(_arrow987(), c))


def to_jsonld_string_with_context(a: Comment) -> str:
    def _arrow988(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, encoder(_arrow988(), a))


__all__ = ["gen_id", "encoder", "decoder", "from_json_string", "to_json_string", "to_jsonld_string", "to_jsonld_string_with_context"]

