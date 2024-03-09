from __future__ import annotations
from typing import Any
from ...fable_modules.fable_library.list import (choose, of_array, FSharpList, empty as empty_1)
from ...fable_modules.fable_library.result import FSharpResult_2
from ...fable_modules.fable_library.seq import (to_list, delay, append, singleton, empty)
from ...fable_modules.fable_library.string_ import (to_text, printf)
from ...fable_modules.fable_library.util import (equals, IEnumerable_1)
from ...fable_modules.thoth_json_core.decode import (IOptionalGetter, string, list_1 as list_1_1, IGetters)
from ...fable_modules.thoth_json_core.types import (Json, Decoder_1)
from ...fable_modules.thoth_json_python.decode import Decode_fromString
from ...fable_modules.thoth_json_python.encode import to_string
from ..ISA.JsonTypes.comment import Comment
from ..ISA.JsonTypes.investigation import Investigation
from ..ISA.JsonTypes.ontology_source_reference import OntologySourceReference
from ..ISA.JsonTypes.person import Person
from ..ISA.JsonTypes.publication import Publication
from ..ISA.JsonTypes.study import Study
from ..ISA_Json.comment import (encoder as encoder_3, decoder as decoder_4)
from ..ISA_Json.context.rocrate.isa_investigation_context import context_jsonvalue
from ..ISA_Json.context.rocrate.rocrate_context import (conforms_to_jsonvalue, context_jsonvalue as context_jsonvalue_1)
from ..ISA_Json.converter_options import (ConverterOptions__get_SetID, ConverterOptions__get_IncludeType, ConverterOptions__get_IncludeContext, ConverterOptions, ConverterOptions__ctor, ConverterOptions__set_SetID_Z1FBCCD16, ConverterOptions__set_IncludeType_Z1FBCCD16, ConverterOptions__set_IncludeContext_Z1FBCCD16, ConverterOptions__set_IsRoCrate_Z1FBCCD16)
from ..ISA_Json.decode import object
from ..ISA_Json.gencode import (try_include, try_include_list)
from ..ISA_Json.ontology import (OntologySourceReference_encoder, OntologySourceReference_decoder)
from ..ISA_Json.person import (encoder as encoder_2, decoder as decoder_3)
from ..ISA_Json.publication import (encoder as encoder_1, decoder as decoder_2)
from ..ISA_Json.study import (Study_encoder, Study_decoder)

def gen_id(i: Investigation) -> str:
    return "./"


