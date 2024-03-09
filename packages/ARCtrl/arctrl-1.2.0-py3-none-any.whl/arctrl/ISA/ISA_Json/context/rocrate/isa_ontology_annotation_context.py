from __future__ import annotations
from dataclasses import dataclass
from .....fable_modules.fable_library.reflection import (TypeInfo, string_type, record_type)
from .....fable_modules.fable_library.types import Record
from .....fable_modules.fable_library.util import to_enumerable
from .....fable_modules.thoth_json_core.types import Json

def _expr940() -> TypeInfo:
    return record_type("ARCtrl.ISA.Json.ROCrateContext.OntologyAnnotation.IContext", [], IContext, lambda: [("sdo", string_type), ("arc", string_type), ("OntologyAnnotation", string_type), ("annotation_value", string_type), ("term_source", string_type), ("term_accession", string_type), ("comments", string_type)])


@dataclass(eq = False, repr = False, slots = True)
class IContext(Record):
    sdo: str
    arc: str
    OntologyAnnotation: str
    annotation_value: str
    term_source: str
    term_accession: str
    comments: str

IContext_reflection = _expr940

context_jsonvalue: Json = Json(5, to_enumerable([("sdo", Json(0, "http://schema.org/")), ("arc", Json(0, "http://purl.org/nfdi4plants/ontology/")), ("OntologyAnnotation", Json(0, "sdo:DefinedTerm")), ("annotationValue", Json(0, "sdo:name")), ("termSource", Json(0, "sdo:inDefinedTermSet")), ("termAccession", Json(0, "sdo:termCode")), ("comments", Json(0, "sdo:disambiguatingDescription"))]))

context_str: str = "\r\n{\r\n  \"@context\": {\r\n    \"sdo\": \"http://schema.org/\",\r\n    \"arc\": \"http://purl.org/nfdi4plants/ontology/\",\r\n\r\n    \"OntologyAnnotation\": \"sdo:DefinedTerm\",\r\n    \r\n    \"annotationValue\": \"sdo:name\",\r\n    \"termSource\": \"sdo:inDefinedTermSet\",\r\n    \"termAccession\": \"sdo:termCode\",\r\n    \"comments\": \"sdo:disambiguatingDescription\"\r\n  }\r\n}\r\n    "

__all__ = ["IContext_reflection", "context_jsonvalue", "context_str"]

