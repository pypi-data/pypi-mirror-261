from __future__ import annotations
from collections.abc import Callable
from typing import Any
from ....fable_modules.fable_library.array_ import (map, contains as contains_1, append as append_3, equals_with, remove_in_place, add_range_in_place)
from ....fable_modules.fable_library.list import (FSharpList, empty, of_array, to_array as to_array_1, map as map_3, of_seq, unzip)
from ....fable_modules.fable_library.option import (default_arg, map as map_1)
from ....fable_modules.fable_library.range import range_big_int
from ....fable_modules.fable_library.reflection import (TypeInfo, class_type)
from ....fable_modules.fable_library.reg_exp import (get_item, groups)
from ....fable_modules.fable_library.resize_array import find_index
from ....fable_modules.fable_library.seq import (to_array, filter, contains, for_all, length, fold, to_list, delay, map as map_2, item, choose, exists, try_find_index, remove_at, try_find, append as append_4, collect, concat)
from ....fable_modules.fable_library.seq2 import (Array_distinct, distinct_by)
from ....fable_modules.fable_library.string_ import (to_text, printf)
from ....fable_modules.fable_library.types import (Array, FSharpRef)
from ....fable_modules.fable_library.util import (string_hash, IEnumerable_1, get_enumerator, dispose, equals, safe_hash, to_enumerable, ignore)
from ..helper import (Option_fromValueWithDefault, HashCodes_boxHashArray, HashCodes_boxHashOption, ResizeArray_map, ResizeArray_filter, ResizeArray_choose)
from ..identifier import (is_missing_identifier, Assay_fileNameFromIdentifier, create_missing_identifier, Assay_identifierFromFileName, Study_fileNameFromIdentifier, Study_identifierFromFileName)
from ..JsonTypes.assay import (Assay_create_3D372A24, Assay)
from ..JsonTypes.assay_materials import (AssayMaterials, AssayMaterials_create_Z253F0553, AssayMaterials_get_empty)
from ..JsonTypes.comment import (Comment, Remark)
from ..JsonTypes.factor import Factor
from ..JsonTypes.investigation import (Investigation_create_4AD66BBE, Investigation)
from ..JsonTypes.ontology_annotation import OntologyAnnotation
from ..JsonTypes.ontology_source_reference import OntologySourceReference
from ..JsonTypes.person import Person
from ..JsonTypes.process import Process
from ..JsonTypes.process_sequence import (get_samples, get_materials, get_data, get_characteristics, get_units, get_protocols, get_sources)
from ..JsonTypes.protocol import Protocol
from ..JsonTypes.publication import Publication
from ..JsonTypes.study import (Study_create_Z2D28E954, Study)
from ..JsonTypes.study_materials import (StudyMaterials, StudyMaterials_create_1BE9FA55, StudyMaterials_get_empty)
from ..JsonTypes.value import Value
from ..regex import ActivePatterns__007CRegex_007C__007C
from .arc_table import ArcTable
from .arc_tables import (ArcTables, ArcTables_reflection, ArcTablesAux_getIOMap, ArcTablesAux_applyIOMap)
from .composite_cell import CompositeCell
from .composite_column import CompositeColumn
from .composite_header import CompositeHeader

def _expr703() -> TypeInfo:
    return class_type("ARCtrl.ISA.ArcAssay", None, ArcAssay, ArcTables_reflection())


