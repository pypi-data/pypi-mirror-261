from __future__ import annotations
from collections.abc import Callable
from typing import Any
from ..fable_modules.fable_library.date import to_string as to_string_1
from ..fable_modules.fable_library.list import (map as map_1, of_array)
from ..fable_modules.fable_library.option import default_arg
from ..fable_modules.fable_library.result import FSharpResult_2
from ..fable_modules.fable_library.seq import (to_list, delay, map)
from ..fable_modules.fable_library.string_ import (to_fail, printf, to_text)
from ..fable_modules.fable_library.types import (to_string, Array)
from ..fable_modules.fable_library.util import (IEnumerable_1, to_enumerable)
from ..fable_modules.thoth_json_core.decode import (and_then, succeed, string, object, IRequiredGetter, guid, array as array_1, datetime_local, IGetters, dict_1)
from ..fable_modules.thoth_json_core.encode import list_1 as list_1_1
from ..fable_modules.thoth_json_core.types import (Json, Decoder_1)
from ..fable_modules.thoth_json_python.decode import Decode_fromString
from ..fable_modules.thoth_json_python.encode import to_string as to_string_2
from ..ISA.ISA_Json.ArcTypes.arc_table import (ArcTable_encoder, ArcTable_decoder)
from ..ISA.ISA_Json.converter_options import (ConverterOptions__ctor, ConverterOptions)
from ..ISA.ISA_Json.ontology import (OntologyAnnotation_encoder, OntologyAnnotation_decoder)
from ..ISA.ISA_Json.person import (encoder, decoder as decoder_1)
from ..ISA.ISA.ArcTypes.arc_table import ArcTable
from ..ISA.ISA.JsonTypes.ontology_annotation import OntologyAnnotation
from ..ISA.ISA.JsonTypes.person import Person
from .template import (Organisation, Template)

def _arrow1743(arg: Organisation) -> Json:
    return Json(0, to_string(arg))


Organisation_encode: Callable[[Organisation], Json] = _arrow1743

def cb(text_value: str) -> Decoder_1[Organisation]:
    return succeed(Organisation.of_string(text_value))


Organisation_decode: Decoder_1[Organisation] = and_then(cb, string)

def Template_encode(template: Template) -> Json:
    person_encoder: Callable[[Person], Json]
    options: ConverterOptions = ConverterOptions__ctor()
    def _arrow1744(oa: Person, template: Any=template) -> Json:
        return encoder(options, oa)

    person_encoder = _arrow1744
    oa_encoder: Callable[[OntologyAnnotation], Json]
    options_1: ConverterOptions = ConverterOptions__ctor()
    def _arrow1745(oa_1: OntologyAnnotation, template: Any=template) -> Json:
        return OntologyAnnotation_encoder(options_1, oa_1)

    oa_encoder = _arrow1745
    def _arrow1746(__unit: None=None, template: Any=template) -> str:
        copy_of_struct: str = template.Id
        return str(copy_of_struct)

    def _arrow1747(__unit: None=None, template: Any=template) -> IEnumerable_1[Json]:
        return map(person_encoder, template.Authors)

    def _arrow1748(__unit: None=None, template: Any=template) -> IEnumerable_1[Json]:
        return map(oa_encoder, template.EndpointRepositories)

    def _arrow1749(__unit: None=None, template: Any=template) -> IEnumerable_1[Json]:
        return map(oa_encoder, template.Tags)

    return Json(5, to_enumerable([("id", Json(0, _arrow1746())), ("table", ArcTable_encoder(template.Table)), ("name", Json(0, template.Name)), ("description", Json(0, template.Description)), ("organisation", Organisation_encode(template.Organisation)), ("version", Json(0, template.Version)), ("authors", list_1_1(to_list(delay(_arrow1747)))), ("endpoint_repositories", list_1_1(to_list(delay(_arrow1748)))), ("tags", list_1_1(to_list(delay(_arrow1749)))), ("last_updated", Json(0, to_string_1(template.LastUpdated, "O", {})))]))


