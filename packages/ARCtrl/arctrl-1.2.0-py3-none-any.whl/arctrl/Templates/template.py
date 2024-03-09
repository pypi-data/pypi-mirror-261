from __future__ import annotations
from typing import Any
from ..fable_modules.fable_library.array_ import equals_with
from ..fable_modules.fable_library.date import (equals as equals_1, now, to_universal_time)
from ..fable_modules.fable_library.guid import new_guid
from ..fable_modules.fable_library.option import default_arg
from ..fable_modules.fable_library.reflection import (TypeInfo, string_type, union_type, class_type)
from ..fable_modules.fable_library.types import (Array, Union)
from ..fable_modules.fable_library.util import (equals, string_hash, safe_hash, identity_hash)
from ..ISA.ISA.ArcTypes.arc_table import ArcTable
from ..ISA.ISA.JsonTypes.ontology_annotation import OntologyAnnotation
from ..ISA.ISA.JsonTypes.person import Person
from ..sem_ver import (SemVer_tryOfString_Z721C83C5, SemVer)

def _expr1723() -> TypeInfo:
    return union_type("ARCtrl.Template.Organisation", [], Organisation, lambda: [[], [("Item", string_type)]])


class Organisation(Union):
    def __init__(self, tag: int, *fields: Any) -> None:
        super().__init__()
        self.tag: int = tag or 0
        self.fields: Array[Any] = list(fields)

    @staticmethod
    def cases() -> list[str]:
        return ["DataPLANT", "Other"]

    @staticmethod
    def of_string(str_1: str) -> Organisation:
        return Organisation(0) if (str_1.lower() == "dataplant") else Organisation(1, str_1)

    def __str__(self, __unit: None=None) -> str:
        this: Organisation = self
        return this.fields[0] if (this.tag == 1) else "DataPLANT"

    def IsOfficial(self, __unit: None=None) -> bool:
        this: Organisation = self
        return equals(this, Organisation(0))


Organisation_reflection = _expr1723

def _expr1727() -> TypeInfo:
    return class_type("ARCtrl.Template.Template", None, Template)