class ArcAssay(ArcTables):
    def __init__(self, identifier: str, measurement_type: OntologyAnnotation | None=None, technology_type: OntologyAnnotation | None=None, technology_platform: OntologyAnnotation | None=None, tables: Array[ArcTable] | None=None, performers: Array[Person] | None=None, comments: Array[Comment] | None=None) -> None:
        super().__init__(default_arg(tables, []))
        performers_1: Array[Person] = default_arg(performers, [])
        comments_1: Array[Comment] = default_arg(comments, [])
        self.identifier_004096: str = identifier
        self.investigation: ArcInvestigation | None = None
        self.measurement_type_004098: OntologyAnnotation | None = measurement_type
        self.technology_type_004099: OntologyAnnotation | None = technology_type
        self.technology_platform_0040100: OntologyAnnotation | None = technology_platform
        self.performers_0040101_002D1: Array[Person] = performers_1
        self.comments_0040102_002D1: Array[Comment] = comments_1
        self.static_hash: int = 0

    @property
    def Identifier(self, __unit: None=None) -> str:
        this: ArcAssay = self
        return this.identifier_004096

    @Identifier.setter
    def Identifier(self, i: str) -> None:
        this: ArcAssay = self
        this.identifier_004096 = i

    @property
    def Investigation(self, __unit: None=None) -> ArcInvestigation | None:
        this: ArcAssay = self
        return this.investigation

    @Investigation.setter
    def Investigation(self, i: ArcInvestigation | None=None) -> None:
        this: ArcAssay = self
        this.investigation = i

    @property
    def MeasurementType(self, __unit: None=None) -> OntologyAnnotation | None:
        this: ArcAssay = self
        return this.measurement_type_004098

    @MeasurementType.setter
    def MeasurementType(self, n: OntologyAnnotation | None=None) -> None:
        this: ArcAssay = self
        this.measurement_type_004098 = n

    @property
    def TechnologyType(self, __unit: None=None) -> OntologyAnnotation | None:
        this: ArcAssay = self
        return this.technology_type_004099

    @TechnologyType.setter
    def TechnologyType(self, n: OntologyAnnotation | None=None) -> None:
        this: ArcAssay = self
        this.technology_type_004099 = n

    @property
    def TechnologyPlatform(self, __unit: None=None) -> OntologyAnnotation | None:
        this: ArcAssay = self
        return this.technology_platform_0040100

    @TechnologyPlatform.setter
    def TechnologyPlatform(self, n: OntologyAnnotation | None=None) -> None:
        this: ArcAssay = self
        this.technology_platform_0040100 = n

    @property
    def Performers(self, __unit: None=None) -> Array[Person]:
        this: ArcAssay = self
        return this.performers_0040101_002D1

    @Performers.setter
    def Performers(self, n: Array[Person]) -> None:
        this: ArcAssay = self
        this.performers_0040101_002D1 = n

    @property
    def Comments(self, __unit: None=None) -> Array[Comment]:
        this: ArcAssay = self
        return this.comments_0040102_002D1

    @Comments.setter
    def Comments(self, n: Array[Comment]) -> None:
        this: ArcAssay = self
        this.comments_0040102_002D1 = n

    @property
    def StaticHash(self, __unit: None=None) -> int:
        this: ArcAssay = self
        return this.static_hash

    @StaticHash.setter
    def StaticHash(self, h: int) -> None:
        this: ArcAssay = self
        this.static_hash = h or 0

    @staticmethod
    def init(identifier: str) -> ArcAssay:
        return ArcAssay(identifier)

    @staticmethod
    def create(identifier: str, measurement_type: OntologyAnnotation | None=None, technology_type: OntologyAnnotation | None=None, technology_platform: OntologyAnnotation | None=None, tables: Array[ArcTable] | None=None, performers: Array[Person] | None=None, comments: Array[Comment] | None=None) -> ArcAssay:
        return ArcAssay(identifier, measurement_type, technology_type, technology_platform, tables, performers, comments)

    @staticmethod
    def make(identifier: str, measurement_type: OntologyAnnotation | None, technology_type: OntologyAnnotation | None, technology_platform: OntologyAnnotation | None, tables: Array[ArcTable], performers: Array[Person], comments: Array[Comment]) -> ArcAssay:
        return ArcAssay(identifier, measurement_type, technology_type, technology_platform, tables, performers, comments)

    @staticmethod
    def FileName() -> str:
        return "isa.assay.xlsx"

    @property
    def StudiesRegisteredIn(self, __unit: None=None) -> Array[ArcStudy]:
        this: ArcAssay = self
        match_value: ArcInvestigation | None = this.Investigation
        if match_value is None:
            return []

        else: 
            i: ArcInvestigation = match_value
            def predicate(s: ArcStudy) -> bool:
                source: Array[str] = s.RegisteredAssayIdentifiers
                class ObjectExpr655:
                    @property
                    def Equals(self) -> Callable[[str, str], bool]:
                        def _arrow654(x: str, y: str) -> bool:
                            return x == y

                        return _arrow654

                    @property
                    def GetHashCode(self) -> Callable[[str], int]:
                        return string_hash

                return contains(this.Identifier, source, ObjectExpr655())

            return to_array(filter(predicate, i.Studies))


    @staticmethod
    def add_table(table: ArcTable, index: int | None=None) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow656(assay: ArcAssay) -> ArcAssay:
            c: ArcAssay = assay.Copy()
            c.AddTable(table, index)
            return c

        return _arrow656

    @staticmethod
    def add_tables(tables: IEnumerable_1[ArcTable], index: int | None=None) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow657(assay: ArcAssay) -> ArcAssay:
            c: ArcAssay = assay.Copy()
            c.AddTables(tables, index)
            return c

        return _arrow657

    @staticmethod
    def init_table(table_name: str, index: int | None=None) -> Callable[[ArcAssay], tuple[ArcAssay, ArcTable]]:
        def _arrow658(assay: ArcAssay) -> tuple[ArcAssay, ArcTable]:
            c: ArcAssay = assay.Copy()
            return (c, c.InitTable(table_name, index))

        return _arrow658

    @staticmethod
    def init_tables(table_names: IEnumerable_1[str], index: int | None=None) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow659(assay: ArcAssay) -> ArcAssay:
            c: ArcAssay = assay.Copy()
            c.InitTables(table_names, index)
            return c

        return _arrow659

    @staticmethod
    def get_table_at(index: int) -> Callable[[ArcAssay], ArcTable]:
        def _arrow660(assay: ArcAssay) -> ArcTable:
            new_assay: ArcAssay = assay.Copy()
            return new_assay.GetTableAt(index)

        return _arrow660

    @staticmethod
    def get_table(name: str) -> Callable[[ArcAssay], ArcTable]:
        def _arrow661(assay: ArcAssay) -> ArcTable:
            new_assay: ArcAssay = assay.Copy()
            return new_assay.GetTable(name)

        return _arrow661

    @staticmethod
    def update_table_at(index: int, table: ArcTable) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow662(assay: ArcAssay) -> ArcAssay:
            new_assay: ArcAssay = assay.Copy()
            new_assay.UpdateTableAt(index, table)
            return new_assay

        return _arrow662

    @staticmethod
    def update_table(name: str, table: ArcTable) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow663(assay: ArcAssay) -> ArcAssay:
            new_assay: ArcAssay = assay.Copy()
            new_assay.UpdateTable(name, table)
            return new_assay

        return _arrow663

    @staticmethod
    def set_table_at(index: int, table: ArcTable) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow664(assay: ArcAssay) -> ArcAssay:
            new_assay: ArcAssay = assay.Copy()
            new_assay.SetTableAt(index, table)
            return new_assay

        return _arrow664

    @staticmethod
    def set_table(name: str, table: ArcTable) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow665(assay: ArcAssay) -> ArcAssay:
            new_assay: ArcAssay = assay.Copy()
            new_assay.SetTable(name, table)
            return new_assay

        return _arrow665

    @staticmethod
    def remove_table_at(index: int) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow666(assay: ArcAssay) -> ArcAssay:
            new_assay: ArcAssay = assay.Copy()
            new_assay.RemoveTableAt(index)
            return new_assay

        return _arrow666

    @staticmethod
    def remove_table(name: str) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow667(assay: ArcAssay) -> ArcAssay:
            new_assay: ArcAssay = assay.Copy()
            new_assay.RemoveTable(name)
            return new_assay

        return _arrow667

    @staticmethod
    def map_table_at(index: int, update_fun: Callable[[ArcTable], None]) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow668(assay: ArcAssay) -> ArcAssay:
            new_assay: ArcAssay = assay.Copy()
            new_assay.MapTableAt(index, update_fun)
            return new_assay

        return _arrow668

    @staticmethod
    def update_table(name: str, update_fun: Callable[[ArcTable], None]) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow670(assay: ArcAssay) -> ArcAssay:
            new_assay: ArcAssay = assay.Copy()
            new_assay.MapTable(name, update_fun)
            return new_assay

        return _arrow670

    @staticmethod
    def rename_table_at(index: int, new_name: str) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow671(assay: ArcAssay) -> ArcAssay:
            new_assay: ArcAssay = assay.Copy()
            new_assay.RenameTableAt(index, new_name)
            return new_assay

        return _arrow671

    @staticmethod
    def rename_table(name: str, new_name: str) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow672(assay: ArcAssay) -> ArcAssay:
            new_assay: ArcAssay = assay.Copy()
            new_assay.RenameTable(name, new_name)
            return new_assay

        return _arrow672

    @staticmethod
    def add_column_at(table_index: int, header: CompositeHeader, cells: Array[CompositeCell] | None=None, column_index: int | None=None, force_replace: bool | None=None) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow675(assay: ArcAssay) -> ArcAssay:
            new_assay: ArcAssay = assay.Copy()
            new_assay.AddColumnAt(table_index, header, cells, column_index, force_replace)
            return new_assay

        return _arrow675

    @staticmethod
    def add_column(table_name: str, header: CompositeHeader, cells: Array[CompositeCell] | None=None, column_index: int | None=None, force_replace: bool | None=None) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow676(assay: ArcAssay) -> ArcAssay:
            new_assay: ArcAssay = assay.Copy()
            new_assay.AddColumn(table_name, header, cells, column_index, force_replace)
            return new_assay

        return _arrow676

    @staticmethod
    def remove_column_at(table_index: int, column_index: int) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow677(assay: ArcAssay) -> ArcAssay:
            new_assay: ArcAssay = assay.Copy()
            new_assay.RemoveColumnAt(table_index, column_index)
            return new_assay

        return _arrow677

    @staticmethod
    def remove_column(table_name: str, column_index: int) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow678(assay: ArcAssay) -> ArcAssay:
            new_assay: ArcAssay = assay.Copy()
            new_assay.RemoveColumn(table_name, column_index)
            return new_assay

        return _arrow678

    @staticmethod
    def update_column_at(table_index: int, column_index: int, header: CompositeHeader, cells: Array[CompositeCell] | None=None) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow679(assay: ArcAssay) -> ArcAssay:
            new_assay: ArcAssay = assay.Copy()
            new_assay.UpdateColumnAt(table_index, column_index, header, cells)
            return new_assay

        return _arrow679

    @staticmethod
    def update_column(table_name: str, column_index: int, header: CompositeHeader, cells: Array[CompositeCell] | None=None) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow680(assay: ArcAssay) -> ArcAssay:
            new_assay: ArcAssay = assay.Copy()
            new_assay.UpdateColumn(table_name, column_index, header, cells)
            return new_assay

        return _arrow680

    @staticmethod
    def get_column_at(table_index: int, column_index: int) -> Callable[[ArcAssay], CompositeColumn]:
        def _arrow681(assay: ArcAssay) -> CompositeColumn:
            new_assay: ArcAssay = assay.Copy()
            return new_assay.GetColumnAt(table_index, column_index)

        return _arrow681

    @staticmethod
    def get_column(table_name: str, column_index: int) -> Callable[[ArcAssay], CompositeColumn]:
        def _arrow682(assay: ArcAssay) -> CompositeColumn:
            new_assay: ArcAssay = assay.Copy()
            return new_assay.GetColumn(table_name, column_index)

        return _arrow682

    @staticmethod
    def add_row_at(table_index: int, cells: Array[CompositeCell] | None=None, row_index: int | None=None) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow683(assay: ArcAssay) -> ArcAssay:
            new_assay: ArcAssay = assay.Copy()
            new_assay.AddRowAt(table_index, cells, row_index)
            return new_assay

        return _arrow683

    @staticmethod
    def add_row(table_name: str, cells: Array[CompositeCell] | None=None, row_index: int | None=None) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow684(assay: ArcAssay) -> ArcAssay:
            new_assay: ArcAssay = assay.Copy()
            new_assay.AddRow(table_name, cells, row_index)
            return new_assay

        return _arrow684

    @staticmethod
    def remove_row_at(table_index: int, row_index: int) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow685(assay: ArcAssay) -> ArcAssay:
            new_assay: ArcAssay = assay.Copy()
            new_assay.RemoveColumnAt(table_index, row_index)
            return new_assay

        return _arrow685

    @staticmethod
    def remove_row(table_name: str, row_index: int) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow686(assay: ArcAssay) -> ArcAssay:
            new_assay: ArcAssay = assay.Copy()
            new_assay.RemoveRow(table_name, row_index)
            return new_assay

        return _arrow686

    @staticmethod
    def update_row_at(table_index: int, row_index: int, cells: Array[CompositeCell]) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow687(assay: ArcAssay) -> ArcAssay:
            new_assay: ArcAssay = assay.Copy()
            new_assay.UpdateRowAt(table_index, row_index, cells)
            return new_assay

        return _arrow687

    @staticmethod
    def update_row(table_name: str, row_index: int, cells: Array[CompositeCell]) -> Callable[[ArcAssay], ArcAssay]:
        def _arrow688(assay: ArcAssay) -> ArcAssay:
            new_assay: ArcAssay = assay.Copy()
            new_assay.UpdateRow(table_name, row_index, cells)
            return new_assay

        return _arrow688

    @staticmethod
    def get_row_at(table_index: int, row_index: int) -> Callable[[ArcAssay], Array[CompositeCell]]:
        def _arrow689(assay: ArcAssay) -> Array[CompositeCell]:
            new_assay: ArcAssay = assay.Copy()
            return new_assay.GetRowAt(table_index, row_index)

        return _arrow689

    @staticmethod
    def get_row(table_name: str, row_index: int) -> Callable[[ArcAssay], Array[CompositeCell]]:
        def _arrow690(assay: ArcAssay) -> Array[CompositeCell]:
            new_assay: ArcAssay = assay.Copy()
            return new_assay.GetRow(table_name, row_index)

        return _arrow690

    @staticmethod
    def set_performers(performers: Array[Person], assay: ArcAssay) -> ArcAssay:
        assay.Performers = performers
        return assay

    def Copy(self, __unit: None=None) -> ArcAssay:
        this: ArcAssay = self
        next_tables: Array[ArcTable] = []
        enumerator: Any = get_enumerator(this.Tables)
        try: 
            while enumerator.System_Collections_IEnumerator_MoveNext():
                table: ArcTable = enumerator.System_Collections_Generic_IEnumerator_1_get_Current()
                copy: ArcTable = table.Copy()
                (next_tables.append(copy))

        finally: 
            dispose(enumerator)

        def mapping(c: Comment) -> Comment:
            return c.Copy()

        next_comments: Array[Comment] = map(mapping, this.Comments, None)
        def mapping_1(c_1: Person) -> Person:
            return c_1.Copy()

        next_performers: Array[Person] = map(mapping_1, this.Performers, None)
        identifier: str = this.Identifier
        measurement_type: OntologyAnnotation | None = this.MeasurementType
        technology_type: OntologyAnnotation | None = this.TechnologyType
        technology_platform: OntologyAnnotation | None = this.TechnologyPlatform
        return ArcAssay.make(identifier, measurement_type, technology_type, technology_platform, next_tables, next_performers, next_comments)

    def UpdateBy(self, assay: ArcAssay, only_replace_existing: bool | None=None, append_sequences: bool | None=None) -> None:
        this: ArcAssay = self
        only_replace_existing_1: bool = default_arg(only_replace_existing, False)
        append_sequences_1: bool = default_arg(append_sequences, False)
        update_always: bool = not only_replace_existing_1
        if True if (assay.MeasurementType is not None) else update_always:
            this.MeasurementType = assay.MeasurementType

        if True if (assay.TechnologyType is not None) else update_always:
            this.TechnologyType = assay.TechnologyType

        if True if (assay.TechnologyPlatform is not None) else update_always:
            this.TechnologyPlatform = assay.TechnologyPlatform

        if True if (len(assay.Tables) != 0) else update_always:
            s: Array[ArcTable]
            origin: Array[ArcTable] = this.Tables
            next_1: Array[ArcTable] = assay.Tables
            if not append_sequences_1:
                s = next_1

            else: 
                enumerator: Any = get_enumerator(next_1)
                try: 
                    while enumerator.System_Collections_IEnumerator_MoveNext():
                        e: ArcTable = enumerator.System_Collections_Generic_IEnumerator_1_get_Current()
                        class ObjectExpr691:
                            @property
                            def Equals(self) -> Callable[[ArcTable, ArcTable], bool]:
                                return equals

                            @property
                            def GetHashCode(self) -> Callable[[ArcTable], int]:
                                return safe_hash

                        if not contains_1(e, origin, ObjectExpr691()):
                            (origin.append(e))


                finally: 
                    dispose(enumerator)

                s = origin

            this.Tables = s

        if True if (len(assay.Performers) != 0) else update_always:
            s_1: Array[Person]
            origin_1: Array[Person] = this.Performers
            next_1_1: Array[Person] = assay.Performers
            class ObjectExpr692:
                @property
                def Equals(self) -> Callable[[Person, Person], bool]:
                    return equals

                @property
                def GetHashCode(self) -> Callable[[Person], int]:
                    return safe_hash

            s_1 = next_1_1 if (not append_sequences_1) else Array_distinct(append_3(origin_1, next_1_1, None), ObjectExpr692())
            this.Performers = s_1

        if True if (len(assay.Comments) != 0) else update_always:
            s_2: Array[Comment]
            origin_2: Array[Comment] = this.Comments
            next_1_2: Array[Comment] = assay.Comments
            class ObjectExpr693:
                @property
                def Equals(self) -> Callable[[Comment, Comment], bool]:
                    return equals

                @property
                def GetHashCode(self) -> Callable[[Comment], int]:
                    return safe_hash

            s_2 = next_1_2 if (not append_sequences_1) else Array_distinct(append_3(origin_2, next_1_2, None), ObjectExpr693())
            this.Comments = s_2


    def __str__(self, __unit: None=None) -> str:
        this: ArcAssay = self
        arg: str = this.Identifier
        arg_1: OntologyAnnotation | None = this.MeasurementType
        arg_2: OntologyAnnotation | None = this.TechnologyType
        arg_3: OntologyAnnotation | None = this.TechnologyPlatform
        arg_4: Array[ArcTable] = this.Tables
        arg_5: Array[Person] = this.Performers
        arg_6: Array[Comment] = this.Comments
        return to_text(printf("ArcAssay({\r\n    Identifier = \"%s\",\r\n    MeasurementType = %A,\r\n    TechnologyType = %A,\r\n    TechnologyPlatform = %A,\r\n    Tables = %A,\r\n    Performers = %A,\r\n    Comments = %A\r\n})"))(arg)(arg_1)(arg_2)(arg_3)(arg_4)(arg_5)(arg_6)

    @staticmethod
    def compose_technology_platform(tp: OntologyAnnotation) -> str:
        match_value: dict[str, Any] | None = tp.TANInfo
        return (("" + tp.NameText) + "") if (match_value is None) else (((("" + tp.NameText) + " (") + tp.TermAccessionShort) + ")")

    @staticmethod
    def decompose_technology_platform(name: str) -> OntologyAnnotation:
        active_pattern_result: Any | None = ActivePatterns__007CRegex_007C__007C("(?<value>[^\\(]+) \\((?<ontology>[^(]*:[^)]*)\\)", name)
        if active_pattern_result is not None:
            r: Any = active_pattern_result
            oa: OntologyAnnotation
            term_annotation: str = get_item(groups(r), "ontology") or ""
            oa = OntologyAnnotation.from_term_annotation(term_annotation)
            v: Value
            value: str = get_item(groups(r), "value") or ""
            v = Value.from_string(value)
            return OntologyAnnotation(oa.ID, v.Text, oa.TermSourceREF, oa.TermAccessionNumber, oa.Comments)

        else: 
            return OntologyAnnotation.from_string(name)


    def AddToInvestigation(self, investigation: ArcInvestigation) -> None:
        this: ArcAssay = self
        this.Investigation = investigation

    def RemoveFromInvestigation(self, __unit: None=None) -> None:
        this: ArcAssay = self
        this.Investigation = None

    def UpdateReferenceByAssayFile(self, assay: ArcAssay, only_replace_existing: bool | None=None) -> None:
        this: ArcAssay = self
        update_always: bool = not default_arg(only_replace_existing, False)
        if True if (assay.MeasurementType is not None) else update_always:
            this.MeasurementType = assay.MeasurementType

        if True if (assay.TechnologyPlatform is not None) else update_always:
            this.TechnologyPlatform = assay.TechnologyPlatform

        if True if (assay.TechnologyType is not None) else update_always:
            this.TechnologyType = assay.TechnologyType

        if True if (len(assay.Tables) != 0) else update_always:
            this.Tables = assay.Tables

        if True if (len(assay.Comments) != 0) else update_always:
            this.Comments = assay.Comments

        if True if (len(assay.Performers) != 0) else update_always:
            this.Performers = assay.Performers


    def ToAssay(self, __unit: None=None) -> Assay:
        this: ArcAssay = self
        process_seq: FSharpList[Process] = ArcTables(this.Tables).GetProcesses()
        assay_materials: AssayMaterials | None
        v_2: AssayMaterials = AssayMaterials_create_Z253F0553(Option_fromValueWithDefault(empty(), get_samples(process_seq)), Option_fromValueWithDefault(empty(), get_materials(process_seq)))
        assay_materials = Option_fromValueWithDefault(AssayMaterials_get_empty(), v_2)
        def mapping(tp: OntologyAnnotation) -> str:
            return ArcAssay.compose_technology_platform(tp)

        return Assay_create_3D372A24(None, None if is_missing_identifier(this.Identifier) else Assay_fileNameFromIdentifier(this.Identifier), this.MeasurementType, this.TechnologyType, map_1(mapping, this.TechnologyPlatform), Option_fromValueWithDefault(empty(), get_data(process_seq)), assay_materials, Option_fromValueWithDefault(empty(), get_characteristics(process_seq)), Option_fromValueWithDefault(empty(), get_units(process_seq)), Option_fromValueWithDefault(empty(), process_seq), Option_fromValueWithDefault(empty(), of_array(this.Comments)))

    @staticmethod
    def from_assay(a: Assay) -> ArcAssay:
        def mapping(arg: FSharpList[Process]) -> Array[ArcTable]:
            t: ArcTables = ArcTables.from_processes(arg)
            return t.Tables

        tables: Array[ArcTable] | None = map_1(mapping, a.ProcessSequence)
        identifer: str
        match_value: str | None = a.FileName
        identifer = create_missing_identifier() if (match_value is None) else Assay_identifierFromFileName(match_value)
        def mapping_1(x: OntologyAnnotation) -> OntologyAnnotation:
            return x.Copy()

        def mapping_2(x_1: OntologyAnnotation) -> OntologyAnnotation:
            return x_1.Copy()

        def mapping_3(name: str) -> OntologyAnnotation:
            return ArcAssay.decompose_technology_platform(name)

        return ArcAssay.create(identifer, map_1(mapping_1, a.MeasurementType), map_1(mapping_2, a.TechnologyType), map_1(mapping_3, a.TechnologyPlatform), tables, None, map_1(to_array_1, a.Comments))

    def StructurallyEquals(self, other: ArcAssay) -> bool:
        this: ArcAssay = self
        def predicate(x: bool) -> bool:
            return x == True

        def _arrow696(__unit: None=None) -> bool:
            a: IEnumerable_1[ArcTable] = this.Tables
            b: IEnumerable_1[ArcTable] = other.Tables
            def folder(acc: bool, e: bool) -> bool:
                if acc:
                    return e

                else: 
                    return False


            def _arrow695(__unit: None=None) -> IEnumerable_1[bool]:
                def _arrow694(i_1: int) -> bool:
                    return equals(item(i_1, a), item(i_1, b))

                return map_2(_arrow694, range_big_int(0, 1, length(a) - 1))

            return fold(folder, True, to_list(delay(_arrow695))) if (length(a) == length(b)) else False

        def _arrow699(__unit: None=None) -> bool:
            a_1: IEnumerable_1[Person] = this.Performers
            b_1: IEnumerable_1[Person] = other.Performers
            def folder_1(acc_1: bool, e_1: bool) -> bool:
                if acc_1:
                    return e_1

                else: 
                    return False


            def _arrow698(__unit: None=None) -> IEnumerable_1[bool]:
                def _arrow697(i_2: int) -> bool:
                    return equals(item(i_2, a_1), item(i_2, b_1))

                return map_2(_arrow697, range_big_int(0, 1, length(a_1) - 1))

            return fold(folder_1, True, to_list(delay(_arrow698))) if (length(a_1) == length(b_1)) else False

        def _arrow702(__unit: None=None) -> bool:
            a_2: IEnumerable_1[Comment] = this.Comments
            b_2: IEnumerable_1[Comment] = other.Comments
            def folder_2(acc_2: bool, e_2: bool) -> bool:
                if acc_2:
                    return e_2

                else: 
                    return False


            def _arrow701(__unit: None=None) -> IEnumerable_1[bool]:
                def _arrow700(i_3: int) -> bool:
                    return equals(item(i_3, a_2), item(i_3, b_2))

                return map_2(_arrow700, range_big_int(0, 1, length(a_2) - 1))

            return fold(folder_2, True, to_list(delay(_arrow701))) if (length(a_2) == length(b_2)) else False

        return for_all(predicate, to_enumerable([this.Identifier == other.Identifier, equals(this.MeasurementType, other.MeasurementType), equals(this.TechnologyType, other.TechnologyType), equals(this.TechnologyPlatform, other.TechnologyPlatform), _arrow696(), _arrow699(), _arrow702()]))

    def ReferenceEquals(self, other: ArcAssay) -> bool:
        this: ArcAssay = self
        return this is other

    def __eq__(self, other: Any=None) -> bool:
        this: ArcAssay = self
        return this.StructurallyEquals(other) if isinstance(other, ArcAssay) else False

    def __hash__(self, __unit: None=None) -> Any:
        this: ArcAssay = self
        return HashCodes_boxHashArray([this.Identifier, HashCodes_boxHashOption(this.MeasurementType), HashCodes_boxHashOption(this.TechnologyType), HashCodes_boxHashOption(this.TechnologyPlatform), HashCodes_boxHashArray(list(this.Tables)), HashCodes_boxHashArray(this.Performers), HashCodes_boxHashArray(this.Comments)])


ArcAssay_reflection = _expr703

