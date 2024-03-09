from __future__ import annotations
from dataclasses import dataclass
from .....fable_modules.fable_library.reflection import (TypeInfo, string_type, record_type)
from .....fable_modules.fable_library.types import Record
from .....fable_modules.fable_library.util import to_enumerable
from .....fable_modules.thoth_json_core.types import Json

def _expr932() -> TypeInfo:
    return record_type("ARCtrl.ISA.Json.ROCrateContext.FactorValue.IContext", [], IContext, lambda: [("sdo", string_type), ("arc", string_type), ("FactorValue", string_type), ("ArcFactorValue", string_type), ("category", string_type), ("value", string_type), ("unit", string_type)])


@dataclass(eq = False, repr = False, slots = True)
class IContext(Record):
    sdo: str
    arc: str
    FactorValue: str
    ArcFactorValue: str
    category: str
    value: str
    unit: str

IContext_reflection = _expr932

context_jsonvalue: Json = Json(5, to_enumerable([("sdo", Json(0, "http://schema.org/")), ("arc", Json(0, "http://purl.org/nfdi4plants/ontology/")), ("FactorValue", Json(0, "sdo:PropertyValue")), ("ArcFactorValue", Json(0, "arc:ARC#ARC_00000084")), ("category", Json(0, "arc:category")), ("value", Json(0, "arc:ARC#ARC_00000044")), ("unit", Json(0, "arc:ARC#ARC_00000106"))]))

context_str: str = "\r\n{\r\n  \"@context\": {\r\n    \"sdo\": \"http://schema.org/\",\r\n    \"arc\": \"http://purl.org/nfdi4plants/ontology/\",\r\n\r\n    \"FactorValue\": \"sdo:PropertyValue\",\r\n    \"ArcFactorValue\": \"arc:ARC#ARC_00000084\",\r\n\r\n    \"category\": \"arc:category\",\r\n    \"value\": \"arc:ARC#ARC_00000044\",\r\n    \"unit\": \"arc:ARC#ARC_00000106\"\r\n  }\r\n}\r\n    "

__all__ = ["IContext_reflection", "context_jsonvalue", "context_str"]