def _arrow1761(__unit: None=None) -> Decoder_1[Template]:
    person_decoder: Decoder_1[Person] = decoder_1(ConverterOptions__ctor())
    oa_decoder: Decoder_1[OntologyAnnotation] = OntologyAnnotation_decoder(ConverterOptions__ctor())
    def _arrow1760(get: IGetters) -> Template:
        def _arrow1750(__unit: None=None) -> str:
            object_arg: IRequiredGetter = get.Required
            return object_arg.Field("id", guid)

        def _arrow1751(__unit: None=None) -> ArcTable:
            object_arg_1: IRequiredGetter = get.Required
            return object_arg_1.Field("table", ArcTable_decoder)

        def _arrow1752(__unit: None=None) -> str:
            object_arg_2: IRequiredGetter = get.Required
            return object_arg_2.Field("name", string)

        def _arrow1753(__unit: None=None) -> str:
            object_arg_3: IRequiredGetter = get.Required
            return object_arg_3.Field("description", string)

        def _arrow1754(__unit: None=None) -> Organisation:
            object_arg_4: IRequiredGetter = get.Required
            return object_arg_4.Field("organisation", Organisation_decode)

        def _arrow1755(__unit: None=None) -> str:
            object_arg_5: IRequiredGetter = get.Required
            return object_arg_5.Field("version", string)

        def _arrow1756(__unit: None=None) -> Array[Person]:
            arg_13: Decoder_1[Array[Person]] = array_1(person_decoder)
            object_arg_6: IRequiredGetter = get.Required
            return object_arg_6.Field("authors", arg_13)

        def _arrow1757(__unit: None=None) -> Array[OntologyAnnotation]:
            arg_15: Decoder_1[Array[OntologyAnnotation]] = array_1(oa_decoder)
            object_arg_7: IRequiredGetter = get.Required
            return object_arg_7.Field("endpoint_repositories", arg_15)

        def _arrow1758(__unit: None=None) -> Array[OntologyAnnotation]:
            arg_17: Decoder_1[Array[OntologyAnnotation]] = array_1(oa_decoder)
            object_arg_8: IRequiredGetter = get.Required
            return object_arg_8.Field("tags", arg_17)

        def _arrow1759(__unit: None=None) -> Any:
            object_arg_9: IRequiredGetter = get.Required
            return object_arg_9.Field("last_updated", datetime_local)

        return Template.create(_arrow1750(), _arrow1751(), _arrow1752(), _arrow1753(), _arrow1754(), _arrow1755(), _arrow1756(), _arrow1757(), _arrow1758(), _arrow1759())

    return object(_arrow1760)


Template_decode: Decoder_1[Template] = _arrow1761()

def Template_fromJsonString(json_string: str) -> Template:
    try: 
        match_value: FSharpResult_2[Template, str] = Decode_fromString(Template_decode, json_string)
        if match_value.tag == 1:
            raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

        else: 
            return match_value.fields[0]


    except Exception as exn:
        return to_fail(printf("Error. Given json string cannot be parsed to Template: %A"))(exn)



def Template_toJsonString(spaces: int, template: Template) -> str:
    return to_string_2(spaces, Template_encode(template))


def Templates_encode(template_list: Array[tuple[str, Template]]) -> Json:
    def mapping(tupled_arg: tuple[str, Template], template_list: Any=template_list) -> tuple[str, Json]:
        return (tupled_arg[0], Template_encode(tupled_arg[1]))

    return Json(5, map_1(mapping, of_array(template_list)))


Templates_decode: Decoder_1[Any] = dict_1(Template_decode)

def Templates_fromJsonString(json_string: str) -> Any:
    try: 
        match_value: FSharpResult_2[Any, str] = Decode_fromString(Templates_decode, json_string)
        if match_value.tag == 1:
            raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

        else: 
            return match_value.fields[0]


    except Exception as exn:
        return to_fail(printf("Error. Given json string cannot be parsed to Templates map: %A"))(exn)



def Templates_toJsonString(spaces: int, template_list: Array[tuple[str, Template]]) -> str:
    return to_string_2(spaces, Templates_encode(template_list))


def ARCtrl_Template_Template__Template_ToJson_71136F3F(this: Template, spaces: int | None=None) -> Callable[[Template], str]:
    spaces_1: int = default_arg(spaces, 0) or 0
    def _arrow1762(template: Template, this: Any=this, spaces: Any=spaces) -> str:
        return Template_toJsonString(spaces_1, template)

    return _arrow1762


__all__ = ["Organisation_encode", "Organisation_decode", "Template_encode", "Template_decode", "Template_fromJsonString", "Template_toJsonString", "Templates_encode", "Templates_decode", "Templates_fromJsonString", "Templates_toJsonString", "ARCtrl_Template_Template__Template_ToJson_71136F3F"]

