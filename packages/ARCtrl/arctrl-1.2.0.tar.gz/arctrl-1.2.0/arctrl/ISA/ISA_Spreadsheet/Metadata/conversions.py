from __future__ import annotations
from collections.abc import Callable
from typing import (Any, TypeVar)
from ....fable_modules.fable_library.array_ import (fold, map3, fill, equals_with, map)
from ....fable_modules.fable_library.list import (empty, of_array, FSharpList, fold as fold_1, map as map_1)
from ....fable_modules.fable_library.option import (some, value)
from ....fable_modules.fable_library.string_ import (to_fail, printf, to_text)
from ....fable_modules.fable_library.types import Array
from ....fable_modules.fable_library.util import equals
from ...ISA.JsonTypes.component import (Component_fromString_Z61E08C1, Component, Component_toString_Z609B8895)
from ...ISA.JsonTypes.ontology_annotation import OntologyAnnotation
from ...ISA.JsonTypes.protocol_parameter import ProtocolParameter
from ...ISA_Spreadsheet.collection_aux import Array_map4

__A = TypeVar("__A")

_T = TypeVar("_T")

def Option_fromValueWithDefault(d: __A, v: __A) -> __A | None:
    if equals(d, v):
        return None

    else: 
        return some(v)



def Option_mapDefault(d: _T, f: Callable[[_T], _T], o: _T | None=None) -> _T | None:
    return Option_fromValueWithDefault(d, f(d) if (o is None) else f(value(o)))


def OntologyAnnotation_getLengthOfAggregatedStrings(separator: str, strings: Array[str]) -> int:
    def folder(l: int, s: str, separator: Any=separator, strings: Any=strings) -> int:
        if s == "":
            return l

        elif l == 0:
            return len(s.split(separator))

        elif l == len(s.split(separator)):
            return l

        else: 
            return to_fail(printf("The length of the aggregated string %s does not match the length of the others"))(s)


    return fold(folder, 0, strings)


def OntologyAnnotation_fromAggregatedStrings(separator: str, terms: str, source: str, accessions: str) -> Array[OntologyAnnotation]:
    l: int = OntologyAnnotation_getLengthOfAggregatedStrings(separator, [terms, source, accessions]) or 0
    if l == 0:
        return []

    else: 
        def _arrow614(a: str, b: str, c: str, separator: Any=separator, terms: Any=terms, source: Any=source, accessions: Any=accessions) -> OntologyAnnotation:
            return OntologyAnnotation.from_string(a, b, c)

        return map3(_arrow614, fill([0] * l, 0, l, "") if (terms == "") else terms.split(separator), fill([0] * l, 0, l, "") if (source == "") else source.split(separator), fill([0] * l, 0, l, "") if (accessions == "") else accessions.split(separator), None)



def OntologyAnnotation_toAggregatedStrings(separator: str, oas: Array[OntologyAnnotation]) -> dict[str, Any]:
    first: bool = True
    def _arrow615(x: OntologyAnnotation, y: OntologyAnnotation, separator: Any=separator, oas: Any=oas) -> bool:
        return equals(x, y)

    if equals_with(_arrow615, oas, []):
        return {
            "TermAccessionNumberAgg": "",
            "TermNameAgg": "",
            "TermSourceREFAgg": ""
        }

    else: 
        def folder(tupled_arg: tuple[str, str, str], term: dict[str, Any], separator: Any=separator, oas: Any=oas) -> tuple[str, str, str]:
            nonlocal first
            if first:
                first = False
                return (term["TermName"], term["TermSourceREF"], term["TermAccessionNumber"])

            else: 
                return (to_text(printf("%s%c%s"))(tupled_arg[0])(separator)(term["TermName"]), to_text(printf("%s%c%s"))(tupled_arg[1])(separator)(term["TermSourceREF"]), to_text(printf("%s%c%s"))(tupled_arg[2])(separator)(term["TermAccessionNumber"]))


        def mapping(oa: OntologyAnnotation, separator: Any=separator, oas: Any=oas) -> dict[str, Any]:
            return OntologyAnnotation.to_string(oa)

        tupled_arg_1: tuple[str, str, str] = fold(folder, ("", "", ""), map(mapping, oas, None))
        return {
            "TermAccessionNumberAgg": tupled_arg_1[2],
            "TermNameAgg": tupled_arg_1[0],
            "TermSourceREFAgg": tupled_arg_1[1]
        }



