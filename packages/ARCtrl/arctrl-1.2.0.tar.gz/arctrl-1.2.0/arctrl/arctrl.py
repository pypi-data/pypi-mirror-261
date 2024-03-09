from __future__ import annotations
from collections.abc import Callable
from typing import Any
from .ISA.ISA.JsonTypes.comment import Comment
from .ISA.ISA.JsonTypes.ontology_annotation import OntologyAnnotation
from .ISA.ISA.JsonTypes.person import Person
from .ISA.ISA.JsonTypes.publication import Publication
from .ISA.ISA.ArcTypes.composite_header import IOType, CompositeHeader
from .ISA.ISA.ArcTypes.composite_cell import CompositeCell
from .ISA.ISA.ArcTypes.composite_column import CompositeColumn
from .ISA.ISA.ArcTypes.arc_table import ArcTable
from .ISA.ISA.ArcTypes.arc_types import ArcAssay, ArcStudy, ArcInvestigation
from .Templates.template import Template, Organisation
from .Templates.templates import Templates
from .arc import ARC