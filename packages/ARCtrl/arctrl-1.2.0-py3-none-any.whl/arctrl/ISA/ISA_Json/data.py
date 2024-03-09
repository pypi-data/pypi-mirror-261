from __future__ import annotations
from typing import (Any, TypeVar)
from ...fable_modules.fable_library.list import (choose, of_array, FSharpList)
from ...fable_modules.fable_library.result import FSharpResult_2
from ...fable_modules.fable_library.seq import (to_list, delay, append, singleton, empty)
from ...fable_modules.fable_library.string_ import (replace, to_text, printf)
from ...fable_modules.fable_library.util import (equals, IEnumerable_1)
from ...fable_modules.thoth_json_core.decode import (string, IOptionalGetter, list_1 as list_1_2, IGetters)
from ...fable_modules.thoth_json_core.encode import list_1 as list_1_1
from ...fable_modules.thoth_json_core.types import (Json, Decoder_1, ErrorReason_1, IDecoderHelpers_1)
from ...fable_modules.thoth_json_python.decode import Decode_fromString
from ...fable_modules.thoth_json_python.encode import to_string
from ..ISA.JsonTypes.comment import Comment
from ..ISA.JsonTypes.data import Data
from ..ISA.JsonTypes.data_file import DataFile
from ..ISA.JsonTypes.factor_value import FactorValue
from ..ISA.JsonTypes.material_attribute_value import MaterialAttributeValue
from ..ISA.JsonTypes.sample import Sample
from ..ISA.JsonTypes.source import Source
from ..ISA.JsonTypes.uri import URIModule_toString
from ..ISA_Json.comment import (encoder, decoder as decoder_1)
from ..ISA_Json.context.rocrate.isa_data_context import context_jsonvalue
from ..ISA_Json.context.rocrate.isa_sample_context import context_jsonvalue as context_jsonvalue_2
from ..ISA_Json.context.rocrate.isa_source_context import context_jsonvalue as context_jsonvalue_1
from ..ISA_Json.converter_options import (ConverterOptions, ConverterOptions__get_SetID, ConverterOptions__get_IncludeType, ConverterOptions__get_IncludeContext, ConverterOptions__ctor, ConverterOptions__set_SetID_Z1FBCCD16, ConverterOptions__set_IncludeType_Z1FBCCD16, ConverterOptions__set_IncludeContext_Z1FBCCD16)
from ..ISA_Json.decode import (object, uri)
from ..ISA_Json.factor import (FactorValue_encoder, FactorValue_decoder)
from ..ISA_Json.gencode import (try_include, try_include_list)
from ..ISA_Json.material import (MaterialAttributeValue_encoder, MaterialAttributeValue_decoder)

__A_ = TypeVar("__A_")

def DataFile_encoder(options: ConverterOptions, value: DataFile) -> Json:
    if value.tag == 1:
        return Json(0, "Derived Data File")

    elif value.tag == 2:
        return Json(0, "Image File")

    else: 
        return Json(0, "Raw Data File")



def DataFile_decoder(options: ConverterOptions) -> Decoder_1[DataFile]:
    class ObjectExpr1190(Decoder_1[DataFile]):
        def Decode(self, s: IDecoderHelpers_1[__A_], json: __A_, options: Any=options) -> FSharpResult_2[DataFile, tuple[str, ErrorReason_1[__A_]]]:
            match_value: FSharpResult_2[str, tuple[str, ErrorReason_1[__A_]]] = string.Decode(s, json)
            if match_value.tag == 1:
                return FSharpResult_2(1, match_value.fields[0])

            elif match_value.fields[0] == "Raw Data File":
                return FSharpResult_2(0, DataFile(0))

            elif match_value.fields[0] == "Derived Data File":
                return FSharpResult_2(0, DataFile(1))

            elif match_value.fields[0] == "Image File":
                return FSharpResult_2(0, DataFile(2))

            else: 
                s_1: str = match_value.fields[0]
                return FSharpResult_2(1, (("Could not parse " + s_1) + ".", ErrorReason_1(0, s_1, json)))


    return ObjectExpr1190()


