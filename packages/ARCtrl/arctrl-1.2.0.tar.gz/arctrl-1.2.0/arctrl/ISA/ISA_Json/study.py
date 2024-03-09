from __future__ import annotations
from typing import Any
from ...fable_modules.fable_library.list import (choose, of_array, FSharpList)
from ...fable_modules.fable_library.result import FSharpResult_2
from ...fable_modules.fable_library.seq import (to_list, delay, append, singleton, empty)
from ...fable_modules.fable_library.string_ import (replace, remove, to_text, printf)
from ...fable_modules.fable_library.util import (equals, max, compare_primitives, IEnumerable_1)
from ...fable_modules.thoth_json_core.decode import (list_1 as list_1_1, IOptionalGetter, IGetters, string)
from ...fable_modules.thoth_json_core.encode import list_1 as list_1_2
from ...fable_modules.thoth_json_core.types import (Json, Decoder_1)
from ...fable_modules.thoth_json_python.decode import Decode_fromString
from ...fable_modules.thoth_json_python.encode import to_string
from ..ISA.JsonTypes.assay import Assay
from ..ISA.JsonTypes.comment import Comment
from ..ISA.JsonTypes.factor import Factor
from ..ISA.JsonTypes.material import Material
from ..ISA.JsonTypes.material_attribute import MaterialAttribute
from ..ISA.JsonTypes.ontology_annotation import OntologyAnnotation
from ..ISA.JsonTypes.person import Person
from ..ISA.JsonTypes.process import Process
from ..ISA.JsonTypes.protocol import Protocol
from ..ISA.JsonTypes.publication import Publication
from ..ISA.JsonTypes.sample import Sample
from ..ISA.JsonTypes.source import Source
from ..ISA.JsonTypes.study import Study
from ..ISA.JsonTypes.study_materials import StudyMaterials
from ..ISA.JsonTypes.uri import URIModule_toString
from ..ISA_Json.assay import (Assay_encoder, Assay_decoder)
from ..ISA_Json.comment import (encoder as encoder_2, decoder as decoder_3)
from ..ISA_Json.context.rocrate.isa_study_context import context_jsonvalue
from ..ISA_Json.converter_options import (ConverterOptions, ConverterOptions__get_SetID, ConverterOptions__get_IncludeType, ConverterOptions__get_IsRoCrate, ConverterOptions__get_IncludeContext, ConverterOptions__ctor, ConverterOptions__set_SetID_Z1FBCCD16, ConverterOptions__set_IncludeType_Z1FBCCD16, ConverterOptions__set_IncludeContext_Z1FBCCD16)
from ..ISA_Json.data import (Source_encoder, Sample_encoder, Source_decoder, Sample_decoder)
from ..ISA_Json.decode import (object, uri)
from ..ISA_Json.factor import (Factor_encoder, Factor_decoder)
from ..ISA_Json.gencode import (try_include_list, try_include)
from ..ISA_Json.material import (Material_encoder, Material_decoder, MaterialAttribute_encoder, MaterialAttribute_decoder)
from ..ISA_Json.ontology import (OntologyAnnotation_encoder, OntologyAnnotation_decoder)
from ..ISA_Json.person import (encoder as encoder_1, decoder as decoder_2)
from ..ISA_Json.process import (Process_encoder, Process_decoder)
from ..ISA_Json.protocol import (Protocol_encoder, Protocol_decoder)
from ..ISA_Json.publication import (encoder, decoder as decoder_1)

def StudyMaterials_encoder(options: ConverterOptions, oa: StudyMaterials) -> Json:
    def chooser(tupled_arg: tuple[str, Json], options: Any=options, oa: Any=oa) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1425(oa_1: Source, options: Any=options, oa: Any=oa) -> Json:
        return Source_encoder(options, oa_1)

    def _arrow1426(oa_2: Sample, options: Any=options, oa: Any=oa) -> Json:
        return Sample_encoder(options, oa_2)

    def _arrow1427(oa_3: Material, options: Any=options, oa: Any=oa) -> Json:
        return Material_encoder(options, oa_3)

    return Json(5, choose(chooser, of_array([try_include_list("sources", _arrow1425, oa.Sources), try_include_list("samples", _arrow1426, oa.Samples), try_include_list("otherMaterials", _arrow1427, oa.OtherMaterials)])))


StudyMaterials_allowedFields: FSharpList[str] = of_array(["sources", "samples", "otherMaterials"])

