from __future__ import annotations
from dataclasses import dataclass
from ....fable_modules.fable_library.option import default_arg
from ....fable_modules.fable_library.reflection import (TypeInfo, string_type, option_type, record_type, int32_type)
from ....fable_modules.fable_library.types import Record

def _expr269() -> TypeInfo:
    return record_type("ARCtrl.ISA.Comment", [], Comment, lambda: [("ID", option_type(string_type)), ("Name", option_type(string_type)), ("Value", option_type(string_type))])


@dataclass(eq = False, repr = False, slots = True)
class Comment(Record):
    ID: str | None
    Name: str | None
    Value: str | None
    @staticmethod
    def make(id: str | None=None, name: str | None=None, value: str | None=None) -> Comment:
        return Comment(id, name, value)

    @staticmethod
    def create(Id: str | None=None, Name: str | None=None, Value: str | None=None) -> Comment:
        return Comment.make(Id, Name, Value)

    @staticmethod
    def from_string(name: str, value: str) -> Comment:
        return Comment.create(None, name, value)

    @staticmethod
    def to_string(comment: Comment) -> tuple[str, str]:
        return (default_arg(comment.Name, ""), default_arg(comment.Value, ""))

    def Copy(self, __unit: None=None) -> Comment:
        this: Comment = self
        return Comment.make(this.ID, this.Name, this.Value)


Comment_reflection = _expr269

def _expr270() -> TypeInfo:
    return record_type("ARCtrl.ISA.Remark", [], Remark, lambda: [("Line", int32_type), ("Value", string_type)])


@dataclass(eq = False, repr = False, slots = True)
class Remark(Record):
    Line: int
    Value: str
    @staticmethod
    def make(line: int, value: str) -> Remark:
        return Remark(line, value)

    @staticmethod
    def create(line: int, value: str) -> Remark:
        return Remark.make(line, value)

    @staticmethod
    def to_tuple(remark: Remark) -> tuple[int, str]:
        return (remark.Line, remark.Value)

    def Copy(self, __unit: None=None) -> Remark:
        this: Remark = self
        return Remark.make(this.Line, this.Value)


Remark_reflection = _expr270

__all__ = ["Comment_reflection", "Remark_reflection"]

