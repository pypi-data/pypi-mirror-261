from __future__ import annotations
from collections.abc import Callable
from typing import Any
from ....fable_modules.fable_library.list import (FSharpList, to_array)
from ....fable_modules.fable_library.mutable_map import Dictionary
from ....fable_modules.fable_library.option import (default_arg, map, value as value_2)
from ....fable_modules.fable_library.result import FSharpResult_2
from ....fable_modules.fable_library.seq import (map as map_1, to_list, delay, append, singleton, empty)
from ....fable_modules.fable_library.string_ import (to_text, printf, to_fail)
from ....fable_modules.fable_library.types import Array
from ....fable_modules.fable_library.util import (IEnumerable_1, equals, safe_hash, to_enumerable)
from ....fable_modules.thoth_json_core.decode import (list_1 as list_1_1, IOptionalGetter, IGetters, string, object, IRequiredGetter, array)
from ....fable_modules.thoth_json_core.encode import seq
from ....fable_modules.thoth_json_core.types import (Decoder_1, Json)
from ....fable_modules.thoth_json_python.decode import Decode_fromString
from ....fable_modules.thoth_json_python.encode import to_string
from ...ISA.ArcTypes.arc_table import ArcTable
from ...ISA.ArcTypes.arc_types import ArcAssay
from ...ISA.ArcTypes.composite_cell import CompositeCell
from ...ISA.JsonTypes.assay import Assay
from ...ISA.JsonTypes.comment import Comment
from ...ISA.JsonTypes.factor import Factor
from ...ISA.JsonTypes.ontology_annotation import OntologyAnnotation
from ...ISA.JsonTypes.ontology_source_reference import OntologySourceReference
from ...ISA.JsonTypes.person import Person
from ...ISA.JsonTypes.publication import Publication
from ...ISA_Json.assay import (Assay_encoder, Assay_decoder)
from ...ISA_Json.comment import (decoder as decoder_3, encoder as encoder_1)
from ...ISA_Json.converter_options import (ConverterOptions__ctor, ConverterOptions, ConverterOptions__set_SetID_Z1FBCCD16, ConverterOptions__set_IncludeType_Z1FBCCD16, ConverterOptions__set_IncludeContext_Z1FBCCD16)
from ...ISA_Json.factor import (Factor_decoder, Factor_encoder)
from ...ISA_Json.ontology import (OntologyAnnotation_decoder, OntologySourceReference_decoder, OntologyAnnotation_encoder, OntologySourceReference_encoder)
from ...ISA_Json.person import (decoder as decoder_2, encoder)
from ...ISA_Json.publication import (decoder as decoder_4, encoder as encoder_2)
from ...ISA_Json.string_table import (StringTable_decoder, StringTable_encoder, StringTable_arrayFromMap)
from ...ISA_Json.ArcTypes.arc_table import (ArcTable_decoder, ArcTable_encoder, ArcTable_compressedEncoder, ArcTable_compressedDecoder)
from ...ISA_Json.ArcTypes.cell_table import (CellTable_decoder, CellTable_encoder, CellTable_arrayFromMap)
from ...ISA_Json.ArcTypes.oatable import (OATable_encodeOA, OATable_decodeOA, OATable_decoder, OATable_encoder, OATable_arrayFromMap)

JsonHelper_DecodeOa: Decoder_1[OntologyAnnotation] = OntologyAnnotation_decoder(ConverterOptions__ctor())

JsonHelper_DecodeTables: Decoder_1[FSharpList[ArcTable]] = list_1_1(ArcTable_decoder)

JsonHelper_DecodePersons: Decoder_1[FSharpList[Person]] = list_1_1(decoder_2(ConverterOptions__ctor()))

JsonHelper_DecodeComments: Decoder_1[FSharpList[Comment]] = list_1_1(decoder_3(ConverterOptions__ctor()))

