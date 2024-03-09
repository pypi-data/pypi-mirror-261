from __future__ import annotations
from dataclasses import dataclass
from .....fable_modules.fable_library.reflection import (TypeInfo, string_type, record_type)
from .....fable_modules.fable_library.types import Record
from .....fable_modules.fable_library.util import to_enumerable
from .....fable_modules.thoth_json_core.types import Json

def _expr962() -> TypeInfo:
    return record_type("ARCtrl.ISA.Json.ROCrateContext.Protocol.IContext", [], IContext, lambda: [("sdo", string_type), ("arc", string_type), ("Protocol", string_type), ("ArcProtocol", string_type), ("name", string_type), ("protocol_type", string_type), ("description", string_type), ("version", string_type), ("components", string_type), ("parameters", string_type), ("uri", string_type), ("comments", string_type)])


@dataclass(eq = False, repr = False, slots = True)
class IContext(Record):
    sdo: str
    arc: str
    Protocol: str
    ArcProtocol: str
    name: str
    protocol_type: str
    description: str
    version: str
    components: str
    parameters: str
    uri: str
    comments: str

IContext_reflection = _expr962

context_jsonvalue: Json = Json(5, to_enumerable([("sdo", Json(0, "http://schema.org/")), ("arc", Json(0, "http://purl.org/nfdi4plants/ontology/")), ("Protocol", Json(0, "sdo:Thing")), ("ArcProtocol", Json(0, "arc:ARC#ARC_00000040")), ("name", Json(0, "arc:ARC#ARC_00000019")), ("protocolType", Json(0, "arc:ARC#ARC_00000060")), ("description", Json(0, "arc:ARC#ARC_00000004")), ("version", Json(0, "arc:ARC#ARC_00000020")), ("components", Json(0, "arc:ARC#ARC_00000064")), ("parameters", Json(0, "arc:ARC#ARC_00000062")), ("uri", Json(0, "arc:ARC#ARC_00000061")), ("comments", Json(0, "arc:ARC#ARC_00000016"))]))

context_str: str = "\r\n{\r\n  \"@context\": {\r\n    \"sdo\": \"http://schema.org/\",\r\n    \"arc\": \"http://purl.org/nfdi4plants/ontology/\",\r\n\r\n    \"Protocol\": \"sdo:Thing\",\r\n    \"ArcProtocol\": \"arc:ARC#ARC_00000040\",\r\n\r\n    \"name\": \"arc:ARC#ARC_00000019\",\r\n    \"protocolType\": \"arc:ARC#ARC_00000060\",\r\n    \"description\": \"arc:ARC#ARC_00000004\",\r\n    \"version\": \"arc:ARC#ARC_00000020\",\r\n    \"components\": \"arc:ARC#ARC_00000064\",\r\n    \"parameters\": \"arc:ARC#ARC_00000062\",\r\n    \"uri\": \"arc:ARC#ARC_00000061\",\r\n    \"comments\": \"arc:ARC#ARC_00000016\"\r\n  }\r\n}\r\n    "

__all__ = ["IContext_reflection", "context_jsonvalue", "context_str"]

