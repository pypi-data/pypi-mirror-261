from __future__ import annotations
from dataclasses import dataclass
from .....fable_modules.fable_library.reflection import (TypeInfo, string_type, record_type)
from .....fable_modules.fable_library.types import Record
from .....fable_modules.fable_library.util import to_enumerable
from .....fable_modules.thoth_json_core.types import Json

def _expr961() -> TypeInfo:
    return record_type("ARCtrl.ISA.Json.ROCrateContext.ProcessParameterValue.IContext", [], IContext, lambda: [("sdo", string_type), ("arc", string_type), ("ProcessParameterValue", string_type), ("ArcProcessParameterValue", string_type), ("category", string_type), ("value", string_type), ("unit", string_type)])


@dataclass(eq = False, repr = False, slots = True)
class IContext(Record):
    sdo: str
    arc: str
    ProcessParameterValue: str
    ArcProcessParameterValue: str
    category: str
    value: str
    unit: str

IContext_reflection = _expr961

context_jsonvalue: Json = Json(5, to_enumerable([("sdo", Json(0, "http://schema.org/")), ("arc", Json(0, "http://purl.org/nfdi4plants/ontology/")), ("ProcessParameterValue", Json(0, "sdo:PropertyValue")), ("ArcProcessParameterValue", Json(0, "arc:ARC#ARC_00000088")), ("category", Json(0, "arc:ARC#ARC_00000062")), ("value", Json(0, "arc:ARC#ARC_00000087")), ("unit", Json(0, "arc:ARC#ARC_00000106"))]))

context_str: str = "\r\n{\r\n  \"@context\": {\r\n    \"sdo\": \"http://schema.org/\",\r\n    \"arc\": \"http://purl.org/nfdi4plants/ontology/\",\r\n\r\n    \"ProcessParameterValue\": \"sdo:PropertyValue\",\r\n    \"ArcProcessParameterValue\": \"arc:ARC#ARC_00000088\",\r\n\r\n    \"category\": \"arc:ARC#ARC_00000062\",\r\n    \"value\": \"arc:ARC#ARC_00000087\",\r\n    \"unit\": \"arc:ARC#ARC_00000106\"\r\n  }\r\n}\r\n    "

__all__ = ["IContext_reflection", "context_jsonvalue", "context_str"]

