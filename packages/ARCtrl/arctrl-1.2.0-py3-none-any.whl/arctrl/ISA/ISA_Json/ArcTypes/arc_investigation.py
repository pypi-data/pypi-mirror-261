from __future__ import annotations
from typing import Any
from ....fable_modules.fable_library.list import FSharpList
from ....fable_modules.fable_library.option import (value as value_7, default_arg, map as map_1)
from ....fable_modules.fable_library.result import FSharpResult_2
from ....fable_modules.fable_library.seq import (to_list, delay, append, singleton, empty, map)
from ....fable_modules.fable_library.string_ import (to_text, printf, to_fail)
from ....fable_modules.fable_library.types import Array
from ....fable_modules.fable_library.util import IEnumerable_1
from ....fable_modules.thoth_json_core.decode import (list_1, object, IRequiredGetter, string, IOptionalGetter, IGetters)
from ....fable_modules.thoth_json_core.encode import seq
from ....fable_modules.thoth_json_core.types import (Json, Decoder_1)
from ....fable_modules.thoth_json_python.decode import Decode_fromString
from ....fable_modules.thoth_json_python.encode import to_string
from ...ISA.ArcTypes.arc_types import (ArcAssay, ArcStudy, ArcInvestigation)
from ...ISA.JsonTypes.comment import Comment
from ...ISA.JsonTypes.investigation import Investigation
from ...ISA.JsonTypes.ontology_source_reference import OntologySourceReference
from ...ISA.JsonTypes.person import Person
from ...ISA.JsonTypes.publication import Publication
from ...ISA_Json.converter_options import (ConverterOptions__ctor, ConverterOptions, ConverterOptions__set_SetID_Z1FBCCD16, ConverterOptions__set_IncludeType_Z1FBCCD16, ConverterOptions__set_IncludeContext_Z1FBCCD16)
from ...ISA_Json.investigation import (encoder, decoder as decoder_1)
from ...ISA_Json.ArcTypes.arc_assay import (JsonHelper_EncoderOntologySourceReferences, JsonHelper_EncoderPublications, JsonHelper_EncoderPersons, ArcAssay_encoder, JsonHelper_EncoderComments, ArcAssay_decoder, JsonHelper_tryGetOntologySourceReferences, JsonHelper_tryGetPublications, JsonHelper_tryGetPersons, JsonHelper_tryGetStringResizeArray, JsonHelper_tryGetComments)
from ...ISA_Json.ArcTypes.arc_study import (ArcStudy_encoder, ArcStudy_decoder)

