from __future__ import annotations
from typing import Any
from ...fable_modules.fable_library.fsharp_core import Operators_FailurePattern
from ...fable_modules.fable_library.list import (choose, of_array, FSharpList)
from ...fable_modules.fable_library.result import FSharpResult_2
from ...fable_modules.fable_library.seq import (to_list, delay, append, singleton, empty)
from ...fable_modules.fable_library.string_ import (remove, replace, to_text, printf)
from ...fable_modules.fable_library.util import (equals, max, compare_primitives, IEnumerable_1)
from ...fable_modules.thoth_json_core.decode import (list_1 as list_1_1, IOptionalGetter, IGetters, string)
from ...fable_modules.thoth_json_core.encode import list_1 as list_1_2
from ...fable_modules.thoth_json_core.types import (Json, Decoder_1)
from ...fable_modules.thoth_json_python.decode import Decode_fromString
from ...fable_modules.thoth_json_python.encode import to_string
from ..ISA.identifier import Assay_identifierFromFileName
from ..ISA.JsonTypes.assay import Assay
from ..ISA.JsonTypes.assay_materials import AssayMaterials
from ..ISA.JsonTypes.comment import Comment
from ..ISA.JsonTypes.data import Data
from ..ISA.JsonTypes.material import Material
from ..ISA.JsonTypes.material_attribute import MaterialAttribute
from ..ISA.JsonTypes.ontology_annotation import OntologyAnnotation
from ..ISA.JsonTypes.process import Process
from ..ISA.JsonTypes.sample import Sample
from ..ISA.JsonTypes.uri import URIModule_toString
from ..ISA_Json.comment import (encoder, decoder as decoder_1)
from ..ISA_Json.context.rocrate.isa_assay_context import context_jsonvalue
from ..ISA_Json.converter_options import (ConverterOptions, ConverterOptions__get_SetID, ConverterOptions__get_IncludeType, ConverterOptions__get_IsRoCrate, ConverterOptions__get_IncludeContext, ConverterOptions__ctor, ConverterOptions__set_SetID_Z1FBCCD16, ConverterOptions__set_IncludeType_Z1FBCCD16, ConverterOptions__set_IncludeContext_Z1FBCCD16)
from ..ISA_Json.data import (Sample_encoder, Sample_decoder, Data_encoder, Data_decoder)
from ..ISA_Json.decode import (object, uri)
from ..ISA_Json.gencode import (try_include_list, try_include)
from ..ISA_Json.material import (Material_encoder, Material_decoder, MaterialAttribute_encoder, MaterialAttribute_decoder)
from ..ISA_Json.ontology import (OntologyAnnotation_encoder, OntologyAnnotation_decoder)
from ..ISA_Json.process import (Process_encoder, Process_decoder)

def AssayMaterials_encoder(options: ConverterOptions, oa: AssayMaterials) -> Json:
    def chooser(tupled_arg: tuple[str, Json], options: Any=options, oa: Any=oa) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1371(oa_1: Sample, options: Any=options, oa: Any=oa) -> Json:
        return Sample_encoder(options, oa_1)

    def _arrow1372(oa_2: Material, options: Any=options, oa: Any=oa) -> Json:
        return Material_encoder(options, oa_2)

    return Json(5, choose(chooser, of_array([try_include_list("samples", _arrow1371, oa.Samples), try_include_list("otherMaterials", _arrow1372, oa.OtherMaterials)])))


AssayMaterials_allowedFields: FSharpList[str] = of_array(["samples", "otherMaterials"])

def AssayMaterials_decoder(options: ConverterOptions) -> Decoder_1[AssayMaterials]:
    def _arrow1375(get: IGetters, options: Any=options) -> AssayMaterials:
        def _arrow1373(__unit: None=None) -> FSharpList[Sample] | None:
            arg_1: Decoder_1[FSharpList[Sample]] = list_1_1(Sample_decoder(options))
            object_arg: IOptionalGetter = get.Optional
            return object_arg.Field("samples", arg_1)

        def _arrow1374(__unit: None=None) -> FSharpList[Material] | None:
            arg_3: Decoder_1[FSharpList[Material]] = list_1_1(Material_decoder(options))
            object_arg_1: IOptionalGetter = get.Optional
            return object_arg_1.Field("otherMaterials", arg_3)

        return AssayMaterials(_arrow1373(), _arrow1374())

    return object(AssayMaterials_allowedFields, _arrow1375)


def Assay_genID(a: Assay) -> str:
    match_value: str | None = a.ID
    if match_value is None:
        match_value_1: str | None = a.FileName
        if match_value_1 is None:
            return "#EmptyAssay"

        else: 
            n: str = match_value_1
            def _arrow1376(x: int, y: int, a: Any=a) -> int:
                return compare_primitives(x, y)

            return remove(replace(n, " ", "_"), 0, 1 + max(_arrow1376, n.rfind("/"), n.rfind("\\")))


    else: 
        return URIModule_toString(match_value)



