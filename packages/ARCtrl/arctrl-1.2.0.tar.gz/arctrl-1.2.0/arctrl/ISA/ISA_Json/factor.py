from __future__ import annotations
from typing import (Any, TypeVar)
from ...fable_modules.fable_library.list import (choose, of_array)
from ...fable_modules.fable_library.result import FSharpResult_2
from ...fable_modules.fable_library.seq import (to_list, delay, append, singleton, empty)
from ...fable_modules.fable_library.string_ import (to_text, printf, replace)
from ...fable_modules.fable_library.types import Array
from ...fable_modules.fable_library.util import (equals, IEnumerable_1)
from ...fable_modules.thoth_json_core.decode import (int_1, float_1, string, object, IOptionalGetter, array, IGetters)
from ...fable_modules.thoth_json_core.encode import list_1 as list_1_1
from ...fable_modules.thoth_json_core.types import (Json, Decoder_1, ErrorReason_1, IDecoderHelpers_1)
from ...fable_modules.thoth_json_python.decode import Decode_fromString
from ...fable_modules.thoth_json_python.encode import to_string
from ..ISA.JsonTypes.comment import Comment
from ..ISA.JsonTypes.factor import Factor
from ..ISA.JsonTypes.factor_value import FactorValue
from ..ISA.JsonTypes.ontology_annotation import OntologyAnnotation
from ..ISA.JsonTypes.uri import URIModule_toString
from ..ISA.JsonTypes.value import Value
from ..ISA_Json.comment import (encoder, decoder as decoder_1)
from ..ISA_Json.context.rocrate.isa_factor_context import context_jsonvalue
from ..ISA_Json.context.rocrate.isa_factor_value_context import context_jsonvalue as context_jsonvalue_1
from ..ISA_Json.converter_options import (ConverterOptions, ConverterOptions__ctor, ConverterOptions__get_SetID, ConverterOptions__get_IncludeType, ConverterOptions__get_IncludeContext, ConverterOptions__set_SetID_Z1FBCCD16, ConverterOptions__set_IncludeType_Z1FBCCD16, ConverterOptions__set_IncludeContext_Z1FBCCD16)
from ..ISA_Json.decode import uri
from ..ISA_Json.gencode import (try_include, try_include_array)
from ..ISA_Json.ontology import (OntologyAnnotation_encoder, OntologyAnnotation_decoder)

__A_ = TypeVar("__A_")

def Value_encoder(options: ConverterOptions, value: Value) -> Json:
    if value.tag == 1:
        return Json(7, int(value.fields[0]+0x100000000 if value.fields[0] < 0 else value.fields[0]))

    elif value.tag == 3:
        return Json(0, value.fields[0])

    elif value.tag == 0:
        return OntologyAnnotation_encoder(options, value.fields[0])

    else: 
        return Json(2, value.fields[0])



def Value_decoder(options: ConverterOptions) -> Decoder_1[Value]:
    class ObjectExpr1050(Decoder_1[Value]):
        def Decode(self, s: IDecoderHelpers_1[__A_], json: __A_, options: Any=options) -> FSharpResult_2[Value, tuple[str, ErrorReason_1[__A_]]]:
            match_value: FSharpResult_2[int, tuple[str, ErrorReason_1[__A_]]] = int_1.Decode(s, json)
            if match_value.tag == 1:
                match_value_1: FSharpResult_2[float, tuple[str, ErrorReason_1[__A_]]] = float_1.Decode(s, json)
                if match_value_1.tag == 1:
                    match_value_2: FSharpResult_2[OntologyAnnotation, tuple[str, ErrorReason_1[__A_]]] = OntologyAnnotation_decoder(options).Decode(s, json)
                    if match_value_2.tag == 1:
                        match_value_3: FSharpResult_2[str, tuple[str, ErrorReason_1[__A_]]] = string.Decode(s, json)
                        return FSharpResult_2(1, match_value_3.fields[0]) if (match_value_3.tag == 1) else FSharpResult_2(0, Value(3, match_value_3.fields[0]))

                    else: 
                        return FSharpResult_2(0, Value(0, match_value_2.fields[0]))


                else: 
                    return FSharpResult_2(0, Value(2, match_value_1.fields[0]))


            else: 
                return FSharpResult_2(0, Value(1, match_value.fields[0]))


    return ObjectExpr1050()