def Component_fromAggregatedStrings(separator: str, names: str, terms: str, source: str, accessions: str) -> FSharpList[Component]:
    l: int = OntologyAnnotation_getLengthOfAggregatedStrings(separator, [names, terms, source, accessions]) or 0
    if l == 0:
        return empty()

    else: 
        def _arrow616(a: str, b: str, c: str, d: str, separator: Any=separator, names: Any=names, terms: Any=terms, source: Any=source, accessions: Any=accessions) -> Component:
            return Component_fromString_Z61E08C1(a, b, c, d)

        return of_array(Array_map4(_arrow616, fill([0] * l, 0, l, "") if (names == "") else names.split(separator), fill([0] * l, 0, l, "") if (terms == "") else terms.split(separator), fill([0] * l, 0, l, "") if (source == "") else source.split(separator), fill([0] * l, 0, l, "") if (accessions == "") else accessions.split(separator)))



def Component_toAggregatedStrings(separator: str, cs: FSharpList[Component]) -> dict[str, Any]:
    first: bool = True
    if equals(cs, empty()):
        return {
            "NameAgg": "",
            "TermAccessionNumberAgg": "",
            "TermNameAgg": "",
            "TermSourceREFAgg": ""
        }

    else: 
        def folder(tupled_arg: tuple[str, str, str, str], tupled_arg_1: tuple[str, dict[str, Any]], separator: Any=separator, cs: Any=cs) -> tuple[str, str, str, str]:
            nonlocal first
            name: str = tupled_arg_1[0]
            term: dict[str, Any] = tupled_arg_1[1]
            if first:
                first = False
                return (name, term["TermName"], term["TermSourceREF"], term["TermAccessionNumber"])

            else: 
                return (to_text(printf("%s%c%s"))(tupled_arg[0])(separator)(name), to_text(printf("%s%c%s"))(tupled_arg[1])(separator)(term["TermName"]), to_text(printf("%s%c%s"))(tupled_arg[2])(separator)(term["TermSourceREF"]), to_text(printf("%s%c%s"))(tupled_arg[3])(separator)(term["TermAccessionNumber"]))


        def mapping(c: Component, separator: Any=separator, cs: Any=cs) -> tuple[str, dict[str, Any]]:
            return Component_toString_Z609B8895(c)

        tupled_arg_2: tuple[str, str, str, str] = fold_1(folder, ("", "", "", ""), map_1(mapping, cs))
        return {
            "NameAgg": tupled_arg_2[0],
            "TermAccessionNumberAgg": tupled_arg_2[3],
            "TermNameAgg": tupled_arg_2[1],
            "TermSourceREFAgg": tupled_arg_2[2]
        }



def ProtocolParameter_fromAggregatedStrings(separator: str, terms: str, source: str, accessions: str) -> Array[ProtocolParameter]:
    def mapping(arg: OntologyAnnotation, separator: Any=separator, terms: Any=terms, source: Any=source, accessions: Any=accessions) -> ProtocolParameter:
        def f2(parameter_name: OntologyAnnotation | None=None, arg: Any=arg) -> ProtocolParameter:
            return ProtocolParameter.make(None, parameter_name)

        return f2(arg)

    return map(mapping, OntologyAnnotation_fromAggregatedStrings(separator, terms, source, accessions), None)


def ProtocolParameter_toAggregatedStrings(separator: str, oas: FSharpList[ProtocolParameter]) -> dict[str, Any]:
    first: bool = True
    if equals(oas, empty()):
        return {
            "TermAccessionNumberAgg": "",
            "TermNameAgg": "",
            "TermSourceREFAgg": ""
        }

    else: 
        def folder(tupled_arg: tuple[str, str, str], term: dict[str, Any], separator: Any=separator, oas: Any=oas) -> tuple[str, str, str]:
            nonlocal first
            if first:
                first = False
                return (term["TermName"], term["TermSourceREF"], term["TermAccessionNumber"])

            else: 
                return (to_text(printf("%s%c%s"))(tupled_arg[0])(separator)(term["TermName"]), to_text(printf("%s%c%s"))(tupled_arg[1])(separator)(term["TermSourceREF"]), to_text(printf("%s%c%s"))(tupled_arg[2])(separator)(term["TermAccessionNumber"]))


        def mapping(pp: ProtocolParameter, separator: Any=separator, oas: Any=oas) -> dict[str, Any]:
            return ProtocolParameter.to_string(pp)

        tupled_arg_1: tuple[str, str, str] = fold_1(folder, ("", "", ""), map_1(mapping, oas))
        return {
            "TermAccessionNumberAgg": tupled_arg_1[2],
            "TermNameAgg": tupled_arg_1[0],
            "TermSourceREFAgg": tupled_arg_1[1]
        }



__all__ = ["Option_fromValueWithDefault", "Option_mapDefault", "OntologyAnnotation_getLengthOfAggregatedStrings", "OntologyAnnotation_fromAggregatedStrings", "OntologyAnnotation_toAggregatedStrings", "Component_fromAggregatedStrings", "Component_toAggregatedStrings", "ProtocolParameter_fromAggregatedStrings", "ProtocolParameter_toAggregatedStrings"]

