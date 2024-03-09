from __future__ import annotations
from typing import (Any, TypeVar)
from ...fable_modules.fable_library.list import (choose, of_array, FSharpList)
from ...fable_modules.fable_library.result import FSharpResult_2
from ...fable_modules.fable_library.seq import (to_list, delay, append, singleton, empty)
from ...fable_modules.fable_library.string_ import (to_text, printf, replace)
from ...fable_modules.fable_library.util import (equals, IEnumerable_1)
from ...fable_modules.thoth_json_core.decode import (string, object, IOptionalGetter, IGetters, list_1 as list_1_2)
from ...fable_modules.thoth_json_core.encode import list_1 as list_1_1
from ...fable_modules.thoth_json_core.types import (Json, Decoder_1, ErrorReason_1, IDecoderHelpers_1)
from ...fable_modules.thoth_json_python.decode import Decode_fromString
from ...fable_modules.thoth_json_python.encode import to_string
from ..ISA.JsonTypes.material import Material
from ..ISA.JsonTypes.material_attribute import MaterialAttribute
from ..ISA.JsonTypes.material_attribute_value import MaterialAttributeValue
from ..ISA.JsonTypes.material_type import MaterialType
from ..ISA.JsonTypes.ontology_annotation import OntologyAnnotation
from ..ISA.JsonTypes.uri import URIModule_toString
from ..ISA.JsonTypes.value import Value
from ..ISA_Json.context.rocrate.isa_material_attribute_context import context_jsonvalue
from ..ISA_Json.context.rocrate.isa_material_attribute_value_context import context_jsonvalue as context_jsonvalue_1
from ..ISA_Json.context.rocrate.isa_material_context import context_jsonvalue as context_jsonvalue_2
from ..ISA_Json.converter_options import (ConverterOptions, ConverterOptions__get_SetID, ConverterOptions__get_IncludeType, ConverterOptions__get_IncludeContext, ConverterOptions__ctor, ConverterOptions__set_SetID_Z1FBCCD16, ConverterOptions__set_IncludeType_Z1FBCCD16, ConverterOptions__set_IncludeContext_Z1FBCCD16)
from ..ISA_Json.decode import (uri, object as object_1)
from ..ISA_Json.factor import (Value_encoder, Value_decoder)
from ..ISA_Json.gencode import (try_include, try_include_list)
from ..ISA_Json.ontology import (OntologyAnnotation_encoder, OntologyAnnotation_decoder)

__A_ = TypeVar("__A_")

def MaterialType_encoder(options: ConverterOptions, value: MaterialType) -> Json:
    if value.tag == 1:
        return Json(0, "Labeled Extract Name")

    else: 
        return Json(0, "Extract Name")



def MaterialType_decoder(options: ConverterOptions) -> Decoder_1[MaterialType]:
    class ObjectExpr1141(Decoder_1[MaterialType]):
        def Decode(self, s: IDecoderHelpers_1[__A_], json: __A_, options: Any=options) -> FSharpResult_2[MaterialType, tuple[str, ErrorReason_1[__A_]]]:
            match_value: FSharpResult_2[str, tuple[str, ErrorReason_1[__A_]]] = string.Decode(s, json)
            if match_value.tag == 1:
                return FSharpResult_2(1, match_value.fields[0])

            elif match_value.fields[0] == "Extract Name":
                return FSharpResult_2(0, MaterialType(0))

            elif match_value.fields[0] == "Labeled Extract Name":
                return FSharpResult_2(0, MaterialType(1))

            else: 
                s_1: str = match_value.fields[0]
                return FSharpResult_2(1, (("Could not parse " + s_1) + "No other value than \"Extract Name\" or \"Labeled Extract Name\" allowed for materialtype", ErrorReason_1(0, s_1, json)))


    return ObjectExpr1141()


def MaterialAttribute_genID(m: MaterialAttribute) -> str:
    match_value: str | None = m.ID
    if match_value is None:
        return "#EmptyMaterialAttribute"

    else: 
        return URIModule_toString(match_value)