def ArcInvestigation_encoder(inv: ArcInvestigation) -> Json:
    def _arrow1682(__unit: None=None, inv: Any=inv) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1681(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1680(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1679(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1678(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        def _arrow1677(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                            def _arrow1676(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                def _arrow1675(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                    def _arrow1674(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                        def _arrow1673(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                            def _arrow1672(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                def _arrow1670(value_5: str) -> Json:
                                                    return Json(0, value_5)

                                                def _arrow1671(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                    return singleton(("Comments", JsonHelper_EncoderComments(inv.Comments))) if (len(inv.Comments) != 0) else empty()

                                                return append(singleton(("RegisteredStudyIdentifiers", seq(map(_arrow1670, inv.RegisteredStudyIdentifiers)))) if (len(inv.RegisteredStudyIdentifiers) != 0) else empty(), delay(_arrow1671))

                                            return append(singleton(("Studies", seq(map(ArcStudy_encoder, inv.Studies)))) if (len(inv.Studies) != 0) else empty(), delay(_arrow1672))

                                        return append(singleton(("Assays", seq(map(ArcAssay_encoder, inv.Assays)))) if (len(inv.Assays) != 0) else empty(), delay(_arrow1673))

                                    return append(singleton(("Contacts", JsonHelper_EncoderPersons(inv.Contacts))) if (len(inv.Contacts) != 0) else empty(), delay(_arrow1674))

                                return append(singleton(("Publications", JsonHelper_EncoderPublications(inv.Publications))) if (len(inv.Publications) != 0) else empty(), delay(_arrow1675))

                            return append(singleton(("OntologySourceReferences", JsonHelper_EncoderOntologySourceReferences(inv.OntologySourceReferences))) if (len(inv.OntologySourceReferences) != 0) else empty(), delay(_arrow1676))

                        return append(singleton(("PublicReleaseDate", Json(0, value_7(inv.PublicReleaseDate)))) if (inv.PublicReleaseDate is not None) else empty(), delay(_arrow1677))

                    return append(singleton(("SubmissionDate", Json(0, value_7(inv.SubmissionDate)))) if (inv.SubmissionDate is not None) else empty(), delay(_arrow1678))

                return append(singleton(("Description", Json(0, value_7(inv.Description)))) if (inv.Description is not None) else empty(), delay(_arrow1679))

            return append(singleton(("Title", Json(0, value_7(inv.Title)))) if (inv.Title is not None) else empty(), delay(_arrow1680))

        return append(singleton(("Identifier", Json(0, inv.Identifier))), delay(_arrow1681))

    return Json(5, to_list(delay(_arrow1682)))


def _arrow1686(__unit: None=None) -> Decoder_1[ArcInvestigation]:
    DecodeAssays: Decoder_1[FSharpList[ArcAssay]] = list_1(ArcAssay_decoder)
    DecodeStudies: Decoder_1[FSharpList[ArcStudy]] = list_1(ArcStudy_decoder)
    def _arrow1685(get_2: IGetters) -> ArcInvestigation:
        identifier: str
        object_arg_2: IRequiredGetter = get_2.Required
        identifier = object_arg_2.Field("Identifier", string)
        title: str | None
        object_arg_3: IOptionalGetter = get_2.Optional
        title = object_arg_3.Field("Title", string)
        description: str | None
        object_arg_4: IOptionalGetter = get_2.Optional
        description = object_arg_4.Field("Description", string)
        submission_date: str | None
        object_arg_5: IOptionalGetter = get_2.Optional
        submission_date = object_arg_5.Field("SubmissionDate", string)
        public_release_date: str | None
        object_arg_6: IOptionalGetter = get_2.Optional
        public_release_date = object_arg_6.Field("PublicReleaseDate", string)
        ontology_source_references: Array[OntologySourceReference] = JsonHelper_tryGetOntologySourceReferences(get_2, "OntologySourceReferences")
        publications: Array[Publication] = JsonHelper_tryGetPublications(get_2, "Publications")
        contacts: Array[Person] = JsonHelper_tryGetPersons(get_2, "Contacts")
        def _arrow1683(__unit: None=None) -> FSharpList[ArcAssay] | None:
            object_arg: IOptionalGetter = get_2.Optional
            return object_arg.Field("Assays", DecodeAssays)

        assays: Array[ArcAssay] = default_arg(map_1(list, _arrow1683()), [])
        def _arrow1684(__unit: None=None) -> FSharpList[ArcStudy] | None:
            object_arg_1: IOptionalGetter = get_2.Optional
            return object_arg_1.Field("Studies", DecodeStudies)

        studies: Array[ArcStudy] = default_arg(map_1(list, _arrow1684()), [])
        registered_study_identifiers: Array[str] = JsonHelper_tryGetStringResizeArray(get_2, "RegisteredStudyIdentifiers")
        comments: Array[Comment] = JsonHelper_tryGetComments(get_2, "Comments")
        return ArcInvestigation.make(identifier, title, description, submission_date, public_release_date, ontology_source_references, publications, contacts, assays, studies, registered_study_identifiers, comments, [])

    return object(_arrow1685)


ArcInvestigation_decoder: Decoder_1[ArcInvestigation] = _arrow1686()

def ArcInvestigation_toJsonldString(a: ArcInvestigation) -> str:
    def _arrow1687(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, encoder(_arrow1687(), a.ToInvestigation()))


def ArcInvestigation_toJsonldStringWithContext(a: ArcInvestigation) -> str:
    def _arrow1688(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, encoder(_arrow1688(), a.ToInvestigation()))


def ArcInvestigation_fromJsonString(s: str) -> ArcInvestigation:
    i: Investigation
    match_value: FSharpResult_2[Investigation, str] = Decode_fromString(decoder_1(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        i = match_value.fields[0]

    return ArcInvestigation.from_investigation(i)


def ArcInvestigation_toJsonString(a: ArcInvestigation) -> str:
    return to_string(2, encoder(ConverterOptions__ctor(), a.ToInvestigation()))


def ArcInvestigation_toArcJsonString(a: ArcInvestigation) -> str:
    return to_string(0, ArcInvestigation_encoder(a))


def ArcInvestigation_fromArcJsonString(json_string: str) -> ArcInvestigation:
    try: 
        match_value: FSharpResult_2[ArcInvestigation, str] = Decode_fromString(ArcInvestigation_decoder, json_string)
        if match_value.tag == 1:
            raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

        else: 
            return match_value.fields[0]


    except Exception as e_1:
        arg_1: str = str(e_1)
        return to_fail(printf("Error. Unable to parse json string to ArcInvestigation: %s"))(arg_1)



def ARCtrl_ISA_ArcInvestigation__ArcInvestigation_fromArcJsonString_Static_Z721C83C5(json_string: str) -> ArcInvestigation:
    try: 
        match_value: FSharpResult_2[ArcInvestigation, str] = Decode_fromString(ArcInvestigation_decoder, json_string)
        if match_value.tag == 1:
            raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

        else: 
            return match_value.fields[0]


    except Exception as e_1:
        arg_1: str = str(e_1)
        return to_fail(printf("Error. Unable to parse json string to ArcInvestigation: %s"))(arg_1)



def ARCtrl_ISA_ArcInvestigation__ArcInvestigation_ToArcJsonString_71136F3F(this: ArcInvestigation, spaces: int | None=None) -> str:
    return to_string(default_arg(spaces, 0), ArcInvestigation_encoder(this))


def ARCtrl_ISA_ArcInvestigation__ArcInvestigation_toArcJsonString_Static_Z4D87C88C(a: ArcInvestigation) -> str:
    return ARCtrl_ISA_ArcInvestigation__ArcInvestigation_ToArcJsonString_71136F3F(a)


__all__ = ["ArcInvestigation_encoder", "ArcInvestigation_decoder", "ArcInvestigation_toJsonldString", "ArcInvestigation_toJsonldStringWithContext", "ArcInvestigation_fromJsonString", "ArcInvestigation_toJsonString", "ArcInvestigation_toArcJsonString", "ArcInvestigation_fromArcJsonString", "ARCtrl_ISA_ArcInvestigation__ArcInvestigation_fromArcJsonString_Static_Z721C83C5", "ARCtrl_ISA_ArcInvestigation__ArcInvestigation_ToArcJsonString_71136F3F", "ARCtrl_ISA_ArcInvestigation__ArcInvestigation_toArcJsonString_Static_Z4D87C88C"]

