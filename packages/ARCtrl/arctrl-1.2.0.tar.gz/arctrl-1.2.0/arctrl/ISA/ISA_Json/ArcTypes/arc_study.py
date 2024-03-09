from __future__ import annotations
from collections.abc import Callable
from typing import Any
from ....fable_modules.fable_library.mutable_map import Dictionary
from ....fable_modules.fable_library.option import (value as value_7, default_arg, map as map_1)
from ....fable_modules.fable_library.result import FSharpResult_2
from ....fable_modules.fable_library.seq import (to_list, delay, append, singleton, empty, map)
from ....fable_modules.fable_library.string_ import (to_text, printf, to_fail)
from ....fable_modules.fable_library.types import Array
from ....fable_modules.fable_library.util import (IEnumerable_1, equals, safe_hash, to_enumerable)
from ....fable_modules.thoth_json_core.decode import (object, IRequiredGetter, string, IOptionalGetter, IGetters, array)
from ....fable_modules.thoth_json_core.encode import seq
from ....fable_modules.thoth_json_core.types import (Json, Decoder_1)
from ....fable_modules.thoth_json_python.decode import Decode_fromString
from ....fable_modules.thoth_json_python.encode import to_string
from ...ISA.ArcTypes.arc_table import ArcTable
from ...ISA.ArcTypes.arc_types import (ArcStudy, ArcAssay)
from ...ISA.ArcTypes.composite_cell import CompositeCell
from ...ISA.JsonTypes.comment import Comment
from ...ISA.JsonTypes.factor import Factor
from ...ISA.JsonTypes.ontology_annotation import OntologyAnnotation
from ...ISA.JsonTypes.person import Person
from ...ISA.JsonTypes.publication import Publication
from ...ISA.JsonTypes.study import Study
from ...ISA_Json.converter_options import (ConverterOptions__ctor, ConverterOptions, ConverterOptions__set_SetID_Z1FBCCD16, ConverterOptions__set_IncludeType_Z1FBCCD16, ConverterOptions__set_IncludeContext_Z1FBCCD16)
from ...ISA_Json.string_table import (StringTable_decoder, StringTable_encoder, StringTable_arrayFromMap)
from ...ISA_Json.study import (Study_encoder, Study_decoder)
from ...ISA_Json.ArcTypes.arc_assay import (JsonHelper_EncoderPublications, JsonHelper_EncoderPersons, JsonHelper_EncoderOAs, JsonHelper_EncoderTables, JsonHelper_EncoderFactors, JsonHelper_EncoderComments, JsonHelper_tryGetPublications, JsonHelper_tryGetPersons, JsonHelper_tryGetOAs, JsonHelper_tryGetTables, JsonHelper_tryGetStringResizeArray, JsonHelper_tryGetFactors, JsonHelper_tryGetComments)
from ...ISA_Json.ArcTypes.arc_table import (ArcTable_compressedEncoder, ArcTable_compressedDecoder)
from ...ISA_Json.ArcTypes.cell_table import (CellTable_decoder, CellTable_encoder, CellTable_arrayFromMap)
from ...ISA_Json.ArcTypes.oatable import (OATable_decoder, OATable_encoder, OATable_arrayFromMap)