class Template:
    def __init__(self, id: str, table: ArcTable, name: str | None=None, description: str | None=None, organisation: Organisation | None=None, version: str | None=None, authors: Array[Person] | None=None, repos: Array[OntologyAnnotation] | None=None, tags: Array[OntologyAnnotation] | None=None, last_updated: Any | None=None) -> None:
        name_1: str = default_arg(name, "")
        description_1: str = default_arg(description, "")
        organisation_1: Organisation = default_arg(organisation, Organisation(1, "Custom Organisation"))
        version_1: str = default_arg(version, "0.0.0")
        authors_1: Array[Person] = default_arg(authors, [])
        repos_1: Array[OntologyAnnotation] = default_arg(repos, [])
        tags_1: Array[OntologyAnnotation] = default_arg(tags, [])
        def _arrow1726(__unit: None=None) -> Any:
            copy_of_struct: Any = now()
            return to_universal_time(copy_of_struct)

        last_updated_1: Any = default_arg(last_updated, _arrow1726())
        self._Id: str = id
        self._Table: ArcTable = table
        self._Name: str = name_1
        self._Description: str = description_1
        self._Organisation: Organisation = organisation_1
        self._Version: str = version_1
        self._Authors: Array[Person] = authors_1
        self._EndpointRepositories: Array[OntologyAnnotation] = repos_1
        self._Tags: Array[OntologyAnnotation] = tags_1
        self._LastUpdated: Any = last_updated_1

    @property
    def Id(self, __unit: None=None) -> str:
        __: Template = self
        return __._Id

    @Id.setter
    def Id(self, v: str) -> None:
        __: Template = self
        __._Id = v

    @property
    def Table(self, __unit: None=None) -> ArcTable:
        __: Template = self
        return __._Table

    @Table.setter
    def Table(self, v: ArcTable) -> None:
        __: Template = self
        __._Table = v

    @property
    def Name(self, __unit: None=None) -> str:
        __: Template = self
        return __._Name

    @Name.setter
    def Name(self, v: str) -> None:
        __: Template = self
        __._Name = v

    @property
    def Description(self, __unit: None=None) -> str:
        __: Template = self
        return __._Description

    @Description.setter
    def Description(self, v: str) -> None:
        __: Template = self
        __._Description = v

    @property
    def Organisation(self, __unit: None=None) -> Organisation:
        __: Template = self
        return __._Organisation

    @Organisation.setter
    def Organisation(self, v: Organisation) -> None:
        __: Template = self
        __._Organisation = v

    @property
    def Version(self, __unit: None=None) -> str:
        __: Template = self
        return __._Version

    @Version.setter
    def Version(self, v: str) -> None:
        __: Template = self
        __._Version = v

    @property
    def Authors(self, __unit: None=None) -> Array[Person]:
        __: Template = self
        return __._Authors

    @Authors.setter
    def Authors(self, v: Array[Person]) -> None:
        __: Template = self
        __._Authors = v

    @property
    def EndpointRepositories(self, __unit: None=None) -> Array[OntologyAnnotation]:
        __: Template = self
        return __._EndpointRepositories

    @EndpointRepositories.setter
    def EndpointRepositories(self, v: Array[OntologyAnnotation]) -> None:
        __: Template = self
        __._EndpointRepositories = v

    @property
    def Tags(self, __unit: None=None) -> Array[OntologyAnnotation]:
        __: Template = self
        return __._Tags

    @Tags.setter
    def Tags(self, v: Array[OntologyAnnotation]) -> None:
        __: Template = self
        __._Tags = v

    @property
    def LastUpdated(self, __unit: None=None) -> Any:
        __: Template = self
        return __._LastUpdated

    @LastUpdated.setter
    def LastUpdated(self, v: Any) -> None:
        __: Template = self
        __._LastUpdated = v

    @staticmethod
    def make(id: str, table: ArcTable, name: str, description: str, organisation: Organisation, version: str, authors: Array[Person], repos: Array[OntologyAnnotation], tags: Array[OntologyAnnotation], last_updated: Any) -> Template:
        return Template(id, table, name, description, organisation, version, authors, repos, tags, last_updated)

    @staticmethod
    def create(id: str, table: ArcTable, name: str | None=None, description: str | None=None, organisation: Organisation | None=None, version: str | None=None, authors: Array[Person] | None=None, repos: Array[OntologyAnnotation] | None=None, tags: Array[OntologyAnnotation] | None=None, last_updated: Any | None=None) -> Template:
        return Template(id, table, name, description, organisation, version, authors, repos, tags, last_updated)

    @staticmethod
    def init(template_name: str) -> Template:
        return Template(new_guid(), ArcTable.init(template_name), template_name)

    @property
    def SemVer(self, __unit: None=None) -> SemVer | None:
        this: Template = self
        return SemVer_tryOfString_Z721C83C5(this.Version)

    def ReferenceEquals(self, other: Template) -> bool:
        this: Template = self
        return this is other

    def StructurallyEquals(self, other: Template) -> bool:
        this: Template = self
        return equals_1(this.LastUpdated, other.LastUpdated) if (equals_with(equals, this.Tags, other.Tags) if (equals_with(equals, this.EndpointRepositories, other.EndpointRepositories) if (equals_with(equals, this.Authors, other.Authors) if ((this.Version == other.Version) if (equals(this.Organisation, other.Organisation) if ((this.Name == other.Name) if (equals(this.Table, other.Table) if (this.Id == other.Id) else False) else False) else False) else False) else False) else False) else False) else False

    def __eq__(self, other: Any=None) -> bool:
        this: Template = self
        return this.StructurallyEquals(other) if isinstance(other, Template) else False

    def __hash__(self, __unit: None=None) -> int:
        this: Template = self
        def _arrow1724(__unit: None=None) -> int:
            copy_of_struct: str = this.Id
            return string_hash(copy_of_struct)

        def _arrow1725(__unit: None=None) -> int:
            copy_of_struct_1: Any = this.LastUpdated
            return safe_hash(copy_of_struct_1)

        return (((((((_arrow1724() + safe_hash(this.Table)) + string_hash(this.Name)) + safe_hash(this.Organisation)) + string_hash(this.Version)) + identity_hash(this.Authors)) + identity_hash(this.EndpointRepositories)) + identity_hash(this.Tags)) + _arrow1725()


Template_reflection = _expr1727

def Template__ctor_4AC720A8(id: str, table: ArcTable, name: str | None=None, description: str | None=None, organisation: Organisation | None=None, version: str | None=None, authors: Array[Person] | None=None, repos: Array[OntologyAnnotation] | None=None, tags: Array[OntologyAnnotation] | None=None, last_updated: Any | None=None) -> Template:
    return Template(id, table, name, description, organisation, version, authors, repos, tags, last_updated)


__all__ = ["Organisation_reflection", "Template_reflection"]