JsonHelper_DecodeFactors: Decoder_1[FSharpList[Factor]] = list_1_1(Factor_decoder(ConverterOptions__ctor()))

JsonHelper_DecodePublications: Decoder_1[FSharpList[Publication]] = list_1_1(decoder_4(ConverterOptions__ctor()))

JsonHelper_DecodeOntologySourceReferences: Decoder_1[FSharpList[OntologySourceReference]] = list_1_1(OntologySourceReference_decoder(ConverterOptions__ctor()))

def JsonHelper_tryGetTables(get: IGetters, field_name: str) -> Array[ArcTable]:
    def mapping(collection: FSharpList[ArcTable], get: Any=get, field_name: Any=field_name) -> Array[ArcTable]:
        return list(collection)

    def _arrow1591(__unit: None=None, get: Any=get, field_name: Any=field_name) -> FSharpList[ArcTable] | None:
        object_arg: IOptionalGetter = get.Optional
        return object_arg.Field(field_name, JsonHelper_DecodeTables)

    return default_arg(map(mapping, _arrow1591()), [])


def JsonHelper_tryGetPersons(get: IGetters, field_name: str) -> Array[Person]:
    def mapping(list_1: FSharpList[Person], get: Any=get, field_name: Any=field_name) -> Array[Person]:
        return to_array(list_1)

    def _arrow1592(__unit: None=None, get: Any=get, field_name: Any=field_name) -> FSharpList[Person] | None:
        object_arg: IOptionalGetter = get.Optional
        return object_arg.Field(field_name, JsonHelper_DecodePersons)

    return default_arg(map(mapping, _arrow1592()), [0] * 0)


def JsonHelper_tryGetComments(get: IGetters, field_name: str) -> Array[Comment]:
    def mapping(list_1: FSharpList[Comment], get: Any=get, field_name: Any=field_name) -> Array[Comment]:
        return to_array(list_1)

    def _arrow1593(__unit: None=None, get: Any=get, field_name: Any=field_name) -> FSharpList[Comment] | None:
        object_arg: IOptionalGetter = get.Optional
        return object_arg.Field(field_name, JsonHelper_DecodeComments)

    return default_arg(map(mapping, _arrow1593()), [0] * 0)


def JsonHelper_tryGetPublications(get: IGetters, field_name: str) -> Array[Publication]:
    def mapping(list_1: FSharpList[Publication], get: Any=get, field_name: Any=field_name) -> Array[Publication]:
        return to_array(list_1)

    def _arrow1594(__unit: None=None, get: Any=get, field_name: Any=field_name) -> FSharpList[Publication] | None:
        object_arg: IOptionalGetter = get.Optional
        return object_arg.Field(field_name, JsonHelper_DecodePublications)

    return default_arg(map(mapping, _arrow1594()), [0] * 0)


def JsonHelper_tryGetOAs(get: IGetters, field_name: str) -> Array[OntologyAnnotation]:
    def mapping(list_1: FSharpList[OntologyAnnotation], get: Any=get, field_name: Any=field_name) -> Array[OntologyAnnotation]:
        return to_array(list_1)

    def _arrow1595(__unit: None=None, get: Any=get, field_name: Any=field_name) -> FSharpList[OntologyAnnotation] | None:
        arg_1: Decoder_1[FSharpList[OntologyAnnotation]] = list_1_1(JsonHelper_DecodeOa)
        object_arg: IOptionalGetter = get.Optional
        return object_arg.Field(field_name, arg_1)

    return default_arg(map(mapping, _arrow1595()), [0] * 0)


def JsonHelper_tryGetFactors(get: IGetters, field_name: str) -> Array[Factor]:
    def mapping(list_1: FSharpList[Factor], get: Any=get, field_name: Any=field_name) -> Array[Factor]:
        return to_array(list_1)

    def _arrow1596(__unit: None=None, get: Any=get, field_name: Any=field_name) -> FSharpList[Factor] | None:
        object_arg: IOptionalGetter = get.Optional
        return object_arg.Field(field_name, JsonHelper_DecodeFactors)

    return default_arg(map(mapping, _arrow1596()), [0] * 0)


