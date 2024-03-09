from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any
from ....fable_modules.fable_library.array_ import (map2, map as map_2)
from ....fable_modules.fable_library.list import (append, singleton, FSharpList, exists, try_find, map, filter)
from ....fable_modules.fable_library.option import map as map_1
from ....fable_modules.fable_library.reflection import (make_record, get_record_fields, TypeInfo, string_type, option_type, array_type, record_type)
from ....fable_modules.fable_library.types import (Array, Record)
from ....fable_modules.fable_library.util import equals
from ..helper import (Update_updateAppend, Update_updateOnlyByExisting, Update_updateOnlyByExistingAppend)
from ..helper import (Update_UpdateOptions, Option_mapDefault)
from .comment import (Comment, Comment_reflection)
from .ontology_annotation import (OntologyAnnotation, OntologyAnnotation_reflection)

def _expr322() -> TypeInfo:
    return record_type("ARCtrl.ISA.Publication", [], Publication, lambda: [("PubMedID", option_type(string_type)), ("DOI", option_type(string_type)), ("Authors", option_type(string_type)), ("Title", option_type(string_type)), ("Status", option_type(OntologyAnnotation_reflection())), ("Comments", option_type(array_type(Comment_reflection())))])


@dataclass(eq = False, repr = False, slots = True)
class Publication(Record):
    PubMedID: str | None
    DOI: str | None
    Authors: str | None
    Title: str | None
    Status: OntologyAnnotation | None
    Comments: Array[Comment] | None
    @staticmethod
    def make(pub_med_id: str | None=None, doi: str | None=None, authors: str | None=None, title: str | None=None, status: OntologyAnnotation | None=None, comments: Array[Comment] | None=None) -> Publication:
        return Publication(pub_med_id, doi, authors, title, status, comments)

    @staticmethod
    def create(PubMedID: str | None=None, Doi: str | None=None, Authors: str | None=None, Title: str | None=None, Status: OntologyAnnotation | None=None, Comments: Array[Comment] | None=None) -> Publication:
        return Publication.make(PubMedID, Doi, Authors, Title, Status, Comments)

    @staticmethod
    def empty() -> Publication:
        return Publication.create()

    @staticmethod
    def add(publications: FSharpList[Publication], publication: Publication) -> FSharpList[Publication]:
        return append(publications, singleton(publication))

    @staticmethod
    def exists_by_doi(doi: str, publications: FSharpList[Publication]) -> bool:
        def _arrow318(p: Publication) -> bool:
            return equals(p.DOI, doi)

        return exists(_arrow318, publications)

    @staticmethod
    def exists_by_pub_med_id(pub_med_id: str, publications: FSharpList[Publication]) -> bool:
        def _arrow319(p: Publication) -> bool:
            return equals(p.PubMedID, pub_med_id)

        return exists(_arrow319, publications)

    @staticmethod
    def try_get_by_doi(doi: str, publications: FSharpList[Publication]) -> Publication | None:
        def predicate(publication: Publication) -> bool:
            return equals(publication.DOI, doi)

        return try_find(predicate, publications)

    @staticmethod
    def update_by(predicate: Callable[[Publication], bool], update_option: Update_UpdateOptions, publication: Publication, publications: FSharpList[Publication]) -> FSharpList[Publication]:
        def mapping_3(p: Publication) -> Publication:
            if predicate(p):
                this: Update_UpdateOptions = update_option
                record_type_1: Publication = p
                record_type_2: Publication = publication
                if this.tag == 2:
                    def mapping(old_val: Any=None, new_val: Any=None, p: Any=p) -> Any:
                        return Update_updateAppend(old_val, new_val)

                    return make_record(Publication_reflection(), map2(mapping, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                elif this.tag == 1:
                    def mapping_1(old_val_1: Any=None, new_val_1: Any=None, p: Any=p) -> Any:
                        return Update_updateOnlyByExisting(old_val_1, new_val_1)

                    return make_record(Publication_reflection(), map2(mapping_1, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                elif this.tag == 3:
                    def mapping_2(old_val_2: Any=None, new_val_2: Any=None, p: Any=p) -> Any:
                        return Update_updateOnlyByExistingAppend(old_val_2, new_val_2)

                    return make_record(Publication_reflection(), map2(mapping_2, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                else: 
                    return record_type_2


            else: 
                return p


        return map(mapping_3, publications) if exists(predicate, publications) else publications

    @staticmethod
    def update_by_doi(update_option: Update_UpdateOptions, publication: Publication, publications: FSharpList[Publication]) -> FSharpList[Publication]:
        def predicate(p: Publication) -> bool:
            return equals(p.DOI, publication.DOI)

        return Publication.update_by(predicate, update_option, publication, publications)

    @staticmethod
    def update_by_pub_med_id(update_option: Update_UpdateOptions, publication: Publication, publications: FSharpList[Publication]) -> FSharpList[Publication]:
        def predicate(p: Publication) -> bool:
            return equals(p.PubMedID, publication.PubMedID)

        return Publication.update_by(predicate, update_option, publication, publications)

    @staticmethod
    def remove_by_doi(doi: str, publications: FSharpList[Publication]) -> FSharpList[Publication]:
        def _arrow320(p: Publication) -> bool:
            return not equals(p.DOI, doi)

        return filter(_arrow320, publications)

    @staticmethod
    def remove_by_pub_med_id(pub_med_id: str, publications: FSharpList[Publication]) -> FSharpList[Publication]:
        def _arrow321(p: Publication) -> bool:
            return not equals(p.PubMedID, pub_med_id)

        return filter(_arrow321, publications)

    @staticmethod
    def get_status(publication: Publication) -> OntologyAnnotation | None:
        return publication.Status

    @staticmethod
    def map_status(f: Callable[[OntologyAnnotation], OntologyAnnotation], publication: Publication) -> Publication:
        return Publication(publication.PubMedID, publication.DOI, publication.Authors, publication.Title, map_1(f, publication.Status), publication.Comments)

    @staticmethod
    def set_status(publication: Publication, status: OntologyAnnotation) -> Publication:
        return Publication(publication.PubMedID, publication.DOI, publication.Authors, publication.Title, status, publication.Comments)

    @staticmethod
    def get_comments(publication: Publication) -> Array[Comment] | None:
        return publication.Comments

    @staticmethod
    def map_comments(f: Callable[[Array[Comment]], Array[Comment]], publication: Publication) -> Publication:
        return Publication(publication.PubMedID, publication.DOI, publication.Authors, publication.Title, publication.Status, Option_mapDefault([], f, publication.Comments))

    @staticmethod
    def set_comments(publication: Publication, comments: Array[Comment]) -> Publication:
        return Publication(publication.PubMedID, publication.DOI, publication.Authors, publication.Title, publication.Status, comments)

    def Copy(self, __unit: None=None) -> Publication:
        this: Publication = self
        def mapping_1(array: Array[Comment]) -> Array[Comment]:
            def mapping(c: Comment, array: Any=array) -> Comment:
                return c.Copy()

            return map_2(mapping, array, None)

        comments: Array[Comment] | None = map_1(mapping_1, this.Comments)
        return Publication.make(this.PubMedID, this.DOI, this.Authors, this.Title, this.Status, comments)


Publication_reflection = _expr322

__all__ = ["Publication_reflection"]