def Data_genID(d: Data) -> str:
    match_value: str | None = d.ID
    if match_value is None:
        match_value_1: str | None = d.Name
        if match_value_1 is None:
            return "#EmptyData"

        else: 
            return replace(match_value_1, " ", "_")


    else: 
        return URIModule_toString(match_value)



def Data_encoder(options: ConverterOptions, oa: Data) -> Json:
    def chooser(tupled_arg: tuple[str, Json], options: Any=options, oa: Any=oa) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1200(__unit: None=None, options: Any=options, oa: Any=oa) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1191(value_1: str) -> Json:
            return Json(0, value_1)

        def _arrow1199(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1198(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1192(value_5: str) -> Json:
                    return Json(0, value_5)

                def _arrow1197(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1193(value_7: DataFile) -> Json:
                        return DataFile_encoder(options, value_7)

                    def _arrow1196(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        def _arrow1194(comment: Comment) -> Json:
                            return encoder(options, comment)

                        def _arrow1195(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                            return singleton(("@context", context_jsonvalue)) if ConverterOptions__get_IncludeContext(options) else empty()

                        return append(singleton(try_include_list("comments", _arrow1194, oa.Comments)), delay(_arrow1195))

                    return append(singleton(try_include("type", _arrow1193, oa.DataType)), delay(_arrow1196))

                return append(singleton(try_include("name", _arrow1192, oa.Name)), delay(_arrow1197))

            return append(singleton(("@type", list_1_1(of_array([Json(0, "Data"), Json(0, "ArcData")])))) if ConverterOptions__get_IncludeType(options) else empty(), delay(_arrow1198))

        return append(singleton(("@id", Json(0, Data_genID(oa)))) if ConverterOptions__get_SetID(options) else singleton(try_include("@id", _arrow1191, oa.ID)), delay(_arrow1199))

    return Json(5, choose(chooser, to_list(delay(_arrow1200))))


Data_allowedFields: FSharpList[str] = of_array(["@id", "name", "type", "comments", "@type", "@context"])

def Data_decoder(options: ConverterOptions) -> Decoder_1[Data]:
    def _arrow1205(get: IGetters, options: Any=options) -> Data:
        def _arrow1201(__unit: None=None) -> str | None:
            object_arg: IOptionalGetter = get.Optional
            return object_arg.Field("@id", uri)

        def _arrow1202(__unit: None=None) -> str | None:
            object_arg_1: IOptionalGetter = get.Optional
            return object_arg_1.Field("name", string)

        def _arrow1203(__unit: None=None) -> DataFile | None:
            arg_5: Decoder_1[DataFile] = DataFile_decoder(options)
            object_arg_2: IOptionalGetter = get.Optional
            return object_arg_2.Field("type", arg_5)

        def _arrow1204(__unit: None=None) -> FSharpList[Comment] | None:
            arg_7: Decoder_1[FSharpList[Comment]] = list_1_2(decoder_1(options))
            object_arg_3: IOptionalGetter = get.Optional
            return object_arg_3.Field("comments", arg_7)

        return Data(_arrow1201(), _arrow1202(), _arrow1203(), _arrow1204())

    return object(Data_allowedFields, _arrow1205)


def Data_fromJsonString(s: str) -> Data:
    match_value: FSharpResult_2[Data, str] = Decode_fromString(Data_decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def Data_toJsonString(m: Data) -> str:
    return to_string(2, Data_encoder(ConverterOptions__ctor(), m))


def Data_toJsonldString(d: Data) -> str:
    def _arrow1206(__unit: None=None, d: Any=d) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, Data_encoder(_arrow1206(), d))


def Data_toJsonldStringWithContext(a: Data) -> str:
    def _arrow1207(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, Data_encoder(_arrow1207(), a))


def Source_genID(s: Source) -> str:
    match_value: str | None = s.ID
    if match_value is None:
        match_value_1: str | None = s.Name
        if match_value_1 is None:
            return "#EmptySource"

        else: 
            return "#Source_" + replace(match_value_1, " ", "_")


    else: 
        return URIModule_toString(match_value)



def Source_encoder(options: ConverterOptions, oa: Source) -> Json:
    def chooser(tupled_arg: tuple[str, Json], options: Any=options, oa: Any=oa) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1215(__unit: None=None, options: Any=options, oa: Any=oa) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1208(value_1: str) -> Json:
            return Json(0, value_1)

        def _arrow1214(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1213(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1209(value_5: str) -> Json:
                    return Json(0, value_5)

                def _arrow1212(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1210(oa_1: MaterialAttributeValue) -> Json:
                        return MaterialAttributeValue_encoder(options, oa_1)

                    def _arrow1211(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        return singleton(("@context", context_jsonvalue_1)) if ConverterOptions__get_IncludeContext(options) else empty()

                    return append(singleton(try_include_list("characteristics", _arrow1210, oa.Characteristics)), delay(_arrow1211))

                return append(singleton(try_include("name", _arrow1209, oa.Name)), delay(_arrow1212))

            return append(singleton(("@type", list_1_1(of_array([Json(0, "Source"), Json(0, "ArcSource")])))) if ConverterOptions__get_IncludeType(options) else empty(), delay(_arrow1213))

        return append(singleton(("@id", Json(0, Source_genID(oa)))) if ConverterOptions__get_SetID(options) else singleton(try_include("@id", _arrow1208, oa.ID)), delay(_arrow1214))

    return Json(5, choose(chooser, to_list(delay(_arrow1215))))


Source_allowedFields: FSharpList[str] = of_array(["@id", "name", "characteristics", "@type", "@context"])

def Source_decoder(options: ConverterOptions) -> Decoder_1[Source]:
    def _arrow1219(get: IGetters, options: Any=options) -> Source:
        def _arrow1216(__unit: None=None) -> str | None:
            object_arg: IOptionalGetter = get.Optional
            return object_arg.Field("@id", uri)

        def _arrow1217(__unit: None=None) -> str | None:
            object_arg_1: IOptionalGetter = get.Optional
            return object_arg_1.Field("name", string)

        def _arrow1218(__unit: None=None) -> FSharpList[MaterialAttributeValue] | None:
            arg_5: Decoder_1[FSharpList[MaterialAttributeValue]] = list_1_2(MaterialAttributeValue_decoder(options))
            object_arg_2: IOptionalGetter = get.Optional
            return object_arg_2.Field("characteristics", arg_5)

        return Source(_arrow1216(), _arrow1217(), _arrow1218())

    return object(Source_allowedFields, _arrow1219)


def Source_fromJsonString(s: str) -> Source:
    match_value: FSharpResult_2[Source, str] = Decode_fromString(Source_decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def Source_toJsonString(m: Source) -> str:
    return to_string(2, Source_encoder(ConverterOptions__ctor(), m))


def Source_toJsonldString(s: Source) -> str:
    def _arrow1220(__unit: None=None, s: Any=s) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, Source_encoder(_arrow1220(), s))


def Source_toJsonldStringWithContext(a: Source) -> str:
    def _arrow1221(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, Source_encoder(_arrow1221(), a))


def Sample_genID(s: Sample) -> str:
    match_value: str | None = s.ID
    if match_value is None:
        match_value_1: str | None = s.Name
        if match_value_1 is None:
            return "#EmptySample"

        else: 
            return "#Sample_" + replace(match_value_1, " ", "_")


    else: 
        return match_value



def Sample_encoder(options: ConverterOptions, oa: Sample) -> Json:
    def chooser(tupled_arg: tuple[str, Json], options: Any=options, oa: Any=oa) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1233(__unit: None=None, options: Any=options, oa: Any=oa) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1222(value_1: str) -> Json:
            return Json(0, value_1)

        def _arrow1232(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1231(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1223(value_5: str) -> Json:
                    return Json(0, value_5)

                def _arrow1230(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1224(oa_1: MaterialAttributeValue) -> Json:
                        return MaterialAttributeValue_encoder(options, oa_1)

                    def _arrow1229(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        def _arrow1225(oa_2: FactorValue) -> Json:
                            return FactorValue_encoder(options, oa_2)

                        def _arrow1228(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                            def _arrow1226(oa_3: Source) -> Json:
                                return Source_encoder(options, oa_3)

                            def _arrow1227(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                return singleton(("@context", context_jsonvalue_2)) if ConverterOptions__get_IncludeContext(options) else empty()

                            return append(singleton(try_include_list("derivesFrom", _arrow1226, oa.DerivesFrom)), delay(_arrow1227))

                        return append(singleton(try_include_list("factorValues", _arrow1225, oa.FactorValues)), delay(_arrow1228))

                    return append(singleton(try_include_list("characteristics", _arrow1224, oa.Characteristics)), delay(_arrow1229))

                return append(singleton(try_include("name", _arrow1223, oa.Name)), delay(_arrow1230))

            return append(singleton(("@type", list_1_1(of_array([Json(0, "Sample"), Json(0, "ArcSample")])))) if ConverterOptions__get_IncludeType(options) else empty(), delay(_arrow1231))

        return append(singleton(("@id", Json(0, Sample_genID(oa)))) if ConverterOptions__get_SetID(options) else singleton(try_include("@id", _arrow1222, oa.ID)), delay(_arrow1232))

    return Json(5, choose(chooser, to_list(delay(_arrow1233))))


Sample_allowedFields: FSharpList[str] = of_array(["@id", "name", "characteristics", "factorValues", "derivesFrom", "@type", "@context"])

def Sample_decoder(options: ConverterOptions) -> Decoder_1[Sample]:
    def _arrow1239(get: IGetters, options: Any=options) -> Sample:
        def _arrow1234(__unit: None=None) -> str | None:
            object_arg: IOptionalGetter = get.Optional
            return object_arg.Field("@id", uri)

        def _arrow1235(__unit: None=None) -> str | None:
            object_arg_1: IOptionalGetter = get.Optional
            return object_arg_1.Field("name", string)

        def _arrow1236(__unit: None=None) -> FSharpList[MaterialAttributeValue] | None:
            arg_5: Decoder_1[FSharpList[MaterialAttributeValue]] = list_1_2(MaterialAttributeValue_decoder(options))
            object_arg_2: IOptionalGetter = get.Optional
            return object_arg_2.Field("characteristics", arg_5)

        def _arrow1237(__unit: None=None) -> FSharpList[FactorValue] | None:
            arg_7: Decoder_1[FSharpList[FactorValue]] = list_1_2(FactorValue_decoder(options))
            object_arg_3: IOptionalGetter = get.Optional
            return object_arg_3.Field("factorValues", arg_7)

        def _arrow1238(__unit: None=None) -> FSharpList[Source] | None:
            arg_9: Decoder_1[FSharpList[Source]] = list_1_2(Source_decoder(options))
            object_arg_4: IOptionalGetter = get.Optional
            return object_arg_4.Field("derivesFrom", arg_9)

        return Sample(_arrow1234(), _arrow1235(), _arrow1236(), _arrow1237(), _arrow1238())

    return object(Sample_allowedFields, _arrow1239)


def Sample_fromJsonString(s: str) -> Sample:
    match_value: FSharpResult_2[Sample, str] = Decode_fromString(Sample_decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def Sample_toJsonString(m: Sample) -> str:
    return to_string(2, Sample_encoder(ConverterOptions__ctor(), m))


def Sample_toJsonldString(s: Sample) -> str:
    def _arrow1240(__unit: None=None, s: Any=s) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, Sample_encoder(_arrow1240(), s))


def Sample_toJsonldStringWithContext(a: Sample) -> str:
    def _arrow1241(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, Sample_encoder(_arrow1241(), a))


__all__ = ["DataFile_encoder", "DataFile_decoder", "Data_genID", "Data_encoder", "Data_allowedFields", "Data_decoder", "Data_fromJsonString", "Data_toJsonString", "Data_toJsonldString", "Data_toJsonldStringWithContext", "Source_genID", "Source_encoder", "Source_allowedFields", "Source_decoder", "Source_fromJsonString", "Source_toJsonString", "Source_toJsonldString", "Source_toJsonldStringWithContext", "Sample_genID", "Sample_encoder", "Sample_allowedFields", "Sample_decoder", "Sample_fromJsonString", "Sample_toJsonString", "Sample_toJsonldString", "Sample_toJsonldStringWithContext"]