def JsonHelper_tryGetStringResizeArray(get: IGetters, field_name: str) -> Array[str]:
    def mapping(collection: FSharpList[str], get: Any=get, field_name: Any=field_name) -> Array[str]:
        return list(collection)

    def _arrow1597(__unit: None=None, get: Any=get, field_name: Any=field_name) -> FSharpList[str] | None:
        arg_1: Decoder_1[FSharpList[str]] = list_1_1(string)
        object_arg: IOptionalGetter = get.Optional
        return object_arg.Field(field_name, arg_1)

    return default_arg(map(mapping, _arrow1597()), [])


def JsonHelper_tryGetOntologySourceReferences(get: IGetters, field_name: str) -> Array[OntologySourceReference]:
    def mapping(list_1: FSharpList[OntologySourceReference], get: Any=get, field_name: Any=field_name) -> Array[OntologySourceReference]:
        return to_array(list_1)

    def _arrow1598(__unit: None=None, get: Any=get, field_name: Any=field_name) -> FSharpList[OntologySourceReference] | None:
        object_arg: IOptionalGetter = get.Optional
        return object_arg.Field(field_name, JsonHelper_DecodeOntologySourceReferences)

    return default_arg(map(mapping, _arrow1598()), [0] * 0)


def JsonHelper_EncoderOA(t: OntologyAnnotation) -> Json:
    return OntologyAnnotation_encoder(ConverterOptions__ctor(), t)


def JsonHelper_EncoderOAs(t: IEnumerable_1[OntologyAnnotation]) -> Json:
    def _arrow1599(t_1: OntologyAnnotation, t: Any=t) -> Json:
        return JsonHelper_EncoderOA(t_1)

    return seq(map_1(_arrow1599, t))


def JsonHelper_EncoderTables(t: IEnumerable_1[ArcTable]) -> Json:
    def _arrow1600(table: ArcTable, t: Any=t) -> Json:
        return ArcTable_encoder(table)

    return seq(map_1(_arrow1600, t))


def JsonHelper_EncoderPerson(t: Person) -> Json:
    return encoder(ConverterOptions__ctor(), t)


def JsonHelper_EncoderPersons(t: IEnumerable_1[Person]) -> Json:
    def _arrow1601(t_1: Person, t: Any=t) -> Json:
        return JsonHelper_EncoderPerson(t_1)

    return seq(map_1(_arrow1601, t))


def JsonHelper_EncoderComment(t: Comment) -> Json:
    return encoder_1(ConverterOptions__ctor(), t)


def JsonHelper_EncoderComments(t: IEnumerable_1[Comment]) -> Json:
    def _arrow1602(t_1: Comment, t: Any=t) -> Json:
        return JsonHelper_EncoderComment(t_1)

    return seq(map_1(_arrow1602, t))


def JsonHelper_EncoderPublication(t: Publication) -> Json:
    return encoder_2(ConverterOptions__ctor(), t)


def JsonHelper_EncoderPublications(t: IEnumerable_1[Publication]) -> Json:
    def _arrow1603(t_1: Publication, t: Any=t) -> Json:
        return JsonHelper_EncoderPublication(t_1)

    return seq(map_1(_arrow1603, t))


def JsonHelper_EncoderFactor(t: Factor) -> Json:
    return Factor_encoder(ConverterOptions__ctor(), t)


def JsonHelper_EncoderFactors(t: IEnumerable_1[Factor]) -> Json:
    def _arrow1604(t_1: Factor, t: Any=t) -> Json:
        return JsonHelper_EncoderFactor(t_1)

    return seq(map_1(_arrow1604, t))


def JsonHelper_EncoderOntologySourceReference(t: OntologySourceReference) -> Json:
    return OntologySourceReference_encoder(ConverterOptions__ctor(), t)


