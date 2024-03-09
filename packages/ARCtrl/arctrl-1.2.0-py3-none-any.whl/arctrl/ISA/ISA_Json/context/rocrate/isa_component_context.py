from __future__ import annotations
from dataclasses import dataclass
from .....fable_modules.fable_library.reflection import (TypeInfo, string_type, record_type)
from .....fable_modules.fable_library.types import Record
from .....fable_modules.fable_library.util import to_enumerable
from .....fable_modules.thoth_json_core.types import Json

def _expr929() -> TypeInfo:
    return record_type("ARCtrl.ISA.Json.ROCrateContext.Component.IContext", [], IContext, lambda: [("sdo", string_type), ("arc", string_type), ("Component", string_type), ("ArcComponent", string_type), ("component_name", string_type), ("component_type", string_type)])


@dataclass(eq = False, repr = False, slots = True)
class IContext(Record):
    sdo: str
    arc: str
    Component: str
    ArcComponent: str
    component_name: str
    component_type: str

IContext_reflection = _expr929

context_jsonvalue: Json = Json(5, to_enumerable([("sdo", Json(0, "http://schema.org/")), ("arc", Json(0, "http://purl.org/nfdi4plants/ontology/")), ("Component", Json(0, "sdo:Thing")), ("ArcComponent", Json(0, "arc:ARC#ARC_00000065")), ("componentName", Json(0, "arc:ARC#ARC_00000019")), ("componentType", Json(0, "arc:ARC#ARC_00000102"))]))

context_str: str = "\r\n{\r\n  \"@context\": {\r\n    \"sdo\": \"http://schema.org/\",\r\n    \"arc\": \"http://purl.org/nfdi4plants/ontology/\",\r\n    \r\n    \"Component\": \"sdo:Thing\",\r\n    \"ArcComponent\": \"arc:ARC#ARC_00000065\",\r\n\r\n    \"componentName\": \"arc:ARC#ARC_00000019\",\r\n    \"componentType\": \"arc:ARC#ARC_00000102\"\r\n  }\r\n}\r\n    "

__all__ = ["IContext_reflection", "context_jsonvalue", "context_str"]

