from __future__ import annotations
from typing import Any
from ...fable_modules.fable_library.array_ import try_pick
from ...fable_modules.fable_library.list import (choose, of_array, FSharpList)
from ...fable_modules.fable_library.result import FSharpResult_2
from ...fable_modules.fable_library.seq import (to_list, delay, append, singleton, empty)
from ...fable_modules.fable_library.string_ import (replace, to_text, printf)
from ...fable_modules.fable_library.types import Array
from ...fable_modules.fable_library.util import (IEnumerable_1, equals)
from ...fable_modules.thoth_json_core.decode import (IOptionalGetter, string, array as array_1, IGetters)
from ...fable_modules.thoth_json_core.types import (Json, Decoder_1)
from ...fable_modules.thoth_json_python.decode import Decode_fromString
from ...fable_modules.thoth_json_python.encode import to_string
from ..ISA.JsonTypes.comment import Comment
from ..ISA.JsonTypes.ontology_annotation import OntologyAnnotation
from ..ISA.JsonTypes.person import Person
from ..ISA.JsonTypes.uri import URIModule_toString
from ..ISA_Json.comment import (encoder as encoder_1, decoder as decoder_2)
from ..ISA_Json.context.rocrate.isa_organization_context import context_jsonvalue
from ..ISA_Json.context.rocrate.isa_person_context import context_jsonvalue as context_jsonvalue_1
from ..ISA_Json.converter_options import (ConverterOptions__get_IsRoCrate, ConverterOptions__get_IncludeContext, ConverterOptions, ConverterOptions__get_SetID, ConverterOptions__get_IncludeType, ConverterOptions__ctor, ConverterOptions__set_SetID_Z1FBCCD16, ConverterOptions__set_IncludeType_Z1FBCCD16, ConverterOptions__set_IncludeContext_Z1FBCCD16)
from ..ISA_Json.decode import (object, uri)
from ..ISA_Json.gencode import (try_include, try_include_array)
from ..ISA_Json.ontology import (OntologyAnnotation_encoder, OntologyAnnotation_decoder)

def gen_id(p: Person) -> str:
    match_value: str | None = p.ID
    if match_value is None:
        orcid: str | None
        match_value_1: Array[Comment] | None = p.Comments
        def chooser(c: Comment, p: Any=p) -> str | None:
            matchValue: str | None = c.Name
            matchValue_1: str | None = c.Value
            (pattern_matching_result, n, v) = (None, None, None)
            if matchValue is not None:
                if matchValue_1 is not None:
                    pattern_matching_result = 0
                    n = matchValue
                    v = matchValue_1

                else: 
                    pattern_matching_result = 1


            else: 
                pattern_matching_result = 1

            if pattern_matching_result == 0:
                if True if (True if (n == "orcid") else (n == "Orcid")) else (n == "ORCID"):
                    return v

                else: 
                    return None


            elif pattern_matching_result == 1:
                return None


        orcid = None if (match_value_1 is None) else try_pick(chooser, match_value_1)
        if orcid is None:
            match_value_3: str | None = p.EMail
            if match_value_3 is None:
                matchValue_2: str | None = p.FirstName
                matchValue_3: str | None = p.MidInitials
                matchValue_4: str | None = p.LastName
                (pattern_matching_result_1, fn, ln, mn, fn_1, ln_1, ln_2, fn_2) = (None, None, None, None, None, None, None, None)
                if matchValue_2 is None:
                    if matchValue_3 is None:
                        if matchValue_4 is not None:
                            pattern_matching_result_1 = 2
                            ln_2 = matchValue_4

                        else: 
                            pattern_matching_result_1 = 4


                    else: 
                        pattern_matching_result_1 = 4


                elif matchValue_3 is None:
                    if matchValue_4 is None:
                        pattern_matching_result_1 = 3
                        fn_2 = matchValue_2

                    else: 
                        pattern_matching_result_1 = 1
                        fn_1 = matchValue_2
                        ln_1 = matchValue_4


                elif matchValue_4 is not None:
                    pattern_matching_result_1 = 0
                    fn = matchValue_2
                    ln = matchValue_4
                    mn = matchValue_3

                else: 
                    pattern_matching_result_1 = 4

                if pattern_matching_result_1 == 0:
                    return (((("#" + replace(fn, " ", "_")) + "_") + replace(mn, " ", "_")) + "_") + replace(ln, " ", "_")

                elif pattern_matching_result_1 == 1:
                    return (("#" + replace(fn_1, " ", "_")) + "_") + replace(ln_1, " ", "_")

                elif pattern_matching_result_1 == 2:
                    return "#" + replace(ln_2, " ", "_")

                elif pattern_matching_result_1 == 3:
                    return "#" + replace(fn_2, " ", "_")

                elif pattern_matching_result_1 == 4:
                    return "#EmptyPerson"


            else: 
                return match_value_3


        else: 
            return orcid


    else: 
        return URIModule_toString(match_value)