def JsonHelper_EncoderOntologySourceReferences(t: IEnumerable_1[OntologySourceReference]) -> Json:
    def _arrow1605(t_1: OntologySourceReference, t: Any=t) -> Json:
        return JsonHelper_EncoderOntologySourceReference(t_1)

    return seq(map_1(_arrow1605, t))


def ArcAssay_encoder(assay: ArcAssay) -> Json:
    def _arrow1612(__unit: None=None, assay: Any=assay) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1611(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1610(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1609(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1608(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        def _arrow1607(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                            def _arrow1606(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                return singleton(("Comments", JsonHelper_EncoderComments(assay.Comments))) if (len(assay.Comments) != 0) else empty()

                            return append(singleton(("Performers", JsonHelper_EncoderPersons(assay.Performers))) if (len(assay.Performers) != 0) else empty(), delay(_arrow1606))

                        return append(singleton(("Tables", JsonHelper_EncoderTables(assay.Tables))) if (len(assay.Tables) != 0) else empty(), delay(_arrow1607))

                    return append(singleton(("TechnologyPlatform", JsonHelper_EncoderOA(value_2(assay.TechnologyPlatform)))) if (assay.TechnologyPlatform is not None) else empty(), delay(_arrow1608))

                return append(singleton(("TechnologyType", JsonHelper_EncoderOA(value_2(assay.TechnologyType)))) if (assay.TechnologyType is not None) else empty(), delay(_arrow1609))

            return append(singleton(("MeasurementType", JsonHelper_EncoderOA(value_2(assay.MeasurementType)))) if (assay.MeasurementType is not None) else empty(), delay(_arrow1610))

        return append(singleton(("Identifier", Json(0, assay.Identifier))), delay(_arrow1611))

    return Json(5, to_list(delay(_arrow1612)))


def _arrow1613(get: IGetters) -> ArcAssay:
    identifier: str
    object_arg: IRequiredGetter = get.Required
    identifier = object_arg.Field("Identifier", string)
    measurement_type: OntologyAnnotation | None
    object_arg_1: IOptionalGetter = get.Optional
    measurement_type = object_arg_1.Field("MeasurementType", JsonHelper_DecodeOa)
    technology_type: OntologyAnnotation | None
    object_arg_2: IOptionalGetter = get.Optional
    technology_type = object_arg_2.Field("TechnologyType", JsonHelper_DecodeOa)
    technology_platform: OntologyAnnotation | None
    object_arg_3: IOptionalGetter = get.Optional
    technology_platform = object_arg_3.Field("TechnologyPlatform", JsonHelper_DecodeOa)
    tables: Array[ArcTable] = JsonHelper_tryGetTables(get, "Tables")
    performers: Array[Person] = JsonHelper_tryGetPersons(get, "Performers")
    comments: Array[Comment] = JsonHelper_tryGetComments(get, "Comments")
    return ArcAssay.make(identifier, measurement_type, technology_type, technology_platform, tables, performers, comments)


ArcAssay_decoder: Decoder_1[ArcAssay] = object(_arrow1613)

def ArcAssay_compressedEncoder(string_table: Any, oa_table: Any, cell_table: Any, assay: ArcAssay) -> Json:
    def _arrow1621(__unit: None=None, string_table: Any=string_table, oa_table: Any=oa_table, cell_table: Any=cell_table, assay: Any=assay) -> IEnumerable_1[tuple[str, Json]]:
        def _arrow1620(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
            def _arrow1619(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                def _arrow1618(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                    def _arrow1617(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                        def _arrow1614(table: ArcTable) -> Json:
                            return ArcTable_compressedEncoder(string_table, oa_table, cell_table, table)

                        def _arrow1616(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                            def _arrow1615(__unit: None=None) -> IEnumerable_1[tuple[str, Json]]:
                                return singleton(("Comments", JsonHelper_EncoderComments(assay.Comments))) if (len(assay.Comments) != 0) else empty()

                            return append(singleton(("Performers", JsonHelper_EncoderPersons(assay.Performers))) if (len(assay.Performers) != 0) else empty(), delay(_arrow1615))

                        return append(singleton(("Tables", seq(map_1(_arrow1614, assay.Tables)))) if (len(assay.Tables) != 0) else empty(), delay(_arrow1616))

                    return append(singleton(("TechnologyPlatform", OATable_encodeOA(oa_table, value_2(assay.TechnologyPlatform)))) if (assay.TechnologyPlatform is not None) else empty(), delay(_arrow1617))

                return append(singleton(("TechnologyType", OATable_encodeOA(oa_table, value_2(assay.TechnologyType)))) if (assay.TechnologyType is not None) else empty(), delay(_arrow1618))

            return append(singleton(("MeasurementType", OATable_encodeOA(oa_table, value_2(assay.MeasurementType)))) if (assay.MeasurementType is not None) else empty(), delay(_arrow1619))

        return append(singleton(("Identifier", Json(0, assay.Identifier))), delay(_arrow1620))

    return Json(5, to_list(delay(_arrow1621)))


def ArcAssay_compressedDecoder(string_table: Array[str], oa_table: Array[OntologyAnnotation], cell_table: Array[CompositeCell]) -> Decoder_1[ArcAssay]:
    def _arrow1623(get: IGetters, string_table: Any=string_table, oa_table: Any=oa_table, cell_table: Any=cell_table) -> ArcAssay:
        def _arrow1622(__unit: None=None) -> Array[ArcTable] | None:
            arg_1: Decoder_1[Array[ArcTable]] = array(ArcTable_compressedDecoder(string_table, oa_table, cell_table))
            object_arg: IOptionalGetter = get.Optional
            return object_arg.Field("Tables", arg_1)

        tables: Array[ArcTable] = default_arg(map(list, _arrow1622()), [])
        identifier: str
        object_arg_1: IRequiredGetter = get.Required
        identifier = object_arg_1.Field("Identifier", string)
        measurement_type: OntologyAnnotation | None
        arg_5: Decoder_1[OntologyAnnotation] = OATable_decodeOA(oa_table)
        object_arg_2: IOptionalGetter = get.Optional
        measurement_type = object_arg_2.Field("MeasurementType", arg_5)
        technology_type: OntologyAnnotation | None
        arg_7: Decoder_1[OntologyAnnotation] = OATable_decodeOA(oa_table)
        object_arg_3: IOptionalGetter = get.Optional
        technology_type = object_arg_3.Field("TechnologyType", arg_7)
        technology_platform: OntologyAnnotation | None
        arg_9: Decoder_1[OntologyAnnotation] = OATable_decodeOA(oa_table)
        object_arg_4: IOptionalGetter = get.Optional
        technology_platform = object_arg_4.Field("TechnologyPlatform", arg_9)
        performers: Array[Person] = JsonHelper_tryGetPersons(get, "Performers")
        comments: Array[Comment] = JsonHelper_tryGetComments(get, "Comments")
        return ArcAssay.make(identifier, measurement_type, technology_type, technology_platform, tables, performers, comments)

    return object(_arrow1623)


def ArcAssay_toJsonldString(a: ArcAssay) -> str:
    def _arrow1624(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, Assay_encoder(_arrow1624(), None, a.ToAssay()))


def ArcAssay_toJsonldStringWithContext(a: ArcAssay) -> str:
    def _arrow1625(__unit: None=None, a: Any=a) -> ConverterOptions:
        return_val: ConverterOptions = ConverterOptions__ctor()
        ConverterOptions__set_SetID_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeType_Z1FBCCD16(return_val, True)
        ConverterOptions__set_IncludeContext_Z1FBCCD16(return_val, True)
        return return_val

    return to_string(2, Assay_encoder(_arrow1625(), None, a.ToAssay()))


def ArcAssay_fromJsonString(s: str) -> ArcAssay:
    a_1: Assay
    match_value: FSharpResult_2[Assay, str] = Decode_fromString(Assay_decoder(ConverterOptions__ctor()), s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        a_1 = match_value.fields[0]

    return ArcAssay.from_assay(a_1)


def ArcAssay_toJsonString(a: ArcAssay) -> str:
    return to_string(2, Assay_encoder(ConverterOptions__ctor(), None, a.ToAssay()))


def ArcAssay_toArcJsonString(a: ArcAssay) -> str:
    return to_string(0, ArcAssay_encoder(a))


def ArcAssay_fromArcJsonString(json_string: str) -> ArcAssay:
    try: 
        match_value: FSharpResult_2[ArcAssay, str] = Decode_fromString(ArcAssay_decoder, json_string)
        if match_value.tag == 1:
            raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

        else: 
            return match_value.fields[0]


    except Exception as e_1:
        arg_1: str = str(e_1)
        return to_fail(printf("Error. Unable to parse json string to ArcAssay: %s"))(arg_1)



def ARCtrl_ISA_ArcAssay__ArcAssay_fromArcJsonString_Static_Z721C83C5(json_string: str) -> ArcAssay:
    try: 
        match_value: FSharpResult_2[ArcAssay, str] = Decode_fromString(ArcAssay_decoder, json_string)
        if match_value.tag == 1:
            raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

        else: 
            return match_value.fields[0]


    except Exception as e_1:
        arg_1: str = str(e_1)
        return to_fail(printf("Error. Unable to parse json string to ArcAssay: %s"))(arg_1)



def ARCtrl_ISA_ArcAssay__ArcAssay_ToArcJsonString_71136F3F(this: ArcAssay, spaces: int | None=None) -> str:
    return to_string(default_arg(spaces, 0), ArcAssay_encoder(this))


def ARCtrl_ISA_ArcAssay__ArcAssay_toArcJsonString_Static_1C75D08D(a: ArcAssay) -> str:
    return ARCtrl_ISA_ArcAssay__ArcAssay_ToArcJsonString_71136F3F(a)


def ARCtrl_ISA_ArcAssay__ArcAssay_fromCompressedJsonString_Static_Z721C83C5(json_string: str) -> ArcAssay:
    def _arrow1627(get: IGetters, json_string: Any=json_string) -> ArcAssay:
        string_table: Array[str]
        object_arg: IRequiredGetter = get.Required
        string_table = object_arg.Field("stringTable", StringTable_decoder)
        oa_table: Array[OntologyAnnotation]
        arg_3: Decoder_1[Array[OntologyAnnotation]] = OATable_decoder(string_table)
        object_arg_1: IRequiredGetter = get.Required
        oa_table = object_arg_1.Field("oaTable", arg_3)
        def _arrow1626(__unit: None=None) -> Array[CompositeCell]:
            arg_5: Decoder_1[Array[CompositeCell]] = CellTable_decoder(string_table, oa_table)
            object_arg_2: IRequiredGetter = get.Required
            return object_arg_2.Field("cellTable", arg_5)

        arg_7: Decoder_1[ArcAssay] = ArcAssay_compressedDecoder(string_table, oa_table, _arrow1626())
        object_arg_3: IRequiredGetter = get.Required
        return object_arg_3.Field("assay", arg_7)

    decoder: Decoder_1[ArcAssay] = object(_arrow1627)
    try: 
        match_value: FSharpResult_2[ArcAssay, str] = Decode_fromString(decoder, json_string)
        if match_value.tag == 1:
            raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

        else: 
            return match_value.fields[0]


    except Exception as e_1:
        arg_9: str = str(e_1)
        return to_fail(printf("Error. Unable to parse json string to ArcAssay: %s"))(arg_9)



def ARCtrl_ISA_ArcAssay__ArcAssay_ToCompressedJsonString_71136F3F(this: ArcAssay, spaces: int | None=None) -> str:
    spaces_1: int = default_arg(spaces, 0) or 0
    string_table: Any = dict([])
    class ObjectExpr1628:
        @property
        def Equals(self) -> Callable[[OntologyAnnotation, OntologyAnnotation], bool]:
            return equals

        @property
        def GetHashCode(self) -> Callable[[OntologyAnnotation], int]:
            return safe_hash

    oa_table: Any = Dictionary([], ObjectExpr1628())
    class ObjectExpr1629:
        @property
        def Equals(self) -> Callable[[CompositeCell, CompositeCell], bool]:
            return equals

        @property
        def GetHashCode(self) -> Callable[[CompositeCell], int]:
            return safe_hash

    cell_table: Any = Dictionary([], ObjectExpr1629())
    arc_assay: Json = ArcAssay_compressedEncoder(string_table, oa_table, cell_table, this)
    return to_string(spaces_1, Json(5, to_enumerable([("cellTable", CellTable_encoder(string_table, oa_table, CellTable_arrayFromMap(cell_table))), ("oaTable", OATable_encoder(string_table, OATable_arrayFromMap(oa_table))), ("stringTable", StringTable_encoder(StringTable_arrayFromMap(string_table))), ("assay", arc_assay)])))


def ARCtrl_ISA_ArcAssay__ArcAssay_toCompressedJsonString_Static_1C75D08D(a: ArcAssay) -> str:
    return ARCtrl_ISA_ArcAssay__ArcAssay_ToCompressedJsonString_71136F3F(a)


__all__ = ["JsonHelper_DecodeOa", "JsonHelper_DecodeTables", "JsonHelper_DecodePersons", "JsonHelper_DecodeComments", "JsonHelper_DecodeFactors", "JsonHelper_DecodePublications", "JsonHelper_DecodeOntologySourceReferences", "JsonHelper_tryGetTables", "JsonHelper_tryGetPersons", "JsonHelper_tryGetComments", "JsonHelper_tryGetPublications", "JsonHelper_tryGetOAs", "JsonHelper_tryGetFactors", "JsonHelper_tryGetStringResizeArray", "JsonHelper_tryGetOntologySourceReferences", "JsonHelper_EncoderOA", "JsonHelper_EncoderOAs", "JsonHelper_EncoderTables", "JsonHelper_EncoderPerson", "JsonHelper_EncoderPersons", "JsonHelper_EncoderComment", "JsonHelper_EncoderComments", "JsonHelper_EncoderPublication", "JsonHelper_EncoderPublications", "JsonHelper_EncoderFactor", "JsonHelper_EncoderFactors", "JsonHelper_EncoderOntologySourceReference", "JsonHelper_EncoderOntologySourceReferences", "ArcAssay_encoder", "ArcAssay_decoder", "ArcAssay_compressedEncoder", "ArcAssay_compressedDecoder", "ArcAssay_toJsonldString", "ArcAssay_toJsonldStringWithContext", "ArcAssay_fromJsonString", "ArcAssay_toJsonString", "ArcAssay_toArcJsonString", "ArcAssay_fromArcJsonString", "ARCtrl_ISA_ArcAssay__ArcAssay_fromArcJsonString_Static_Z721C83C5", "ARCtrl_ISA_ArcAssay__ArcAssay_ToArcJsonString_71136F3F", "ARCtrl_ISA_ArcAssay__ArcAssay_toArcJsonString_Static_1C75D08D", "ARCtrl_ISA_ArcAssay__ArcAssay_fromCompressedJsonString_Static_Z721C83C5", "ARCtrl_ISA_ArcAssay__ArcAssay_ToCompressedJsonString_71136F3F", "ARCtrl_ISA_ArcAssay__ArcAssay_toCompressedJsonString_Static_1C75D08D"]

