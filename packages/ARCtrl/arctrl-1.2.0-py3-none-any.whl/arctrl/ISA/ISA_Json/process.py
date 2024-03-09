from __future__ import annotations
from collections.abc import Callable
from typing import (Any, TypeVar)
from ...fable_modules.fable_library.list import (choose, of_array, FSharpList, map)
from ...fable_modules.fable_library.result import FSharpResult_2
from ...fable_modules.fable_library.seq import (to_list, delay, append, singleton, empty)
from ...fable_modules.fable_library.string_ import (replace, to_text, printf)
from ...fable_modules.fable_library.util import (equals, IEnumerable_1)
from ...fable_modules.thoth_json_core.decode import (object, IOptionalGetter, IGetters, string, list_1 as list_1_2)
from ...fable_modules.thoth_json_core.encode import list_1 as list_1_1
from ...fable_modules.thoth_json_core.types import (Json, Decoder_1, ErrorReason_1, IDecoderHelpers_1)
from ...fable_modules.thoth_json_python.decode import Decode_fromString
from ...fable_modules.thoth_json_python.encode import to_string
from ..ISA.JsonTypes.comment import Comment
from ..ISA.JsonTypes.data import Data
from ..ISA.JsonTypes.material import Material
from ..ISA.JsonTypes.ontology_annotation import OntologyAnnotation
from ..ISA.JsonTypes.process import Process
from ..ISA.JsonTypes.process_input import ProcessInput
from ..ISA.JsonTypes.process_output import ProcessOutput
from ..ISA.JsonTypes.process_parameter_value import ProcessParameterValue
from ..ISA.JsonTypes.protocol import Protocol
from ..ISA.JsonTypes.protocol_parameter import ProtocolParameter
from ..ISA.JsonTypes.sample import Sample
from ..ISA.JsonTypes.source import Source
from ..ISA.JsonTypes.uri import URIModule_toString
from ..ISA.JsonTypes.value import Value
from ..ISA_Json.comment import (encoder, decoder as decoder_1)
from ..ISA_Json.context.rocrate.isa_process_context import context_jsonvalue as context_jsonvalue_1
from ..ISA_Json.context.rocrate.isa_process_parameter_value_context import context_jsonvalue
from ..ISA_Json.converter_options import (ConverterOptions__get_SetID, ConverterOptions__get_IncludeType, ConverterOptions__get_IncludeContext, ConverterOptions, ConverterOptions__ctor, ConverterOptions__set_SetID_Z1FBCCD16, ConverterOptions__set_IncludeType_Z1FBCCD16, ConverterOptions__set_IncludeContext_Z1FBCCD16)
from ..ISA_Json.data import (Sample_encoder, Data_encoder, Source_encoder, Source_decoder, Sample_decoder, Data_decoder)
from ..ISA_Json.decode import uri
from ..ISA_Json.factor import (Value_encoder, Value_decoder)
from ..ISA_Json.gencode import (try_include, try_include_list)
from ..ISA_Json.material import (Material_encoder, Material_decoder)
from ..ISA_Json.ontology import (OntologyAnnotation_encoder, OntologyAnnotation_decoder)
from ..ISA_Json.protocol import (ProtocolParameter_encoder, ProtocolParameter_decoder, Protocol_encoder, Protocol_decoder)

__A_ = TypeVar("__A_")

def ProcessParameterValue_genID(p: ProcessParameterValue) -> str:
    matchValue: Value | None = p.Value
    matchValue_1: ProtocolParameter | None = p.Category
    (pattern_matching_result, c, v) = (None, None, None)
    if matchValue is not None:
        if matchValue_1 is not None:
            pattern_matching_result = 0
            c = matchValue_1
            v = matchValue

        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        return (("#Param_" + replace(ProtocolParameter.get_name_text(c), " ", "_")) + "_") + replace(Value.get_text(v), " ", "_")

    elif pattern_matching_result == 1:
        return "#EmptyParameterValue"



