from __future__ import annotations
from typing import (Any, TypeVar)
from ...fable_modules.fable_library.list import choose
from ...fable_modules.fable_library.result import FSharpResult_2
from ...fable_modules.fable_library.seq import (to_list, delay, append, singleton, empty)
from ...fable_modules.fable_library.string_ import (replace, to_text, printf)
from ...fable_modules.fable_library.types import (to_string, Array)
from ...fable_modules.fable_library.util import (int32_to_string, equals, IEnumerable_1)
from ...fable_modules.thoth_json_core.decode import (int_1, float_1, string, object, IOptionalGetter, array, IGetters)
from ...fable_modules.thoth_json_core.types import (Decoder_1, ErrorReason_1, IDecoderHelpers_1, Json)
from ...fable_modules.thoth_json_python.decode import Decode_fromString
from ...fable_modules.thoth_json_python.encode import to_string as to_string_1
from ..ISA.JsonTypes.comment import Comment
from ..ISA.JsonTypes.ontology_annotation import OntologyAnnotation
from ..ISA.JsonTypes.ontology_source_reference import OntologySourceReference
from ..ISA.JsonTypes.uri import URIModule_toString
from ..ISA_Json.comment import (encoder, decoder as decoder_1)
from ..ISA_Json.context.rocrate.isa_ontology_annotation_context import context_jsonvalue as context_jsonvalue_1
from ..ISA_Json.context.rocrate.isa_ontology_source_reference_context import context_jsonvalue
from ..ISA_Json.converter_options import (ConverterOptions, ConverterOptions__get_SetID, ConverterOptions__get_IncludeType, ConverterOptions__get_IncludeContext, ConverterOptions__ctor, ConverterOptions__set_SetID_Z1FBCCD16, ConverterOptions__set_IncludeType_Z1FBCCD16, ConverterOptions__set_IncludeContext_Z1FBCCD16)
from ..ISA_Json.decode import uri
from ..ISA_Json.gencode import (try_include, try_include_array)
from ..ISA_Json.string_table import (StringTable_encodeString, StringTable_decodeString)

__A_ = TypeVar("__A_")

def AnnotationValue_decoder(options: ConverterOptions) -> Decoder_1[str]:
    class ObjectExpr991(Decoder_1[str]):
        def Decode(self, s: IDecoderHelpers_1[__A_], json: __A_, options: Any=options) -> FSharpResult_2[str, tuple[str, ErrorReason_1[__A_]]]:
            match_value: FSharpResult_2[int, tuple[str, ErrorReason_1[__A_]]] = int_1.Decode(s, json)
            if match_value.tag == 1:
                match_value_1: FSharpResult_2[float, tuple[str, ErrorReason_1[__A_]]] = float_1.Decode(s, json)
                if match_value_1.tag == 1:
                    match_value_2: FSharpResult_2[str, tuple[str, ErrorReason_1[__A_]]] = string.Decode(s, json)
                    return FSharpResult_2(1, match_value_2.fields[0]) if (match_value_2.tag == 1) else FSharpResult_2(0, match_value_2.fields[0])

                else: 
                    return FSharpResult_2(0, to_string(match_value_1.fields[0]))


            else: 
                return FSharpResult_2(0, int32_to_string(match_value.fields[0]))


    return ObjectExpr991()


def OntologySourceReference_genID(o: OntologySourceReference) -> str:
    match_value: str | None = o.File
    if match_value is None:
        match_value_1: str | None = o.Name
        if match_value_1 is None:
            return "#DummyOntologySourceRef"

        else: 
            return "#OntologySourceRef_" + replace(match_value_1, " ", "_")


    else: 
        return match_value



