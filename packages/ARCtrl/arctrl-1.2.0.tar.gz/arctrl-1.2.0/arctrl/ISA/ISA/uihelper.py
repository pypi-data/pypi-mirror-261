from __future__ import annotations
from .ArcTypes.composite_cell import CompositeCell
from .JsonTypes.ontology_annotation import OntologyAnnotation

def update_with_oa(oa: OntologyAnnotation, cell: CompositeCell) -> CompositeCell:
    if cell.tag == 2:
        return CompositeCell.create_unitized(cell.fields[0], oa)

    elif cell.tag == 1:
        return CompositeCell.create_free_text(oa.NameText)

    else: 
        return CompositeCell.create_term(oa)



__all__ = ["update_with_oa"]

