from __future__ import annotations
from typing import (Any, TypeVar)
from ...fable_modules.fable_library.list import (choose, of_array, FSharpList)
from ...fable_modules.fable_library.option import value as value_13
from ...fable_modules.fable_library.result import (FSharpResult_2, Result_Map)
from ...fable_modules.fable_library.seq import (to_list, delay, append, singleton, empty)
from ...fable_modules.fable_library.string_ import (to_text, printf, replace)
from ...fable_modules.fable_library.util import (equals, IEnumerable_1)
from ...fable_modules.thoth_json_core.decode import (object, IOptionalGetter, IGetters, string, list_1 as list_1_2)
from ...fable_modules.thoth_json_core.encode import list_1 as list_1_1
from ...fable_modules.thoth_json_core.types import (Json, Decoder_1, IDecoderHelpers_1, ErrorReason_1)
from ...fable_modules.thoth_json_python.decode import Decode_fromString
from ...fable_modules.thoth_json_python.encode import to_string
from ..ISA.JsonTypes.comment import Comment
from ..ISA.JsonTypes.component import (Component, Component_decomposeName_Z721C83C5)
from ..ISA.JsonTypes.ontology_annotation import OntologyAnnotation
from ..ISA.JsonTypes.protocol import Protocol
from ..ISA.JsonTypes.protocol_parameter import ProtocolParameter
from ..ISA.JsonTypes.uri import URIModule_toString
from ..ISA.JsonTypes.value import Value
from ..ISA_Json.comment import (encoder, decoder as decoder_1)
from ..ISA_Json.context.rocrate.isa_component_context import context_jsonvalue as context_jsonvalue_1
from ..ISA_Json.context.rocrate.isa_protocol_context import context_jsonvalue as context_jsonvalue_2
from ..ISA_Json.context.rocrate.isa_protocol_parameter_context import context_jsonvalue
from ..ISA_Json.converter_options import (ConverterOptions__get_SetID, ConverterOptions__get_IncludeType, ConverterOptions__get_IncludeContext, ConverterOptions, ConverterOptions__ctor, ConverterOptions__set_SetID_Z1FBCCD16, ConverterOptions__set_IncludeType_Z1FBCCD16, ConverterOptions__set_IncludeContext_Z1FBCCD16)
from ..ISA_Json.decode import uri
from ..ISA_Json.gencode import (try_include, try_include_list)
from ..ISA_Json.ontology import (OntologyAnnotation_encoder, OntologyAnnotation_decoder)

__A_ = TypeVar("__A_")

def ProtocolParameter_genID(pp: ProtocolParameter) -> str:
    match_value: str | None = pp.ID
    if match_value is None:
        match_value_1: OntologyAnnotation | None = pp.ParameterName
        (pattern_matching_result, n_1) = (None, None)
        if match_value_1 is not None:
            if not (match_value_1.ID is None):
                pattern_matching_result = 0
                n_1 = match_value_1

            else: 
                pattern_matching_result = 1


        else: 
            pattern_matching_result = 1

        if pattern_matching_result == 0:
            return "#Param_" + value_13(n_1.ID)

        elif pattern_matching_result == 1:
            return "#EmptyProtocolParameter"


    else: 
        return URIModule_toString(match_value)



