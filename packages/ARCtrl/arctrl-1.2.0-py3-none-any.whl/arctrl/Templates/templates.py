from __future__ import annotations
from collections.abc import Callable
from typing import Any
from ..fable_modules.fable_library.array_ import (filter, contains as contains_1, collect, add_range_in_place, append)
from ..fable_modules.fable_library.option import default_arg
from ..fable_modules.fable_library.reflection import (TypeInfo, class_type)
from ..fable_modules.fable_library.seq2 import Array_distinct
from ..fable_modules.fable_library.types import Array
from ..fable_modules.fable_library.util import (equals, safe_hash, uncurry2)
from ..ISA.ISA.JsonTypes.ontology_annotation import OntologyAnnotation
from .template import Template

def TemplatesAux_getComparer(match_all: bool | None=None) -> Callable[[bool, bool], bool]:
    if default_arg(match_all, False):
        def _arrow1729(e: bool, match_all: Any=match_all) -> Callable[[bool], bool]:
            def _arrow1728(e_1: bool) -> bool:
                return e and e_1

            return _arrow1728

        return _arrow1729

    else: 
        def _arrow1731(e_2: bool, match_all: Any=match_all) -> Callable[[bool], bool]:
            def _arrow1730(e_3: bool) -> bool:
                return e_2 or e_3

            return _arrow1730

        return _arrow1731



def TemplatesAux_filterOnTags(tag_getter: Callable[[Template], Array[OntologyAnnotation]], query_tags: Array[OntologyAnnotation], comparer: Callable[[bool, bool], bool], templates: Array[Template]) -> Array[Template]:
    def predicate(t: Template, tag_getter: Any=tag_getter, query_tags: Any=query_tags, comparer: Any=comparer, templates: Any=templates) -> bool:
        template_tags: Array[OntologyAnnotation] = tag_getter(t)
        is_valid: bool | None = None
        for idx in range(0, (len(query_tags) - 1) + 1, 1):
            class ObjectExpr1732:
                @property
                def Equals(self) -> Callable[[OntologyAnnotation, OntologyAnnotation], bool]:
                    return equals

                @property
                def GetHashCode(self) -> Callable[[OntologyAnnotation], int]:
                    return safe_hash

            contains: bool = contains_1(query_tags[idx], template_tags, ObjectExpr1732())
            is_valid_1: bool | None = is_valid
            if is_valid_1 is not None:
                maybe: bool = is_valid_1
                is_valid = comparer(maybe, contains)

            else: 
                is_valid = contains

        return default_arg(is_valid, False)

    return filter(predicate, templates)


def _expr1742() -> TypeInfo:
    return class_type("ARCtrl.Template.Templates", None, Templates)


class Templates:
    @staticmethod
    def get_distinct_tags(templates: Array[Template]) -> Array[OntologyAnnotation]:
        def mapping(t: Template) -> Array[OntologyAnnotation]:
            return t.Tags

        class ObjectExpr1733:
            @property
            def Equals(self) -> Callable[[OntologyAnnotation, OntologyAnnotation], bool]:
                return equals

            @property
            def GetHashCode(self) -> Callable[[OntologyAnnotation], int]:
                return safe_hash

        return Array_distinct(collect(mapping, templates, None), ObjectExpr1733())

    @staticmethod
    def get_distinct_endpoint_repositories(templates: Array[Template]) -> Array[OntologyAnnotation]:
        def mapping(t: Template) -> Array[OntologyAnnotation]:
            return t.EndpointRepositories

        class ObjectExpr1734:
            @property
            def Equals(self) -> Callable[[OntologyAnnotation, OntologyAnnotation], bool]:
                return equals

            @property
            def GetHashCode(self) -> Callable[[OntologyAnnotation], int]:
                return safe_hash

        return Array_distinct(collect(mapping, templates, None), ObjectExpr1734())

    @staticmethod
    def get_distinct_ontology_annotations(templates: Array[Template]) -> Array[OntologyAnnotation]:
        oas: Array[OntologyAnnotation] = []
        for idx in range(0, (len(templates) - 1) + 1, 1):
            t: Template = templates[idx]
            add_range_in_place(t.Tags, oas)
            add_range_in_place(t.EndpointRepositories, oas)
        class ObjectExpr1735:
            @property
            def Equals(self) -> Callable[[OntologyAnnotation, OntologyAnnotation], bool]:
                return equals

            @property
            def GetHashCode(self) -> Callable[[OntologyAnnotation], int]:
                return safe_hash

        return Array_distinct(list(oas), ObjectExpr1735())

    @staticmethod
    def filter_by_tags(query_tags: Array[OntologyAnnotation], match_all: bool | None=None) -> Callable[[Array[Template]], Array[Template]]:
        def _arrow1737(templates: Array[Template]) -> Array[Template]:
            def _arrow1736(t: Template) -> Array[OntologyAnnotation]:
                return t.Tags

            return TemplatesAux_filterOnTags(_arrow1736, query_tags, uncurry2(TemplatesAux_getComparer(match_all)), templates)

        return _arrow1737

    @staticmethod
    def filter_by_endpoint_repositories(query_tags: Array[OntologyAnnotation], match_all: bool | None=None) -> Callable[[Array[Template]], Array[Template]]:
        def _arrow1739(templates: Array[Template]) -> Array[Template]:
            def _arrow1738(t: Template) -> Array[OntologyAnnotation]:
                return t.EndpointRepositories

            return TemplatesAux_filterOnTags(_arrow1738, query_tags, uncurry2(TemplatesAux_getComparer(match_all)), templates)

        return _arrow1739

    @staticmethod
    def filter_by_ontology_annotation(query_tags: Array[OntologyAnnotation], match_all: bool | None=None) -> Callable[[Array[Template]], Array[Template]]:
        def _arrow1741(templates: Array[Template]) -> Array[Template]:
            def _arrow1740(t: Template) -> Array[OntologyAnnotation]:
                return append(t.Tags, t.EndpointRepositories, None)

            return TemplatesAux_filterOnTags(_arrow1740, query_tags, uncurry2(TemplatesAux_getComparer(match_all)), templates)

        return _arrow1741

    @staticmethod
    def filter_by_data_plant(templates: Array[Template]) -> Array[Template]:
        def predicate(t: Template) -> bool:
            return t.Organisation.IsOfficial()

        return filter(predicate, templates)


Templates_reflection = _expr1742

__all__ = ["TemplatesAux_getComparer", "TemplatesAux_filterOnTags", "Templates_reflection"]

