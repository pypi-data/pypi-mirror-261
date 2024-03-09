from __future__ import annotations
from dataclasses import dataclass
from .....fable_modules.fable_library.reflection import (TypeInfo, string_type, record_type)
from .....fable_modules.fable_library.types import Record
from .....fable_modules.fable_library.util import to_enumerable
from .....fable_modules.thoth_json_core.types import Json

def _expr967() -> TypeInfo:
    return record_type("ARCtrl.ISA.Json.ROCrateContext.Study.IContext", [], IContext, lambda: [("sdo", string_type), ("arc", string_type), ("Study", string_type), ("ArcStudy", string_type), ("identifier", string_type), ("title", string_type), ("description", string_type), ("submission_date", string_type), ("public_release_date", string_type), ("publications", string_type), ("people", string_type), ("assays", string_type), ("filename", string_type), ("comments", string_type), ("protocols", string_type), ("materials", string_type), ("other_materials", string_type), ("sources", string_type), ("samples", string_type), ("process_sequence", string_type), ("factors", string_type), ("characteristic_categories", string_type), ("unit_categories", string_type), ("study_design_descriptors", string_type)])


@dataclass(eq = False, repr = False, slots = True)
class IContext(Record):
    sdo: str
    arc: str
    Study: str
    ArcStudy: str
    identifier: str
    title: str
    description: str
    submission_date: str
    public_release_date: str
    publications: str
    people: str
    assays: str
    filename: str
    comments: str
    protocols: str
    materials: str
    other_materials: str
    sources: str
    samples: str
    process_sequence: str
    factors: str
    characteristic_categories: str
    unit_categories: str
    study_design_descriptors: str

IContext_reflection = _expr967

context_jsonvalue: Json = Json(5, to_enumerable([("sdo", Json(0, "http://schema.org/")), ("arc", Json(0, "http://purl.org/nfdi4plants/ontology/")), ("Study", Json(0, "sdo:Dataset")), ("ArcStudy", Json(0, "arc:ARC#ARC_00000014")), ("identifier", Json(0, "sdo:identifier")), ("title", Json(0, "sdo:headline")), ("description", Json(0, "sdo:description")), ("submissionDate", Json(0, "sdo:dateCreated")), ("publicReleaseDate", Json(0, "sdo:datePublished")), ("publications", Json(0, "sdo:citation")), ("people", Json(0, "sdo:creator")), ("assays", Json(0, "sdo:hasPart")), ("filename", Json(0, "sdo:description")), ("comments", Json(0, "sdo:disambiguatingDescription")), ("protocols", Json(0, "arc:ARC#ARC_00000039")), ("materials", Json(0, "arc:ARC#ARC_00000045")), ("otherMaterials", Json(0, "arc:ARC#ARC_00000045")), ("sources", Json(0, "arc:ARC#ARC_00000045")), ("samples", Json(0, "arc:ARC#ARC_00000045")), ("processSequence", Json(0, "arc:ARC#ARC_00000047")), ("factors", Json(0, "arc:ARC#ARC_00000043")), ("characteristicCategories", Json(0, "arc:ARC#ARC_00000049")), ("unitCategories", Json(0, "arc:ARC#ARC_00000051")), ("studyDesignDescriptors", Json(0, "arc:ARC#ARC_00000037"))]))

context_str: str = "\r\n{\r\n  \"@context\": {\r\n    \"sdo\": \"http://schema.org/\",\r\n    \"arc\": \"http://purl.org/nfdi4plants/ontology/\",\r\n\r\n    \"Study\": \"sdo:Dataset\",\r\n    \"ArcStudy\": \"arc:ARC#ARC_00000014\",\r\n\r\n    \"identifier\": \"sdo:identifier\",\r\n    \"title\": \"sdo:headline\",\r\n    \"description\": \"sdo:description\",\r\n    \"submissionDate\": \"sdo:dateCreated\",\r\n    \"publicReleaseDate\": \"sdo:datePublished\",\r\n    \"publications\": \"sdo:citation\",\r\n    \"people\": \"sdo:creator\",\r\n    \"assays\": \"sdo:hasPart\",\r\n    \"filename\": \"sdo:description\",\r\n    \"comments\": \"sdo:disambiguatingDescription\",\r\n\r\n    \"protocols\": \"arc:ARC#ARC_00000039\",\r\n    \"materials\": \"arc:ARC#ARC_00000045\",\r\n    \"otherMaterials\": \"arc:ARC#ARC_00000045\",\r\n    \"sources\": \"arc:ARC#ARC_00000045\",\r\n    \"samples\": \"arc:ARC#ARC_00000045\",\r\n    \"processSequence\": \"arc:ARC#ARC_00000047\",\r\n    \"factors\": \"arc:ARC#ARC_00000043\",\r\n    \"characteristicCategories\": \"arc:ARC#ARC_00000049\",\r\n    \"unitCategories\": \"arc:ARC#ARC_00000051\",\r\n    \"studyDesignDescriptors\": \"arc:ARC#ARC_00000037\"\r\n  }\r\n}\r\n    "

__all__ = ["IContext_reflection", "context_jsonvalue", "context_str"]