def affiliation_encoder(options: ConverterOptions, affiliation: str) -> Json:
    if ConverterOptions__get_IsRoCrate(options):
        def _arrow1333(__unit: None=None, options: Any=options, affiliation: Any=affiliation) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1332(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1331(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1330(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        return singleton(("@context", context_jsonvalue)) if ConverterOptions__get_IncludeContext(options) else empty()

                    return append(singleton(("name", Json(0, affiliation))), delay(_arrow1330))

                return append(singleton(("@id", Json(0, ("Organization/" + affiliation) + ""))), delay(_arrow1331))

            return append(singleton(("@type", Json(0, "Organization"))), delay(_arrow1332))

        return Json(5, to_list(delay(_arrow1333)))

    else: 
        return Json(0, affiliation)



def encoder(options: ConverterOptions, oa: Person) -> Json:
    oa_1: Person = Person.set_comment_from_orcid(oa)
    def chooser(tupled_arg: tuple[str, Json], options: Any=options, oa: Any=oa) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1357(__unit: None=None, options: Any=options, oa: Any=oa) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1334(value_1: str) -> Json:
            return Json(0, value_1)

        def _arrow1356(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1355(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1335(value_4: str) -> Json:
                    return Json(0, value_4)

                def _arrow1354(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1336(value_6: str) -> Json:
                        return Json(0, value_6)

                    def _arrow1353(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        def _arrow1337(value_8: str) -> Json:
                            return Json(0, value_8)

                        def _arrow1352(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                            def _arrow1338(value_10: str) -> Json:
                                return Json(0, value_10)

                            def _arrow1351(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                def _arrow1339(value_12: str) -> Json:
                                    return Json(0, value_12)

                                def _arrow1350(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                    def _arrow1340(value_14: str) -> Json:
                                        return Json(0, value_14)

                                    def _arrow1349(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                        def _arrow1341(value_16: str) -> Json:
                                            return Json(0, value_16)

                                        def _arrow1348(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                            def _arrow1342(affiliation: str) -> Json:
                                                return affiliation_encoder(options, affiliation)

                                            def _arrow1347(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                def _arrow1343(oa_2: OntologyAnnotation) -> Json:
                                                    return OntologyAnnotation_encoder(options, oa_2)

                                                def _arrow1346(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                    def _arrow1344(comment: Comment) -> Json:
                                                        return encoder_1(options, comment)

                                                    def _arrow1345(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                        return singleton(("@context", context_jsonvalue_1)) if ConverterOptions__get_IncludeContext(options) else empty()

                                                    return append(singleton(try_include_array("comments", _arrow1344, oa_1.Comments)), delay(_arrow1345))

                                                return append(singleton(try_include_array("roles", _arrow1343, oa_1.Roles)), delay(_arrow1346))

                                            return append(singleton(try_include("affiliation", _arrow1342, oa_1.Affiliation)), delay(_arrow1347))

                                        return append(singleton(try_include("address", _arrow1341, oa_1.Address)), delay(_arrow1348))

                                    return append(singleton(try_include("fax", _arrow1340, oa_1.Fax)), delay(_arrow1349))

                                return append(singleton(try_include("phone", _arrow1339, oa_1.Phone)), delay(_arrow1350))

                            return append(singleton(try_include("email", _arrow1338, oa_1.EMail)), delay(_arrow1351))

                        return append(singleton(try_include("midInitials", _arrow1337, oa_1.MidInitials)), delay(_arrow1352))

                    return append(singleton(try_include("lastName", _arrow1336, oa_1.LastName)), delay(_arrow1353))

                return append(singleton(try_include("firstName", _arrow1335, oa_1.FirstName)), delay(_arrow1354))

            return append(singleton(("@type", Json(0, "Person"))) if ConverterOptions__get_IncludeType(options) else empty(), delay(_arrow1355))

        return append(singleton(("@id", Json(0, gen_id(oa_1)))) if ConverterOptions__get_SetID(options) else singleton(try_include("@id", _arrow1334, oa_1.ID)), delay(_arrow1356))

    return Json(5, choose(chooser, to_list(delay(_arrow1357))))


allowed_fields: FSharpList[str] = of_array(["@id", "firstName", "lastName", "midInitials", "email", "phone", "fax", "address", "affiliation", "roles", "comments", "@type", "@context"])

def decoder(options: ConverterOptions) -> Decoder_1[Person]:
    def _arrow1367(get: IGetters, options: Any=options) -> Person:
        person: Person
        ID: str | None
        object_arg: IOptionalGetter = get.Optional
        ID = object_arg.Field("@id", uri)
        FirstName: str | None
        object_arg_1: IOptionalGetter = get.Optional
        FirstName = object_arg_1.Field("firstName", string)
        def _arrow1358(__unit: None=None) -> str | None:
            object_arg_2: IOptionalGetter = get.Optional
            return object_arg_2.Field("lastName", string)

        def _arrow1359(__unit: None=None) -> str | None:
            object_arg_3: IOptionalGetter = get.Optional
            return object_arg_3.Field("midInitials", string)

        def _arrow1360(__unit: None=None) -> str | None:
            object_arg_4: IOptionalGetter = get.Optional
            return object_arg_4.Field("email", string)

        def _arrow1361(__unit: None=None) -> str | None:
            object_arg_5: IOptionalGetter = get.Optional
            return object_arg_5.Field("phone", string)

        def _arrow1362(__unit: None=None) -> str | None:
            object_arg_6: IOptionalGetter = get.Optional
            return object_arg_6.Field("fax", string)

        def _arrow1363(__unit: None=None) -> str | None:
            object_arg_7: IOptionalGetter = get.Optional
            return object_arg_7.Field("address", string)

        def _arrow1364(__unit: None=None) -> str | None:
            object_arg_8: IOptionalGetter = get.Optional
            return object_arg_8.Field("affiliation", string)

        def _arrow1365(__unit: None=None) -> Array[OntologyAnnotation] | None:
            arg_19: Decoder_1[Array[OntologyAnnotation]] = array_1(OntologyAnnotation_decoder(options))
            object_arg_9: IOptionalGetter = get.Optional
            return object_arg_9.Field("roles", arg_19)

        def _arrow1366(__unit: None=None) -> Array[Comment] | None:
            arg_21: Decoder_1[Array[Comment]] = array_1(decoder_2(options))
            object_arg_10: IOptionalGetter = get.Optional
            return object_arg_10.Field("comments", arg_21)

        person = Person(ID, None, _arrow1358(), FirstName, _arrow1359(), _arrow1360(), _arrow1361(), _arrow1362(), _arrow1363(), _arrow1364(), _arrow1365(), _arrow1366())
        return Person.set_orcid_from_comments(person)

    return object(allowed_fields, _arrow1367)


def from_json_string(s: str) -> Person:
    match_value: FSharpResult_2[Person, str] = Decode_fromString(decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def to_json_string(p: Person) -> str:
    return to_string(2, encoder(ConverterOptions__ctor(), p))


def to_jsonld_string(p: Person) -> str:
    def _arrow1368(__unit: None=None, p: Any=p) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, encoder(_arrow1368(), p))


def to_jsonld_string_with_context(a: Person) -> str:
    def _arrow1369(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, encoder(_arrow1369(), a))


__all__ = ["gen_id", "affiliation_encoder", "encoder", "allowed_fields", "decoder", "from_json_string", "to_json_string", "to_jsonld_string", "to_jsonld_string_with_context"]