def MaterialAttribute_encoder(options: ConverterOptions, oa: MaterialAttribute) -> Json:
    def chooser(tupled_arg: tuple[str, Json], options: Any=options, oa: Any=oa) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1147(__unit: None=None, options: Any=options, oa: Any=oa) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1142(value_1: str) -> Json:
            return Json(0, value_1)

        def _arrow1146(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1145(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1143(oa_1: OntologyAnnotation) -> Json:
                    return OntologyAnnotation_encoder(options, oa_1)

                def _arrow1144(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    return singleton(("@context", context_jsonvalue)) if ConverterOptions__get_IncludeContext(options) else empty()

                return append(singleton(try_include("characteristicType", _arrow1143, oa.CharacteristicType)), delay(_arrow1144))

            return append(singleton(("@type", list_1_1(of_array([Json(0, "MaterialAttribute"), Json(0, "ArcMaterialAttribute")])))) if ConverterOptions__get_IncludeType(options) else empty(), delay(_arrow1145))

        return append(singleton(("@id", Json(0, MaterialAttribute_genID(oa)))) if ConverterOptions__get_SetID(options) else singleton(try_include("@id", _arrow1142, oa.ID)), delay(_arrow1146))

    return Json(5, choose(chooser, to_list(delay(_arrow1147))))


def MaterialAttribute_decoder(options: ConverterOptions) -> Decoder_1[MaterialAttribute]:
    def _arrow1150(get: IGetters, options: Any=options) -> MaterialAttribute:
        def _arrow1148(__unit: None=None) -> str | None:
            object_arg: IOptionalGetter = get.Optional
            return object_arg.Field("@id", uri)

        def _arrow1149(__unit: None=None) -> OntologyAnnotation | None:
            arg_3: Decoder_1[OntologyAnnotation] = OntologyAnnotation_decoder(options)
            object_arg_1: IOptionalGetter = get.Optional
            return object_arg_1.Field("characteristicType", arg_3)

        return MaterialAttribute(_arrow1148(), _arrow1149())

    return object(_arrow1150)


def MaterialAttribute_fromJsonString(s: str) -> MaterialAttribute:
    match_value: FSharpResult_2[MaterialAttribute, str] = Decode_fromString(MaterialAttribute_decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def MaterialAttribute_toJsonString(m: MaterialAttribute) -> str:
    return to_string(2, MaterialAttribute_encoder(ConverterOptions__ctor(), m))


def MaterialAttribute_toJsonldString(m: MaterialAttribute) -> str:
    def _arrow1151(__unit: None=None, m: Any=m) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, MaterialAttribute_encoder(_arrow1151(), m))


def MaterialAttribute_toJsonldStringWithContext(a: MaterialAttribute) -> str:
    def _arrow1152(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, MaterialAttribute_encoder(_arrow1152(), a))


def MaterialAttributeValue_genID(m: MaterialAttributeValue) -> str:
    match_value: str | None = m.ID
    if match_value is None:
        return "#EmptyMaterialAttributeValue"

    else: 
        return URIModule_toString(match_value)



def MaterialAttributeValue_encoder(options: ConverterOptions, oa: MaterialAttributeValue) -> Json:
    def chooser(tupled_arg: tuple[str, Json], options: Any=options, oa: Any=oa) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1162(__unit: None=None, options: Any=options, oa: Any=oa) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1153(value_1: str) -> Json:
            return Json(0, value_1)

        def _arrow1161(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1160(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1154(oa_1: MaterialAttribute) -> Json:
                    return MaterialAttribute_encoder(options, oa_1)

                def _arrow1159(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1155(value_5: Value) -> Json:
                        return Value_encoder(options, value_5)

                    def _arrow1158(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        def _arrow1156(oa_2: OntologyAnnotation) -> Json:
                            return OntologyAnnotation_encoder(options, oa_2)

                        def _arrow1157(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                            return singleton(("@context", context_jsonvalue_1)) if ConverterOptions__get_IncludeContext(options) else empty()

                        return append(singleton(try_include("unit", _arrow1156, oa.Unit)), delay(_arrow1157))

                    return append(singleton(try_include("value", _arrow1155, oa.Value)), delay(_arrow1158))

                return append(singleton(try_include("category", _arrow1154, oa.Category)), delay(_arrow1159))

            return append(singleton(("@type", list_1_1(of_array([Json(0, "MaterialAttributeValue"), Json(0, "ArcMaterialAttributeValue")])))) if ConverterOptions__get_IncludeType(options) else empty(), delay(_arrow1160))

        return append(singleton(("@id", Json(0, MaterialAttributeValue_genID(oa)))) if ConverterOptions__get_SetID(options) else singleton(try_include("@id", _arrow1153, oa.ID)), delay(_arrow1161))

    return Json(5, choose(chooser, to_list(delay(_arrow1162))))


def MaterialAttributeValue_decoder(options: ConverterOptions) -> Decoder_1[MaterialAttributeValue]:
    def _arrow1167(get: IGetters, options: Any=options) -> MaterialAttributeValue:
        def _arrow1163(__unit: None=None) -> str | None:
            object_arg: IOptionalGetter = get.Optional
            return object_arg.Field("@id", uri)

        def _arrow1164(__unit: None=None) -> MaterialAttribute | None:
            arg_3: Decoder_1[MaterialAttribute] = MaterialAttribute_decoder(options)
            object_arg_1: IOptionalGetter = get.Optional
            return object_arg_1.Field("category", arg_3)

        def _arrow1165(__unit: None=None) -> Value | None:
            arg_5: Decoder_1[Value] = Value_decoder(options)
            object_arg_2: IOptionalGetter = get.Optional
            return object_arg_2.Field("value", arg_5)

        def _arrow1166(__unit: None=None) -> OntologyAnnotation | None:
            arg_7: Decoder_1[OntologyAnnotation] = OntologyAnnotation_decoder(options)
            object_arg_3: IOptionalGetter = get.Optional
            return object_arg_3.Field("unit", arg_7)

        return MaterialAttributeValue(_arrow1163(), _arrow1164(), _arrow1165(), _arrow1166())

    return object(_arrow1167)


def MaterialAttributeValue_fromJsonString(s: str) -> MaterialAttributeValue:
    match_value: FSharpResult_2[MaterialAttributeValue, str] = Decode_fromString(MaterialAttributeValue_decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def MaterialAttributeValue_toJsonString(m: MaterialAttributeValue) -> str:
    return to_string(2, MaterialAttributeValue_encoder(ConverterOptions__ctor(), m))


def MaterialAttributeValue_toJsonldString(m: MaterialAttributeValue) -> str:
    def _arrow1168(__unit: None=None, m: Any=m) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, MaterialAttributeValue_encoder(_arrow1168(), m))


def MaterialAttributeValue_toJsonldStringWithContext(a: MaterialAttributeValue) -> str:
    def _arrow1169(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, MaterialAttributeValue_encoder(_arrow1169(), a))


def Material_genID(m: Material) -> str:
    match_value: str | None = m.ID
    if match_value is None:
        match_value_1: str | None = m.Name
        if match_value_1 is None:
            return "#EmptyMaterial"

        else: 
            return "#Material_" + replace(match_value_1, " ", "_")


    else: 
        return match_value



def Material_encoder(options: ConverterOptions, oa: Material) -> Json:
    def chooser(tupled_arg: tuple[str, Json], options: Any=options, oa: Any=oa) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1181(__unit: None=None, options: Any=options, oa: Any=oa) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1170(value_1: str) -> Json:
            return Json(0, value_1)

        def _arrow1180(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1179(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1171(value_5: str) -> Json:
                    return Json(0, value_5)

                def _arrow1178(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1172(value_7: MaterialType) -> Json:
                        return MaterialType_encoder(options, value_7)

                    def _arrow1177(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        def _arrow1173(oa_1: MaterialAttributeValue) -> Json:
                            return MaterialAttributeValue_encoder(options, oa_1)

                        def _arrow1176(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                            def _arrow1174(oa_2: Material) -> Json:
                                return Material_encoder(options, oa_2)

                            def _arrow1175(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                return singleton(("@context", context_jsonvalue_2)) if ConverterOptions__get_IncludeContext(options) else empty()

                            return append(singleton(try_include_list("derivesFrom", _arrow1174, oa.DerivesFrom)), delay(_arrow1175))

                        return append(singleton(try_include_list("characteristics", _arrow1173, oa.Characteristics)), delay(_arrow1176))

                    return append(singleton(try_include("type", _arrow1172, oa.MaterialType)), delay(_arrow1177))

                return append(singleton(try_include("name", _arrow1171, oa.Name)), delay(_arrow1178))

            return append(singleton(("@type", list_1_1(of_array([Json(0, "Material"), Json(0, "ArcMaterial")])))) if ConverterOptions__get_IncludeType(options) else empty(), delay(_arrow1179))

        return append(singleton(("@id", Json(0, Material_genID(oa)))) if ConverterOptions__get_SetID(options) else singleton(try_include("@id", _arrow1170, oa.ID)), delay(_arrow1180))

    return Json(5, choose(chooser, to_list(delay(_arrow1181))))


Material_allowedFields: FSharpList[str] = of_array(["@id", "@type", "name", "type", "characteristics", "derivesFrom", "@context"])

def Material_decoder(options: ConverterOptions) -> Decoder_1[Material]:
    def _arrow1187(get: IGetters, options: Any=options) -> Material:
        def _arrow1182(__unit: None=None) -> str | None:
            object_arg: IOptionalGetter = get.Optional
            return object_arg.Field("@id", uri)

        def _arrow1183(__unit: None=None) -> str | None:
            object_arg_1: IOptionalGetter = get.Optional
            return object_arg_1.Field("name", string)

        def _arrow1184(__unit: None=None) -> MaterialType | None:
            arg_5: Decoder_1[MaterialType] = MaterialType_decoder(options)
            object_arg_2: IOptionalGetter = get.Optional
            return object_arg_2.Field("type", arg_5)

        def _arrow1185(__unit: None=None) -> FSharpList[MaterialAttributeValue] | None:
            arg_7: Decoder_1[FSharpList[MaterialAttributeValue]] = list_1_2(MaterialAttributeValue_decoder(options))
            object_arg_3: IOptionalGetter = get.Optional
            return object_arg_3.Field("characteristics", arg_7)

        def _arrow1186(__unit: None=None) -> FSharpList[Material] | None:
            arg_9: Decoder_1[FSharpList[Material]] = list_1_2(Material_decoder(options))
            object_arg_4: IOptionalGetter = get.Optional
            return object_arg_4.Field("derivesFrom", arg_9)

        return Material(_arrow1182(), _arrow1183(), _arrow1184(), _arrow1185(), _arrow1186())

    return object_1(Material_allowedFields, _arrow1187)


def Material_fromJsonString(s: str) -> Material:
    match_value: FSharpResult_2[Material, str] = Decode_fromString(Material_decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def Material_toJsonString(m: Material) -> str:
    return to_string(2, Material_encoder(ConverterOptions__ctor(), m))


def Material_toJsonldString(m: Material) -> str:
    def _arrow1188(__unit: None=None, m: Any=m) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, Material_encoder(_arrow1188(), m))


def Material_toJsonldStringWithContext(a: Material) -> str:
    def _arrow1189(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, Material_encoder(_arrow1189(), a))


__all__ = ["MaterialType_encoder", "MaterialType_decoder", "MaterialAttribute_genID", "MaterialAttribute_encoder", "MaterialAttribute_decoder", "MaterialAttribute_fromJsonString", "MaterialAttribute_toJsonString", "MaterialAttribute_toJsonldString", "MaterialAttribute_toJsonldStringWithContext", "MaterialAttributeValue_genID", "MaterialAttributeValue_encoder", "MaterialAttributeValue_decoder", "MaterialAttributeValue_fromJsonString", "MaterialAttributeValue_toJsonString", "MaterialAttributeValue_toJsonldString", "MaterialAttributeValue_toJsonldStringWithContext", "Material_genID", "Material_encoder", "Material_allowedFields", "Material_decoder", "Material_fromJsonString", "Material_toJsonString", "Material_toJsonldString", "Material_toJsonldStringWithContext"]

