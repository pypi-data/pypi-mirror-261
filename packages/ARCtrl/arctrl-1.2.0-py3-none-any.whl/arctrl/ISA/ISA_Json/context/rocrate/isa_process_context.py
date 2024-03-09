from __future__ import annotations
from dataclasses import dataclass
from .....fable_modules.fable_library.reflection import (TypeInfo, string_type, record_type)
from .....fable_modules.fable_library.types import Record
from .....fable_modules.fable_library.util import to_enumerable
from .....fable_modules.thoth_json_core.types import Json

def _expr960() -> TypeInfo:
    return record_type("ARCtrl.ISA.Json.ROCrateContext.Process.IContext", [], IContext, lambda: [("sdo", string_type), ("arc", string_type), ("Process", string_type), ("ArcProcess", string_type), ("name", string_type), ("executes_protocol", string_type), ("performer", string_type), ("date", string_type), ("previous_process", string_type), ("next_process", string_type), ("input", string_type), ("output", string_type), ("comments", string_type)])


@dataclass(eq = False, repr = False, slots = True)
class IContext(Record):
    sdo: str
    arc: str
    Process: str
    ArcProcess: str
    name: str
    executes_protocol: str
    performer: str
    date: str
    previous_process: str
    next_process: str
    input: str
    output: str
    comments: str

IContext_reflection = _expr960

context_jsonvalue: Json = Json(5, to_enumerable([("sdo", Json(0, "http://schema.org/")), ("arc", Json(0, "http://purl.org/nfdi4plants/ontology/")), ("Process", Json(0, "sdo:Thing")), ("ArcProcess", Json(0, "arc:ARC#ARC_00000048")), ("name", Json(0, "arc:ARC#ARC_00000019")), ("executesProtocol", Json(0, "arc:ARC#ARC_00000086")), ("performer", Json(0, "arc:ARC#ARC_00000089")), ("date", Json(0, "arc:ARC#ARC_00000090")), ("previousProcess", Json(0, "arc:ARC#ARC_00000091")), ("nextProcess", Json(0, "arc:ARC#ARC_00000092")), ("input", Json(0, "arc:ARC#ARC_00000095")), ("output", Json(0, "arc:ARC#ARC_00000096")), ("comments", Json(0, "sdo:disambiguatingDescription"))]))

context_str: str = "\r\n{\r\n  \"@context\": {\r\n    \"sdo\": \"http://schema.org/\",\r\n    \"arc\": \"http://purl.org/nfdi4plants/ontology/\",\r\n\r\n    \"Process\": \"sdo:Thing\",\r\n    \"ArcProcess\": \"arc:ARC#ARC_00000048\",\r\n\r\n    \"name\": \"arc:ARC#ARC_00000019\",\r\n    \"executesProtocol\": \"arc:ARC#ARC_00000086\",\r\n    \"performer\": \"arc:ARC#ARC_00000089\",\r\n    \"date\": \"arc:ARC#ARC_00000090\",\r\n    \"previousProcess\": \"arc:ARC#ARC_00000091\",\r\n    \"nextProcess\": \"arc:ARC#ARC_00000092\",\r\n    \"input\": \"arc:ARC#ARC_00000095\",\r\n    \"output\": \"arc:ARC#ARC_00000096\",\r\n\r\n    \"comments\": \"sdo:disambiguatingDescription\"\r\n  }\r\n}\r\n    "

__all__ = ["IContext_reflection", "context_jsonvalue", "context_str"]

