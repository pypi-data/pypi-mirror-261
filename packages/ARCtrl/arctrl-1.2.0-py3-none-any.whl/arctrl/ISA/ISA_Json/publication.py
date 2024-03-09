from __future__ import annotations
from typing import Any
from ...fable_modules.fable_library.list import (choose, of_array, FSharpList)
from ...fable_modules.fable_library.result import FSharpResult_2
from ...fable_modules.fable_library.seq import (to_list, delay, append, singleton, empty)
from ...fable_modules.fable_library.string_ import (replace, to_text, printf)
from ...fable_modules.fable_library.types import Array
from ...fable_modules.fable_library.util import (equals, IEnumerable_1)
from ...fable_modules.thoth_json_core.decode import (IOptionalGetter, string, array, IGetters)
from ...fable_modules.thoth_json_core.types import (Json, Decoder_1)
from ...fable_modules.thoth_json_python.decode import Decode_fromString
from ...fable_modules.thoth_json_python.encode import to_string
from ..ISA.JsonTypes.comment import Comment
from ..ISA.JsonTypes.ontology_annotation import OntologyAnnotation
from ..ISA.JsonTypes.publication import Publication
from ..ISA_Json.comment import (encoder as encoder_1, decoder as decoder_2)
from ..ISA_Json.context.rocrate.isa_publication_context import context_jsonvalue
from ..ISA_Json.converter_options import (ConverterOptions__get_SetID, ConverterOptions__get_IncludeType, ConverterOptions__get_IncludeContext, ConverterOptions, ConverterOptions__ctor, ConverterOptions__set_SetID_Z1FBCCD16, ConverterOptions__set_IncludeType_Z1FBCCD16, ConverterOptions__set_IncludeContext_Z1FBCCD16)
from ..ISA_Json.decode import (object, uri)
from ..ISA_Json.gencode import (try_include, try_include_array)
from ..ISA_Json.ontology import (OntologyAnnotation_encoder, OntologyAnnotation_decoder)

def gen_id(p: Publication) -> str:
    match_value: str | None = p.DOI
    if match_value is None:
        match_value_1: str | None = p.PubMedID
        if match_value_1 is None:
            match_value_2: str | None = p.Title
            if match_value_2 is None:
                return "#EmptyPublication"

            else: 
                return "#Pub_" + replace(match_value_2, " ", "_")


        else: 
            return match_value_1


    else: 
        return match_value



def encoder(options: ConverterOptions, oa: Publication) -> Json:
    def chooser(tupled_arg: tuple[str, Json], options: Any=options, oa: Any=oa) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1256(__unit: None=None, options: Any=options, oa: Any=oa) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1255(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1254(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1242(value_2: str) -> Json:
                    return Json(0, value_2)

                def _arrow1253(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1243(value_4: str) -> Json:
                        return Json(0, value_4)

                    def _arrow1252(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        def _arrow1244(value_6: str) -> Json:
                            return Json(0, value_6)

                        def _arrow1251(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                            def _arrow1245(value_8: str) -> Json:
                                return Json(0, value_8)

                            def _arrow1250(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                def _arrow1246(oa_1: OntologyAnnotation) -> Json:
                                    return OntologyAnnotation_encoder(options, oa_1)

                                def _arrow1249(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                    def _arrow1247(comment: Comment) -> Json:
                                        return encoder_1(options, comment)

                                    def _arrow1248(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                        return singleton(("@context", context_jsonvalue)) if ConverterOptions__get_IncludeContext(options) else empty()

                                    return append(singleton(try_include_array("comments", _arrow1247, oa.Comments)), delay(_arrow1248))

                                return append(singleton(try_include("status", _arrow1246, oa.Status)), delay(_arrow1249))

                            return append(singleton(try_include("title", _arrow1245, oa.Title)), delay(_arrow1250))

                        return append(singleton(try_include("authorList", _arrow1244, oa.Authors)), delay(_arrow1251))

                    return append(singleton(try_include("doi", _arrow1243, oa.DOI)), delay(_arrow1252))

                return append(singleton(try_include("pubMedID", _arrow1242, oa.PubMedID)), delay(_arrow1253))

            return append(singleton(("@type", Json(0, "Publication"))) if ConverterOptions__get_IncludeType(options) else empty(), delay(_arrow1254))

        return append(singleton(("@id", Json(0, gen_id(oa)))) if ConverterOptions__get_SetID(options) else empty(), delay(_arrow1255))

    return Json(5, choose(chooser, to_list(delay(_arrow1256))))


allowed_fields: FSharpList[str] = of_array(["@id", "pubMedID", "doi", "authorList", "title", "status", "comments", "@type", "@context"])

def decoder(options: ConverterOptions) -> Decoder_1[Publication]:
    def _arrow1263(get: IGetters, options: Any=options) -> Publication:
        def _arrow1257(__unit: None=None) -> str | None:
            object_arg: IOptionalGetter = get.Optional
            return object_arg.Field("pubMedID", uri)

        def _arrow1258(__unit: None=None) -> str | None:
            object_arg_1: IOptionalGetter = get.Optional
            return object_arg_1.Field("doi", string)

        def _arrow1259(__unit: None=None) -> str | None:
            object_arg_2: IOptionalGetter = get.Optional
            return object_arg_2.Field("authorList", string)

        def _arrow1260(__unit: None=None) -> str | None:
            object_arg_3: IOptionalGetter = get.Optional
            return object_arg_3.Field("title", string)

        def _arrow1261(__unit: None=None) -> OntologyAnnotation | None:
            arg_9: Decoder_1[OntologyAnnotation] = OntologyAnnotation_decoder(options)
            object_arg_4: IOptionalGetter = get.Optional
            return object_arg_4.Field("status", arg_9)

        def _arrow1262(__unit: None=None) -> Array[Comment] | None:
            arg_11: Decoder_1[Array[Comment]] = array(decoder_2(options))
            object_arg_5: IOptionalGetter = get.Optional
            return object_arg_5.Field("comments", arg_11)

        return Publication(_arrow1257(), _arrow1258(), _arrow1259(), _arrow1260(), _arrow1261(), _arrow1262())

    return object(allowed_fields, _arrow1263)


def from_json_string(s: str) -> Publication:
    match_value: FSharpResult_2[Publication, str] = Decode_fromString(decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def to_json_string(p: Publication) -> str:
    return to_string(2, encoder(ConverterOptions__ctor(), p))


def to_jsonld_string(p: Publication) -> str:
    def _arrow1264(__unit: None=None, p: Any=p) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, encoder(_arrow1264(), p))


def to_jsonld_string_with_context(a: Publication) -> str:
    def _arrow1265(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, encoder(_arrow1265(), a))


__all__ = ["gen_id", "encoder", "allowed_fields", "decoder", "from_json_string", "to_json_string", "to_jsonld_string", "to_jsonld_string_with_context"]