def Assay_encoder(options: ConverterOptions, study_name: str | None, oa: Assay) -> Json:
    assay_name: str | None
    try: 
        match_value: str | None = oa.FileName
        assay_name = None if (match_value is None) else Assay_identifierFromFileName(match_value)

    except Exception as match_value_1:
        active_pattern_result: str | None = Operators_FailurePattern(match_value_1)
        if active_pattern_result is not None:
            msg: str = active_pattern_result
            assay_name = None

        else: 
            raise match_value_1


    def chooser(tupled_arg: tuple[str, Json], options: Any=options, study_name: Any=study_name, oa: Any=oa) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1405(__unit: None=None, options: Any=options, study_name: Any=study_name, oa: Any=oa) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1377(value_1: str) -> Json:
            return Json(0, value_1)

        def _arrow1404(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1403(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1378(value_5: str) -> Json:
                    return Json(0, value_5)

                def _arrow1402(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1379(oa_1: OntologyAnnotation) -> Json:
                        return OntologyAnnotation_encoder(options, oa_1)

                    def _arrow1401(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        def _arrow1380(oa_2: OntologyAnnotation) -> Json:
                            return OntologyAnnotation_encoder(options, oa_2)

                        def _arrow1400(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                            def _arrow1381(value_7: str) -> Json:
                                return Json(0, value_7)

                            def _arrow1399(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                def _arrow1382(oa_3: Data) -> Json:
                                    return Data_encoder(options, oa_3)

                                def _arrow1398(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                    def _arrow1386(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                        match_value_2: AssayMaterials | None = oa.Materials
                                        if match_value_2 is None:
                                            return empty()

                                        else: 
                                            m: AssayMaterials = match_value_2
                                            def _arrow1383(oa_4: Sample) -> Json:
                                                return Sample_encoder(options, oa_4)

                                            def _arrow1385(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                def _arrow1384(oa_5: Material) -> Json:
                                                    return Material_encoder(options, oa_5)

                                                return singleton(try_include_list("materials", _arrow1384, m.OtherMaterials))

                                            return append(singleton(try_include_list("samples", _arrow1383, m.Samples)), delay(_arrow1385))


                                    def _arrow1397(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                        def _arrow1387(oa_6: AssayMaterials) -> Json:
                                            return AssayMaterials_encoder(options, oa_6)

                                        def _arrow1396(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                            def _arrow1388(oa_7: MaterialAttribute) -> Json:
                                                return MaterialAttribute_encoder(options, oa_7)

                                            def _arrow1395(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                def _arrow1389(oa_8: OntologyAnnotation) -> Json:
                                                    return OntologyAnnotation_encoder(options, oa_8)

                                                def _arrow1394(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                    def _arrow1390(oa_9: Process) -> Json:
                                                        return Process_encoder(options, study_name, assay_name, oa_9)

                                                    def _arrow1393(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                        def _arrow1391(comment: Comment) -> Json:
                                                            return encoder(options, comment)

                                                        def _arrow1392(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                            return singleton(("@context", context_jsonvalue)) if ConverterOptions__get_IncludeContext(options) else empty()

                                                        return append(singleton(try_include_list("comments", _arrow1391, oa.Comments)), delay(_arrow1392))

                                                    return append(singleton(try_include_list("processSequence", _arrow1390, oa.ProcessSequence)), delay(_arrow1393))

                                                return append(singleton(try_include_list("unitCategories", _arrow1389, oa.UnitCategories)), delay(_arrow1394))

                                            return append(singleton(try_include_list("characteristicCategories", _arrow1388, oa.CharacteristicCategories)), delay(_arrow1395))

                                        return append(singleton(try_include("materials", _arrow1387, oa.Materials)) if (not ConverterOptions__get_IsRoCrate(options)) else empty(), delay(_arrow1396))

                                    return append(_arrow1386() if ConverterOptions__get_IsRoCrate(options) else empty(), delay(_arrow1397))

                                return append(singleton(try_include_list("dataFiles", _arrow1382, oa.DataFiles)), delay(_arrow1398))

                            return append(singleton(try_include("technologyPlatform", _arrow1381, oa.TechnologyPlatform)), delay(_arrow1399))

                        return append(singleton(try_include("technologyType", _arrow1380, oa.TechnologyType)), delay(_arrow1400))

                    return append(singleton(try_include("measurementType", _arrow1379, oa.MeasurementType)), delay(_arrow1401))

                return append(singleton(try_include("filename", _arrow1378, oa.FileName)), delay(_arrow1402))

            return append(singleton(("@type", list_1_2(of_array([Json(0, "Assay"), Json(0, "ArcAssay")])))) if ConverterOptions__get_IncludeType(options) else empty(), delay(_arrow1403))

        return append(singleton(("@id", Json(0, Assay_genID(oa)))) if ConverterOptions__get_SetID(options) else singleton(try_include("@id", _arrow1377, oa.ID)), delay(_arrow1404))

    return Json(5, choose(chooser, to_list(delay(_arrow1405))))


Assay_allowedFields: FSharpList[str] = of_array(["@id", "filename", "measurementType", "technologyType", "technologyPlatform", "dataFiles", "materials", "characteristicCategories", "unitCategories", "processSequence", "comments", "@type", "@context"])

def Assay_decoder(options: ConverterOptions) -> Decoder_1[Assay]:
    def _arrow1417(get: IGetters, options: Any=options) -> Assay:
        def _arrow1406(__unit: None=None) -> str | None:
            object_arg: IOptionalGetter = get.Optional
            return object_arg.Field("@id", uri)

        def _arrow1407(__unit: None=None) -> str | None:
            object_arg_1: IOptionalGetter = get.Optional
            return object_arg_1.Field("filename", string)

        def _arrow1408(__unit: None=None) -> OntologyAnnotation | None:
            arg_5: Decoder_1[OntologyAnnotation] = OntologyAnnotation_decoder(options)
            object_arg_2: IOptionalGetter = get.Optional
            return object_arg_2.Field("measurementType", arg_5)

        def _arrow1409(__unit: None=None) -> OntologyAnnotation | None:
            arg_7: Decoder_1[OntologyAnnotation] = OntologyAnnotation_decoder(options)
            object_arg_3: IOptionalGetter = get.Optional
            return object_arg_3.Field("technologyType", arg_7)

        def _arrow1410(__unit: None=None) -> str | None:
            object_arg_4: IOptionalGetter = get.Optional
            return object_arg_4.Field("technologyPlatform", string)

        def _arrow1411(__unit: None=None) -> FSharpList[Data] | None:
            arg_11: Decoder_1[FSharpList[Data]] = list_1_1(Data_decoder(options))
            object_arg_5: IOptionalGetter = get.Optional
            return object_arg_5.Field("dataFiles", arg_11)

        def _arrow1412(__unit: None=None) -> AssayMaterials | None:
            arg_13: Decoder_1[AssayMaterials] = AssayMaterials_decoder(options)
            object_arg_6: IOptionalGetter = get.Optional
            return object_arg_6.Field("materials", arg_13)

        def _arrow1413(__unit: None=None) -> FSharpList[MaterialAttribute] | None:
            arg_15: Decoder_1[FSharpList[MaterialAttribute]] = list_1_1(MaterialAttribute_decoder(options))
            object_arg_7: IOptionalGetter = get.Optional
            return object_arg_7.Field("characteristicCategories", arg_15)

        def _arrow1414(__unit: None=None) -> FSharpList[OntologyAnnotation] | None:
            arg_17: Decoder_1[FSharpList[OntologyAnnotation]] = list_1_1(OntologyAnnotation_decoder(options))
            object_arg_8: IOptionalGetter = get.Optional
            return object_arg_8.Field("unitCategories", arg_17)

        def _arrow1415(__unit: None=None) -> FSharpList[Process] | None:
            arg_19: Decoder_1[FSharpList[Process]] = list_1_1(Process_decoder(options))
            object_arg_9: IOptionalGetter = get.Optional
            return object_arg_9.Field("processSequence", arg_19)

        def _arrow1416(__unit: None=None) -> FSharpList[Comment] | None:
            arg_21: Decoder_1[FSharpList[Comment]] = list_1_1(decoder_1(options))
            object_arg_10: IOptionalGetter = get.Optional
            return object_arg_10.Field("comments", arg_21)

        return Assay(_arrow1406(), _arrow1407(), _arrow1408(), _arrow1409(), _arrow1410(), _arrow1411(), _arrow1412(), _arrow1413(), _arrow1414(), _arrow1415(), _arrow1416())

    return object(Assay_allowedFields, _arrow1417)


def Assay_fromJsonString(s: str) -> Assay:
    match_value: FSharpResult_2[Assay, str] = Decode_fromString(Assay_decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def Assay_toJsonString(p: Assay) -> str:
    return to_string(2, Assay_encoder(ConverterOptions__ctor(), None, p))


def Assay_toJsonldString(a: Assay) -> str:
    def _arrow1418(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, Assay_encoder(_arrow1418(), None, a))


def Assay_toJsonldStringWithContext(a: Assay) -> str:
    def _arrow1419(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, Assay_encoder(_arrow1419(), None, a))


__all__ = ["AssayMaterials_encoder", "AssayMaterials_allowedFields", "AssayMaterials_decoder", "Assay_genID", "Assay_encoder", "Assay_allowedFields", "Assay_decoder", "Assay_fromJsonString", "Assay_toJsonString", "Assay_toJsonldString", "Assay_toJsonldStringWithContext"]