def Value_fromJsonString(s: str) -> Value:
    match_value: FSharpResult_2[Value, str] = Decode_fromString(Value_decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def Value_toJsonString(v: Value) -> str:
    return to_string(2, Value_encoder(ConverterOptions__ctor(), v))


def Factor_genID(f: Factor) -> str:
    match_value: str | None = f.ID
    if match_value is None:
        match_value_1: str | None = f.Name
        if match_value_1 is None:
            return "#EmptyFactor"

        else: 
            return "#Factor_" + replace(match_value_1, " ", "_")


    else: 
        return URIModule_toString(match_value)



def Factor_encoder(options: ConverterOptions, oa: Factor) -> Json:
    def chooser(tupled_arg: tuple[str, Json], options: Any=options, oa: Any=oa) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1060(__unit: None=None, options: Any=options, oa: Any=oa) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1051(value_1: str) -> Json:
            return Json(0, value_1)

        def _arrow1059(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1058(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1052(value_5: str) -> Json:
                    return Json(0, value_5)

                def _arrow1057(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1053(oa_1: OntologyAnnotation) -> Json:
                        return OntologyAnnotation_encoder(options, oa_1)

                    def _arrow1056(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        def _arrow1054(comment: Comment) -> Json:
                            return encoder(options, comment)

                        def _arrow1055(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                            return singleton(("@context", context_jsonvalue)) if ConverterOptions__get_IncludeContext(options) else empty()

                        return append(singleton(try_include_array("comments", _arrow1054, oa.Comments)), delay(_arrow1055))

                    return append(singleton(try_include("factorType", _arrow1053, oa.FactorType)), delay(_arrow1056))

                return append(singleton(try_include("factorName", _arrow1052, oa.Name)), delay(_arrow1057))

            return append(singleton(("@type", list_1_1(of_array([Json(0, "Factor"), Json(0, "ArcFactor")])))) if ConverterOptions__get_IncludeType(options) else empty(), delay(_arrow1058))

        return append(singleton(("@id", Json(0, Factor_genID(oa)))) if ConverterOptions__get_SetID(options) else singleton(try_include("@id", _arrow1051, oa.ID)), delay(_arrow1059))

    return Json(5, choose(chooser, to_list(delay(_arrow1060))))


def Factor_decoder(options: ConverterOptions) -> Decoder_1[Factor]:
    def _arrow1065(get: IGetters, options: Any=options) -> Factor:
        def _arrow1061(__unit: None=None) -> str | None:
            object_arg: IOptionalGetter = get.Optional
            return object_arg.Field("@id", uri)

        def _arrow1062(__unit: None=None) -> str | None:
            object_arg_1: IOptionalGetter = get.Optional
            return object_arg_1.Field("factorName", string)

        def _arrow1063(__unit: None=None) -> OntologyAnnotation | None:
            arg_5: Decoder_1[OntologyAnnotation] = OntologyAnnotation_decoder(options)
            object_arg_2: IOptionalGetter = get.Optional
            return object_arg_2.Field("factorType", arg_5)

        def _arrow1064(__unit: None=None) -> Array[Comment] | None:
            arg_7: Decoder_1[Array[Comment]] = array(decoder_1(options))
            object_arg_3: IOptionalGetter = get.Optional
            return object_arg_3.Field("comments", arg_7)

        return Factor(_arrow1061(), _arrow1062(), _arrow1063(), _arrow1064())

    return object(_arrow1065)


def Factor_fromJsonString(s: str) -> Factor:
    match_value: FSharpResult_2[Factor, str] = Decode_fromString(Factor_decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def Factor_toJsonString(f: Factor) -> str:
    return to_string(2, Factor_encoder(ConverterOptions__ctor(), f))


def Factor_toJsonldString(f: Factor) -> str:
    def _arrow1066(__unit: None=None, f: Any=f) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, Factor_encoder(_arrow1066(), f))


def Factor_toJsonldStringWithContext(a: Factor) -> str:
    def _arrow1067(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, Factor_encoder(_arrow1067(), a))


def FactorValue_genID(fv: FactorValue) -> str:
    match_value: str | None = fv.ID
    if match_value is None:
        return "#EmptyFactorValue"

    else: 
        return URIModule_toString(match_value)



def FactorValue_encoder(options: ConverterOptions, oa: FactorValue) -> Json:
    def chooser(tupled_arg: tuple[str, Json], options: Any=options, oa: Any=oa) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1077(__unit: None=None, options: Any=options, oa: Any=oa) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1068(value_1: str) -> Json:
            return Json(0, value_1)

        def _arrow1076(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1075(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1069(oa_1: Factor) -> Json:
                    return Factor_encoder(options, oa_1)

                def _arrow1074(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1070(value_5: Value) -> Json:
                        return Value_encoder(options, value_5)

                    def _arrow1073(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        def _arrow1071(oa_2: OntologyAnnotation) -> Json:
                            return OntologyAnnotation_encoder(options, oa_2)

                        def _arrow1072(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                            return singleton(("@context", context_jsonvalue_1)) if ConverterOptions__get_IncludeContext(options) else empty()

                        return append(singleton(try_include("unit", _arrow1071, oa.Unit)), delay(_arrow1072))

                    return append(singleton(try_include("value", _arrow1070, oa.Value)), delay(_arrow1073))

                return append(singleton(try_include("category", _arrow1069, oa.Category)), delay(_arrow1074))

            return append(singleton(("@type", list_1_1(of_array([Json(0, "FactorValue"), Json(0, "ArcFactorValue")])))) if ConverterOptions__get_IncludeType(options) else empty(), delay(_arrow1075))

        return append(singleton(("@id", Json(0, FactorValue_genID(oa)))) if ConverterOptions__get_SetID(options) else singleton(try_include("@id", _arrow1068, oa.ID)), delay(_arrow1076))

    return Json(5, choose(chooser, to_list(delay(_arrow1077))))


def FactorValue_decoder(options: ConverterOptions) -> Decoder_1[FactorValue]:
    def _arrow1082(get: IGetters, options: Any=options) -> FactorValue:
        def _arrow1078(__unit: None=None) -> str | None:
            object_arg: IOptionalGetter = get.Optional
            return object_arg.Field("@id", uri)

        def _arrow1079(__unit: None=None) -> Factor | None:
            arg_3: Decoder_1[Factor] = Factor_decoder(options)
            object_arg_1: IOptionalGetter = get.Optional
            return object_arg_1.Field("category", arg_3)

        def _arrow1080(__unit: None=None) -> Value | None:
            arg_5: Decoder_1[Value] = Value_decoder(options)
            object_arg_2: IOptionalGetter = get.Optional
            return object_arg_2.Field("value", arg_5)

        def _arrow1081(__unit: None=None) -> OntologyAnnotation | None:
            arg_7: Decoder_1[OntologyAnnotation] = OntologyAnnotation_decoder(options)
            object_arg_3: IOptionalGetter = get.Optional
            return object_arg_3.Field("unit", arg_7)

        return FactorValue(_arrow1078(), _arrow1079(), _arrow1080(), _arrow1081())

    return object(_arrow1082)


def FactorValue_fromJsonString(s: str) -> FactorValue:
    match_value: FSharpResult_2[FactorValue, str] = Decode_fromString(FactorValue_decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def FactorValue_toJsonString(f: FactorValue) -> str:
    return to_string(2, FactorValue_encoder(ConverterOptions__ctor(), f))


def FactorValue_toJsonldString(f: FactorValue) -> str:
    def _arrow1083(__unit: None=None, f: Any=f) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, FactorValue_encoder(_arrow1083(), f))


def FactorValue_toJsonldStringWithContext(a: FactorValue) -> str:
    def _arrow1084(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, FactorValue_encoder(_arrow1084(), a))


__all__ = ["Value_encoder", "Value_decoder", "Value_fromJsonString", "Value_toJsonString", "Factor_genID", "Factor_encoder", "Factor_decoder", "Factor_fromJsonString", "Factor_toJsonString", "Factor_toJsonldString", "Factor_toJsonldStringWithContext", "FactorValue_genID", "FactorValue_encoder", "FactorValue_decoder", "FactorValue_fromJsonString", "FactorValue_toJsonString", "FactorValue_toJsonldString", "FactorValue_toJsonldStringWithContext"]