def ProcessParameterValue_encoder(options: ConverterOptions, oa: ProcessParameterValue) -> Json:
    def chooser(tupled_arg: tuple[str, Json], options: Any=options, oa: Any=oa) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1274(__unit: None=None, options: Any=options, oa: Any=oa) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1273(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1272(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1266(oa_1: ProtocolParameter) -> Json:
                    return ProtocolParameter_encoder(options, oa_1)

                def _arrow1271(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1267(value_3: Value) -> Json:
                        return Value_encoder(options, value_3)

                    def _arrow1270(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        def _arrow1268(oa_2: OntologyAnnotation) -> Json:
                            return OntologyAnnotation_encoder(options, oa_2)

                        def _arrow1269(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                            return singleton(("@context", context_jsonvalue)) if ConverterOptions__get_IncludeContext(options) else empty()

                        return append(singleton(try_include("unit", _arrow1268, oa.Unit)), delay(_arrow1269))

                    return append(singleton(try_include("value", _arrow1267, oa.Value)), delay(_arrow1270))

                return append(singleton(try_include("category", _arrow1266, oa.Category)), delay(_arrow1271))

            return append(singleton(("@type", list_1_1(of_array([Json(0, "ProcessParameterValue"), Json(0, "ArcProcessParameterValue")])))) if ConverterOptions__get_IncludeType(options) else empty(), delay(_arrow1272))

        return append(singleton(("@id", Json(0, ProcessParameterValue_genID(oa)))) if ConverterOptions__get_SetID(options) else empty(), delay(_arrow1273))

    return Json(5, choose(chooser, to_list(delay(_arrow1274))))


def ProcessParameterValue_decoder(options: ConverterOptions) -> Decoder_1[ProcessParameterValue]:
    def _arrow1278(get: IGetters, options: Any=options) -> ProcessParameterValue:
        def _arrow1275(__unit: None=None) -> ProtocolParameter | None:
            arg_1: Decoder_1[ProtocolParameter] = ProtocolParameter_decoder(options)
            object_arg: IOptionalGetter = get.Optional
            return object_arg.Field("category", arg_1)

        def _arrow1276(__unit: None=None) -> Value | None:
            arg_3: Decoder_1[Value] = Value_decoder(options)
            object_arg_1: IOptionalGetter = get.Optional
            return object_arg_1.Field("value", arg_3)

        def _arrow1277(__unit: None=None) -> OntologyAnnotation | None:
            arg_5: Decoder_1[OntologyAnnotation] = OntologyAnnotation_decoder(options)
            object_arg_2: IOptionalGetter = get.Optional
            return object_arg_2.Field("unit", arg_5)

        return ProcessParameterValue(_arrow1275(), _arrow1276(), _arrow1277())

    return object(_arrow1278)


def ProcessParameterValue_fromJsonString(s: str) -> ProcessParameterValue:
    match_value: FSharpResult_2[ProcessParameterValue, str] = Decode_fromString(ProcessParameterValue_decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def ProcessParameterValue_toJsonString(p: ProcessParameterValue) -> str:
    return to_string(2, ProcessParameterValue_encoder(ConverterOptions__ctor(), p))


def ProcessParameterValue_toJsonldString(p: ProcessParameterValue) -> str:
    def _arrow1279(__unit: None=None, p: Any=p) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, ProcessParameterValue_encoder(_arrow1279(), p))


def ProcessParameterValue_toJsonldStringWithContext(a: ProcessParameterValue) -> str:
    def _arrow1280(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, ProcessParameterValue_encoder(_arrow1280(), a))


def ProcessInput_encoder(options: ConverterOptions, value: ProcessInput) -> Json:
    if value.tag == 1:
        return Sample_encoder(options, value.fields[0])

    elif value.tag == 2:
        return Data_encoder(options, value.fields[0])

    elif value.tag == 3:
        return Material_encoder(options, value.fields[0])

    else: 
        return Source_encoder(options, value.fields[0])



def ProcessInput_decoder(options: ConverterOptions) -> Decoder_1[ProcessInput]:
    class ObjectExpr1281(Decoder_1[ProcessInput]):
        def Decode(self, s: IDecoderHelpers_1[__A_], json: __A_, options: Any=options) -> FSharpResult_2[ProcessInput, tuple[str, ErrorReason_1[__A_]]]:
            match_value: FSharpResult_2[Source, tuple[str, ErrorReason_1[__A_]]] = Source_decoder(options).Decode(s, json)
            if match_value.tag == 1:
                match_value_1: FSharpResult_2[Sample, tuple[str, ErrorReason_1[__A_]]] = Sample_decoder(options).Decode(s, json)
                if match_value_1.tag == 1:
                    match_value_2: FSharpResult_2[Data, tuple[str, ErrorReason_1[__A_]]] = Data_decoder(options).Decode(s, json)
                    if match_value_2.tag == 1:
                        match_value_3: FSharpResult_2[Material, tuple[str, ErrorReason_1[__A_]]] = Material_decoder(options).Decode(s, json)
                        return FSharpResult_2(1, match_value_3.fields[0]) if (match_value_3.tag == 1) else FSharpResult_2(0, ProcessInput(3, match_value_3.fields[0]))

                    else: 
                        return FSharpResult_2(0, ProcessInput(2, match_value_2.fields[0]))


                else: 
                    return FSharpResult_2(0, ProcessInput(1, match_value_1.fields[0]))


            else: 
                return FSharpResult_2(0, ProcessInput(0, match_value.fields[0]))


    return ObjectExpr1281()


def ProcessInput_fromJsonString(s: str) -> ProcessInput:
    match_value: FSharpResult_2[ProcessInput, str] = Decode_fromString(ProcessInput_decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def ProcessInput_toJsonString(m: ProcessInput) -> str:
    return to_string(2, ProcessInput_encoder(ConverterOptions__ctor(), m))


def ProcessInput_toJsonldString(m: ProcessInput) -> str:
    def _arrow1282(__unit: None=None, m: Any=m) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, ProcessInput_encoder(_arrow1282(), m))


def ProcessInput_toJsonldStringWithContext(a: ProcessInput) -> str:
    def _arrow1283(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, ProcessInput_encoder(_arrow1283(), a))


def ProcessOutput_encoder(options: ConverterOptions, value: ProcessOutput) -> Json:
    if value.tag == 1:
        return Data_encoder(options, value.fields[0])

    elif value.tag == 2:
        return Material_encoder(options, value.fields[0])

    else: 
        return Sample_encoder(options, value.fields[0])



def ProcessOutput_decoder(options: ConverterOptions) -> Decoder_1[ProcessOutput]:
    class ObjectExpr1284(Decoder_1[ProcessOutput]):
        def Decode(self, s: IDecoderHelpers_1[__A_], json: __A_, options: Any=options) -> FSharpResult_2[ProcessOutput, tuple[str, ErrorReason_1[__A_]]]:
            match_value: FSharpResult_2[Sample, tuple[str, ErrorReason_1[__A_]]] = Sample_decoder(options).Decode(s, json)
            if match_value.tag == 1:
                match_value_1: FSharpResult_2[Data, tuple[str, ErrorReason_1[__A_]]] = Data_decoder(options).Decode(s, json)
                if match_value_1.tag == 1:
                    match_value_2: FSharpResult_2[Material, tuple[str, ErrorReason_1[__A_]]] = Material_decoder(options).Decode(s, json)
                    return FSharpResult_2(1, match_value_2.fields[0]) if (match_value_2.tag == 1) else FSharpResult_2(0, ProcessOutput(2, match_value_2.fields[0]))

                else: 
                    return FSharpResult_2(0, ProcessOutput(1, match_value_1.fields[0]))


            else: 
                return FSharpResult_2(0, ProcessOutput(0, match_value.fields[0]))


    return ObjectExpr1284()


def ProcessOutput_fromJsonString(s: str) -> ProcessOutput:
    match_value: FSharpResult_2[ProcessOutput, str] = Decode_fromString(ProcessOutput_decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def ProcessOutput_toJsonString(m: ProcessOutput) -> str:
    return to_string(2, ProcessOutput_encoder(ConverterOptions__ctor(), m))


def ProcessOutput_toJsonldStringWithContext(a: ProcessOutput) -> str:
    def _arrow1285(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, ProcessOutput_encoder(_arrow1285(), a))


def Process_genID(p: Process) -> str:
    match_value: str | None = p.ID
    if match_value is None:
        match_value_1: str | None = p.Name
        if match_value_1 is None:
            return "#EmptyProcess"

        else: 
            return "#Process_" + replace(match_value_1, " ", "_")


    else: 
        return URIModule_toString(match_value)



def Process_encoder(options: ConverterOptions, study_name: str | None, assay_name: str | None, oa: Process) -> Json:
    def chooser(tupled_arg: tuple[str, Json], options: Any=options, study_name: Any=study_name, assay_name: Any=assay_name, oa: Any=oa) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1309(__unit: None=None, options: Any=options, study_name: Any=study_name, assay_name: Any=assay_name, oa: Any=oa) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1286(value_1: str) -> Json:
            return Json(0, value_1)

        def _arrow1308(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1307(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1287(value_5: str) -> Json:
                    return Json(0, value_5)

                def _arrow1306(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1288(oa_1: Protocol) -> Json:
                        return Protocol_encoder(options, study_name, assay_name, oa.Name, oa_1)

                    def _arrow1305(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        def _arrow1289(oa_2: ProcessParameterValue) -> Json:
                            return ProcessParameterValue_encoder(options, oa_2)

                        def _arrow1304(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                            def _arrow1290(value_7: str) -> Json:
                                return Json(0, value_7)

                            def _arrow1303(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                def _arrow1291(value_9: str) -> Json:
                                    return Json(0, value_9)

                                def _arrow1302(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                    def _arrow1292(oa_3: Process) -> Json:
                                        return Process_encoder(options, study_name, assay_name, oa_3)

                                    def _arrow1301(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                        def _arrow1293(oa_4: Process) -> Json:
                                            return Process_encoder(options, study_name, assay_name, oa_4)

                                        def _arrow1300(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                            def _arrow1294(value_11: ProcessInput) -> Json:
                                                return ProcessInput_encoder(options, value_11)

                                            def _arrow1299(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                def _arrow1295(value_12: ProcessOutput) -> Json:
                                                    return ProcessOutput_encoder(options, value_12)

                                                def _arrow1298(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                    def _arrow1296(comment: Comment) -> Json:
                                                        return encoder(options, comment)

                                                    def _arrow1297(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                        return singleton(("@context", context_jsonvalue_1)) if ConverterOptions__get_IncludeContext(options) else empty()

                                                    return append(singleton(try_include_list("comments", _arrow1296, oa.Comments)), delay(_arrow1297))

                                                return append(singleton(try_include_list("outputs", _arrow1295, oa.Outputs)), delay(_arrow1298))

                                            return append(singleton(try_include_list("inputs", _arrow1294, oa.Inputs)), delay(_arrow1299))

                                        return append(singleton(try_include("nextProcess", _arrow1293, oa.NextProcess)), delay(_arrow1300))

                                    return append(singleton(try_include("previousProcess", _arrow1292, oa.PreviousProcess)), delay(_arrow1301))

                                return append(singleton(try_include("date", _arrow1291, oa.Date)), delay(_arrow1302))

                            return append(singleton(try_include("performer", _arrow1290, oa.Performer)), delay(_arrow1303))

                        return append(singleton(try_include_list("parameterValues", _arrow1289, oa.ParameterValues)), delay(_arrow1304))

                    return append(singleton(try_include("executesProtocol", _arrow1288, oa.ExecutesProtocol)), delay(_arrow1305))

                return append(singleton(try_include("name", _arrow1287, oa.Name)), delay(_arrow1306))

            return append(singleton(("@type", list_1_1(of_array([Json(0, "Process"), Json(0, "ArcProcess")])))) if ConverterOptions__get_IncludeType(options) else empty(), delay(_arrow1307))

        return append(singleton(("@id", Json(0, Process_genID(oa)))) if ConverterOptions__get_SetID(options) else singleton(try_include("@id", _arrow1286, oa.ID)), delay(_arrow1308))

    return Json(5, choose(chooser, to_list(delay(_arrow1309))))


def Process_decoder(options: ConverterOptions) -> Decoder_1[Process]:
    def _arrow1321(get: IGetters, options: Any=options) -> Process:
        def _arrow1310(__unit: None=None) -> str | None:
            object_arg: IOptionalGetter = get.Optional
            return object_arg.Field("@id", uri)

        def _arrow1311(__unit: None=None) -> str | None:
            object_arg_1: IOptionalGetter = get.Optional
            return object_arg_1.Field("name", string)

        def _arrow1312(__unit: None=None) -> Protocol | None:
            arg_5: Decoder_1[Protocol] = Protocol_decoder(options)
            object_arg_2: IOptionalGetter = get.Optional
            return object_arg_2.Field("executesProtocol", arg_5)

        def _arrow1313(__unit: None=None) -> FSharpList[ProcessParameterValue] | None:
            arg_7: Decoder_1[FSharpList[ProcessParameterValue]] = list_1_2(ProcessParameterValue_decoder(options))
            object_arg_3: IOptionalGetter = get.Optional
            return object_arg_3.Field("parameterValues", arg_7)

        def _arrow1314(__unit: None=None) -> str | None:
            object_arg_4: IOptionalGetter = get.Optional
            return object_arg_4.Field("performer", string)

        def _arrow1315(__unit: None=None) -> str | None:
            object_arg_5: IOptionalGetter = get.Optional
            return object_arg_5.Field("date", string)

        def _arrow1316(__unit: None=None) -> Process | None:
            arg_13: Decoder_1[Process] = Process_decoder(options)
            object_arg_6: IOptionalGetter = get.Optional
            return object_arg_6.Field("previousProcess", arg_13)

        def _arrow1317(__unit: None=None) -> Process | None:
            arg_15: Decoder_1[Process] = Process_decoder(options)
            object_arg_7: IOptionalGetter = get.Optional
            return object_arg_7.Field("nextProcess", arg_15)

        def _arrow1318(__unit: None=None) -> FSharpList[ProcessInput] | None:
            arg_17: Decoder_1[FSharpList[ProcessInput]] = list_1_2(ProcessInput_decoder(options))
            object_arg_8: IOptionalGetter = get.Optional
            return object_arg_8.Field("inputs", arg_17)

        def _arrow1319(__unit: None=None) -> FSharpList[ProcessOutput] | None:
            arg_19: Decoder_1[FSharpList[ProcessOutput]] = list_1_2(ProcessOutput_decoder(options))
            object_arg_9: IOptionalGetter = get.Optional
            return object_arg_9.Field("outputs", arg_19)

        def _arrow1320(__unit: None=None) -> FSharpList[Comment] | None:
            arg_21: Decoder_1[FSharpList[Comment]] = list_1_2(decoder_1(options))
            object_arg_10: IOptionalGetter = get.Optional
            return object_arg_10.Field("comments", arg_21)

        return Process(_arrow1310(), _arrow1311(), _arrow1312(), _arrow1313(), _arrow1314(), _arrow1315(), _arrow1316(), _arrow1317(), _arrow1318(), _arrow1319(), _arrow1320())

    return object(_arrow1321)


def Process_fromJsonString(s: str) -> Process:
    match_value: FSharpResult_2[Process, str] = Decode_fromString(Process_decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def Process_toJsonString(p: Process) -> str:
    return to_string(2, Process_encoder(ConverterOptions__ctor(), None, None, p))


def Process_toJsonldString(p: Process) -> str:
    def _arrow1322(__unit: None=None, p: Any=p) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, Process_encoder(_arrow1322(), None, None, p))


def Process_toJsonldStringWithContext(a: Process) -> str:
    def _arrow1323(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, Process_encoder(_arrow1323(), None, None, a))


def ProcessSequence_fromJsonString(s: str) -> FSharpList[Process]:
    match_value: FSharpResult_2[FSharpList[Process], str] = Decode_fromString(list_1_2(Process_decoder(ConverterOptions__ctor())), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def ProcessSequence_toJsonString(p: FSharpList[Process]) -> str:
    def _arrow1325(__unit: None=None, p: Any=p) -> Callable[[Process], Json]:
        options: ConverterOptions = ConverterOptions__ctor()
        def _arrow1324(oa: Process) -> Json:
            return Process_encoder(options, None, None, oa)

        return _arrow1324

    return to_string(2, list_1_1(map(_arrow1325(), p)))


def ProcessSequence_toJsonldString(p: FSharpList[Process]) -> str:
    def _arrow1327(__unit: None=None, p: Any=p) -> Callable[[Process], Json]:
        options: ConverterOptions
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        options = return_val
        def _arrow1326(oa: Process) -> Json:
            return Process_encoder(options, None, None, oa)

        return _arrow1326

    return to_string(2, list_1_1(map(_arrow1327(), p)))


def ProcessSequence_toJsonldStringWithContext(p: FSharpList[Process]) -> str:
    def _arrow1329(__unit: None=None, p: Any=p) -> Callable[[Process], Json]:
        options: ConverterOptions
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        options = return_val
        def _arrow1328(oa: Process) -> Json:
            return Process_encoder(options, None, None, oa)

        return _arrow1328

    return to_string(2, list_1_1(map(_arrow1329(), p)))


__all__ = ["ProcessParameterValue_genID", "ProcessParameterValue_encoder", "ProcessParameterValue_decoder", "ProcessParameterValue_fromJsonString", "ProcessParameterValue_toJsonString", "ProcessParameterValue_toJsonldString", "ProcessParameterValue_toJsonldStringWithContext", "ProcessInput_encoder", "ProcessInput_decoder", "ProcessInput_fromJsonString", "ProcessInput_toJsonString", "ProcessInput_toJsonldString", "ProcessInput_toJsonldStringWithContext", "ProcessOutput_encoder", "ProcessOutput_decoder", "ProcessOutput_fromJsonString", "ProcessOutput_toJsonString", "ProcessOutput_toJsonldStringWithContext", "Process_genID", "Process_encoder", "Process_decoder", "Process_fromJsonString", "Process_toJsonString", "Process_toJsonldString", "Process_toJsonldStringWithContext", "ProcessSequence_fromJsonString", "ProcessSequence_toJsonString", "ProcessSequence_toJsonldString", "ProcessSequence_toJsonldStringWithContext"]