def ProtocolParameter_encoder(options: ConverterOptions, oa: ProtocolParameter) -> Json:
    def chooser(tupled_arg: tuple[str, Json], options: Any=options, oa: Any=oa) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1090(__unit: None=None, options: Any=options, oa: Any=oa) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1085(value_1: str) -> Json:
            return Json(0, value_1)

        def _arrow1089(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1088(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1086(oa_1: OntologyAnnotation) -> Json:
                    return OntologyAnnotation_encoder(options, oa_1)

                def _arrow1087(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    return singleton(("@context", context_jsonvalue)) if ConverterOptions__get_IncludeContext(options) else empty()

                return append(singleton(try_include("parameterName", _arrow1086, oa.ParameterName)), delay(_arrow1087))

            return append(singleton(("@type", list_1_1(of_array([Json(0, "ProtocolParameter"), Json(0, "ArcProtocolParameter")])))) if ConverterOptions__get_IncludeType(options) else empty(), delay(_arrow1088))

        return append(singleton(("@id", Json(0, ProtocolParameter_genID(oa)))) if ConverterOptions__get_SetID(options) else singleton(try_include("@id", _arrow1085, oa.ID)), delay(_arrow1089))

    return Json(5, choose(chooser, to_list(delay(_arrow1090))))


def ProtocolParameter_decoder(options: ConverterOptions) -> Decoder_1[ProtocolParameter]:
    def _arrow1093(get: IGetters, options: Any=options) -> ProtocolParameter:
        def _arrow1091(__unit: None=None) -> str | None:
            object_arg: IOptionalGetter = get.Optional
            return object_arg.Field("@id", uri)

        def _arrow1092(__unit: None=None) -> OntologyAnnotation | None:
            arg_3: Decoder_1[OntologyAnnotation] = OntologyAnnotation_decoder(options)
            object_arg_1: IOptionalGetter = get.Optional
            return object_arg_1.Field("parameterName", arg_3)

        return ProtocolParameter(_arrow1091(), _arrow1092())

    return object(_arrow1093)


def ProtocolParameter_fromJsonString(s: str) -> ProtocolParameter:
    match_value: FSharpResult_2[ProtocolParameter, str] = Decode_fromString(ProtocolParameter_decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def ProtocolParameter_toString(p: ProtocolParameter) -> str:
    return to_string(2, ProtocolParameter_encoder(ConverterOptions__ctor(), p))


def ProtocolParameter_toJsonldString(p: ProtocolParameter) -> str:
    def _arrow1094(__unit: None=None, p: Any=p) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, ProtocolParameter_encoder(_arrow1094(), p))


def ProtocolParameter_toJsonldStringWithContext(a: ProtocolParameter) -> str:
    def _arrow1095(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, ProtocolParameter_encoder(_arrow1095(), a))


def Component_genID(c: Component) -> str:
    match_value: str | None = c.ComponentName
    if match_value is None:
        return "#EmptyComponent"

    else: 
        return "#Component_" + replace(match_value, " ", "_")



def Component_encoder(options: ConverterOptions, oa: Component) -> Json:
    def chooser(tupled_arg: tuple[str, Json], options: Any=options, oa: Any=oa) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1102(__unit: None=None, options: Any=options, oa: Any=oa) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1101(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1100(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1096(value_3: str) -> Json:
                    return Json(0, value_3)

                def _arrow1099(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1097(oa_1: OntologyAnnotation) -> Json:
                        return OntologyAnnotation_encoder(options, oa_1)

                    def _arrow1098(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        return singleton(("@context", context_jsonvalue_1)) if ConverterOptions__get_IncludeContext(options) else empty()

                    return append(singleton(try_include("componentType", _arrow1097, oa.ComponentType)), delay(_arrow1098))

                return append(singleton(try_include("componentName", _arrow1096, oa.ComponentName)), delay(_arrow1099))

            return append(singleton(("@type", list_1_1(of_array([Json(0, "Component"), Json(0, "ArcComponent")])))) if ConverterOptions__get_IncludeType(options) else empty(), delay(_arrow1100))

        return append(singleton(("@id", Json(0, Component_genID(oa)))) if ConverterOptions__get_SetID(options) else empty(), delay(_arrow1101))

    return Json(5, choose(chooser, to_list(delay(_arrow1102))))


def Component_decoder(options: ConverterOptions) -> Decoder_1[Component]:
    class ObjectExpr1106(Decoder_1[Component]):
        def Decode(self, s: IDecoderHelpers_1[__A_], json: __A_, options: Any=options) -> FSharpResult_2[Component, tuple[str, ErrorReason_1[__A_]]]:
            def mapping(c: Component) -> Component:
                pattern_input: tuple[Value | None, OntologyAnnotation | None]
                match_value: str | None = c.ComponentName
                if match_value is None:
                    pattern_input = (None, None)

                else: 
                    tupled_arg: tuple[Value, OntologyAnnotation | None] = Component_decomposeName_Z721C83C5(match_value)
                    pattern_input = (tupled_arg[0], tupled_arg[1])

                return Component(c.ComponentName, pattern_input[0], pattern_input[1], c.ComponentType)

            def _arrow1105(get: IGetters) -> Component:
                def _arrow1103(__unit: None=None) -> str | None:
                    object_arg: IOptionalGetter = get.Optional
                    return object_arg.Field("componentName", uri)

                def _arrow1104(__unit: None=None) -> OntologyAnnotation | None:
                    arg_3: Decoder_1[OntologyAnnotation] = OntologyAnnotation_decoder(options)
                    object_arg_1: IOptionalGetter = get.Optional
                    return object_arg_1.Field("componentType", arg_3)

                return Component(_arrow1103(), None, None, _arrow1104())

            return Result_Map(mapping, object(_arrow1105).Decode(s, json))

    return ObjectExpr1106()


def Component_fromJsonString(s: str) -> Component:
    match_value: FSharpResult_2[Component, str] = Decode_fromString(Component_decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def Component_toJsonString(p: Component) -> str:
    return to_string(2, Component_encoder(ConverterOptions__ctor(), p))


def Component_toJsonldString(p: Component) -> str:
    def _arrow1107(__unit: None=None, p: Any=p) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, Component_encoder(_arrow1107(), p))


def Component_toJsonldStringWithContext(a: Component) -> str:
    def _arrow1108(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, Component_encoder(_arrow1108(), a))


def Protocol_genID(study_name: str | None, assay_name: str | None, process_name: str | None, p: Protocol) -> str:
    match_value: str | None = p.ID
    if match_value is None:
        match_value_1: str | None = p.Uri
        if match_value_1 is None:
            match_value_2: str | None = p.Name
            if match_value_2 is None:
                (pattern_matching_result, an, pn, sn, pn_1, sn_1, pn_2) = (None, None, None, None, None, None, None)
                if study_name is None:
                    if assay_name is None:
                        if process_name is not None:
                            pattern_matching_result = 2
                            pn_2 = process_name

                        else: 
                            pattern_matching_result = 3


                    else: 
                        pattern_matching_result = 3


                elif assay_name is None:
                    if process_name is not None:
                        pattern_matching_result = 1
                        pn_1 = process_name
                        sn_1 = study_name

                    else: 
                        pattern_matching_result = 3


                elif process_name is not None:
                    pattern_matching_result = 0
                    an = assay_name
                    pn = process_name
                    sn = study_name

                else: 
                    pattern_matching_result = 3

                if pattern_matching_result == 0:
                    return (((("#Protocol_" + replace(sn, " ", "_")) + "_") + replace(an, " ", "_")) + "_") + replace(pn, " ", "_")

                elif pattern_matching_result == 1:
                    return (("#Protocol_" + replace(sn_1, " ", "_")) + "_") + replace(pn_1, " ", "_")

                elif pattern_matching_result == 2:
                    return "#Protocol_" + replace(pn_2, " ", "_")

                elif pattern_matching_result == 3:
                    return "#EmptyProtocol"


            else: 
                return "#Protocol_" + replace(match_value_2, " ", "_")


        else: 
            return match_value_1


    else: 
        return URIModule_toString(match_value)



def Protocol_encoder(options: ConverterOptions, study_name: str | None, assay_name: str | None, process_name: str | None, oa: Protocol) -> Json:
    def chooser(tupled_arg: tuple[str, Json], options: Any=options, study_name: Any=study_name, assay_name: Any=assay_name, process_name: Any=process_name, oa: Any=oa) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1128(__unit: None=None, options: Any=options, study_name: Any=study_name, assay_name: Any=assay_name, process_name: Any=process_name, oa: Any=oa) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1109(value_1: str) -> Json:
            return Json(0, value_1)

        def _arrow1127(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1126(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1110(value_5: str) -> Json:
                    return Json(0, value_5)

                def _arrow1125(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1111(oa_1: OntologyAnnotation) -> Json:
                        return OntologyAnnotation_encoder(options, oa_1)

                    def _arrow1124(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        def _arrow1112(value_7: str) -> Json:
                            return Json(0, value_7)

                        def _arrow1123(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                            def _arrow1113(value_9: str) -> Json:
                                return Json(0, value_9)

                            def _arrow1122(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                def _arrow1114(value_11: str) -> Json:
                                    return Json(0, value_11)

                                def _arrow1121(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                    def _arrow1115(oa_2: ProtocolParameter) -> Json:
                                        return ProtocolParameter_encoder(options, oa_2)

                                    def _arrow1120(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                        def _arrow1116(oa_3: Component) -> Json:
                                            return Component_encoder(options, oa_3)

                                        def _arrow1119(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                            def _arrow1117(comment: Comment) -> Json:
                                                return encoder(options, comment)

                                            def _arrow1118(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                return singleton(("@context", context_jsonvalue_2)) if ConverterOptions__get_IncludeContext(options) else empty()

                                            return append(singleton(try_include_list("comments", _arrow1117, oa.Comments)), delay(_arrow1118))

                                        return append(singleton(try_include_list("components", _arrow1116, oa.Components)), delay(_arrow1119))

                                    return append(singleton(try_include_list("parameters", _arrow1115, oa.Parameters)), delay(_arrow1120))

                                return append(singleton(try_include("version", _arrow1114, oa.Version)), delay(_arrow1121))

                            return append(singleton(try_include("uri", _arrow1113, oa.Uri)), delay(_arrow1122))

                        return append(singleton(try_include("description", _arrow1112, oa.Description)), delay(_arrow1123))

                    return append(singleton(try_include("protocolType", _arrow1111, oa.ProtocolType)), delay(_arrow1124))

                return append(singleton(try_include("name", _arrow1110, oa.Name)), delay(_arrow1125))

            return append(singleton(("@type", list_1_1(of_array([Json(0, "Protocol"), Json(0, "ArcProtocol")])))) if ConverterOptions__get_IncludeType(options) else empty(), delay(_arrow1126))

        return append(singleton(("@id", Json(0, Protocol_genID(study_name, assay_name, process_name, oa)))) if ConverterOptions__get_SetID(options) else singleton(try_include("@id", _arrow1109, oa.ID)), delay(_arrow1127))

    return Json(5, choose(chooser, to_list(delay(_arrow1128))))


def Protocol_decoder(options: ConverterOptions) -> Decoder_1[Protocol]:
    def _arrow1138(get: IGetters, options: Any=options) -> Protocol:
        def _arrow1129(__unit: None=None) -> str | None:
            object_arg: IOptionalGetter = get.Optional
            return object_arg.Field("@id", uri)

        def _arrow1130(__unit: None=None) -> str | None:
            object_arg_1: IOptionalGetter = get.Optional
            return object_arg_1.Field("name", string)

        def _arrow1131(__unit: None=None) -> OntologyAnnotation | None:
            arg_5: Decoder_1[OntologyAnnotation] = OntologyAnnotation_decoder(options)
            object_arg_2: IOptionalGetter = get.Optional
            return object_arg_2.Field("protocolType", arg_5)

        def _arrow1132(__unit: None=None) -> str | None:
            object_arg_3: IOptionalGetter = get.Optional
            return object_arg_3.Field("description", string)

        def _arrow1133(__unit: None=None) -> str | None:
            object_arg_4: IOptionalGetter = get.Optional
            return object_arg_4.Field("uri", uri)

        def _arrow1134(__unit: None=None) -> str | None:
            object_arg_5: IOptionalGetter = get.Optional
            return object_arg_5.Field("version", string)

        def _arrow1135(__unit: None=None) -> FSharpList[ProtocolParameter] | None:
            arg_13: Decoder_1[FSharpList[ProtocolParameter]] = list_1_2(ProtocolParameter_decoder(options))
            object_arg_6: IOptionalGetter = get.Optional
            return object_arg_6.Field("parameters", arg_13)

        def _arrow1136(__unit: None=None) -> FSharpList[Component] | None:
            arg_15: Decoder_1[FSharpList[Component]] = list_1_2(Component_decoder(options))
            object_arg_7: IOptionalGetter = get.Optional
            return object_arg_7.Field("components", arg_15)

        def _arrow1137(__unit: None=None) -> FSharpList[Comment] | None:
            arg_17: Decoder_1[FSharpList[Comment]] = list_1_2(decoder_1(options))
            object_arg_8: IOptionalGetter = get.Optional
            return object_arg_8.Field("comments", arg_17)

        return Protocol(_arrow1129(), _arrow1130(), _arrow1131(), _arrow1132(), _arrow1133(), _arrow1134(), _arrow1135(), _arrow1136(), _arrow1137())

    return object(_arrow1138)


def Protocol_fromJsonString(s: str) -> Protocol:
    match_value: FSharpResult_2[Protocol, str] = Decode_fromString(Protocol_decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def Protocol_toJsonString(p: Protocol) -> str:
    return to_string(2, Protocol_encoder(ConverterOptions__ctor(), None, None, None, p))


def Protocol_toJsonldString(p: Protocol) -> str:
    def _arrow1139(__unit: None=None, p: Any=p) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, Protocol_encoder(_arrow1139(), None, None, None, p))


def Protocol_toJsonldStringWithContext(a: Protocol) -> str:
    def _arrow1140(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, Protocol_encoder(_arrow1140(), None, None, None, a))


__all__ = ["ProtocolParameter_genID", "ProtocolParameter_encoder", "ProtocolParameter_decoder", "ProtocolParameter_fromJsonString", "ProtocolParameter_toString", "ProtocolParameter_toJsonldString", "ProtocolParameter_toJsonldStringWithContext", "Component_genID", "Component_encoder", "Component_decoder", "Component_fromJsonString", "Component_toJsonString", "Component_toJsonldString", "Component_toJsonldStringWithContext", "Protocol_genID", "Protocol_encoder", "Protocol_decoder", "Protocol_fromJsonString", "Protocol_toJsonString", "Protocol_toJsonldString", "Protocol_toJsonldStringWithContext"]