def ArcAssay__ctor_Z1126B596(identifier: str, measurement_type: OntologyAnnotation | None=None, technology_type: OntologyAnnotation | None=None, technology_platform: OntologyAnnotation | None=None, tables: Array[ArcTable] | None=None, performers: Array[Person] | None=None, comments: Array[Comment] | None=None) -> ArcAssay:
    return ArcAssay(identifier, measurement_type, technology_type, technology_platform, tables, performers, comments)


def _expr770() -> TypeInfo:
    return class_type("ARCtrl.ISA.ArcStudy", None, ArcStudy, ArcTables_reflection())


class ArcStudy(ArcTables):
    def __init__(self, identifier: str, title: str | None=None, description: str | None=None, submission_date: str | None=None, public_release_date: str | None=None, publications: Array[Publication] | None=None, contacts: Array[Person] | None=None, study_design_descriptors: Array[OntologyAnnotation] | None=None, tables: Array[ArcTable] | None=None, registered_assay_identifiers: Array[str] | None=None, factors: Array[Factor] | None=None, comments: Array[Comment] | None=None) -> None:
        super().__init__(default_arg(tables, []))
        publications_1: Array[Publication] = default_arg(publications, [])
        contacts_1: Array[Person] = default_arg(contacts, [])
        study_design_descriptors_1: Array[OntologyAnnotation] = default_arg(study_design_descriptors, [])
        registered_assay_identifiers_1: Array[str] = default_arg(registered_assay_identifiers, [])
        factors_1: Array[Factor] = default_arg(factors, [])
        comments_1: Array[Comment] = default_arg(comments, [])
        self.identifier_0040572: str = identifier
        self.investigation: ArcInvestigation | None = None
        self.title_0040574: str | None = title
        self.description_0040575: str | None = description
        self.submission_date_0040576: str | None = submission_date
        self.public_release_date_0040577: str | None = public_release_date
        self.publications_0040578_002D1: Array[Publication] = publications_1
        self.contacts_0040579_002D1: Array[Person] = contacts_1
        self.study_design_descriptors_0040580_002D1: Array[OntologyAnnotation] = study_design_descriptors_1
        self.registered_assay_identifiers_0040581_002D1: Array[str] = registered_assay_identifiers_1
        self.factors_0040582_002D1: Array[Factor] = factors_1
        self.comments_0040583_002D1: Array[Comment] = comments_1
        self.static_hash: int = 0

    @property
    def Identifier(self, __unit: None=None) -> str:
        this: ArcStudy = self
        return this.identifier_0040572

    @Identifier.setter
    def Identifier(self, i: str) -> None:
        this: ArcStudy = self
        this.identifier_0040572 = i

    @property
    def Investigation(self, __unit: None=None) -> ArcInvestigation | None:
        this: ArcStudy = self
        return this.investigation

    @Investigation.setter
    def Investigation(self, i: ArcInvestigation | None=None) -> None:
        this: ArcStudy = self
        this.investigation = i

    @property
    def Title(self, __unit: None=None) -> str | None:
        this: ArcStudy = self
        return this.title_0040574

    @Title.setter
    def Title(self, n: str | None=None) -> None:
        this: ArcStudy = self
        this.title_0040574 = n

    @property
    def Description(self, __unit: None=None) -> str | None:
        this: ArcStudy = self
        return this.description_0040575

    @Description.setter
    def Description(self, n: str | None=None) -> None:
        this: ArcStudy = self
        this.description_0040575 = n

    @property
    def SubmissionDate(self, __unit: None=None) -> str | None:
        this: ArcStudy = self
        return this.submission_date_0040576

    @SubmissionDate.setter
    def SubmissionDate(self, n: str | None=None) -> None:
        this: ArcStudy = self
        this.submission_date_0040576 = n

    @property
    def PublicReleaseDate(self, __unit: None=None) -> str | None:
        this: ArcStudy = self
        return this.public_release_date_0040577

    @PublicReleaseDate.setter
    def PublicReleaseDate(self, n: str | None=None) -> None:
        this: ArcStudy = self
        this.public_release_date_0040577 = n

    @property
    def Publications(self, __unit: None=None) -> Array[Publication]:
        this: ArcStudy = self
        return this.publications_0040578_002D1

    @Publications.setter
    def Publications(self, n: Array[Publication]) -> None:
        this: ArcStudy = self
        this.publications_0040578_002D1 = n

    @property
    def Contacts(self, __unit: None=None) -> Array[Person]:
        this: ArcStudy = self
        return this.contacts_0040579_002D1

    @Contacts.setter
    def Contacts(self, n: Array[Person]) -> None:
        this: ArcStudy = self
        this.contacts_0040579_002D1 = n

    @property
    def StudyDesignDescriptors(self, __unit: None=None) -> Array[OntologyAnnotation]:
        this: ArcStudy = self
        return this.study_design_descriptors_0040580_002D1

    @StudyDesignDescriptors.setter
    def StudyDesignDescriptors(self, n: Array[OntologyAnnotation]) -> None:
        this: ArcStudy = self
        this.study_design_descriptors_0040580_002D1 = n

    @property
    def RegisteredAssayIdentifiers(self, __unit: None=None) -> Array[str]:
        this: ArcStudy = self
        return this.registered_assay_identifiers_0040581_002D1

    @RegisteredAssayIdentifiers.setter
    def RegisteredAssayIdentifiers(self, n: Array[str]) -> None:
        this: ArcStudy = self
        this.registered_assay_identifiers_0040581_002D1 = n

    @property
    def Factors(self, __unit: None=None) -> Array[Factor]:
        this: ArcStudy = self
        return this.factors_0040582_002D1

    @Factors.setter
    def Factors(self, n: Array[Factor]) -> None:
        this: ArcStudy = self
        this.factors_0040582_002D1 = n

    @property
    def Comments(self, __unit: None=None) -> Array[Comment]:
        this: ArcStudy = self
        return this.comments_0040583_002D1

    @Comments.setter
    def Comments(self, n: Array[Comment]) -> None:
        this: ArcStudy = self
        this.comments_0040583_002D1 = n

    @property
    def StaticHash(self, __unit: None=None) -> int:
        this: ArcStudy = self
        return this.static_hash

    @StaticHash.setter
    def StaticHash(self, h: int) -> None:
        this: ArcStudy = self
        this.static_hash = h or 0

    @staticmethod
    def init(identifier: str) -> ArcStudy:
        return ArcStudy(identifier)

    @staticmethod
    def create(identifier: str, title: str | None=None, description: str | None=None, submission_date: str | None=None, public_release_date: str | None=None, publications: Array[Publication] | None=None, contacts: Array[Person] | None=None, study_design_descriptors: Array[OntologyAnnotation] | None=None, tables: Array[ArcTable] | None=None, registered_assay_identifiers: Array[str] | None=None, factors: Array[Factor] | None=None, comments: Array[Comment] | None=None) -> ArcStudy:
        return ArcStudy(identifier, title, description, submission_date, public_release_date, publications, contacts, study_design_descriptors, tables, registered_assay_identifiers, factors, comments)

    @staticmethod
    def make(identifier: str, title: str | None, description: str | None, submission_date: str | None, public_release_date: str | None, publications: Array[Publication], contacts: Array[Person], study_design_descriptors: Array[OntologyAnnotation], tables: Array[ArcTable], registered_assay_identifiers: Array[str], factors: Array[Factor], comments: Array[Comment]) -> ArcStudy:
        return ArcStudy(identifier, title, description, submission_date, public_release_date, publications, contacts, study_design_descriptors, tables, registered_assay_identifiers, factors, comments)

    @property
    def is_empty(self, __unit: None=None) -> bool:
        this: ArcStudy = self
        return equals_with(equals, this.Comments, []) if (equals_with(equals, this.Factors, []) if ((len(this.RegisteredAssayIdentifiers) == 0) if ((len(this.Tables) == 0) if (equals_with(equals, this.StudyDesignDescriptors, []) if (equals_with(equals, this.Contacts, []) if (equals_with(equals, this.Publications, []) if (equals(this.PublicReleaseDate, None) if (equals(this.SubmissionDate, None) if (equals(this.Description, None) if equals(this.Title, None) else False) else False) else False) else False) else False) else False) else False) else False) else False) else False

    @staticmethod
    def FileName() -> str:
        return "isa.study.xlsx"

    @property
    def RegisteredAssayIdentifierCount(self, __unit: None=None) -> int:
        this: ArcStudy = self
        return len(this.RegisteredAssayIdentifiers)

    @property
    def RegisteredAssayCount(self, __unit: None=None) -> int:
        this: ArcStudy = self
        return len(this.RegisteredAssays)

    @property
    def RegisteredAssays(self, __unit: None=None) -> Array[ArcAssay]:
        this: ArcStudy = self
        inv: ArcInvestigation
        investigation: ArcInvestigation | None = this.Investigation
        if investigation is not None:
            inv = investigation

        else: 
            raise Exception("Cannot execute this function. Object is not part of ArcInvestigation.")

        def chooser(assay_identifier: str) -> ArcAssay | None:
            return inv.TryGetAssay(assay_identifier)

        return list(choose(chooser, this.RegisteredAssayIdentifiers))

    @property
    def VacantAssayIdentifiers(self, __unit: None=None) -> Array[str]:
        this: ArcStudy = self
        inv: ArcInvestigation
        investigation: ArcInvestigation | None = this.Investigation
        if investigation is not None:
            inv = investigation

        else: 
            raise Exception("Cannot execute this function. Object is not part of ArcInvestigation.")

        def predicate(arg: str) -> bool:
            return not inv.ContainsAssay(arg)

        return list(filter(predicate, this.RegisteredAssayIdentifiers))

    def AddRegisteredAssay(self, assay: ArcAssay) -> None:
        this: ArcStudy = self
        inv: ArcInvestigation
        investigation: ArcInvestigation | None = this.Investigation
        if investigation is not None:
            inv = investigation

        else: 
            raise Exception("Cannot execute this function. Object is not part of ArcInvestigation.")

        inv.AddAssay(assay)
        inv.RegisterAssay(this.Identifier, assay.Identifier)

    @staticmethod
    def add_registered_assay(assay: ArcAssay) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow704(study: ArcStudy) -> ArcStudy:
            new_study: ArcStudy = study.Copy()
            new_study.AddRegisteredAssay(assay)
            return new_study

        return _arrow704

    def InitRegisteredAssay(self, assay_identifier: str) -> ArcAssay:
        this: ArcStudy = self
        assay: ArcAssay = ArcAssay(assay_identifier)
        this.AddRegisteredAssay(assay)
        return assay

    @staticmethod
    def init_registered_assay(assay_identifier: str) -> Callable[[ArcStudy], tuple[ArcStudy, ArcAssay]]:
        def _arrow705(study: ArcStudy) -> tuple[ArcStudy, ArcAssay]:
            copy: ArcStudy = study.Copy()
            return (copy, copy.InitRegisteredAssay(assay_identifier))

        return _arrow705

    def RegisterAssay(self, assay_identifier: str) -> None:
        this: ArcStudy = self
        class ObjectExpr707:
            @property
            def Equals(self) -> Callable[[str, str], bool]:
                def _arrow706(x: str, y: str) -> bool:
                    return x == y

                return _arrow706

            @property
            def GetHashCode(self) -> Callable[[str], int]:
                return string_hash

        if contains(assay_identifier, this.RegisteredAssayIdentifiers, ObjectExpr707()):
            raise Exception(("Assay `" + assay_identifier) + "` is already registered on the study.")

        (this.RegisteredAssayIdentifiers.append(assay_identifier))

    @staticmethod
    def register_assay(assay_identifier: str) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow708(study: ArcStudy) -> ArcStudy:
            copy: ArcStudy = study.Copy()
            copy.RegisterAssay(assay_identifier)
            return copy

        return _arrow708

    def DeregisterAssay(self, assay_identifier: str) -> None:
        this: ArcStudy = self
        class ObjectExpr710:
            @property
            def Equals(self) -> Callable[[str, str], bool]:
                def _arrow709(x: str, y: str) -> bool:
                    return x == y

                return _arrow709

            @property
            def GetHashCode(self) -> Callable[[str], int]:
                return string_hash

        ignore(remove_in_place(assay_identifier, this.RegisteredAssayIdentifiers, ObjectExpr710()))

    @staticmethod
    def deregister_assay(assay_identifier: str) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow711(study: ArcStudy) -> ArcStudy:
            copy: ArcStudy = study.Copy()
            copy.DeregisterAssay(assay_identifier)
            return copy

        return _arrow711

    def GetRegisteredAssay(self, assay_identifier: str) -> ArcAssay:
        this: ArcStudy = self
        class ObjectExpr713:
            @property
            def Equals(self) -> Callable[[str, str], bool]:
                def _arrow712(x: str, y: str) -> bool:
                    return x == y

                return _arrow712

            @property
            def GetHashCode(self) -> Callable[[str], int]:
                return string_hash

        if not contains(assay_identifier, this.RegisteredAssayIdentifiers, ObjectExpr713()):
            raise Exception(("Assay `" + assay_identifier) + "` is not registered on the study.")

        inv: ArcInvestigation
        investigation: ArcInvestigation | None = this.Investigation
        if investigation is not None:
            inv = investigation

        else: 
            raise Exception("Cannot execute this function. Object is not part of ArcInvestigation.")

        return inv.GetAssay(assay_identifier)

    @staticmethod
    def get_registered_assay(assay_identifier: str) -> Callable[[ArcStudy], ArcAssay]:
        def _arrow714(study: ArcStudy) -> ArcAssay:
            copy: ArcStudy = study.Copy()
            return copy.GetRegisteredAssay(assay_identifier)

        return _arrow714

    @staticmethod
    def get_registered_assays(__unit: None=None) -> Callable[[ArcStudy], Array[ArcAssay]]:
        def _arrow715(study: ArcStudy) -> Array[ArcAssay]:
            copy: ArcStudy = study.Copy()
            return copy.RegisteredAssays

        return _arrow715

    def GetRegisteredAssaysOrIdentifier(self, __unit: None=None) -> Array[ArcAssay]:
        this: ArcStudy = self
        match_value: ArcInvestigation | None = this.Investigation
        if match_value is None:
            def f_1(identifier_1: str) -> ArcAssay:
                return ArcAssay.init(identifier_1)

            return ResizeArray_map(f_1, this.RegisteredAssayIdentifiers)

        else: 
            i: ArcInvestigation = match_value
            def f(identifier: str) -> ArcAssay:
                match_value_1: ArcAssay | None = i.TryGetAssay(identifier)
                if match_value_1 is None:
                    return ArcAssay.init(identifier)

                else: 
                    return match_value_1


            return ResizeArray_map(f, this.RegisteredAssayIdentifiers)


    @staticmethod
    def get_registered_assays_or_identifier(__unit: None=None) -> Callable[[ArcStudy], Array[ArcAssay]]:
        def _arrow716(study: ArcStudy) -> Array[ArcAssay]:
            copy: ArcStudy = study.Copy()
            return copy.GetRegisteredAssaysOrIdentifier()

        return _arrow716

    @staticmethod
    def add_table(table: ArcTable, index: int | None=None) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow717(study: ArcStudy) -> ArcStudy:
            c: ArcStudy = study.Copy()
            c.AddTable(table, index)
            return c

        return _arrow717

    @staticmethod
    def add_tables(tables: IEnumerable_1[ArcTable], index: int | None=None) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow718(study: ArcStudy) -> ArcStudy:
            c: ArcStudy = study.Copy()
            c.AddTables(tables, index)
            return c

        return _arrow718

    @staticmethod
    def init_table(table_name: str, index: int | None=None) -> Callable[[ArcStudy], tuple[ArcStudy, ArcTable]]:
        def _arrow719(study: ArcStudy) -> tuple[ArcStudy, ArcTable]:
            c: ArcStudy = study.Copy()
            return (c, c.InitTable(table_name, index))

        return _arrow719

    @staticmethod
    def init_tables(table_names: IEnumerable_1[str], index: int | None=None) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow720(study: ArcStudy) -> ArcStudy:
            c: ArcStudy = study.Copy()
            c.InitTables(table_names, index)
            return c

        return _arrow720

    @staticmethod
    def get_table_at(index: int) -> Callable[[ArcStudy], ArcTable]:
        def _arrow721(study: ArcStudy) -> ArcTable:
            new_assay: ArcStudy = study.Copy()
            return new_assay.GetTableAt(index)

        return _arrow721

    @staticmethod
    def get_table(name: str) -> Callable[[ArcStudy], ArcTable]:
        def _arrow722(study: ArcStudy) -> ArcTable:
            new_assay: ArcStudy = study.Copy()
            return new_assay.GetTable(name)

        return _arrow722

    @staticmethod
    def update_table_at(index: int, table: ArcTable) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow723(study: ArcStudy) -> ArcStudy:
            new_assay: ArcStudy = study.Copy()
            new_assay.UpdateTableAt(index, table)
            return new_assay

        return _arrow723

    @staticmethod
    def update_table(name: str, table: ArcTable) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow724(study: ArcStudy) -> ArcStudy:
            new_assay: ArcStudy = study.Copy()
            new_assay.UpdateTable(name, table)
            return new_assay

        return _arrow724

    @staticmethod
    def set_table_at(index: int, table: ArcTable) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow725(study: ArcStudy) -> ArcStudy:
            new_assay: ArcStudy = study.Copy()
            new_assay.SetTableAt(index, table)
            return new_assay

        return _arrow725

    @staticmethod
    def set_table(name: str, table: ArcTable) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow726(study: ArcStudy) -> ArcStudy:
            new_assay: ArcStudy = study.Copy()
            new_assay.SetTable(name, table)
            return new_assay

        return _arrow726

    @staticmethod
    def remove_table_at(index: int) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow727(study: ArcStudy) -> ArcStudy:
            new_assay: ArcStudy = study.Copy()
            new_assay.RemoveTableAt(index)
            return new_assay

        return _arrow727

    @staticmethod
    def remove_table(name: str) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow728(study: ArcStudy) -> ArcStudy:
            new_assay: ArcStudy = study.Copy()
            new_assay.RemoveTable(name)
            return new_assay

        return _arrow728

    @staticmethod
    def map_table_at(index: int, update_fun: Callable[[ArcTable], None]) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow729(study: ArcStudy) -> ArcStudy:
            new_assay: ArcStudy = study.Copy()
            new_assay.MapTableAt(index, update_fun)
            return new_assay

        return _arrow729

    @staticmethod
    def map_table(name: str, update_fun: Callable[[ArcTable], None]) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow730(study: ArcStudy) -> ArcStudy:
            new_assay: ArcStudy = study.Copy()
            new_assay.MapTable(name, update_fun)
            return new_assay

        return _arrow730

    @staticmethod
    def rename_table_at(index: int, new_name: str) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow731(study: ArcStudy) -> ArcStudy:
            new_assay: ArcStudy = study.Copy()
            new_assay.RenameTableAt(index, new_name)
            return new_assay

        return _arrow731

    @staticmethod
    def rename_table(name: str, new_name: str) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow732(study: ArcStudy) -> ArcStudy:
            new_assay: ArcStudy = study.Copy()
            new_assay.RenameTable(name, new_name)
            return new_assay

        return _arrow732

    @staticmethod
    def add_column_at(table_index: int, header: CompositeHeader, cells: Array[CompositeCell] | None=None, column_index: int | None=None, force_replace: bool | None=None) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow733(study: ArcStudy) -> ArcStudy:
            new_assay: ArcStudy = study.Copy()
            new_assay.AddColumnAt(table_index, header, cells, column_index, force_replace)
            return new_assay

        return _arrow733

    @staticmethod
    def add_column(table_name: str, header: CompositeHeader, cells: Array[CompositeCell] | None=None, column_index: int | None=None, force_replace: bool | None=None) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow734(study: ArcStudy) -> ArcStudy:
            new_assay: ArcStudy = study.Copy()
            new_assay.AddColumn(table_name, header, cells, column_index, force_replace)
            return new_assay

        return _arrow734

    @staticmethod
    def remove_column_at(table_index: int, column_index: int) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow735(study: ArcStudy) -> ArcStudy:
            new_assay: ArcStudy = study.Copy()
            new_assay.RemoveColumnAt(table_index, column_index)
            return new_assay

        return _arrow735

    @staticmethod
    def remove_column(table_name: str, column_index: int) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow736(study: ArcStudy) -> ArcStudy:
            new_assay: ArcStudy = study.Copy()
            new_assay.RemoveColumn(table_name, column_index)
            return new_assay

        return _arrow736

    @staticmethod
    def update_column_at(table_index: int, column_index: int, header: CompositeHeader, cells: Array[CompositeCell] | None=None) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow737(study: ArcStudy) -> ArcStudy:
            new_assay: ArcStudy = study.Copy()
            new_assay.UpdateColumnAt(table_index, column_index, header, cells)
            return new_assay

        return _arrow737

    @staticmethod
    def update_column(table_name: str, column_index: int, header: CompositeHeader, cells: Array[CompositeCell] | None=None) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow738(study: ArcStudy) -> ArcStudy:
            new_assay: ArcStudy = study.Copy()
            new_assay.UpdateColumn(table_name, column_index, header, cells)
            return new_assay

        return _arrow738

    @staticmethod
    def get_column_at(table_index: int, column_index: int) -> Callable[[ArcStudy], CompositeColumn]:
        def _arrow739(study: ArcStudy) -> CompositeColumn:
            new_assay: ArcStudy = study.Copy()
            return new_assay.GetColumnAt(table_index, column_index)

        return _arrow739

    @staticmethod
    def get_column(table_name: str, column_index: int) -> Callable[[ArcStudy], CompositeColumn]:
        def _arrow740(study: ArcStudy) -> CompositeColumn:
            new_assay: ArcStudy = study.Copy()
            return new_assay.GetColumn(table_name, column_index)

        return _arrow740

    @staticmethod
    def add_row_at(table_index: int, cells: Array[CompositeCell] | None=None, row_index: int | None=None) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow741(study: ArcStudy) -> ArcStudy:
            new_assay: ArcStudy = study.Copy()
            new_assay.AddRowAt(table_index, cells, row_index)
            return new_assay

        return _arrow741

    @staticmethod
    def add_row(table_name: str, cells: Array[CompositeCell] | None=None, row_index: int | None=None) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow742(study: ArcStudy) -> ArcStudy:
            new_assay: ArcStudy = study.Copy()
            new_assay.AddRow(table_name, cells, row_index)
            return new_assay

        return _arrow742

    @staticmethod
    def remove_row_at(table_index: int, row_index: int) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow743(study: ArcStudy) -> ArcStudy:
            new_assay: ArcStudy = study.Copy()
            new_assay.RemoveColumnAt(table_index, row_index)
            return new_assay

        return _arrow743

    @staticmethod
    def remove_row(table_name: str, row_index: int) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow744(study: ArcStudy) -> ArcStudy:
            new_assay: ArcStudy = study.Copy()
            new_assay.RemoveRow(table_name, row_index)
            return new_assay

        return _arrow744

    @staticmethod
    def update_row_at(table_index: int, row_index: int, cells: Array[CompositeCell]) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow745(study: ArcStudy) -> ArcStudy:
            new_assay: ArcStudy = study.Copy()
            new_assay.UpdateRowAt(table_index, row_index, cells)
            return new_assay

        return _arrow745

    @staticmethod
    def update_row(table_name: str, row_index: int, cells: Array[CompositeCell]) -> Callable[[ArcStudy], ArcStudy]:
        def _arrow746(study: ArcStudy) -> ArcStudy:
            new_assay: ArcStudy = study.Copy()
            new_assay.UpdateRow(table_name, row_index, cells)
            return new_assay

        return _arrow746

    @staticmethod
    def get_row_at(table_index: int, row_index: int) -> Callable[[ArcStudy], Array[CompositeCell]]:
        def _arrow747(study: ArcStudy) -> Array[CompositeCell]:
            new_assay: ArcStudy = study.Copy()
            return new_assay.GetRowAt(table_index, row_index)

        return _arrow747

    @staticmethod
    def get_row(table_name: str, row_index: int) -> Callable[[ArcStudy], Array[CompositeCell]]:
        def _arrow748(study: ArcStudy) -> Array[CompositeCell]:
            new_assay: ArcStudy = study.Copy()
            return new_assay.GetRow(table_name, row_index)

        return _arrow748

    def AddToInvestigation(self, investigation: ArcInvestigation) -> None:
        this: ArcStudy = self
        this.Investigation = investigation

    def RemoveFromInvestigation(self, __unit: None=None) -> None:
        this: ArcStudy = self
        this.Investigation = None

    def Copy(self, __unit: None=None) -> ArcStudy:
        this: ArcStudy = self
        next_tables: Array[ArcTable] = []
        next_assay_identifiers: Array[str] = list(this.RegisteredAssayIdentifiers)
        enumerator: Any = get_enumerator(this.Tables)
        try: 
            while enumerator.System_Collections_IEnumerator_MoveNext():
                table: ArcTable = enumerator.System_Collections_Generic_IEnumerator_1_get_Current()
                copy: ArcTable = table.Copy()
                (next_tables.append(copy))

        finally: 
            dispose(enumerator)

        def mapping(c: Comment) -> Comment:
            return c.Copy()

        next_comments: Array[Comment] = map(mapping, this.Comments, None)
        def mapping_1(c_1: Factor) -> Factor:
            return c_1.Copy()

        next_factors: Array[Factor] = map(mapping_1, this.Factors, None)
        def mapping_2(c_2: Person) -> Person:
            return c_2.Copy()

        next_contacts: Array[Person] = map(mapping_2, this.Contacts, None)
        def mapping_3(c_3: Publication) -> Publication:
            return c_3.Copy()

        next_publications: Array[Publication] = map(mapping_3, this.Publications, None)
        def mapping_4(c_4: OntologyAnnotation) -> OntologyAnnotation:
            return c_4.Copy()

        next_study_design_descriptors: Array[OntologyAnnotation] = map(mapping_4, this.StudyDesignDescriptors, None)
        identifier: str = this.Identifier
        title: str | None = this.Title
        description: str | None = this.Description
        submission_date: str | None = this.SubmissionDate
        public_release_date: str | None = this.PublicReleaseDate
        return ArcStudy.make(identifier, title, description, submission_date, public_release_date, next_publications, next_contacts, next_study_design_descriptors, next_tables, next_assay_identifiers, next_factors, next_comments)

    def UpdateReferenceByStudyFile(self, study: ArcStudy, only_replace_existing: bool | None=None, keep_unused_ref_tables: bool | None=None) -> None:
        this: ArcStudy = self
        update_always: bool = not default_arg(only_replace_existing, False)
        if True if (study.Title is not None) else update_always:
            this.Title = study.Title

        if True if (study.Description is not None) else update_always:
            this.Description = study.Description

        if True if (study.SubmissionDate is not None) else update_always:
            this.SubmissionDate = study.SubmissionDate

        if True if (study.PublicReleaseDate is not None) else update_always:
            this.PublicReleaseDate = study.PublicReleaseDate

        if True if (len(study.Publications) != 0) else update_always:
            this.Publications = study.Publications

        if True if (len(study.Contacts) != 0) else update_always:
            this.Contacts = study.Contacts

        if True if (len(study.StudyDesignDescriptors) != 0) else update_always:
            this.StudyDesignDescriptors = study.StudyDesignDescriptors

        if True if (len(study.Tables) != 0) else update_always:
            tables: ArcTables = ArcTables.update_reference_tables_by_sheets(ArcTables(this.Tables), ArcTables(study.Tables), keep_unused_ref_tables)
            this.Tables = tables.Tables

        if True if (len(study.RegisteredAssayIdentifiers) != 0) else update_always:
            this.RegisteredAssayIdentifiers = study.RegisteredAssayIdentifiers

        if True if (len(study.Factors) != 0) else update_always:
            this.Factors = study.Factors

        if True if (len(study.Comments) != 0) else update_always:
            this.Comments = study.Comments


    def ToStudy(self, arc_assays: Array[ArcAssay] | None=None) -> Study:
        this: ArcStudy = self
        process_seq: FSharpList[Process] = ArcTables(this.Tables).GetProcesses()
        protocols: FSharpList[Protocol] | None = Option_fromValueWithDefault(empty(), get_protocols(process_seq))
        study_materials: StudyMaterials | None
        v_4: StudyMaterials = StudyMaterials_create_1BE9FA55(Option_fromValueWithDefault(empty(), get_sources(process_seq)), Option_fromValueWithDefault(empty(), get_samples(process_seq)), Option_fromValueWithDefault(empty(), get_materials(process_seq)))
        study_materials = Option_fromValueWithDefault(StudyMaterials_get_empty(), v_4)
        pattern_input: tuple[str | None, str | None] = ((None, None)) if is_missing_identifier(this.Identifier) else ((this.Identifier, Study_fileNameFromIdentifier(this.Identifier)))
        def mapping(a: ArcAssay) -> Assay:
            return a.ToAssay()

        assays: FSharpList[Assay] = map_3(mapping, of_seq(default_arg(arc_assays, this.GetRegisteredAssaysOrIdentifier())))
        return Study_create_Z2D28E954(None, pattern_input[1], pattern_input[0], this.Title, this.Description, this.SubmissionDate, this.PublicReleaseDate, Option_fromValueWithDefault(empty(), of_array(this.Publications)), Option_fromValueWithDefault(empty(), of_array(this.Contacts)), Option_fromValueWithDefault(empty(), of_array(this.StudyDesignDescriptors)), protocols, study_materials, Option_fromValueWithDefault(empty(), process_seq), Option_fromValueWithDefault(empty(), assays), Option_fromValueWithDefault(empty(), of_array(this.Factors)), Option_fromValueWithDefault(empty(), get_characteristics(process_seq)), Option_fromValueWithDefault(empty(), get_units(process_seq)), Option_fromValueWithDefault(empty(), of_array(this.Comments)))

    @staticmethod
    def from_study(s: Study) -> tuple[ArcStudy, Array[ArcAssay]]:
        def mapping(arg: FSharpList[Process]) -> Array[ArcTable]:
            t: ArcTables = ArcTables.from_processes(arg)
            return t.Tables

        tables: Array[ArcTable] | None = map_1(mapping, s.ProcessSequence)
        identifer: str
        match_value: str | None = s.FileName
        identifer = create_missing_identifier() if (match_value is None) else Study_identifierFromFileName(match_value)
        def mapping_2(arg_1: FSharpList[Assay]) -> Array[ArcAssay]:
            def mapping_1(a: Assay, arg_1: Any=arg_1) -> ArcAssay:
                return ArcAssay.from_assay(a)

            return list(map_3(mapping_1, arg_1))

        assays: Array[ArcAssay] = default_arg(map_1(mapping_2, s.Assays), [])
        def mapping_3(a_1: ArcAssay) -> str:
            return a_1.Identifier

        assays_identifiers: Array[str] = list(map_2(mapping_3, assays))
        return (ArcStudy.create(identifer, s.Title, s.Description, s.SubmissionDate, s.PublicReleaseDate, map_1(to_array_1, s.Publications), map_1(to_array_1, s.Contacts), map_1(to_array_1, s.StudyDesignDescriptors), tables, assays_identifiers, map_1(to_array_1, s.Factors), map_1(to_array_1, s.Comments)), assays)

    def StructurallyEquals(self, other: ArcStudy) -> bool:
        this: ArcStudy = self
        def predicate(x: bool) -> bool:
            return x == True

        def _arrow751(__unit: None=None) -> bool:
            a: IEnumerable_1[Publication] = this.Publications
            b: IEnumerable_1[Publication] = other.Publications
            def folder(acc: bool, e: bool) -> bool:
                if acc:
                    return e

                else: 
                    return False


            def _arrow750(__unit: None=None) -> IEnumerable_1[bool]:
                def _arrow749(i_1: int) -> bool:
                    return equals(item(i_1, a), item(i_1, b))

                return map_2(_arrow749, range_big_int(0, 1, length(a) - 1))

            return fold(folder, True, to_list(delay(_arrow750))) if (length(a) == length(b)) else False

        def _arrow754(__unit: None=None) -> bool:
            a_1: IEnumerable_1[Person] = this.Contacts
            b_1: IEnumerable_1[Person] = other.Contacts
            def folder_1(acc_1: bool, e_1: bool) -> bool:
                if acc_1:
                    return e_1

                else: 
                    return False


            def _arrow753(__unit: None=None) -> IEnumerable_1[bool]:
                def _arrow752(i_2: int) -> bool:
                    return equals(item(i_2, a_1), item(i_2, b_1))

                return map_2(_arrow752, range_big_int(0, 1, length(a_1) - 1))

            return fold(folder_1, True, to_list(delay(_arrow753))) if (length(a_1) == length(b_1)) else False

        def _arrow757(__unit: None=None) -> bool:
            a_2: IEnumerable_1[OntologyAnnotation] = this.StudyDesignDescriptors
            b_2: IEnumerable_1[OntologyAnnotation] = other.StudyDesignDescriptors
            def folder_2(acc_2: bool, e_2: bool) -> bool:
                if acc_2:
                    return e_2

                else: 
                    return False


            def _arrow756(__unit: None=None) -> IEnumerable_1[bool]:
                def _arrow755(i_3: int) -> bool:
                    return equals(item(i_3, a_2), item(i_3, b_2))

                return map_2(_arrow755, range_big_int(0, 1, length(a_2) - 1))

            return fold(folder_2, True, to_list(delay(_arrow756))) if (length(a_2) == length(b_2)) else False

        def _arrow760(__unit: None=None) -> bool:
            a_3: IEnumerable_1[ArcTable] = this.Tables
            b_3: IEnumerable_1[ArcTable] = other.Tables
            def folder_3(acc_3: bool, e_3: bool) -> bool:
                if acc_3:
                    return e_3

                else: 
                    return False


            def _arrow759(__unit: None=None) -> IEnumerable_1[bool]:
                def _arrow758(i_4: int) -> bool:
                    return equals(item(i_4, a_3), item(i_4, b_3))

                return map_2(_arrow758, range_big_int(0, 1, length(a_3) - 1))

            return fold(folder_3, True, to_list(delay(_arrow759))) if (length(a_3) == length(b_3)) else False

        def _arrow763(__unit: None=None) -> bool:
            a_4: IEnumerable_1[str] = this.RegisteredAssayIdentifiers
            b_4: IEnumerable_1[str] = other.RegisteredAssayIdentifiers
            def folder_4(acc_4: bool, e_4: bool) -> bool:
                if acc_4:
                    return e_4

                else: 
                    return False


            def _arrow762(__unit: None=None) -> IEnumerable_1[bool]:
                def _arrow761(i_5: int) -> bool:
                    return item(i_5, a_4) == item(i_5, b_4)

                return map_2(_arrow761, range_big_int(0, 1, length(a_4) - 1))

            return fold(folder_4, True, to_list(delay(_arrow762))) if (length(a_4) == length(b_4)) else False

        def _arrow766(__unit: None=None) -> bool:
            a_5: IEnumerable_1[Factor] = this.Factors
            b_5: IEnumerable_1[Factor] = other.Factors
            def folder_5(acc_5: bool, e_5: bool) -> bool:
                if acc_5:
                    return e_5

                else: 
                    return False


            def _arrow765(__unit: None=None) -> IEnumerable_1[bool]:
                def _arrow764(i_6: int) -> bool:
                    return equals(item(i_6, a_5), item(i_6, b_5))

                return map_2(_arrow764, range_big_int(0, 1, length(a_5) - 1))

            return fold(folder_5, True, to_list(delay(_arrow765))) if (length(a_5) == length(b_5)) else False

        def _arrow769(__unit: None=None) -> bool:
            a_6: IEnumerable_1[Comment] = this.Comments
            b_6: IEnumerable_1[Comment] = other.Comments
            def folder_6(acc_6: bool, e_6: bool) -> bool:
                if acc_6:
                    return e_6

                else: 
                    return False


            def _arrow768(__unit: None=None) -> IEnumerable_1[bool]:
                def _arrow767(i_7: int) -> bool:
                    return equals(item(i_7, a_6), item(i_7, b_6))

                return map_2(_arrow767, range_big_int(0, 1, length(a_6) - 1))

            return fold(folder_6, True, to_list(delay(_arrow768))) if (length(a_6) == length(b_6)) else False

        return for_all(predicate, to_enumerable([this.Identifier == other.Identifier, equals(this.Title, other.Title), equals(this.Description, other.Description), equals(this.SubmissionDate, other.SubmissionDate), equals(this.PublicReleaseDate, other.PublicReleaseDate), _arrow751(), _arrow754(), _arrow757(), _arrow760(), _arrow763(), _arrow766(), _arrow769()]))

    def ReferenceEquals(self, other: ArcStudy) -> bool:
        this: ArcStudy = self
        return this is other

    def __eq__(self, other: Any=None) -> bool:
        this: ArcStudy = self
        return this.StructurallyEquals(other) if isinstance(other, ArcStudy) else False

    def __hash__(self, __unit: None=None) -> Any:
        this: ArcStudy = self
        return HashCodes_boxHashArray([this.Identifier, HashCodes_boxHashOption(this.Title), HashCodes_boxHashOption(this.Description), HashCodes_boxHashOption(this.SubmissionDate), HashCodes_boxHashOption(this.PublicReleaseDate), HashCodes_boxHashArray(this.Publications), HashCodes_boxHashArray(this.Contacts), HashCodes_boxHashArray(this.StudyDesignDescriptors), HashCodes_boxHashArray(list(this.Tables)), HashCodes_boxHashArray(list(this.RegisteredAssayIdentifiers)), HashCodes_boxHashArray(this.Factors), HashCodes_boxHashArray(this.Comments)])

    def GetLightHashCode(self, __unit: None=None) -> Any:
        this: ArcStudy = self
        return HashCodes_boxHashArray([this.Identifier, HashCodes_boxHashOption(this.Title), HashCodes_boxHashOption(this.Description), HashCodes_boxHashOption(this.SubmissionDate), HashCodes_boxHashOption(this.PublicReleaseDate), HashCodes_boxHashArray(this.Publications), HashCodes_boxHashArray(this.Contacts), HashCodes_boxHashArray(this.StudyDesignDescriptors), HashCodes_boxHashArray(list(this.Tables)), HashCodes_boxHashArray(this.Factors), HashCodes_boxHashArray(this.Comments)])