def OntologySourceReference_encoder(options: ConverterOptions, osr: OntologySourceReference) -> Json:
    def chooser(tupled_arg: tuple[str, Json], options: Any=options, osr: Any=osr) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1004(__unit: None=None, options: Any=options, osr: Any=osr) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1003(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1002(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow992(value_2: str) -> Json:
                    return Json(0, value_2)

                def _arrow1001(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow993(value_4: str) -> Json:
                        return Json(0, value_4)

                    def _arrow1000(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        def _arrow994(value_6: str) -> Json:
                            return Json(0, value_6)

                        def _arrow999(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                            def _arrow995(value_8: str) -> Json:
                                return Json(0, value_8)

                            def _arrow998(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                def _arrow996(comment: Comment) -> Json:
                                    return encoder(options, comment)

                                def _arrow997(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                    return singleton(("@context", context_jsonvalue)) if ConverterOptions__get_IncludeContext(options) else empty()

                                return append(singleton(try_include_array("comments", _arrow996, osr.Comments)), delay(_arrow997))

                            return append(singleton(try_include("version", _arrow995, osr.Version)), delay(_arrow998))

                        return append(singleton(try_include("name", _arrow994, osr.Name)), delay(_arrow999))

                    return append(singleton(try_include("file", _arrow993, osr.File)), delay(_arrow1000))

                return append(singleton(try_include("description", _arrow992, osr.Description)), delay(_arrow1001))

            return append(singleton(("@type", Json(0, "OntologySourceReference"))) if ConverterOptions__get_IncludeType(options) else empty(), delay(_arrow1002))

        return append(singleton(("@id", Json(0, OntologySourceReference_genID(osr)))) if ConverterOptions__get_SetID(options) else empty(), delay(_arrow1003))

    return Json(5, choose(chooser, to_list(delay(_arrow1004))))


def OntologySourceReference_decoder(options: ConverterOptions) -> Decoder_1[OntologySourceReference]:
    def _arrow1010(get: IGetters, options: Any=options) -> OntologySourceReference:
        def _arrow1005(__unit: None=None) -> str | None:
            object_arg: IOptionalGetter = get.Optional
            return object_arg.Field("description", uri)

        def _arrow1006(__unit: None=None) -> str | None:
            object_arg_1: IOptionalGetter = get.Optional
            return object_arg_1.Field("file", string)

        def _arrow1007(__unit: None=None) -> str | None:
            object_arg_2: IOptionalGetter = get.Optional
            return object_arg_2.Field("name", string)

        def _arrow1008(__unit: None=None) -> str | None:
            object_arg_3: IOptionalGetter = get.Optional
            return object_arg_3.Field("version", string)

        def _arrow1009(__unit: None=None) -> Array[Comment] | None:
            arg_9: Decoder_1[Array[Comment]] = array(decoder_1(options))
            object_arg_4: IOptionalGetter = get.Optional
            return object_arg_4.Field("comments", arg_9)

        return OntologySourceReference(_arrow1005(), _arrow1006(), _arrow1007(), _arrow1008(), _arrow1009())

    return object(_arrow1010)


def OntologySourceReference_fromJsonString(s: str) -> OntologySourceReference:
    match_value: FSharpResult_2[OntologySourceReference, str] = Decode_fromString(OntologySourceReference_decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def OntologySourceReference_toJsonString(oa: OntologySourceReference) -> str:
    return to_string_1(2, OntologySourceReference_encoder(ConverterOptions__ctor(), oa))


def OntologySourceReference_toJsonldString(oa: OntologySourceReference) -> str:
    def _arrow1011(__unit: None=None, oa: Any=oa) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string_1(2, OntologySourceReference_encoder(_arrow1011(), oa))


def OntologySourceReference_toJsonldStringWithContext(a: OntologySourceReference) -> str:
    def _arrow1012(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string_1(2, OntologySourceReference_encoder(_arrow1012(), a))


def OntologyAnnotation_genID(o: OntologyAnnotation) -> str:
    match_value: str | None = o.ID
    if match_value is None:
        match_value_1: str | None = o.TermAccessionNumber
        if match_value_1 is None:
            match_value_2: str | None = o.TermSourceREF
            if match_value_2 is None:
                match_value_3: str | None = o.Name
                if match_value_3 is None:
                    return "#DummyOntologyAnnotation"

                else: 
                    return "#UserTerm_" + replace(match_value_3, " ", "_")


            else: 
                return "#" + replace(match_value_2, " ", "_")


        else: 
            return URIModule_toString(match_value_1)


    else: 
        return URIModule_toString(match_value)



def OntologyAnnotation_encoder(options: ConverterOptions, oa: OntologyAnnotation) -> Json:
    def chooser(tupled_arg: tuple[str, Json], options: Any=options, oa: Any=oa) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1024(__unit: None=None, options: Any=options, oa: Any=oa) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1013(value_1: str) -> Json:
            return Json(0, value_1)

        def _arrow1023(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1022(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1014(value_4: str) -> Json:
                    return Json(0, value_4)

                def _arrow1021(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1015(value_6: str) -> Json:
                        return Json(0, value_6)

                    def _arrow1020(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        def _arrow1016(value_8: str) -> Json:
                            return Json(0, value_8)

                        def _arrow1019(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                            def _arrow1017(comment: Comment) -> Json:
                                return encoder(options, comment)

                            def _arrow1018(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                return singleton(("@context", context_jsonvalue_1)) if ConverterOptions__get_IncludeContext(options) else empty()

                            return append(singleton(try_include_array("comments", _arrow1017, oa.Comments)), delay(_arrow1018))

                        return append(singleton(try_include("termAccession", _arrow1016, oa.TermAccessionNumber)), delay(_arrow1019))

                    return append(singleton(try_include("termSource", _arrow1015, oa.TermSourceREF)), delay(_arrow1020))

                return append(singleton(try_include("annotationValue", _arrow1014, oa.Name)), delay(_arrow1021))

            return append(singleton(("@type", Json(0, "OntologyAnnotation"))) if ConverterOptions__get_IncludeType(options) else empty(), delay(_arrow1022))

        return append(singleton(("@id", Json(0, OntologyAnnotation_genID(oa)))) if ConverterOptions__get_SetID(options) else singleton(try_include("@id", _arrow1013, oa.ID)), delay(_arrow1023))

    return Json(5, choose(chooser, to_list(delay(_arrow1024))))


def OntologyAnnotation_decoder(options: ConverterOptions) -> Decoder_1[OntologyAnnotation]:
    def _arrow1030(get: IGetters, options: Any=options) -> OntologyAnnotation:
        def _arrow1025(__unit: None=None) -> str | None:
            object_arg: IOptionalGetter = get.Optional
            return object_arg.Field("@id", uri)

        def _arrow1026(__unit: None=None) -> str | None:
            arg_3: Decoder_1[str] = AnnotationValue_decoder(options)
            object_arg_1: IOptionalGetter = get.Optional
            return object_arg_1.Field("annotationValue", arg_3)

        def _arrow1027(__unit: None=None) -> str | None:
            object_arg_2: IOptionalGetter = get.Optional
            return object_arg_2.Field("termSource", string)

        def _arrow1028(__unit: None=None) -> str | None:
            object_arg_3: IOptionalGetter = get.Optional
            return object_arg_3.Field("termAccession", string)

        def _arrow1029(__unit: None=None) -> Array[Comment] | None:
            arg_9: Decoder_1[Array[Comment]] = array(decoder_1(options))
            object_arg_4: IOptionalGetter = get.Optional
            return object_arg_4.Field("comments", arg_9)

        return OntologyAnnotation.create(_arrow1025(), _arrow1026(), _arrow1027(), _arrow1028(), _arrow1029())

    return object(_arrow1030)


def OntologyAnnotation_compressedEncoder(string_table: Any, options: ConverterOptions, oa: OntologyAnnotation) -> Json:
    def chooser(tupled_arg: tuple[str, Json], string_table: Any=string_table, options: Any=options, oa: Any=oa) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1041(__unit: None=None, string_table: Any=string_table, options: Any=options, oa: Any=oa) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1031(value_1: str) -> Json:
            return Json(0, value_1)

        def _arrow1040(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1039(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1032(s: str) -> Json:
                    return StringTable_encodeString(string_table, s)

                def _arrow1038(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1033(s_1: str) -> Json:
                        return StringTable_encodeString(string_table, s_1)

                    def _arrow1037(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        def _arrow1034(s_2: str) -> Json:
                            return StringTable_encodeString(string_table, s_2)

                        def _arrow1036(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                            def _arrow1035(comment: Comment) -> Json:
                                return encoder(options, comment)

                            return singleton(try_include_array("comments", _arrow1035, oa.Comments))

                        return append(singleton(try_include("ta", _arrow1034, oa.TermAccessionNumber)), delay(_arrow1036))

                    return append(singleton(try_include("ts", _arrow1033, oa.TermSourceREF)), delay(_arrow1037))

                return append(singleton(try_include("a", _arrow1032, oa.Name)), delay(_arrow1038))

            return append(singleton(("@type", Json(0, "OntologyAnnotation"))) if ConverterOptions__get_IncludeType(options) else empty(), delay(_arrow1039))

        return append(singleton(("@id", Json(0, OntologyAnnotation_genID(oa)))) if ConverterOptions__get_SetID(options) else singleton(try_include("@id", _arrow1031, oa.ID)), delay(_arrow1040))

    return Json(5, choose(chooser, to_list(delay(_arrow1041))))


def OntologyAnnotation_compressedDecoder(string_table: Array[str], options: ConverterOptions) -> Decoder_1[OntologyAnnotation]:
    def _arrow1047(get: IGetters, string_table: Any=string_table, options: Any=options) -> OntologyAnnotation:
        def _arrow1042(__unit: None=None) -> str | None:
            object_arg: IOptionalGetter = get.Optional
            return object_arg.Field("@id", uri)

        def _arrow1043(__unit: None=None) -> str | None:
            arg_3: Decoder_1[str] = StringTable_decodeString(string_table)
            object_arg_1: IOptionalGetter = get.Optional
            return object_arg_1.Field("a", arg_3)

        def _arrow1044(__unit: None=None) -> str | None:
            arg_5: Decoder_1[str] = StringTable_decodeString(string_table)
            object_arg_2: IOptionalGetter = get.Optional
            return object_arg_2.Field("ts", arg_5)

        def _arrow1045(__unit: None=None) -> str | None:
            arg_7: Decoder_1[str] = StringTable_decodeString(string_table)
            object_arg_3: IOptionalGetter = get.Optional
            return object_arg_3.Field("ta", arg_7)

        def _arrow1046(__unit: None=None) -> Array[Comment] | None:
            arg_9: Decoder_1[Array[Comment]] = array(decoder_1(options))
            object_arg_4: IOptionalGetter = get.Optional
            return object_arg_4.Field("comments", arg_9)

        return OntologyAnnotation.create(_arrow1042(), _arrow1043(), _arrow1044(), _arrow1045(), _arrow1046())

    return object(_arrow1047)


def OntologyAnnotation_fromJsonString(s: str) -> OntologyAnnotation:
    match_value: FSharpResult_2[OntologyAnnotation, str] = Decode_fromString(OntologyAnnotation_decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def OntologyAnnotation_toJsonString(oa: OntologyAnnotation) -> str:
    return to_string_1(2, OntologyAnnotation_encoder(ConverterOptions__ctor(), oa))


def OntologyAnnotation_toJsonldString(oa: OntologyAnnotation) -> str:
    def _arrow1048(__unit: None=None, oa: Any=oa) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string_1(2, OntologyAnnotation_encoder(_arrow1048(), oa))


def OntologyAnnotation_toJsonldStringWithContext(a: OntologyAnnotation) -> str:
    def _arrow1049(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string_1(2, OntologyAnnotation_encoder(_arrow1049(), a))


__all__ = ["AnnotationValue_decoder", "OntologySourceReference_genID", "OntologySourceReference_encoder", "OntologySourceReference_decoder", "OntologySourceReference_fromJsonString", "OntologySourceReference_toJsonString", "OntologySourceReference_toJsonldString", "OntologySourceReference_toJsonldStringWithContext", "OntologyAnnotation_genID", "OntologyAnnotation_encoder", "OntologyAnnotation_decoder", "OntologyAnnotation_compressedEncoder", "OntologyAnnotation_compressedDecoder", "OntologyAnnotation_fromJsonString", "OntologyAnnotation_toJsonString", "OntologyAnnotation_toJsonldString", "OntologyAnnotation_toJsonldStringWithContext"]

