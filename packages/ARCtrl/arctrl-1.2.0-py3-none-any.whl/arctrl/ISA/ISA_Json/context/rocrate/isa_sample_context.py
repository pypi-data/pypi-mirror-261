from __future__ import annotations
from dataclasses import dataclass
from .....fable_modules.fable_library.reflection import (TypeInfo, string_type, record_type)
from .....fable_modules.fable_library.types import Record
from .....fable_modules.fable_library.util import to_enumerable
from .....fable_modules.thoth_json_core.types import Json

def _expr965() -> TypeInfo:
    return record_type("ARCtrl.ISA.Json.ROCrateContext.Sample.IContext", [], IContext, lambda: [("sdo", string_type), ("arc", string_type), ("Sample", string_type), ("ArcSample", string_type), ("name", string_type), ("characteristics", string_type), ("factor_values", string_type), ("derives_from", string_type)])


@dataclass(eq = False, repr = False, slots = True)
class IContext(Record):
    sdo: str
    arc: str
    Sample: str
    ArcSample: str
    name: str
    characteristics: str
    factor_values: str
    derives_from: str

IContext_reflection = _expr965

context_jsonvalue: Json = Json(5, to_enumerable([("sdo", Json(0, "http://schema.org/")), ("arc", Json(0, "http://purl.org/nfdi4plants/ontology/")), ("Sample", Json(0, "sdo:Thing")), ("ArcSample", Json(0, "arc:ARC#ARC_00000070")), ("name", Json(0, "arc:name")), ("characteristics", Json(0, "arc:ARC#ARC_00000080")), ("factorValues", Json(0, "arc:ARC#ARC_00000083")), ("derivesFrom", Json(0, "arc:ARC#ARC_00000082"))]))

context_str: str = "\r\n{\r\n  \"@context\": {\r\n    \"sdo\": \"http://schema.org/\",\r\n    \"arc\": \"http://purl.org/nfdi4plants/ontology/\",\r\n\r\n    \"Sample\": \"sdo:Thing\",\r\n    \"ArcSample\": \"arc:ARC#ARC_00000070\",\r\n\r\n    \"name\": \"arc:name\",\r\n    \"characteristics\": \"arc:ARC#ARC_00000080\",\r\n    \"factorValues\": \"arc:ARC#ARC_00000083\",\r\n    \"derivesFrom\": \"arc:ARC#ARC_00000082\"\r\n  }\r\n}\r\n    "

__all__ = ["IContext_reflection", "context_jsonvalue", "context_str"]

