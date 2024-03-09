from __future__ import annotations
from dataclasses import dataclass
from .....fable_modules.fable_library.reflection import (TypeInfo, string_type, record_type)
from .....fable_modules.fable_library.types import Record
from .....fable_modules.fable_library.util import to_enumerable
from .....fable_modules.thoth_json_core.types import Json

def _expr927() -> TypeInfo:
    return record_type("ARCtrl.ISA.Json.ROCrateContext.Assay.IContext", [], IContext, lambda: [("sdo", string_type), ("arc", string_type), ("Assay", string_type), ("ArcAssay", string_type), ("measurement_type", string_type), ("technology_type", string_type), ("technology_platform", string_type), ("data_files", string_type), ("materials", string_type), ("other_materials", string_type), ("samples", string_type), ("characteristic_categories", string_type), ("process_sequences", string_type), ("unit_categories", string_type), ("comments", string_type), ("filename", string_type)])


@dataclass(eq = False, repr = False, slots = True)
class IContext(Record):
    sdo: str
    arc: str
    Assay: str
    ArcAssay: str
    measurement_type: str
    technology_type: str
    technology_platform: str
    data_files: str
    materials: str
    other_materials: str
    samples: str
    characteristic_categories: str
    process_sequences: str
    unit_categories: str
    comments: str
    filename: str

IContext_reflection = _expr927

context_jsonvalue: Json = Json(5, to_enumerable([("sdo", Json(0, "http://schema.org/")), ("arc", Json(0, "http://purl.org/nfdi4plants/ontology/")), ("Assay", Json(0, "sdo:Dataset")), ("ArcAssay", Json(0, "arc:ARC#ARC_00000042")), ("measurementType", Json(0, "sdo:variableMeasured")), ("technologyType", Json(0, "sdo:measurementTechnique")), ("technologyPlatform", Json(0, "sdo:instrument")), ("dataFiles", Json(0, "sdo:hasPart")), ("materials", Json(0, "arc:ARC#ARC_00000074")), ("otherMaterials", Json(0, "arc:ARC#ARC_00000074")), ("samples", Json(0, "arc:ARC#ARC_00000074")), ("characteristicCategories", Json(0, "arc:ARC#ARC_00000049")), ("processSequences", Json(0, "arc:ARC#ARC_00000047")), ("unitCategories", Json(0, "arc:ARC#ARC_00000051")), ("comments", Json(0, "sdo:disambiguatingDescription")), ("filename", Json(0, "sdo:url"))]))

context_str: str = "\r\n{\r\n  \"@context\": {\r\n    \"sdo\": \"https://schema.org/\",\r\n    \"arc\": \"http://purl.org/nfdi4plants/ontology/\",\r\n\r\n    \"Assay\": \"sdo:Dataset\",\r\n    \"ArcAssay\": \"arc:ARC#ARC_00000042\",\r\n\r\n    \"measurementType\": \"sdo:variableMeasured\",\r\n    \"technologyType\": \"sdo:measurementTechnique\",\r\n    \"technologyPlatform\": \"sdo:instrument\",\r\n    \"dataFiles\": \"sdo:hasPart\",\r\n\r\n    \"materials\": \"arc:ARC#ARC_00000074\",\r\n    \"otherMaterials\": \"arc:ARC#ARC_00000074\",\r\n    \"samples\": \"arc:ARC#ARC_00000074\",\r\n    \"characteristicCategories\": \"arc:ARC#ARC_00000049\",\r\n    \"processSequences\": \"arc:ARC#ARC_00000047\",\r\n    \"unitCategories\": \"arc:ARC#ARC_00000051\",\r\n\r\n    \"comments\": \"sdo:disambiguatingDescription\",\r\n    \"filename\": \"sdo:url\"\r\n  }\r\n}\r\n    "

__all__ = ["IContext_reflection", "context_jsonvalue", "context_str"]