def StudyMaterials_decoder(options: ConverterOptions) -> Decoder_1[StudyMaterials]:
    def _arrow1431(get: IGetters, options: Any=options) -> StudyMaterials:
        def _arrow1428(__unit: None=None) -> FSharpList[Source] | None:
            arg_1: Decoder_1[FSharpList[Source]] = list_1_1(Source_decoder(options))
            object_arg: IOptionalGetter = get.Optional
            return object_arg.Field("sources", arg_1)

        def _arrow1429(__unit: None=None) -> FSharpList[Sample] | None:
            arg_3: Decoder_1[FSharpList[Sample]] = list_1_1(Sample_decoder(options))
            object_arg_1: IOptionalGetter = get.Optional
            return object_arg_1.Field("samples", arg_3)

        def _arrow1430(__unit: None=None) -> FSharpList[Material] | None:
            arg_5: Decoder_1[FSharpList[Material]] = list_1_1(Material_decoder(options))
            object_arg_2: IOptionalGetter = get.Optional
            return object_arg_2.Field("otherMaterials", arg_5)

        return StudyMaterials(_arrow1428(), _arrow1429(), _arrow1430())

    return object(StudyMaterials_allowedFields, _arrow1431)


def Study_genID(s: Study) -> str:
    match_value: str | None = s.ID
    if match_value is None:
        match_value_1: str | None = s.FileName
        if match_value_1 is None:
            match_value_2: str | None = s.Identifier
            if match_value_2 is None:
                match_value_3: str | None = s.Title
                if match_value_3 is None:
                    return "#EmptyStudy"

                else: 
                    return "#Study_" + replace(match_value_3, " ", "_")


            else: 
                return "#Study_" + replace(match_value_2, " ", "_")


        else: 
            n: str = match_value_1
            def _arrow1432(x: int, y: int, s: Any=s) -> int:
                return compare_primitives(x, y)

            return remove(replace(n, " ", "_"), 0, 1 + max(_arrow1432, n.rfind("/"), n.rfind("\\")))


    else: 
        return URIModule_toString(match_value)



