from __future__ import annotations
from dataclasses import dataclass
from .....fable_modules.fable_library.reflection import (TypeInfo, string_type, record_type)
from .....fable_modules.fable_library.types import Record
from .....fable_modules.fable_library.util import to_enumerable
from .....fable_modules.thoth_json_core.types import Json

def _expr935() -> TypeInfo:
    return record_type("ARCtrl.ISA.Json.ROCrateContext.MaterialAttributeValue.IContext", [], IContext, lambda: [("sdo", string_type), ("arc", string_type), ("MaterialAttributeValue", string_type), ("ArcMaterialAttributeValue", string_type), ("category", string_type), ("value", string_type), ("unit", string_type)])


@dataclass(eq = False, repr = False, slots = True)
class IContext(Record):
    sdo: str
    arc: str
    MaterialAttributeValue: str
    ArcMaterialAttributeValue: str
    category: str
    value: str
    unit: str

IContext_reflection = _expr935

context_jsonvalue: Json = Json(5, to_enumerable([("sdo", Json(0, "http://schema.org/")), ("arc", Json(0, "http://purl.org/nfdi4plants/ontology/")), ("MaterialAttributeValue", Json(0, "sdo:PropertyValue")), ("ArcMaterialAttributeValue", Json(0, "arc:ARC#ARC_00000079")), ("category", Json(0, "arc:ARC#ARC_00000049")), ("value", Json(0, "arc:ARC#ARC_00000036")), ("unit", Json(0, "arc:ARC#ARC_00000106"))]))

context_str: str = "\r\n{\r\n  \"@context\": {\r\n    \"sdo\": \"http://schema.org/\",\r\n    \"arc\": \"http://purl.org/nfdi4plants/ontology/\",\r\n\r\n    \"MaterialAttributeValue\": \"sdo:PropertyValue\",\r\n    \"ArcMaterialAttributeValue\": \"arc:ARC#ARC_00000079\",\r\n\r\n    \"category\": \"arc:ARC#ARC_00000049\",\r\n    \"value\": \"arc:ARC#ARC_00000036\",\r\n    \"unit\": \"arc:ARC#ARC_00000106\"\r\n  }\r\n}\r\n   "

__all__ = ["IContext_reflection", "context_jsonvalue", "context_str"]