ArcStudy_reflection = _expr770

def ArcStudy__ctor_Z4F2D842F(identifier: str, title: str | None=None, description: str | None=None, submission_date: str | None=None, public_release_date: str | None=None, publications: Array[Publication] | None=None, contacts: Array[Person] | None=None, study_design_descriptors: Array[OntologyAnnotation] | None=None, tables: Array[ArcTable] | None=None, registered_assay_identifiers: Array[str] | None=None, factors: Array[Factor] | None=None, comments: Array[Comment] | None=None) -> ArcStudy:
    return ArcStudy(identifier, title, description, submission_date, public_release_date, publications, contacts, study_design_descriptors, tables, registered_assay_identifiers, factors, comments)


def _expr870() -> TypeInfo:
    return class_type("ARCtrl.ISA.ArcInvestigation", None, ArcInvestigation)


class ArcInvestigation:
    def __init__(self, identifier: str, title: str | None=None, description: str | None=None, submission_date: str | None=None, public_release_date: str | None=None, ontology_source_references: Array[OntologySourceReference] | None=None, publications: Array[Publication] | None=None, contacts: Array[Person] | None=None, assays: Array[ArcAssay] | None=None, studies: Array[ArcStudy] | None=None, registered_study_identifiers: Array[str] | None=None, comments: Array[Comment] | None=None, remarks: Array[Remark] | None=None) -> None:
        this: FSharpRef[ArcInvestigation] = FSharpRef(None)
        this.contents = self
        ontology_source_references_1: Array[OntologySourceReference] = default_arg(ontology_source_references, [])
        publications_1: Array[Publication] = default_arg(publications, [])
        contacts_1: Array[Person] = default_arg(contacts, [])
        assays_1: Array[ArcAssay]
        ass: Array[ArcAssay] = default_arg(assays, [])
        enumerator: Any = get_enumerator(ass)
        try: 
            while enumerator.System_Collections_IEnumerator_MoveNext():
                a: ArcAssay = enumerator.System_Collections_Generic_IEnumerator_1_get_Current()
                a.Investigation = this.contents

        finally: 
            dispose(enumerator)

        assays_1 = ass
        studies_1: Array[ArcStudy]
        sss: Array[ArcStudy] = default_arg(studies, [])
        enumerator_1: Any = get_enumerator(sss)
        try: 
            while enumerator_1.System_Collections_IEnumerator_MoveNext():
                s: ArcStudy = enumerator_1.System_Collections_Generic_IEnumerator_1_get_Current()
                s.Investigation = this.contents

        finally: 
            dispose(enumerator_1)

        studies_1 = sss
        registered_study_identifiers_1: Array[str] = default_arg(registered_study_identifiers, [])
        comments_1: Array[Comment] = default_arg(comments, [])
        remarks_1: Array[Remark] = default_arg(remarks, [])
        self.identifier_00401195: str = identifier
        self.title_00401196: str | None = title
        self.description_00401197: str | None = description
        self.submission_date_00401198: str | None = submission_date
        self.public_release_date_00401199: str | None = public_release_date
        self.ontology_source_references_00401200_002D1: Array[OntologySourceReference] = ontology_source_references_1
        self.publications_00401201_002D1: Array[Publication] = publications_1
        self.contacts_00401202_002D1: Array[Person] = contacts_1
        self.assays_00401203_002D1: Array[ArcAssay] = assays_1
        self.studies_00401204_002D1: Array[ArcStudy] = studies_1
        self.registered_study_identifiers_00401205_002D1: Array[str] = registered_study_identifiers_1
        self.comments_00401206_002D1: Array[Comment] = comments_1
        self.remarks_00401207_002D1: Array[Remark] = remarks_1
        self.static_hash: int = 0
        self.init_00401176: int = 1

    @property
    def Identifier(self, __unit: None=None) -> str:
        this: ArcInvestigation = self
        return this.identifier_00401195

    @Identifier.setter
    def Identifier(self, i: str) -> None:
        this: ArcInvestigation = self
        this.identifier_00401195 = i

    @property
    def Title(self, __unit: None=None) -> str | None:
        this: ArcInvestigation = self
        return this.title_00401196

    @Title.setter
    def Title(self, n: str | None=None) -> None:
        this: ArcInvestigation = self
        this.title_00401196 = n

    @property
    def Description(self, __unit: None=None) -> str | None:
        this: ArcInvestigation = self
        return this.description_00401197

    @Description.setter
    def Description(self, n: str | None=None) -> None:
        this: ArcInvestigation = self
        this.description_00401197 = n

    @property
    def SubmissionDate(self, __unit: None=None) -> str | None:
        this: ArcInvestigation = self
        return this.submission_date_00401198

    @SubmissionDate.setter
    def SubmissionDate(self, n: str | None=None) -> None:
        this: ArcInvestigation = self
        this.submission_date_00401198 = n

    @property
    def PublicReleaseDate(self, __unit: None=None) -> str | None:
        this: ArcInvestigation = self
        return this.public_release_date_00401199

    @PublicReleaseDate.setter
    def PublicReleaseDate(self, n: str | None=None) -> None:
        this: ArcInvestigation = self
        this.public_release_date_00401199 = n

    @property
    def OntologySourceReferences(self, __unit: None=None) -> Array[OntologySourceReference]:
        this: ArcInvestigation = self
        return this.ontology_source_references_00401200_002D1

    @OntologySourceReferences.setter
    def OntologySourceReferences(self, n: Array[OntologySourceReference]) -> None:
        this: ArcInvestigation = self
        this.ontology_source_references_00401200_002D1 = n

    @property
    def Publications(self, __unit: None=None) -> Array[Publication]:
        this: ArcInvestigation = self
        return this.publications_00401201_002D1

    @Publications.setter
    def Publications(self, n: Array[Publication]) -> None:
        this: ArcInvestigation = self
        this.publications_00401201_002D1 = n

    @property
    def Contacts(self, __unit: None=None) -> Array[Person]:
        this: ArcInvestigation = self
        return this.contacts_00401202_002D1

    @Contacts.setter
    def Contacts(self, n: Array[Person]) -> None:
        this: ArcInvestigation = self
        this.contacts_00401202_002D1 = n

    @property
    def Assays(self, __unit: None=None) -> Array[ArcAssay]:
        this: ArcInvestigation = self
        return this.assays_00401203_002D1

    @Assays.setter
    def Assays(self, n: Array[ArcAssay]) -> None:
        this: ArcInvestigation = self
        this.assays_00401203_002D1 = n

    @property
    def Studies(self, __unit: None=None) -> Array[ArcStudy]:
        this: ArcInvestigation = self
        return this.studies_00401204_002D1

    @Studies.setter
    def Studies(self, n: Array[ArcStudy]) -> None:
        this: ArcInvestigation = self
        this.studies_00401204_002D1 = n

    @property
    def RegisteredStudyIdentifiers(self, __unit: None=None) -> Array[str]:
        this: ArcInvestigation = self
        return this.registered_study_identifiers_00401205_002D1

    @RegisteredStudyIdentifiers.setter
    def RegisteredStudyIdentifiers(self, n: Array[str]) -> None:
        this: ArcInvestigation = self
        this.registered_study_identifiers_00401205_002D1 = n

    @property
    def Comments(self, __unit: None=None) -> Array[Comment]:
        this: ArcInvestigation = self
        return this.comments_00401206_002D1

    @Comments.setter
    def Comments(self, n: Array[Comment]) -> None:
        this: ArcInvestigation = self
        this.comments_00401206_002D1 = n

    @property
    def Remarks(self, __unit: None=None) -> Array[Remark]:
        this: ArcInvestigation = self
        return this.remarks_00401207_002D1

    @Remarks.setter
    def Remarks(self, n: Array[Remark]) -> None:
        this: ArcInvestigation = self
        this.remarks_00401207_002D1 = n

    @property
    def StaticHash(self, __unit: None=None) -> int:
        this: ArcInvestigation = self
        return this.static_hash

    @StaticHash.setter
    def StaticHash(self, h: int) -> None:
        this: ArcInvestigation = self
        this.static_hash = h or 0

    @staticmethod
    def FileName() -> str:
        return "isa.investigation.xlsx"

    @staticmethod
    def init(identifier: str) -> ArcInvestigation:
        return ArcInvestigation(identifier)

    @staticmethod
    def create(identifier: str, title: str | None=None, description: str | None=None, submission_date: str | None=None, public_release_date: str | None=None, ontology_source_references: Array[OntologySourceReference] | None=None, publications: Array[Publication] | None=None, contacts: Array[Person] | None=None, assays: Array[ArcAssay] | None=None, studies: Array[ArcStudy] | None=None, registered_study_identifiers: Array[str] | None=None, comments: Array[Comment] | None=None, remarks: Array[Remark] | None=None) -> ArcInvestigation:
        return ArcInvestigation(identifier, title, description, submission_date, public_release_date, ontology_source_references, publications, contacts, assays, studies, registered_study_identifiers, comments, remarks)

    @staticmethod
    def make(identifier: str, title: str | None, description: str | None, submission_date: str | None, public_release_date: str | None, ontology_source_references: Array[OntologySourceReference], publications: Array[Publication], contacts: Array[Person], assays: Array[ArcAssay], studies: Array[ArcStudy], registered_study_identifiers: Array[str], comments: Array[Comment], remarks: Array[Remark]) -> ArcInvestigation:
        return ArcInvestigation(identifier, title, description, submission_date, public_release_date, ontology_source_references, publications, contacts, assays, studies, registered_study_identifiers, comments, remarks)

    @property
    def AssayCount(self, __unit: None=None) -> int:
        this: ArcInvestigation = self
        return len(this.Assays)

    @property
    def AssayIdentifiers(self, __unit: None=None) -> Array[str]:
        this: ArcInvestigation = self
        def mapping(x: ArcAssay) -> str:
            return x.Identifier

        return list(map_2(mapping, this.Assays))

    @property
    def UnregisteredAssays(self, __unit: None=None) -> Array[ArcAssay]:
        this: ArcInvestigation = self
        def f(a: ArcAssay) -> bool:
            def predicate(s: ArcStudy, a: Any=a) -> bool:
                def _arrow774(i: str, s: Any=s) -> bool:
                    return i == a.Identifier

                return exists(_arrow774, s.RegisteredAssayIdentifiers)

            return not exists(predicate, this.RegisteredStudies)

        return ResizeArray_filter(f, this.Assays)

    def AddAssay(self, assay: ArcAssay) -> None:
        this: ArcInvestigation = self
        assay_ident: str = assay.Identifier
        def predicate(x_1: str) -> bool:
            return x_1 == assay_ident

        def mapping(x: ArcAssay) -> str:
            return x.Identifier

        match_value: int | None = try_find_index(predicate, map_2(mapping, this.Assays))
        if match_value is None:
            pass

        else: 
            raise Exception(((("Cannot create assay with name " + assay_ident) + ", as assay names must be unique and assay at index ") + str(match_value)) + " has the same name.")

        assay.Investigation = this
        (this.Assays.append(assay))

    @staticmethod
    def add_assay(assay: ArcAssay) -> Callable[[ArcInvestigation], ArcInvestigation]:
        def _arrow775(inv: ArcInvestigation) -> ArcInvestigation:
            new_investigation: ArcInvestigation = inv.Copy()
            new_investigation.AddAssay(assay)
            return new_investigation

        return _arrow775

    def InitAssay(self, assay_identifier: str) -> ArcAssay:
        this: ArcInvestigation = self
        assay: ArcAssay = ArcAssay(assay_identifier)
        this.AddAssay(assay)
        return assay

    @staticmethod
    def init_assay(assay_identifier: str) -> Callable[[ArcInvestigation], ArcAssay]:
        def _arrow776(inv: ArcInvestigation) -> ArcAssay:
            new_investigation: ArcInvestigation = inv.Copy()
            return new_investigation.InitAssay(assay_identifier)

        return _arrow776

    def DeleteAssayAt(self, index: int) -> None:
        this: ArcInvestigation = self
        this.Assays.pop(index)

    @staticmethod
    def delete_assay_at(index: int) -> Callable[[ArcInvestigation], ArcInvestigation]:
        def _arrow777(inv: ArcInvestigation) -> ArcInvestigation:
            new_investigation: ArcInvestigation = inv.Copy()
            new_investigation.DeleteAssayAt(index)
            return new_investigation

        return _arrow777

    def DeleteAssay(self, assay_identifier: str) -> None:
        this: ArcInvestigation = self
        index: int = this.GetAssayIndex(assay_identifier) or 0
        this.DeleteAssayAt(index)

    @staticmethod
    def delete_assay(assay_identifier: str) -> Callable[[ArcInvestigation], ArcInvestigation]:
        def _arrow778(inv: ArcInvestigation) -> ArcInvestigation:
            new_inv: ArcInvestigation = inv.Copy()
            new_inv.DeleteAssay(assay_identifier)
            return new_inv

        return _arrow778

    def RemoveAssayAt(self, index: int) -> None:
        this: ArcInvestigation = self
        ident: str = this.GetAssayAt(index).Identifier
        this.Assays.pop(index)
        enumerator: Any = get_enumerator(this.Studies)
        try: 
            while enumerator.System_Collections_IEnumerator_MoveNext():
                study: ArcStudy = enumerator.System_Collections_Generic_IEnumerator_1_get_Current()
                study.DeregisterAssay(ident)

        finally: 
            dispose(enumerator)


    @staticmethod
    def remove_assay_at(index: int) -> Callable[[ArcInvestigation], ArcInvestigation]:
        def _arrow779(inv: ArcInvestigation) -> ArcInvestigation:
            new_investigation: ArcInvestigation = inv.Copy()
            new_investigation.RemoveAssayAt(index)
            return new_investigation

        return _arrow779

    def RemoveAssay(self, assay_identifier: str) -> None:
        this: ArcInvestigation = self
        index: int = this.GetAssayIndex(assay_identifier) or 0
        this.RemoveAssayAt(index)

    @staticmethod
    def remove_assay(assay_identifier: str) -> Callable[[ArcInvestigation], ArcInvestigation]:
        def _arrow780(inv: ArcInvestigation) -> ArcInvestigation:
            new_inv: ArcInvestigation = inv.Copy()
            new_inv.RemoveAssay(assay_identifier)
            return new_inv

        return _arrow780

    def SetAssayAt(self, index: int, assay: ArcAssay) -> None:
        this: ArcInvestigation = self
        assay_ident: str = assay.Identifier
        def predicate(x: str) -> bool:
            return x == assay_ident

        def mapping(a: ArcAssay) -> str:
            return a.Identifier

        match_value: int | None = try_find_index(predicate, map_2(mapping, remove_at(index, this.Assays)))
        if match_value is None:
            pass

        else: 
            raise Exception(((("Cannot create assay with name " + assay_ident) + ", as assay names must be unique and assay at index ") + str(match_value)) + " has the same name.")

        assay.Investigation = this
        this.Assays[index] = assay
        this.DeregisterMissingAssays()

    @staticmethod
    def set_assay_at(index: int, assay: ArcAssay) -> Callable[[ArcInvestigation], ArcInvestigation]:
        def _arrow781(inv: ArcInvestigation) -> ArcInvestigation:
            new_investigation: ArcInvestigation = inv.Copy()
            new_investigation.SetAssayAt(index, assay)
            return new_investigation

        return _arrow781

    def SetAssay(self, assay_identifier: str, assay: ArcAssay) -> None:
        this: ArcInvestigation = self
        index: int = this.GetAssayIndex(assay_identifier) or 0
        this.SetAssayAt(index, assay)

    @staticmethod
    def set_assay(assay_identifier: str, assay: ArcAssay) -> Callable[[ArcInvestigation], ArcInvestigation]:
        def _arrow782(inv: ArcInvestigation) -> ArcInvestigation:
            new_investigation: ArcInvestigation = inv.Copy()
            new_investigation.SetAssay(assay_identifier, assay)
            return new_investigation

        return _arrow782

    def GetAssayIndex(self, assay_identifier: str) -> int:
        this: ArcInvestigation = self
        def _arrow783(a: ArcAssay) -> bool:
            return a.Identifier == assay_identifier

        index: int = find_index(_arrow783, this.Assays) or 0
        if index == -1:
            raise Exception(("Unable to find assay with specified identifier \'" + assay_identifier) + "\'!")

        return index

    @staticmethod
    def get_assay_index(assay_identifier: str) -> Callable[[ArcInvestigation], int]:
        def _arrow784(inv: ArcInvestigation) -> int:
            return inv.GetAssayIndex(assay_identifier)

        return _arrow784

    def GetAssayAt(self, index: int) -> ArcAssay:
        this: ArcInvestigation = self
        return this.Assays[index]

    @staticmethod
    def get_assay_at(index: int) -> Callable[[ArcInvestigation], ArcAssay]:
        def _arrow785(inv: ArcInvestigation) -> ArcAssay:
            new_investigation: ArcInvestigation = inv.Copy()
            return new_investigation.GetAssayAt(index)

        return _arrow785

    def GetAssay(self, assay_identifier: str) -> ArcAssay:
        this: ArcInvestigation = self
        match_value: ArcAssay | None = this.TryGetAssay(assay_identifier)
        if match_value is None:
            raise Exception(ArcTypesAux_ErrorMsgs_unableToFindAssayIdentifier(assay_identifier, this.Identifier))

        else: 
            return match_value


    @staticmethod
    def get_assay(assay_identifier: str) -> Callable[[ArcInvestigation], ArcAssay]:
        def _arrow786(inv: ArcInvestigation) -> ArcAssay:
            new_investigation: ArcInvestigation = inv.Copy()
            return new_investigation.GetAssay(assay_identifier)

        return _arrow786

    def TryGetAssay(self, assay_identifier: str) -> ArcAssay | None:
        this: ArcInvestigation = self
        def _arrow787(a: ArcAssay) -> bool:
            return a.Identifier == assay_identifier

        return try_find(_arrow787, this.Assays)

    @staticmethod
    def try_get_assay(assay_identifier: str) -> Callable[[ArcInvestigation], ArcAssay | None]:
        def _arrow788(inv: ArcInvestigation) -> ArcAssay | None:
            new_investigation: ArcInvestigation = inv.Copy()
            return new_investigation.TryGetAssay(assay_identifier)

        return _arrow788

    def ContainsAssay(self, assay_identifier: str) -> bool:
        this: ArcInvestigation = self
        def predicate(a: ArcAssay) -> bool:
            return a.Identifier == assay_identifier

        return exists(predicate, this.Assays)

    @staticmethod
    def contains_assay(assay_identifier: str) -> Callable[[ArcInvestigation], bool]:
        def _arrow789(inv: ArcInvestigation) -> bool:
            return inv.ContainsAssay(assay_identifier)

        return _arrow789

    @property
    def RegisteredStudyIdentifierCount(self, __unit: None=None) -> int:
        this: ArcInvestigation = self
        return len(this.RegisteredStudyIdentifiers)

    @property
    def RegisteredStudies(self, __unit: None=None) -> Array[ArcStudy]:
        this: ArcInvestigation = self
        def f(identifier: str) -> ArcStudy | None:
            return this.TryGetStudy(identifier)

        return ResizeArray_choose(f, this.RegisteredStudyIdentifiers)

    @property
    def RegisteredStudyCount(self, __unit: None=None) -> int:
        this: ArcInvestigation = self
        return len(this.RegisteredStudies)

    @property
    def VacantStudyIdentifiers(self, __unit: None=None) -> Array[str]:
        this: ArcInvestigation = self
        def f(arg: str) -> bool:
            return not this.ContainsStudy(arg)

        return ResizeArray_filter(f, this.RegisteredStudyIdentifiers)

    @property
    def StudyCount(self, __unit: None=None) -> int:
        this: ArcInvestigation = self
        return len(this.Studies)

    @property
    def StudyIdentifiers(self, __unit: None=None) -> Array[str]:
        this: ArcInvestigation = self
        def mapping(x: ArcStudy) -> str:
            return x.Identifier

        return to_array(map_2(mapping, this.Studies))

    @property
    def UnregisteredStudies(self, __unit: None=None) -> Array[ArcStudy]:
        this: ArcInvestigation = self
        def f(s: ArcStudy) -> bool:
            def _arrow792(__unit: None=None, s: Any=s) -> bool:
                source: Array[str] = this.RegisteredStudyIdentifiers
                def _arrow791(__unit: None=None) -> Callable[[str], bool]:
                    x: str = s.Identifier
                    def _arrow790(y: str) -> bool:
                        return x == y

                    return _arrow790

                return exists(_arrow791(), source)

            return not _arrow792()

        return ResizeArray_filter(f, this.Studies)

    def AddStudy(self, study: ArcStudy) -> None:
        this: ArcInvestigation = self
        study_1: ArcStudy = study
        def predicate(x: ArcStudy) -> bool:
            return x.Identifier == study_1.Identifier

        match_value: int | None = try_find_index(predicate, this.Studies)
        if match_value is None:
            pass

        else: 
            raise Exception(((("Cannot create study with name " + study_1.Identifier) + ", as study names must be unique and study at index ") + str(match_value)) + " has the same name.")

        study.Investigation = this
        (this.Studies.append(study))

    @staticmethod
    def add_study(study: ArcStudy) -> Callable[[ArcInvestigation], ArcInvestigation]:
        def _arrow793(inv: ArcInvestigation) -> ArcInvestigation:
            copy: ArcInvestigation = inv.Copy()
            copy.AddStudy(study)
            return copy

        return _arrow793

    def InitStudy(self, study_identifier: str) -> ArcStudy:
        this: ArcInvestigation = self
        study: ArcStudy = ArcStudy.init(study_identifier)
        this.AddStudy(study)
        return study

    @staticmethod
    def init_study(study_identifier: str) -> Callable[[ArcInvestigation], tuple[ArcInvestigation, ArcStudy]]:
        def _arrow794(inv: ArcInvestigation) -> tuple[ArcInvestigation, ArcStudy]:
            copy: ArcInvestigation = inv.Copy()
            return (copy, copy.InitStudy(study_identifier))

        return _arrow794

    def RegisterStudy(self, study_identifier: str) -> None:
        this: ArcInvestigation = self
        study_ident: str = study_identifier
        def predicate(x: str) -> bool:
            return x == study_ident

        match_value: str | None = try_find(predicate, this.StudyIdentifiers)
        if match_value is not None:
            pass

        else: 
            raise Exception(("The given study with identifier \'" + study_ident) + "\' must be added to Investigation before it can be registered.")

        study_ident_1: str = study_identifier
        class ObjectExpr796:
            @property
            def Equals(self) -> Callable[[str, str], bool]:
                def _arrow795(x_1: str, y: str) -> bool:
                    return x_1 == y

                return _arrow795

            @property
            def GetHashCode(self) -> Callable[[str], int]:
                return string_hash

        if contains(study_ident_1, this.RegisteredStudyIdentifiers, ObjectExpr796()):
            raise Exception(("Study with identifier \'" + study_ident_1) + "\' is already registered!")

        (this.RegisteredStudyIdentifiers.append(study_identifier))

    @staticmethod
    def register_study(study_identifier: str) -> Callable[[ArcInvestigation], ArcInvestigation]:
        def _arrow797(inv: ArcInvestigation) -> ArcInvestigation:
            copy: ArcInvestigation = inv.Copy()
            copy.RegisterStudy(study_identifier)
            return copy

        return _arrow797

    def AddRegisteredStudy(self, study: ArcStudy) -> None:
        this: ArcInvestigation = self
        this.AddStudy(study)
        this.RegisterStudy(study.Identifier)

    @staticmethod
    def add_registered_study(study: ArcStudy) -> Callable[[ArcInvestigation], ArcInvestigation]:
        def _arrow798(inv: ArcInvestigation) -> ArcInvestigation:
            copy: ArcInvestigation = inv.Copy()
            study_1: ArcStudy = study.Copy()
            copy.AddRegisteredStudy(study_1)
            return copy

        return _arrow798

    def DeleteStudyAt(self, index: int) -> None:
        this: ArcInvestigation = self
        this.Studies.pop(index)

    @staticmethod
    def delete_study_at(index: int) -> Callable[[ArcInvestigation], ArcInvestigation]:
        def _arrow799(i: ArcInvestigation) -> ArcInvestigation:
            copy: ArcInvestigation = i.Copy()
            copy.DeleteStudyAt(index)
            return copy

        return _arrow799

    def DeleteStudy(self, study_identifier: str) -> None:
        this: ArcInvestigation = self
        def _arrow800(s: ArcStudy) -> bool:
            return s.Identifier == study_identifier

        index: int = find_index(_arrow800, this.Studies) or 0
        this.DeleteStudyAt(index)

    @staticmethod
    def delete_study(study_identifier: str) -> Callable[[ArcInvestigation], ArcInvestigation]:
        def _arrow801(i: ArcInvestigation) -> ArcInvestigation:
            copy: ArcInvestigation = i.Copy()
            copy.DeleteStudy(study_identifier)
            return copy

        return _arrow801

    def RemoveStudyAt(self, index: int) -> None:
        this: ArcInvestigation = self
        ident: str = this.GetStudyAt(index).Identifier
        this.Studies.pop(index)
        this.DeregisterStudy(ident)

    @staticmethod
    def remove_study_at(index: int) -> Callable[[ArcInvestigation], ArcInvestigation]:
        def _arrow802(inv: ArcInvestigation) -> ArcInvestigation:
            new_inv: ArcInvestigation = inv.Copy()
            new_inv.RemoveStudyAt(index)
            return new_inv

        return _arrow802

    def RemoveStudy(self, study_identifier: str) -> None:
        this: ArcInvestigation = self
        index: int = this.GetStudyIndex(study_identifier) or 0
        this.RemoveStudyAt(index)

    @staticmethod
    def remove_study(study_identifier: str) -> Callable[[ArcInvestigation], ArcInvestigation]:
        def _arrow803(inv: ArcInvestigation) -> ArcInvestigation:
            copy: ArcInvestigation = inv.Copy()
            copy.RemoveStudy(study_identifier)
            return copy

        return _arrow803

    def SetStudyAt(self, index: int, study: ArcStudy) -> None:
        this: ArcInvestigation = self
        study_1: ArcStudy = study
        def predicate(x: ArcStudy) -> bool:
            return x.Identifier == study_1.Identifier

        match_value: int | None = try_find_index(predicate, remove_at(index, this.Studies))
        if match_value is None:
            pass

        else: 
            raise Exception(((("Cannot create study with name " + study_1.Identifier) + ", as study names must be unique and study at index ") + str(match_value)) + " has the same name.")

        study.Investigation = this
        this.Studies[index] = study

    @staticmethod
    def set_study_at(index: int, study: ArcStudy) -> Callable[[ArcInvestigation], ArcInvestigation]:
        def _arrow804(inv: ArcInvestigation) -> ArcInvestigation:
            new_inv: ArcInvestigation = inv.Copy()
            new_inv.SetStudyAt(index, study)
            return new_inv

        return _arrow804

    def SetStudy(self, study_identifier: str, study: ArcStudy) -> None:
        this: ArcInvestigation = self
        index: int = this.GetStudyIndex(study_identifier) or 0
        this.SetStudyAt(index, study)

    @staticmethod
    def set_study(study_identifier: str, study: ArcStudy) -> Callable[[ArcInvestigation], ArcInvestigation]:
        def _arrow805(inv: ArcInvestigation) -> ArcInvestigation:
            new_inv: ArcInvestigation = inv.Copy()
            new_inv.SetStudy(study_identifier, study)
            return new_inv

        return _arrow805

    def GetStudyIndex(self, study_identifier: str) -> int:
        this: ArcInvestigation = self
        def _arrow806(s: ArcStudy) -> bool:
            return s.Identifier == study_identifier

        index: int = find_index(_arrow806, this.Studies) or 0
        if index == -1:
            raise Exception(("Unable to find study with specified identifier \'" + study_identifier) + "\'!")

        return index

    @staticmethod
    def get_study_index(study_identifier: str) -> Callable[[ArcInvestigation], int]:
        def _arrow807(inv: ArcInvestigation) -> int:
            return inv.GetStudyIndex(study_identifier)

        return _arrow807

    def GetStudyAt(self, index: int) -> ArcStudy:
        this: ArcInvestigation = self
        return this.Studies[index]

    @staticmethod
    def get_study_at(index: int) -> Callable[[ArcInvestigation], ArcStudy]:
        def _arrow808(inv: ArcInvestigation) -> ArcStudy:
            new_inv: ArcInvestigation = inv.Copy()
            return new_inv.GetStudyAt(index)

        return _arrow808

    def GetStudy(self, study_identifier: str) -> ArcStudy:
        this: ArcInvestigation = self
        match_value: ArcStudy | None = this.TryGetStudy(study_identifier)
        if match_value is None:
            raise Exception(ArcTypesAux_ErrorMsgs_unableToFindStudyIdentifier(study_identifier, this.Identifier))

        else: 
            return match_value


    @staticmethod
    def get_study(study_identifier: str) -> Callable[[ArcInvestigation], ArcStudy]:
        def _arrow809(inv: ArcInvestigation) -> ArcStudy:
            new_inv: ArcInvestigation = inv.Copy()
            return new_inv.GetStudy(study_identifier)

        return _arrow809

    def TryGetStudy(self, study_identifier: str) -> ArcStudy | None:
        this: ArcInvestigation = self
        def predicate(s: ArcStudy) -> bool:
            return s.Identifier == study_identifier

        return try_find(predicate, this.Studies)

    @staticmethod
    def try_get_study(study_identifier: str) -> Callable[[ArcInvestigation], ArcStudy | None]:
        def _arrow810(inv: ArcInvestigation) -> ArcStudy | None:
            new_inv: ArcInvestigation = inv.Copy()
            return new_inv.TryGetStudy(study_identifier)

        return _arrow810

    def ContainsStudy(self, study_identifier: str) -> bool:
        this: ArcInvestigation = self
        def predicate(s: ArcStudy) -> bool:
            return s.Identifier == study_identifier

        return exists(predicate, this.Studies)

    @staticmethod
    def contains_study(study_identifier: str) -> Callable[[ArcInvestigation], bool]:
        def _arrow811(inv: ArcInvestigation) -> bool:
            return inv.ContainsStudy(study_identifier)

        return _arrow811

    def RegisterAssayAt(self, study_index: int, assay_identifier: str) -> None:
        this: ArcInvestigation = self
        study: ArcStudy = this.GetStudyAt(study_index)
        def predicate(x: str) -> bool:
            return x == assay_identifier

        def mapping(a: ArcAssay) -> str:
            return a.Identifier

        match_value: str | None = try_find(predicate, map_2(mapping, this.Assays))
        if match_value is not None:
            pass

        else: 
            raise Exception("The given assay must be added to Investigation before it can be registered.")

        assay_ident_1: str = assay_identifier
        def predicate_1(x_1: str) -> bool:
            return x_1 == assay_ident_1

        match_value_1: int | None = try_find_index(predicate_1, study.RegisteredAssayIdentifiers)
        if match_value_1 is None:
            pass

        else: 
            raise Exception(((("Cannot create assay with name " + assay_ident_1) + ", as assay names must be unique and assay at index ") + str(match_value_1)) + " has the same name.")

        study.RegisterAssay(assay_identifier)

    @staticmethod
    def register_assay_at(study_index: int, assay_identifier: str) -> Callable[[ArcInvestigation], ArcInvestigation]:
        def _arrow812(inv: ArcInvestigation) -> ArcInvestigation:
            copy: ArcInvestigation = inv.Copy()
            copy.RegisterAssayAt(study_index, assay_identifier)
            return copy

        return _arrow812

    def RegisterAssay(self, study_identifier: str, assay_identifier: str) -> None:
        this: ArcInvestigation = self
        index: int = this.GetStudyIndex(study_identifier) or 0
        this.RegisterAssayAt(index, assay_identifier)

    @staticmethod
    def register_assay(study_identifier: str, assay_identifier: str) -> Callable[[ArcInvestigation], ArcInvestigation]:
        def _arrow813(inv: ArcInvestigation) -> ArcInvestigation:
            copy: ArcInvestigation = inv.Copy()
            copy.RegisterAssay(study_identifier, assay_identifier)
            return copy

        return _arrow813

    def DeregisterAssayAt(self, study_index: int, assay_identifier: str) -> None:
        this: ArcInvestigation = self
        study: ArcStudy = this.GetStudyAt(study_index)
        study.DeregisterAssay(assay_identifier)

    @staticmethod
    def deregister_assay_at(study_index: int, assay_identifier: str) -> Callable[[ArcInvestigation], ArcInvestigation]:
        def _arrow814(inv: ArcInvestigation) -> ArcInvestigation:
            copy: ArcInvestigation = inv.Copy()
            copy.DeregisterAssayAt(study_index, assay_identifier)
            return copy

        return _arrow814

    def DeregisterAssay(self, study_identifier: str, assay_identifier: str) -> None:
        this: ArcInvestigation = self
        index: int = this.GetStudyIndex(study_identifier) or 0
        this.DeregisterAssayAt(index, assay_identifier)

    @staticmethod
    def deregister_assay(study_identifier: str, assay_identifier: str) -> Callable[[ArcInvestigation], ArcInvestigation]:
        def _arrow815(inv: ArcInvestigation) -> ArcInvestigation:
            copy: ArcInvestigation = inv.Copy()
            copy.DeregisterAssay(study_identifier, assay_identifier)
            return copy

        return _arrow815

    def DeregisterStudy(self, study_identifier: str) -> None:
        this: ArcInvestigation = self
        class ObjectExpr817:
            @property
            def Equals(self) -> Callable[[str, str], bool]:
                def _arrow816(x: str, y: str) -> bool:
                    return x == y

                return _arrow816

            @property
            def GetHashCode(self) -> Callable[[str], int]:
                return string_hash

        ignore(remove_in_place(study_identifier, this.RegisteredStudyIdentifiers, ObjectExpr817()))

    @staticmethod
    def deregister_study(study_identifier: str) -> Callable[[ArcInvestigation], ArcInvestigation]:
        def _arrow818(i: ArcInvestigation) -> ArcInvestigation:
            copy: ArcInvestigation = i.Copy()
            copy.DeregisterStudy(study_identifier)
            return copy

        return _arrow818

    def GetAllPersons(self, __unit: None=None) -> Array[Person]:
        this: ArcInvestigation = self
        persons: Array[Person] = []
        enumerator: Any = get_enumerator(this.Assays)
        try: 
            while enumerator.System_Collections_IEnumerator_MoveNext():
                a: ArcAssay = enumerator.System_Collections_Generic_IEnumerator_1_get_Current()
                add_range_in_place(a.Performers, persons)

        finally: 
            dispose(enumerator)

        enumerator_1: Any = get_enumerator(this.Studies)
        try: 
            while enumerator_1.System_Collections_IEnumerator_MoveNext():
                s: ArcStudy = enumerator_1.System_Collections_Generic_IEnumerator_1_get_Current()
                add_range_in_place(s.Contacts, persons)

        finally: 
            dispose(enumerator_1)

        add_range_in_place(this.Contacts, persons)
        class ObjectExpr820:
            @property
            def Equals(self) -> Callable[[Person, Person], bool]:
                return equals

            @property
            def GetHashCode(self) -> Callable[[Person], int]:
                return safe_hash

        return Array_distinct(list(persons), ObjectExpr820())

    def GetAllPublications(self, __unit: None=None) -> Array[Publication]:
        this: ArcInvestigation = self
        pubs: Array[Publication] = []
        enumerator: Any = get_enumerator(this.Studies)
        try: 
            while enumerator.System_Collections_IEnumerator_MoveNext():
                s: ArcStudy = enumerator.System_Collections_Generic_IEnumerator_1_get_Current()
                add_range_in_place(s.Publications, pubs)

        finally: 
            dispose(enumerator)

        add_range_in_place(this.Publications, pubs)
        class ObjectExpr821:
            @property
            def Equals(self) -> Callable[[Publication, Publication], bool]:
                return equals

            @property
            def GetHashCode(self) -> Callable[[Publication], int]:
                return safe_hash

        return Array_distinct(list(pubs), ObjectExpr821())

    def DeregisterMissingAssays(self, __unit: None=None) -> None:
        this: ArcInvestigation = self
        inv: ArcInvestigation = this
        existing_assays: Array[str] = inv.AssayIdentifiers
        enumerator: Any = get_enumerator(inv.Studies)
        try: 
            while enumerator.System_Collections_IEnumerator_MoveNext():
                study: ArcStudy = enumerator.System_Collections_Generic_IEnumerator_1_get_Current()
                enumerator_1: Any = get_enumerator(list(study.RegisteredAssayIdentifiers))
                try: 
                    while enumerator_1.System_Collections_IEnumerator_MoveNext():
                        registered_assay: str = enumerator_1.System_Collections_Generic_IEnumerator_1_get_Current()
                        class ObjectExpr823:
                            @property
                            def Equals(self) -> Callable[[str, str], bool]:
                                def _arrow822(x: str, y: str) -> bool:
                                    return x == y

                                return _arrow822

                            @property
                            def GetHashCode(self) -> Callable[[str], int]:
                                return string_hash

                        if not contains(registered_assay, existing_assays, ObjectExpr823()):
                            value_1: None = study.DeregisterAssay(registered_assay)
                            ignore(None)


                finally: 
                    dispose(enumerator_1)


        finally: 
            dispose(enumerator)


    @staticmethod
    def deregister_missing_assays(__unit: None=None) -> Callable[[ArcInvestigation], ArcInvestigation]:
        def _arrow824(inv: ArcInvestigation) -> ArcInvestigation:
            copy: ArcInvestigation = inv.Copy()
            copy.DeregisterMissingAssays()
            return copy

        return _arrow824

    def UpdateIOTypeByEntityID(self, __unit: None=None) -> None:
        this: ArcInvestigation = self
        def _arrow828(__unit: None=None) -> IEnumerable_1[ArcTable]:
            def _arrow825(study: ArcStudy) -> IEnumerable_1[ArcTable]:
                return study.Tables

            def _arrow827(__unit: None=None) -> IEnumerable_1[ArcTable]:
                def _arrow826(assay: ArcAssay) -> IEnumerable_1[ArcTable]:
                    return assay.Tables

                return collect(_arrow826, this.Assays)

            return append_4(collect(_arrow825, this.Studies), delay(_arrow827))

        io_map: Any = ArcTablesAux_getIOMap(list(to_list(delay(_arrow828))))
        enumerator: Any = get_enumerator(this.Studies)
        try: 
            while enumerator.System_Collections_IEnumerator_MoveNext():
                study_1: ArcStudy = enumerator.System_Collections_Generic_IEnumerator_1_get_Current()
                ArcTablesAux_applyIOMap(io_map, study_1.Tables)

        finally: 
            dispose(enumerator)

        enumerator_1: Any = get_enumerator(this.Assays)
        try: 
            while enumerator_1.System_Collections_IEnumerator_MoveNext():
                assay_1: ArcAssay = enumerator_1.System_Collections_Generic_IEnumerator_1_get_Current()
                ArcTablesAux_applyIOMap(io_map, assay_1.Tables)

        finally: 
            dispose(enumerator_1)


    def Copy(self, __unit: None=None) -> ArcInvestigation:
        this: ArcInvestigation = self
        next_assays: Array[ArcAssay] = []
        next_studies: Array[ArcStudy] = []
        enumerator: Any = get_enumerator(this.Assays)
        try: 
            while enumerator.System_Collections_IEnumerator_MoveNext():
                assay: ArcAssay = enumerator.System_Collections_Generic_IEnumerator_1_get_Current()
                copy: ArcAssay = assay.Copy()
                (next_assays.append(copy))

        finally: 
            dispose(enumerator)

        enumerator_1: Any = get_enumerator(this.Studies)
        try: 
            while enumerator_1.System_Collections_IEnumerator_MoveNext():
                study: ArcStudy = enumerator_1.System_Collections_Generic_IEnumerator_1_get_Current()
                copy_1: ArcStudy = study.Copy()
                (next_studies.append(copy_1))

        finally: 
            dispose(enumerator_1)

        def mapping(c: Comment) -> Comment:
            return c.Copy()

        next_comments: Array[Comment] = map(mapping, this.Comments, None)
        def mapping_1(c_1: Remark) -> Remark:
            return c_1.Copy()

        next_remarks: Array[Remark] = map(mapping_1, this.Remarks, None)
        def mapping_2(c_2: Person) -> Person:
            return c_2.Copy()

        next_contacts: Array[Person] = map(mapping_2, this.Contacts, None)
        def mapping_3(c_3: Publication) -> Publication:
            return c_3.Copy()

        next_publications: Array[Publication] = map(mapping_3, this.Publications, None)
        def mapping_4(c_4: OntologySourceReference) -> OntologySourceReference:
            return c_4.Copy()

        next_ontology_source_references: Array[OntologySourceReference] = map(mapping_4, this.OntologySourceReferences, None)
        next_study_identifiers: Array[str] = list(this.RegisteredStudyIdentifiers)
        return ArcInvestigation(this.Identifier, this.Title, this.Description, this.SubmissionDate, this.PublicReleaseDate, next_ontology_source_references, next_publications, next_contacts, next_assays, next_studies, next_study_identifiers, next_comments, next_remarks)

    def ToInvestigation(self, __unit: None=None) -> Investigation:
        this: ArcInvestigation = self
        def mapping(a: ArcStudy) -> Study:
            return a.ToStudy()

        studies: FSharpList[Study] | None = Option_fromValueWithDefault(empty(), map_3(mapping, to_list(this.RegisteredStudies)))
        return Investigation_create_4AD66BBE(None, "isa.investigation.xlsx", None if is_missing_identifier(this.Identifier) else this.Identifier, this.Title, this.Description, this.SubmissionDate, this.PublicReleaseDate, None, Option_fromValueWithDefault(empty(), of_array(this.Publications)), Option_fromValueWithDefault(empty(), of_array(this.Contacts)), studies, Option_fromValueWithDefault(empty(), of_array(this.Comments)))

    @staticmethod
    def from_investigation(i: Investigation) -> ArcInvestigation:
        identifer: str
        match_value: str | None = i.Identifier
        identifer = create_missing_identifier() if (match_value is None) else match_value
        def mapping(s: Study) -> tuple[ArcStudy, Array[ArcAssay]]:
            return ArcStudy.from_study(s)

        pattern_input: tuple[FSharpList[ArcStudy], FSharpList[Array[ArcAssay]]] = unzip(map_3(mapping, default_arg(i.Studies, empty())))
        studies_raw: FSharpList[ArcStudy] = pattern_input[0]
        studies: Array[ArcStudy] = list(studies_raw)
        def mapping_1(a: ArcStudy) -> str:
            return a.Identifier

        study_identifiers: Array[str] = list(map_2(mapping_1, studies_raw))
        def projection(a_1: ArcAssay) -> str:
            return a_1.Identifier

        class ObjectExpr832:
            @property
            def Equals(self) -> Callable[[str, str], bool]:
                def _arrow831(x: str, y: str) -> bool:
                    return x == y

                return _arrow831

            @property
            def GetHashCode(self) -> Callable[[str], int]:
                return string_hash

        assays: Array[ArcAssay] = list(distinct_by(projection, concat(pattern_input[1]), ObjectExpr832()))
        return ArcInvestigation.create(identifer, i.Title, i.Description, i.SubmissionDate, i.PublicReleaseDate, None, map_1(to_array_1, i.Publications), map_1(to_array_1, i.Contacts), assays, studies, study_identifiers, map_1(to_array_1, i.Comments))

    def StructurallyEquals(self, other: ArcInvestigation) -> bool:
        this: ArcInvestigation = self
        def predicate(x: bool) -> bool:
            return x == True

        def _arrow848(__unit: None=None) -> bool:
            a: IEnumerable_1[Publication] = this.Publications
            b: IEnumerable_1[Publication] = other.Publications
            def folder(acc: bool, e: bool) -> bool:
                if acc:
                    return e

                else: 
                    return False


            def _arrow847(__unit: None=None) -> IEnumerable_1[bool]:
                def _arrow846(i_1: int) -> bool:
                    return equals(item(i_1, a), item(i_1, b))

                return map_2(_arrow846, range_big_int(0, 1, length(a) - 1))

            return fold(folder, True, to_list(delay(_arrow847))) if (length(a) == length(b)) else False

        def _arrow851(__unit: None=None) -> bool:
            a_1: IEnumerable_1[Person] = this.Contacts
            b_1: IEnumerable_1[Person] = other.Contacts
            def folder_1(acc_1: bool, e_1: bool) -> bool:
                if acc_1:
                    return e_1

                else: 
                    return False


            def _arrow850(__unit: None=None) -> IEnumerable_1[bool]:
                def _arrow849(i_2: int) -> bool:
                    return equals(item(i_2, a_1), item(i_2, b_1))

                return map_2(_arrow849, range_big_int(0, 1, length(a_1) - 1))

            return fold(folder_1, True, to_list(delay(_arrow850))) if (length(a_1) == length(b_1)) else False

        def _arrow854(__unit: None=None) -> bool:
            a_2: IEnumerable_1[OntologySourceReference] = this.OntologySourceReferences
            b_2: IEnumerable_1[OntologySourceReference] = other.OntologySourceReferences
            def folder_2(acc_2: bool, e_2: bool) -> bool:
                if acc_2:
                    return e_2

                else: 
                    return False


            def _arrow853(__unit: None=None) -> IEnumerable_1[bool]:
                def _arrow852(i_3: int) -> bool:
                    return equals(item(i_3, a_2), item(i_3, b_2))

                return map_2(_arrow852, range_big_int(0, 1, length(a_2) - 1))

            return fold(folder_2, True, to_list(delay(_arrow853))) if (length(a_2) == length(b_2)) else False

        def _arrow857(__unit: None=None) -> bool:
            a_3: IEnumerable_1[ArcAssay] = this.Assays
            b_3: IEnumerable_1[ArcAssay] = other.Assays
            def folder_3(acc_3: bool, e_3: bool) -> bool:
                if acc_3:
                    return e_3

                else: 
                    return False


            def _arrow856(__unit: None=None) -> IEnumerable_1[bool]:
                def _arrow855(i_4: int) -> bool:
                    return equals(item(i_4, a_3), item(i_4, b_3))

                return map_2(_arrow855, range_big_int(0, 1, length(a_3) - 1))

            return fold(folder_3, True, to_list(delay(_arrow856))) if (length(a_3) == length(b_3)) else False

        def _arrow860(__unit: None=None) -> bool:
            a_4: IEnumerable_1[ArcStudy] = this.Studies
            b_4: IEnumerable_1[ArcStudy] = other.Studies
            def folder_4(acc_4: bool, e_4: bool) -> bool:
                if acc_4:
                    return e_4

                else: 
                    return False


            def _arrow859(__unit: None=None) -> IEnumerable_1[bool]:
                def _arrow858(i_5: int) -> bool:
                    return equals(item(i_5, a_4), item(i_5, b_4))

                return map_2(_arrow858, range_big_int(0, 1, length(a_4) - 1))

            return fold(folder_4, True, to_list(delay(_arrow859))) if (length(a_4) == length(b_4)) else False

        def _arrow863(__unit: None=None) -> bool:
            a_5: IEnumerable_1[str] = this.RegisteredStudyIdentifiers
            b_5: IEnumerable_1[str] = other.RegisteredStudyIdentifiers
            def folder_5(acc_5: bool, e_5: bool) -> bool:
                if acc_5:
                    return e_5

                else: 
                    return False


            def _arrow862(__unit: None=None) -> IEnumerable_1[bool]:
                def _arrow861(i_6: int) -> bool:
                    return item(i_6, a_5) == item(i_6, b_5)

                return map_2(_arrow861, range_big_int(0, 1, length(a_5) - 1))

            return fold(folder_5, True, to_list(delay(_arrow862))) if (length(a_5) == length(b_5)) else False

        def _arrow866(__unit: None=None) -> bool:
            a_6: IEnumerable_1[Comment] = this.Comments
            b_6: IEnumerable_1[Comment] = other.Comments
            def folder_6(acc_6: bool, e_6: bool) -> bool:
                if acc_6:
                    return e_6

                else: 
                    return False


            def _arrow865(__unit: None=None) -> IEnumerable_1[bool]:
                def _arrow864(i_7: int) -> bool:
                    return equals(item(i_7, a_6), item(i_7, b_6))

                return map_2(_arrow864, range_big_int(0, 1, length(a_6) - 1))

            return fold(folder_6, True, to_list(delay(_arrow865))) if (length(a_6) == length(b_6)) else False

        def _arrow869(__unit: None=None) -> bool:
            a_7: IEnumerable_1[Remark] = this.Remarks
            b_7: IEnumerable_1[Remark] = other.Remarks
            def folder_7(acc_7: bool, e_7: bool) -> bool:
                if acc_7:
                    return e_7

                else: 
                    return False


            def _arrow868(__unit: None=None) -> IEnumerable_1[bool]:
                def _arrow867(i_8: int) -> bool:
                    return equals(item(i_8, a_7), item(i_8, b_7))

                return map_2(_arrow867, range_big_int(0, 1, length(a_7) - 1))

            return fold(folder_7, True, to_list(delay(_arrow868))) if (length(a_7) == length(b_7)) else False

        return for_all(predicate, to_enumerable([this.Identifier == other.Identifier, equals(this.Title, other.Title), equals(this.Description, other.Description), equals(this.SubmissionDate, other.SubmissionDate), equals(this.PublicReleaseDate, other.PublicReleaseDate), _arrow848(), _arrow851(), _arrow854(), _arrow857(), _arrow860(), _arrow863(), _arrow866(), _arrow869()]))

    def ReferenceEquals(self, other: ArcStudy) -> bool:
        this: ArcInvestigation = self
        return this is other

    def __eq__(self, other: Any=None) -> bool:
        this: ArcInvestigation = self
        return this.StructurallyEquals(other) if isinstance(other, ArcInvestigation) else False

    def __hash__(self, __unit: None=None) -> Any:
        this: ArcInvestigation = self
        return HashCodes_boxHashArray([this.Identifier, HashCodes_boxHashOption(this.Title), HashCodes_boxHashOption(this.Description), HashCodes_boxHashOption(this.SubmissionDate), HashCodes_boxHashOption(this.PublicReleaseDate), HashCodes_boxHashArray(this.Publications), HashCodes_boxHashArray(this.Contacts), HashCodes_boxHashArray(this.OntologySourceReferences), HashCodes_boxHashArray(list(this.Assays)), HashCodes_boxHashArray(list(this.Studies)), HashCodes_boxHashArray(list(this.RegisteredStudyIdentifiers)), HashCodes_boxHashArray(this.Comments), HashCodes_boxHashArray(this.Remarks)])

    def GetLightHashCode(self, __unit: None=None) -> Any:
        this: ArcInvestigation = self
        return HashCodes_boxHashArray([this.Identifier, HashCodes_boxHashOption(this.Title), HashCodes_boxHashOption(this.Description), HashCodes_boxHashOption(this.SubmissionDate), HashCodes_boxHashOption(this.PublicReleaseDate), HashCodes_boxHashArray(this.Publications), HashCodes_boxHashArray(this.Contacts), HashCodes_boxHashArray(this.OntologySourceReferences), HashCodes_boxHashArray(this.Comments), HashCodes_boxHashArray(this.Remarks)])