def ArcStudy_encoder(study: ArcStudy) -> Json:
    def _arrow1642(__unit: None=None, study: Any=study) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1641(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1640(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1639(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1638(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        def _arrow1637(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                            def _arrow1636(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                def _arrow1635(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                    def _arrow1634(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                        def _arrow1633(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                            def _arrow1630(value_5: str) -> Json:
                                                return Json(0, value_5)

                                            def _arrow1632(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                def _arrow1631(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                    return singleton(("Comments", JsonHelper_EncoderComments(study.Comments))) if (len(study.Comments) != 0) else empty()

                                                return append(singleton(("Factors", JsonHelper_EncoderFactors(study.Factors))) if (len(study.Factors) != 0) else empty(), delay(_arrow1631))

                                            return append(singleton(("RegisteredAssayIdentifiers", seq(map(_arrow1630, study.RegisteredAssayIdentifiers)))) if (len(study.RegisteredAssayIdentifiers) != 0) else empty(), delay(_arrow1632))

                                        return append(singleton(("Tables", JsonHelper_EncoderTables(study.Tables))) if (study.TableCount != 0) else empty(), delay(_arrow1633))

                                    return append(singleton(("StudyDesignDescriptors", JsonHelper_EncoderOAs(study.StudyDesignDescriptors))) if (len(study.StudyDesignDescriptors) != 0) else empty(), delay(_arrow1634))

                                return append(singleton(("Contacts", JsonHelper_EncoderPersons(study.Contacts))) if (len(study.Contacts) != 0) else empty(), delay(_arrow1635))

                            return append(singleton(("Publications", JsonHelper_EncoderPublications(study.Publications))) if (len(study.Publications) != 0) else empty(), delay(_arrow1636))

                        return append(singleton(("PublicReleaseDate", Json(0, value_7(study.PublicReleaseDate)))) if (study.PublicReleaseDate is not None) else empty(), delay(_arrow1637))

                    return append(singleton(("SubmissionDate", Json(0, value_7(study.SubmissionDate)))) if (study.SubmissionDate is not None) else empty(), delay(_arrow1638))

                return append(singleton(("Description", Json(0, value_7(study.Description)))) if (study.Description is not None) else empty(), delay(_arrow1639))

            return append(singleton(("Title", Json(0, value_7(study.Title)))) if (study.Title is not None) else empty(), delay(_arrow1640))

        return append(singleton(("Identifier", Json(0, study.Identifier))), delay(_arrow1641))

    return Json(5, to_list(delay(_arrow1642)))


def _arrow1643(get: IGetters) -> ArcStudy:
    identifier: str
    object_arg: IRequiredGetter = get.Required
    identifier = object_arg.Field("Identifier", string)
    title: str | None
    object_arg_1: IOptionalGetter = get.Optional
    title = object_arg_1.Field("Title", string)
    description: str | None
    object_arg_2: IOptionalGetter = get.Optional
    description = object_arg_2.Field("Description", string)
    submission_date: str | None
    object_arg_3: IOptionalGetter = get.Optional
    submission_date = object_arg_3.Field("SubmissionDate", string)
    public_release_date: str | None
    object_arg_4: IOptionalGetter = get.Optional
    public_release_date = object_arg_4.Field("PublicReleaseDate", string)
    publications: Array[Publication] = JsonHelper_tryGetPublications(get, "Publications")
    contacts: Array[Person] = JsonHelper_tryGetPersons(get, "Contacts")
    study_design_descriptors: Array[OntologyAnnotation] = JsonHelper_tryGetOAs(get, "StudyDesignDescriptors")
    tables: Array[ArcTable] = JsonHelper_tryGetTables(get, "Tables")
    registered_assay_identifiers: Array[str] = JsonHelper_tryGetStringResizeArray(get, "RegisteredAssayIdentifiers")
    factors: Array[Factor] = JsonHelper_tryGetFactors(get, "Factors")
    comments: Array[Comment] = JsonHelper_tryGetComments(get, "Comments")
    return ArcStudy.make(identifier, title, description, submission_date, public_release_date, publications, contacts, study_design_descriptors, tables, registered_assay_identifiers, factors, comments)


ArcStudy_decoder: Decoder_1[ArcStudy] = object(_arrow1643)

def ArcStudy_compressedEncoder(string_table: Any, oa_table: Any, cell_table: Any, study: ArcStudy) -> Json:
    def _arrow1657(__unit: None=None, string_table: Any=string_table, oa_table: Any=oa_table, cell_table: Any=cell_table, study: Any=study) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1656(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1655(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1654(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1653(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        def _arrow1652(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                            def _arrow1651(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                def _arrow1650(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                    def _arrow1649(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                        def _arrow1644(table: ArcTable) -> Json:
                                            return ArcTable_compressedEncoder(string_table, oa_table, cell_table, table)

                                        def _arrow1648(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                            def _arrow1645(value_5: str) -> Json:
                                                return Json(0, value_5)

                                            def _arrow1647(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                def _arrow1646(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                                    return singleton(("Comments", JsonHelper_EncoderComments(study.Comments))) if (len(study.Comments) != 0) else empty()

                                                return append(singleton(("Factors", JsonHelper_EncoderFactors(study.Factors))) if (len(study.Factors) != 0) else empty(), delay(_arrow1646))

                                            return append(singleton(("RegisteredAssayIdentifiers", seq(map(_arrow1645, study.RegisteredAssayIdentifiers)))) if (len(study.RegisteredAssayIdentifiers) != 0) else empty(), delay(_arrow1647))

                                        return append(singleton(("Tables", seq(map(_arrow1644, study.Tables)))) if (study.TableCount != 0) else empty(), delay(_arrow1648))

                                    return append(singleton(("StudyDesignDescriptors", JsonHelper_EncoderOAs(study.StudyDesignDescriptors))) if (len(study.StudyDesignDescriptors) != 0) else empty(), delay(_arrow1649))

                                return append(singleton(("Contacts", JsonHelper_EncoderPersons(study.Contacts))) if (len(study.Contacts) != 0) else empty(), delay(_arrow1650))

                            return append(singleton(("Publications", JsonHelper_EncoderPublications(study.Publications))) if (len(study.Publications) != 0) else empty(), delay(_arrow1651))

                        return append(singleton(("PublicReleaseDate", Json(0, value_7(study.PublicReleaseDate)))) if (study.PublicReleaseDate is not None) else empty(), delay(_arrow1652))

                    return append(singleton(("SubmissionDate", Json(0, value_7(study.SubmissionDate)))) if (study.SubmissionDate is not None) else empty(), delay(_arrow1653))

                return append(singleton(("Description", Json(0, value_7(study.Description)))) if (study.Description is not None) else empty(), delay(_arrow1654))

            return append(singleton(("Title", Json(0, value_7(study.Title)))) if (study.Title is not None) else empty(), delay(_arrow1655))

        return append(singleton(("Identifier", Json(0, study.Identifier))), delay(_arrow1656))

    return Json(5, to_list(delay(_arrow1657)))


def ArcStudy_compressedDecoder(string_table: Array[str], oa_table: Array[OntologyAnnotation], cell_table: Array[CompositeCell]) -> Decoder_1[ArcStudy]:
    def _arrow1659(get: IGetters, string_table: Any=string_table, oa_table: Any=oa_table, cell_table: Any=cell_table) -> ArcStudy:
        def _arrow1658(__unit: None=None) -> Array[ArcTable] | None:
            arg_1: Decoder_1[Array[ArcTable]] = array(ArcTable_compressedDecoder(string_table, oa_table, cell_table))
            object_arg: IOptionalGetter = get.Optional
            return object_arg.Field("Tables", arg_1)

        tables: Array[ArcTable] = default_arg(map_1(list, _arrow1658()), [])
        identifier: str
        object_arg_1: IRequiredGetter = get.Required
        identifier = object_arg_1.Field("Identifier", string)
        title: str | None
        object_arg_2: IOptionalGetter = get.Optional
        title = object_arg_2.Field("Title", string)
        description: str | None
        object_arg_3: IOptionalGetter = get.Optional
        description = object_arg_3.Field("Description", string)
        submission_date: str | None
        object_arg_4: IOptionalGetter = get.Optional
        submission_date = object_arg_4.Field("SubmissionDate", string)
        public_release_date: str | None
        object_arg_5: IOptionalGetter = get.Optional
        public_release_date = object_arg_5.Field("PublicReleaseDate", string)
        publications: Array[Publication] = JsonHelper_tryGetPublications(get, "Publications")
        contacts: Array[Person] = JsonHelper_tryGetPersons(get, "Contacts")
        study_design_descriptors: Array[OntologyAnnotation] = JsonHelper_tryGetOAs(get, "StudyDesignDescriptors")
        registered_assay_identifiers: Array[str] = JsonHelper_tryGetStringResizeArray(get, "RegisteredAssayIdentifiers")
        factors: Array[Factor] = JsonHelper_tryGetFactors(get, "Factors")
        comments: Array[Comment] = JsonHelper_tryGetComments(get, "Comments")
        return ArcStudy.make(identifier, title, description, submission_date, public_release_date, publications, contacts, study_design_descriptors, tables, registered_assay_identifiers, factors, comments)

    return object(_arrow1659)


def ArcStudy_toJsonldString(a: ArcStudy, assays: Array[ArcAssay]) -> str:
    def _arrow1660(__unit: None=None, a: Any=a, assays: Any=assays) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, Study_encoder(_arrow1660(), a.ToStudy(assays)))


def ArcStudy_toJsonldStringWithContext(a: ArcStudy, assays: Array[ArcAssay]) -> str:
    def _arrow1661(__unit: None=None, a: Any=a, assays: Any=assays) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, Study_encoder(_arrow1661(), a.ToStudy(assays)))


def ArcStudy_fromJsonString(s: str) -> tuple[ArcStudy, Array[ArcAssay]]:
    s_2: Study
    match_value: FSharpResult_2[Study, str] = Decode_fromString(Study_decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        s_2 = match_value.fields[0]

    return ArcStudy.from_study(s_2)


def ArcStudy_toJsonString(a: ArcStudy, assays: Array[ArcAssay]) -> str:
    return to_string(2, Study_encoder(ConverterOptions__ctor(), a.ToStudy(assays)))


def ArcStudy_toArcJsonString(a: ArcStudy) -> str:
    return to_string(0, ArcStudy_encoder(a))


def ArcStudy_fromArcJsonString(json_string: str) -> ArcStudy:
    try: 
        match_value: FSharpResult_2[ArcStudy, str] = Decode_fromString(ArcStudy_decoder, json_string)
        if match_value.tag == 1:
            raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

        else: 
            return match_value.fields[0]


    except Exception as e_1:
        arg_1: str = str(e_1)
        return to_fail(printf("Error. Unable to parse json string to ArcStudy: %s"))(arg_1)



def ARCtrl_ISA_ArcStudy__ArcStudy_fromArcJsonString_Static_Z721C83C5(json_string: str) -> ArcStudy:
    try: 
        match_value: FSharpResult_2[ArcStudy, str] = Decode_fromString(ArcStudy_decoder, json_string)
        if match_value.tag == 1:
            raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

        else: 
            return match_value.fields[0]


    except Exception as e_1:
        arg_1: str = str(e_1)
        return to_fail(printf("Error. Unable to parse json string to ArcStudy: %s"))(arg_1)



def ARCtrl_ISA_ArcStudy__ArcStudy_ToArcJsonString_71136F3F(this: ArcStudy, spaces: int | None=None) -> str:
    return to_string(default_arg(spaces, 0), ArcStudy_encoder(this))


def ARCtrl_ISA_ArcStudy__ArcStudy_toArcJsonString_Static_1B3D5E9B(a: ArcStudy) -> str:
    return ARCtrl_ISA_ArcStudy__ArcStudy_ToArcJsonString_71136F3F(a)


def ARCtrl_ISA_ArcStudy__ArcStudy_fromCompressedJsonString_Static_Z721C83C5(json_string: str) -> ArcStudy:
    def _arrow1666(get: IGetters, json_string: Any=json_string) -> ArcStudy:
        string_table: Array[str]
        object_arg: IRequiredGetter = get.Required
        string_table = object_arg.Field("stringTable", StringTable_decoder)
        oa_table: Array[OntologyAnnotation]
        arg_3: Decoder_1[Array[OntologyAnnotation]] = OATable_decoder(string_table)
        object_arg_1: IRequiredGetter = get.Required
        oa_table = object_arg_1.Field("oaTable", arg_3)
        def _arrow1665(__unit: None=None) -> Array[CompositeCell]:
            arg_5: Decoder_1[Array[CompositeCell]] = CellTable_decoder(string_table, oa_table)
            object_arg_2: IRequiredGetter = get.Required
            return object_arg_2.Field("cellTable", arg_5)

        arg_7: Decoder_1[ArcStudy] = ArcStudy_compressedDecoder(string_table, oa_table, _arrow1665())
        object_arg_3: IRequiredGetter = get.Required
        return object_arg_3.Field("study", arg_7)

    decoder: Decoder_1[ArcStudy] = object(_arrow1666)
    try: 
        match_value: FSharpResult_2[ArcStudy, str] = Decode_fromString(decoder, json_string)
        if match_value.tag == 1:
            raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

        else: 
            return match_value.fields[0]


    except Exception as e_1:
        arg_9: str = str(e_1)
        return to_fail(printf("Error. Unable to parse json string to ArcAssay: %s"))(arg_9)



def ARCtrl_ISA_ArcStudy__ArcStudy_ToCompressedJsonString_71136F3F(this: ArcStudy, spaces: int | None=None) -> str:
    spaces_1: int = default_arg(spaces, 0) or 0
    string_table: Any = dict([])
    class ObjectExpr1667:
        @property
        def Equals(self) -> Callable[[OntologyAnnotation, OntologyAnnotation], bool]:
            return equals

        @property
        def GetHashCode(self) -> Callable[[OntologyAnnotation], int]:
            return safe_hash

    oa_table: Any = Dictionary([], ObjectExpr1667())
    class ObjectExpr1668:
        @property
        def Equals(self) -> Callable[[CompositeCell, CompositeCell], bool]:
            return equals

        @property
        def GetHashCode(self) -> Callable[[CompositeCell], int]:
            return safe_hash

    cell_table: Any = Dictionary([], ObjectExpr1668())
    arc_study: Json = ArcStudy_compressedEncoder(string_table, oa_table, cell_table, this)
    return to_string(spaces_1, Json(5, to_enumerable([("cellTable", CellTable_encoder(string_table, oa_table, CellTable_arrayFromMap(cell_table))), ("oaTable", OATable_encoder(string_table, OATable_arrayFromMap(oa_table))), ("stringTable", StringTable_encoder(StringTable_arrayFromMap(string_table))), ("study", arc_study)])))


def ARCtrl_ISA_ArcStudy__ArcStudy_toCompressedJsonString_Static_1B3D5E9B(s: ArcStudy) -> str:
    return ARCtrl_ISA_ArcStudy__ArcStudy_ToCompressedJsonString_71136F3F(s)


__all__ = ["ArcStudy_encoder", "ArcStudy_decoder", "ArcStudy_compressedEncoder", "ArcStudy_compressedDecoder", "ArcStudy_toJsonldString", "ArcStudy_toJsonldStringWithContext", "ArcStudy_fromJsonString", "ArcStudy_toJsonString", "ArcStudy_toArcJsonString", "ArcStudy_fromArcJsonString", "ARCtrl_ISA_ArcStudy__ArcStudy_fromArcJsonString_Static_Z721C83C5", "ARCtrl_ISA_ArcStudy__ArcStudy_ToArcJsonString_71136F3F", "ARCtrl_ISA_ArcStudy__ArcStudy_toArcJsonString_Static_1B3D5E9B", "ARCtrl_ISA_ArcStudy__ArcStudy_fromCompressedJsonString_Static_Z721C83C5", "ARCtrl_ISA_ArcStudy__ArcStudy_ToCompressedJsonString_71136F3F", "ARCtrl_ISA_ArcStudy__ArcStudy_toCompressedJsonString_Static_1B3D5E9B"]

