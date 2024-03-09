from __future__ import annotations
from typing import Any
from ....fable_modules.fable_library.option import default_arg
from ....fable_modules.fable_library.reflection import (TypeInfo, string_type, union_type)
from ....fable_modules.fable_library.types import (to_string, Array, Union)
from ....fable_modules.fable_library.util import int32_to_string
from ..JsonTypes.ontology_annotation import (OntologyAnnotation, OntologyAnnotation_reflection)
from ..JsonTypes.value import Value

def _expr438() -> TypeInfo:
    return union_type("ARCtrl.ISA.CompositeCell", [], CompositeCell, lambda: [[("Item", OntologyAnnotation_reflection())], [("Item", string_type)], [("Item1", string_type), ("Item2", OntologyAnnotation_reflection())]])


class CompositeCell(Union):
    def __init__(self, tag: int, *fields: Any) -> None:
        super().__init__()
        self.tag: int = tag or 0
        self.fields: Array[Any] = list(fields)

    @staticmethod
    def cases() -> list[str]:
        return ["Term", "FreeText", "Unitized"]

    @staticmethod
    def from_value(value: Value, unit: OntologyAnnotation | None=None) -> CompositeCell:
        (pattern_matching_result, t, i, i_1, u, f, f_1, u_1, s) = (None, None, None, None, None, None, None, None, None)
        if value.tag == 1:
            if unit is not None:
                pattern_matching_result = 2
                i_1 = value.fields[0]
                u = unit

            else: 
                pattern_matching_result = 1
                i = value.fields[0]


        elif value.tag == 2:
            if unit is not None:
                pattern_matching_result = 4
                f_1 = value.fields[0]
                u_1 = unit

            else: 
                pattern_matching_result = 3
                f = value.fields[0]


        elif value.tag == 3:
            if unit is None:
                pattern_matching_result = 5
                s = value.fields[0]

            else: 
                pattern_matching_result = 6


        elif unit is None:
            pattern_matching_result = 0
            t = value.fields[0]

        else: 
            pattern_matching_result = 6

        if pattern_matching_result == 0:
            return CompositeCell(0, t)

        elif pattern_matching_result == 1:
            return CompositeCell(1, int32_to_string(i))

        elif pattern_matching_result == 2:
            return CompositeCell(2, int32_to_string(i_1), u)

        elif pattern_matching_result == 3:
            return CompositeCell(1, to_string(f))

        elif pattern_matching_result == 4:
            return CompositeCell(2, to_string(f_1), u_1)

        elif pattern_matching_result == 5:
            return CompositeCell(1, s)

        elif pattern_matching_result == 6:
            raise Exception("could not convert value to cell, invalid combination of value and unit")


    @property
    def is_unitized(self, __unit: None=None) -> bool:
        this: CompositeCell = self
        return True if (this.tag == 2) else False

    @property
    def is_term(self, __unit: None=None) -> bool:
        this: CompositeCell = self
        return True if (this.tag == 0) else False

    @property
    def is_free_text(self, __unit: None=None) -> bool:
        this: CompositeCell = self
        return True if (this.tag == 1) else False

    def GetEmptyCell(self, __unit: None=None) -> CompositeCell:
        this: CompositeCell = self
        if this.tag == 2:
            return CompositeCell.empty_unitized()

        elif this.tag == 1:
            return CompositeCell.empty_free_text()

        else: 
            return CompositeCell.empty_term()


    def GetContent(self, __unit: None=None) -> Array[str]:
        this: CompositeCell = self
        if this.tag == 0:
            oa: OntologyAnnotation = this.fields[0]
            return [oa.NameText, default_arg(oa.TermSourceREF, ""), default_arg(oa.TermAccessionNumber, "")]

        elif this.tag == 2:
            oa_1: OntologyAnnotation = this.fields[1]
            return [this.fields[0], oa_1.NameText, default_arg(oa_1.TermSourceREF, ""), default_arg(oa_1.TermAccessionNumber, "")]

        else: 
            return [this.fields[0]]


    def ToUnitizedCell(self, __unit: None=None) -> CompositeCell:
        this: CompositeCell = self
        if this.tag == 1:
            return CompositeCell(2, "", OntologyAnnotation.create(None, this.fields[0]))

        elif this.tag == 0:
            return CompositeCell(2, "", this.fields[0])

        else: 
            return this


    def ToTermCell(self, __unit: None=None) -> CompositeCell:
        this: CompositeCell = self
        if this.tag == 2:
            return CompositeCell(0, this.fields[1])

        elif this.tag == 1:
            return CompositeCell(0, OntologyAnnotation.create(None, this.fields[0]))

        else: 
            return this


    def ToFreeTextCell(self, __unit: None=None) -> CompositeCell:
        this: CompositeCell = self
        if this.tag == 0:
            return CompositeCell(1, this.fields[0].NameText)

        elif this.tag == 2:
            return CompositeCell(1, this.fields[1].NameText)

        else: 
            return this


    @property
    def AsUnitized(self, __unit: None=None) -> tuple[str, OntologyAnnotation]:
        this: CompositeCell = self
        if this.tag == 2:
            return (this.fields[0], this.fields[1])

        else: 
            raise Exception("Not a Unitized cell.")


    @property
    def AsTerm(self, __unit: None=None) -> OntologyAnnotation:
        this: CompositeCell = self
        if this.tag == 0:
            return this.fields[0]

        else: 
            raise Exception("Not a Swate TermCell.")


    @property
    def AsFreeText(self, __unit: None=None) -> str:
        this: CompositeCell = self
        if this.tag == 1:
            return this.fields[0]

        else: 
            raise Exception("Not a Swate TermCell.")


    @staticmethod
    def create_term(oa: OntologyAnnotation) -> CompositeCell:
        return CompositeCell(0, oa)

    @staticmethod
    def create_term_from_string(name: str | None=None, tsr: str | None=None, tan: str | None=None) -> CompositeCell:
        return CompositeCell(0, OntologyAnnotation.from_string(name, tsr, tan))

    @staticmethod
    def create_unitized(value: str, oa: OntologyAnnotation | None=None) -> CompositeCell:
        return CompositeCell(2, value, default_arg(oa, OntologyAnnotation.empty()))

    @staticmethod
    def create_unitized_from_string(value: str, name: str | None=None, tsr: str | None=None, tan: str | None=None) -> CompositeCell:
        tupled_arg: tuple[str, OntologyAnnotation] = (value, OntologyAnnotation.from_string(name, tsr, tan))
        return CompositeCell(2, tupled_arg[0], tupled_arg[1])

    @staticmethod
    def create_free_text(value: str) -> CompositeCell:
        return CompositeCell(1, value)

    @staticmethod
    def empty_term() -> CompositeCell:
        return CompositeCell(0, OntologyAnnotation.empty())

    @staticmethod
    def empty_free_text() -> CompositeCell:
        return CompositeCell(1, "")

    @staticmethod
    def empty_unitized() -> CompositeCell:
        return CompositeCell(2, "", OntologyAnnotation.empty())

    def __str__(self, __unit: None=None) -> str:
        this: CompositeCell = self
        if this.tag == 1:
            return this.fields[0]

        elif this.tag == 2:
            return ((("" + this.fields[0]) + " ") + this.fields[1].NameText) + ""

        else: 
            return ("" + this.fields[0].NameText) + ""


    @staticmethod
    def term(oa: OntologyAnnotation) -> CompositeCell:
        return CompositeCell(0, oa)

    @staticmethod
    def free_text(s: str) -> CompositeCell:
        return CompositeCell(1, s)

    @staticmethod
    def unitized(v: str, oa: OntologyAnnotation) -> CompositeCell:
        return CompositeCell(2, v, oa)


CompositeCell_reflection = _expr438

__all__ = ["CompositeCell_reflection"]