ArcInvestigation_reflection = _expr870

def ArcInvestigation__ctor_21AB11E9(identifier: str, title: str | None=None, description: str | None=None, submission_date: str | None=None, public_release_date: str | None=None, ontology_source_references: Array[OntologySourceReference] | None=None, publications: Array[Publication] | None=None, contacts: Array[Person] | None=None, assays: Array[ArcAssay] | None=None, studies: Array[ArcStudy] | None=None, registered_study_identifiers: Array[str] | None=None, comments: Array[Comment] | None=None, remarks: Array[Remark] | None=None) -> ArcInvestigation:
    return ArcInvestigation(identifier, title, description, submission_date, public_release_date, ontology_source_references, publications, contacts, assays, studies, registered_study_identifiers, comments, remarks)


def ArcTypesAux_ErrorMsgs_unableToFindAssayIdentifier(assay_identifier: Any, investigation_identifier: Any) -> str:
    return ((("Error. Unable to find assay with identifier \'" + str(assay_identifier)) + "\' in investigation ") + str(investigation_identifier)) + "."


def ArcTypesAux_ErrorMsgs_unableToFindStudyIdentifier(study_identifer: Any, investigation_identifier: Any) -> str:
    return ((("Error. Unable to find study with identifier \'" + str(study_identifer)) + "\' in investigation ") + str(investigation_identifier)) + "."


__all__ = ["ArcAssay_reflection", "ArcStudy_reflection", "ArcInvestigation_reflection", "ArcTypesAux_ErrorMsgs_unableToFindAssayIdentifier", "ArcTypesAux_ErrorMsgs_unableToFindStudyIdentifier"]

