from __future__ import annotations
from dataclasses import dataclass
from .....fable_modules.fable_library.reflection import (TypeInfo, string_type, record_type)
from .....fable_modules.fable_library.types import Record
from .....fable_modules.fable_library.util import to_enumerable
from .....fable_modules.thoth_json_core.types import Json

def _expr928() -> TypeInfo:
    return record_type("ARCtrl.ISA.Json.ROCrateContext.Comment.IContext", [], IContext, lambda: [("sdo", string_type), ("arc", string_type), ("Comment", string_type), ("name", string_type), ("value", string_type)])


@dataclass(eq = False, repr = False, slots = True)
class IContext(Record):
    sdo: str
    arc: str
    Comment: str
    name: str
    value: str

IContext_reflection = _expr928

context_jsonvalue: Json = Json(5, to_enumerable([("sdo", Json(0, "http://schema.org/")), ("arc", Json(0, "http://purl.org/nfdi4plants/ontology/")), ("Comment", Json(0, "sdo:Comment")), ("name", Json(0, "sdo:name")), ("value", Json(0, "sdo:value"))]))

context_str: str = "\r\n{\r\n  \"@context\": {\r\n    \"sdo\": \"http://schema.org/\",\r\n    \"arc\": \"http://purl.org/nfdi4plants/ontology/\",\r\n    \r\n    \"Comment\": \"sdo:Comment\",\r\n    \"name\": \"sdo:name\",\r\n    \"value\": \"sdo:value\"\r\n  }\r\n}\r\n    "

__all__ = ["IContext_reflection", "context_jsonvalue", "context_str"]