def encoder(options: ConverterOptions, oa: Investigation) -> Json:
    def chooser(tupled_arg: tuple[str, Json], options: Any=options, oa: Any=oa) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1503(__unit: None=None, options: Any=options, oa: Any=oa) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1455(value_1: str) -> Json:
            return Json(0, value_1)

        def _arrow1502(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1501(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1458(value_4: str) -> Json:
                    return Json(0, value_4)

                def _arrow1500(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1459(value_6: str) -> Json:
                        return Json(0, value_6)

                    def _arrow1499(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        def _arrow1462(value_8: str) -> Json:
                            return Json(0, value_8)

                        def _arrow1498(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                            def _arrow1465(value_10: str) -> Json:
                                return Json(0, value_10)

                            def _arrow1497(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                def _arrow1468(value_12: str) -> Json:
                                    return Json(0, value_12)

                                def _arrow1496(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                    def _arrow1471(value_14: str) -> Json:
                                        return Json(0, value_14)

                                    def _arrow1495(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                        def _arrow1474(osr: OntologySourceReference) -> Json:
                                            return OntologySourceReference_encoder(options, osr)

                                        def _arrow1494(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                            def _arrow1478(oa_1: Publication) -> Json:
                                                return encoder_1(options, oa_1)

                                            def _arrow1493(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                def _arrow1482(oa_2: Person) -> Json:
                                                    return encoder_2(options, oa_2)

                                                def _arrow1492(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                    def _arrow1485(oa_3: Study) -> Json:
                                                        return Study_encoder(options, oa_3)

                                                    def _arrow1491(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                        def _arrow1488(comment: Comment) -> Json:
                                                            return encoder_3(options, comment)

                                                        def _arrow1490(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                            return singleton(("@context", context_jsonvalue)) if ConverterOptions__get_IncludeContext(options) else empty()

                                                        return append(singleton(try_include_list("comments", _arrow1488, oa.Comments)), delay(_arrow1490))

                                                    return append(singleton(try_include_list("studies", _arrow1485, oa.Studies)), delay(_arrow1491))

                                                return append(singleton(try_include_list("people", _arrow1482, oa.Contacts)), delay(_arrow1492))

                                            return append(singleton(try_include_list("publications", _arrow1478, oa.Publications)), delay(_arrow1493))

                                        return append(singleton(try_include_list("ontologySourceReferences", _arrow1474, oa.OntologySourceReferences)), delay(_arrow1494))

                                    return append(singleton(try_include("publicReleaseDate", _arrow1471, oa.PublicReleaseDate)), delay(_arrow1495))

                                return append(singleton(try_include("submissionDate", _arrow1468, oa.SubmissionDate)), delay(_arrow1496))

                            return append(singleton(try_include("description", _arrow1465, oa.Description)), delay(_arrow1497))

                        return append(singleton(try_include("title", _arrow1462, oa.Title)), delay(_arrow1498))

                    return append(singleton(try_include("identifier", _arrow1459, oa.Identifier)), delay(_arrow1499))

                return append(singleton(try_include("filename", _arrow1458, oa.FileName)), delay(_arrow1500))

            return append(singleton(("@type", Json(0, "Investigation"))) if ConverterOptions__get_IncludeType(options) else empty(), delay(_arrow1501))

        return append(singleton(("@id", Json(0, gen_id(oa)))) if ConverterOptions__get_SetID(options) else singleton(try_include("@id", _arrow1455, oa.ID)), delay(_arrow1502))

    return Json(5, choose(chooser, to_list(delay(_arrow1503))))


def encode_ro_crate(options: ConverterOptions, oa: Investigation) -> Json:
    def chooser(tupled_arg: tuple[str, Json], options: Any=options, oa: Any=oa) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1511(__unit: None=None, options: Any=options, oa: Any=oa) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1504(value: str) -> Json:
            return Json(0, value)

        def _arrow1510(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1505(value_2: str) -> Json:
                return Json(0, value_2)

            def _arrow1509(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1506(oa_1: Investigation) -> Json:
                    return encoder(options, oa_1)

                def _arrow1508(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1507(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        return singleton(("@context", context_jsonvalue_1)) if ConverterOptions__get_IncludeContext(options) else empty()

                    return append(singleton(("conformsTo", conforms_to_jsonvalue)), delay(_arrow1507))

                return append(singleton(try_include("about", _arrow1506, oa)), delay(_arrow1508))

            return append(singleton(try_include("@id", _arrow1505, "ro-crate-metadata.json")), delay(_arrow1509))

        return append(singleton(try_include("@type", _arrow1504, "CreativeWork")), delay(_arrow1510))

    return Json(5, choose(chooser, to_list(delay(_arrow1511))))


allowed_fields: FSharpList[str] = of_array(["@id", "filename", "identifier", "title", "description", "submissionDate", "publicReleaseDate", "ontologySourceReferences", "publications", "people", "studies", "comments", "@type", "@context"])

def decoder(options: ConverterOptions) -> Decoder_1[Investigation]:
    def _arrow1527(get: IGetters, options: Any=options) -> Investigation:
        def _arrow1512(__unit: None=None) -> str | None:
            object_arg: IOptionalGetter = get.Optional
            return object_arg.Field("@id", string)

        def _arrow1513(__unit: None=None) -> str | None:
            object_arg_1: IOptionalGetter = get.Optional
            return object_arg_1.Field("filename", string)

        def _arrow1514(__unit: None=None) -> str | None:
            object_arg_2: IOptionalGetter = get.Optional
            return object_arg_2.Field("identifier", string)

        def _arrow1515(__unit: None=None) -> str | None:
            object_arg_3: IOptionalGetter = get.Optional
            return object_arg_3.Field("title", string)

        def _arrow1516(__unit: None=None) -> str | None:
            object_arg_4: IOptionalGetter = get.Optional
            return object_arg_4.Field("description", string)

        def _arrow1517(__unit: None=None) -> str | None:
            object_arg_5: IOptionalGetter = get.Optional
            return object_arg_5.Field("submissionDate", string)

        def _arrow1518(__unit: None=None) -> str | None:
            object_arg_6: IOptionalGetter = get.Optional
            return object_arg_6.Field("publicReleaseDate", string)

        def _arrow1519(__unit: None=None) -> FSharpList[OntologySourceReference] | None:
            arg_15: Decoder_1[FSharpList[OntologySourceReference]] = list_1_1(OntologySourceReference_decoder(options))
            object_arg_7: IOptionalGetter = get.Optional
            return object_arg_7.Field("ontologySourceReferences", arg_15)

        def _arrow1520(__unit: None=None) -> FSharpList[Publication] | None:
            arg_17: Decoder_1[FSharpList[Publication]] = list_1_1(decoder_2(options))
            object_arg_8: IOptionalGetter = get.Optional
            return object_arg_8.Field("publications", arg_17)

        def _arrow1522(__unit: None=None) -> FSharpList[Person] | None:
            arg_19: Decoder_1[FSharpList[Person]] = list_1_1(decoder_3(options))
            object_arg_9: IOptionalGetter = get.Optional
            return object_arg_9.Field("people", arg_19)

        def _arrow1525(__unit: None=None) -> FSharpList[Study] | None:
            arg_21: Decoder_1[FSharpList[Study]] = list_1_1(Study_decoder(options))
            object_arg_10: IOptionalGetter = get.Optional
            return object_arg_10.Field("studies", arg_21)

        def _arrow1526(__unit: None=None) -> FSharpList[Comment] | None:
            arg_23: Decoder_1[FSharpList[Comment]] = list_1_1(decoder_4(options))
            object_arg_11: IOptionalGetter = get.Optional
            return object_arg_11.Field("comments", arg_23)

        return Investigation(_arrow1512(), _arrow1513(), _arrow1514(), _arrow1515(), _arrow1516(), _arrow1517(), _arrow1518(), _arrow1519(), _arrow1520(), _arrow1522(), _arrow1525(), _arrow1526(), empty_1())

    return object(allowed_fields, _arrow1527)


def from_json_string(s: str) -> Investigation:
    match_value: FSharpResult_2[Investigation, str] = Decode_fromString(decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def to_json_string(p: Investigation) -> str:
    return to_string(2, encoder(ConverterOptions__ctor(), p))


def to_jsonld_string(i: Investigation) -> str:
    def _arrow1529(__unit: None=None, i: Any=i) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, encoder(_arrow1529(), i))


def to_jsonld_string_with_context(i: Investigation) -> str:
    def _arrow1531(__unit: None=None, i: Any=i) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, encoder(_arrow1531(), i))


def to_ro_crate_string(i: Investigation) -> str:
    def _arrow1532(__unit: None=None, i: Any=i) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IsRoCrate_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, encode_ro_crate(_arrow1532(), i))


__all__ = ["gen_id", "encoder", "encode_ro_crate", "allowed_fields", "decoder", "from_json_string", "to_json_string", "to_jsonld_string", "to_jsonld_string_with_context", "to_ro_crate_string"]