def Study_encoder(options: ConverterOptions, oa: Study) -> Json:
    def chooser(tupled_arg: tuple[str, Json], options: Any=options, oa: Any=oa) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1489(__unit: None=None, options: Any=options, oa: Any=oa) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1433(value_1: str) -> Json:
            return Json(0, value_1)

        def _arrow1487(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1486(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1434(value_5: str) -> Json:
                    return Json(0, value_5)

                def _arrow1484(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1435(value_7: str) -> Json:
                        return Json(0, value_7)

                    def _arrow1483(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        def _arrow1436(value_9: str) -> Json:
                            return Json(0, value_9)

                        def _arrow1481(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                            def _arrow1437(value_11: str) -> Json:
                                return Json(0, value_11)

                            def _arrow1480(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                def _arrow1438(value_13: str) -> Json:
                                    return Json(0, value_13)

                                def _arrow1479(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                    def _arrow1439(value_15: str) -> Json:
                                        return Json(0, value_15)

                                    def _arrow1477(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                        def _arrow1440(oa_1: Publication) -> Json:
                                            return encoder(options, oa_1)

                                        def _arrow1476(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                            def _arrow1441(oa_2: Person) -> Json:
                                                return encoder_1(options, oa_2)

                                            def _arrow1475(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                def _arrow1442(oa_3: OntologyAnnotation) -> Json:
                                                    return OntologyAnnotation_encoder(options, oa_3)

                                                def _arrow1473(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                    def _arrow1443(oa_4: Protocol) -> Json:
                                                        return Protocol_encoder(options, None, None, None, oa_4)

                                                    def _arrow1472(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                        def _arrow1449(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                            match_value: StudyMaterials | None = oa.Materials
                                                            if match_value is None:
                                                                return empty()

                                                            else: 
                                                                m: StudyMaterials = match_value
                                                                def _arrow1444(oa_5: Sample) -> Json:
                                                                    return Sample_encoder(options, oa_5)

                                                                def _arrow1448(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                                    def _arrow1445(oa_6: Source) -> Json:
                                                                        return Source_encoder(options, oa_6)

                                                                    def _arrow1447(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                                        def _arrow1446(oa_7: Material) -> Json:
                                                                            return Material_encoder(options, oa_7)

                                                                        return singleton(try_include_list("materials", _arrow1446, m.OtherMaterials))

                                                                    return append(singleton(try_include_list("sources", _arrow1445, m.Sources)), delay(_arrow1447))

                                                                return append(singleton(try_include_list("samples", _arrow1444, m.Samples)), delay(_arrow1448))


                                                        def _arrow1470(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                            def _arrow1450(oa_8: StudyMaterials) -> Json:
                                                                return StudyMaterials_encoder(options, oa_8)

                                                            def _arrow1469(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                                def _arrow1451(oa_9: Process) -> Json:
                                                                    return Process_encoder(options, oa.Identifier, None, oa_9)

                                                                def _arrow1467(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                                    def _arrow1452(oa_10: Assay) -> Json:
                                                                        return Assay_encoder(options, oa.Identifier, oa_10)

                                                                    def _arrow1466(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                                        def _arrow1453(oa_11: Factor) -> Json:
                                                                            return Factor_encoder(options, oa_11)

                                                                        def _arrow1464(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                                            def _arrow1454(oa_12: MaterialAttribute) -> Json:
                                                                                return MaterialAttribute_encoder(options, oa_12)

                                                                            def _arrow1463(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                                                def _arrow1456(oa_13: OntologyAnnotation) -> Json:
                                                                                    return OntologyAnnotation_encoder(options, oa_13)

                                                                                def _arrow1461(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                                                    def _arrow1457(comment: Comment) -> Json:
                                                                                        return encoder_2(options, comment)

                                                                                    def _arrow1460(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                                                        return singleton(("@context", context_jsonvalue)) if ConverterOptions__get_IncludeContext(options) else empty()

                                                                                    return append(singleton(try_include_list("comments", _arrow1457, oa.Comments)), delay(_arrow1460))

                                                                                return append(singleton(try_include_list("unitCategories", _arrow1456, oa.UnitCategories)), delay(_arrow1461))

                                                                            return append(singleton(try_include_list("characteristicCategories", _arrow1454, oa.CharacteristicCategories)), delay(_arrow1463))

                                                                        return append(singleton(try_include_list("factors", _arrow1453, oa.Factors)), delay(_arrow1464))

                                                                    return append(singleton(try_include_list("assays", _arrow1452, oa.Assays)), delay(_arrow1466))

                                                                return append(singleton(try_include_list("processSequence", _arrow1451, oa.ProcessSequence)), delay(_arrow1467))

                                                            return append(singleton(try_include("materials", _arrow1450, oa.Materials)) if (not ConverterOptions__get_IsRoCrate(options)) else empty(), delay(_arrow1469))

                                                        return append(_arrow1449() if ConverterOptions__get_IsRoCrate(options) else empty(), delay(_arrow1470))

                                                    return append(singleton(try_include_list("protocols", _arrow1443, oa.Protocols)) if (not ConverterOptions__get_IsRoCrate(options)) else empty(), delay(_arrow1472))

                                                return append(singleton(try_include_list("studyDesignDescriptors", _arrow1442, oa.StudyDesignDescriptors)), delay(_arrow1473))

                                            return append(singleton(try_include_list("people", _arrow1441, oa.Contacts)), delay(_arrow1475))

                                        return append(singleton(try_include_list("publications", _arrow1440, oa.Publications)), delay(_arrow1476))

                                    return append(singleton(try_include("publicReleaseDate", _arrow1439, oa.PublicReleaseDate)), delay(_arrow1477))

                                return append(singleton(try_include("submissionDate", _arrow1438, oa.SubmissionDate)), delay(_arrow1479))

                            return append(singleton(try_include("description", _arrow1437, oa.Description)), delay(_arrow1480))

                        return append(singleton(try_include("title", _arrow1436, oa.Title)), delay(_arrow1481))

                    return append(singleton(try_include("identifier", _arrow1435, oa.Identifier)), delay(_arrow1483))

                return append(singleton(try_include("filename", _arrow1434, oa.FileName)), delay(_arrow1484))

            return append(singleton(("@type", list_1_2(of_array([Json(0, "Study"), Json(0, "ArcStudy")])))) if ConverterOptions__get_IncludeType(options) else empty(), delay(_arrow1486))

        return append(singleton(("@id", Json(0, Study_genID(oa)))) if ConverterOptions__get_SetID(options) else singleton(try_include("@id", _arrow1433, oa.ID)), delay(_arrow1487))

    return Json(5, choose(chooser, to_list(delay(_arrow1489))))


Study_allowedFields: FSharpList[str] = of_array(["@id", "filename", "identifier", "title", "description", "submissionDate", "publicReleaseDate", "publications", "people", "studyDesignDescriptors", "protocols", "materials", "assays", "factors", "characteristicCategories", "unitCategories", "processSequence", "comments", "@type", "@context"])

def Study_decoder(options: ConverterOptions) -> Decoder_1[Study]:
    def _arrow1524(get: IGetters, options: Any=options) -> Study:
        ID: str | None
        object_arg: IOptionalGetter = get.Optional
        ID = object_arg.Field("@id", uri)
        FileName: str | None
        object_arg_1: IOptionalGetter = get.Optional
        FileName = object_arg_1.Field("filename", string)
        Identifier: str | None
        object_arg_2: IOptionalGetter = get.Optional
        Identifier = object_arg_2.Field("identifier", string)
        Title: str | None
        object_arg_3: IOptionalGetter = get.Optional
        Title = object_arg_3.Field("title", string)
        Description: str | None
        object_arg_4: IOptionalGetter = get.Optional
        Description = object_arg_4.Field("description", string)
        SubmissionDate: str | None
        object_arg_5: IOptionalGetter = get.Optional
        SubmissionDate = object_arg_5.Field("submissionDate", string)
        PublicReleaseDate: str | None
        object_arg_6: IOptionalGetter = get.Optional
        PublicReleaseDate = object_arg_6.Field("publicReleaseDate", string)
        Publications: FSharpList[Publication] | None
        arg_15: Decoder_1[FSharpList[Publication]] = list_1_1(decoder_1(options))
        object_arg_7: IOptionalGetter = get.Optional
        Publications = object_arg_7.Field("publications", arg_15)
        Contacts: FSharpList[Person] | None
        arg_17: Decoder_1[FSharpList[Person]] = list_1_1(decoder_2(options))
        object_arg_8: IOptionalGetter = get.Optional
        Contacts = object_arg_8.Field("people", arg_17)
        StudyDesignDescriptors: FSharpList[OntologyAnnotation] | None
        arg_19: Decoder_1[FSharpList[OntologyAnnotation]] = list_1_1(OntologyAnnotation_decoder(options))
        object_arg_9: IOptionalGetter = get.Optional
        StudyDesignDescriptors = object_arg_9.Field("studyDesignDescriptors", arg_19)
        Protocols: FSharpList[Protocol] | None
        arg_21: Decoder_1[FSharpList[Protocol]] = list_1_1(Protocol_decoder(options))
        object_arg_10: IOptionalGetter = get.Optional
        Protocols = object_arg_10.Field("protocols", arg_21)
        Materials: StudyMaterials | None
        arg_23: Decoder_1[StudyMaterials] = StudyMaterials_decoder(options)
        object_arg_11: IOptionalGetter = get.Optional
        Materials = object_arg_11.Field("materials", arg_23)
        Assays: FSharpList[Assay] | None
        arg_25: Decoder_1[FSharpList[Assay]] = list_1_1(Assay_decoder(options))
        object_arg_12: IOptionalGetter = get.Optional
        Assays = object_arg_12.Field("assays", arg_25)
        Factors: FSharpList[Factor] | None
        arg_27: Decoder_1[FSharpList[Factor]] = list_1_1(Factor_decoder(options))
        object_arg_13: IOptionalGetter = get.Optional
        Factors = object_arg_13.Field("factors", arg_27)
        CharacteristicCategories: FSharpList[MaterialAttribute] | None
        arg_29: Decoder_1[FSharpList[MaterialAttribute]] = list_1_1(MaterialAttribute_decoder(options))
        object_arg_14: IOptionalGetter = get.Optional
        CharacteristicCategories = object_arg_14.Field("characteristicCategories", arg_29)
        UnitCategories: FSharpList[OntologyAnnotation] | None
        arg_31: Decoder_1[FSharpList[OntologyAnnotation]] = list_1_1(OntologyAnnotation_decoder(options))
        object_arg_15: IOptionalGetter = get.Optional
        UnitCategories = object_arg_15.Field("unitCategories", arg_31)
        def _arrow1521(__unit: None=None) -> FSharpList[Process] | None:
            arg_33: Decoder_1[FSharpList[Process]] = list_1_1(Process_decoder(options))
            object_arg_16: IOptionalGetter = get.Optional
            return object_arg_16.Field("processSequence", arg_33)

        def _arrow1523(__unit: None=None) -> FSharpList[Comment] | None:
            arg_35: Decoder_1[FSharpList[Comment]] = list_1_1(decoder_3(options))
            object_arg_17: IOptionalGetter = get.Optional
            return object_arg_17.Field("comments", arg_35)

        return Study(ID, FileName, Identifier, Title, Description, SubmissionDate, PublicReleaseDate, Publications, Contacts, StudyDesignDescriptors, Protocols, Materials, _arrow1521(), Assays, Factors, CharacteristicCategories, UnitCategories, _arrow1523())

    return object(Study_allowedFields, _arrow1524)


def Study_fromJsonString(s: str) -> Study:
    match_value: FSharpResult_2[Study, str] = Decode_fromString(Study_decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def Study_toJsonString(p: Study) -> str:
    return to_string(2, Study_encoder(ConverterOptions__ctor(), p))


def Study_toJsonldString(s: Study) -> str:
    def _arrow1528(__unit: None=None, s: Any=s) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, Study_encoder(_arrow1528(), s))


def Study_toJsonldStringWithContext(a: Study) -> str:
    def _arrow1530(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, Study_encoder(_arrow1530(), a))


__all__ = ["StudyMaterials_encoder", "StudyMaterials_allowedFields", "StudyMaterials_decoder", "Study_genID", "Study_encoder", "Study_allowedFields", "Study_decoder", "Study_fromJsonString", "Study_toJsonString", "Study_toJsonldString", "Study_toJsonldStringWithContext"]

