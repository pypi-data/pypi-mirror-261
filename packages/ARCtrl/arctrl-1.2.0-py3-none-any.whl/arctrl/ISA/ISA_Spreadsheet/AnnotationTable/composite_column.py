from __future__ import annotations
from typing import Any
from ....fable_modules.fable_library.array_ import map as map_2
from ....fable_modules.fable_library.list import (map, item, FSharpList, of_array, singleton as singleton_1)
from ....fable_modules.fable_library.range import range_big_int
from ....fable_modules.fable_library.seq import (to_array, delay, map as map_1, exists, to_list, append, singleton)
from ....fable_modules.fable_library.types import (to_string, Array)
from ....fable_modules.fable_library.util import IEnumerable_1
from ....fable_modules.fs_spreadsheet.Cells.fs_cell import FsCell
from ....fable_modules.fs_spreadsheet.fs_address import FsAddress__get_RowNumber
from ....fable_modules.fs_spreadsheet.fs_column import FsColumn
from ....fable_modules.fs_spreadsheet.Ranges.fs_range_address import FsRangeAddress__get_LastAddress
from ....fable_modules.fs_spreadsheet.Ranges.fs_range_base import FsRangeBase__get_RangeAddress
from ...ISA.ArcTypes.composite_cell import CompositeCell
from ...ISA.ArcTypes.composite_column import CompositeColumn
from ...ISA.ArcTypes.composite_header import (IOType, CompositeHeader)
from ...ISA_Spreadsheet.AnnotationTable.composite_cell import (from_fs_cells as from_fs_cells_1, to_fs_cells as to_fs_cells_1)
from ...ISA_Spreadsheet.AnnotationTable.composite_header import (from_fs_cells, to_fs_cells)

def fix_deprecated_ioheader(col: FsColumn) -> FsColumn:
    match_value: IOType = IOType.of_string(col.Item(1).ValueAsString())
    if match_value.tag == 6:
        return col

    elif match_value.tag == 0:
        col.Item(1).SetValueAs(to_string(CompositeHeader(11, IOType(0))))
        return col

    else: 
        col.Item(1).SetValueAs(to_string(CompositeHeader(12, match_value)))
        return col



def from_fs_columns(columns: FSharpList[FsColumn]) -> CompositeColumn:
    def mapping(c: FsColumn, columns: Any=columns) -> FsCell:
        return c.Item(1)

    header: CompositeHeader = from_fs_cells(map(mapping, columns))
    l: int = FsAddress__get_RowNumber(FsRangeAddress__get_LastAddress(FsRangeBase__get_RangeAddress(item(0, columns)))) or 0
    def _arrow884(__unit: None=None, columns: Any=columns) -> IEnumerable_1[CompositeCell]:
        def _arrow883(i: int) -> CompositeCell:
            def mapping_1(c_1: FsColumn) -> FsCell:
                return c_1.Item(i)

            return from_fs_cells_1(map(mapping_1, columns))

        return map_1(_arrow883, range_big_int(2, 1, l))

    cells_2: Array[CompositeCell] = to_array(delay(_arrow884))
    return CompositeColumn.create(header, cells_2)


def to_fs_columns(column: CompositeColumn) -> FSharpList[FSharpList[FsCell]]:
    def predicate(c: CompositeCell, column: Any=column) -> bool:
        return c.is_unitized

    has_unit: bool = exists(predicate, column.Cells)
    is_term: bool = column.Header.IsTermColumn
    header: FSharpList[FsCell] = to_fs_cells(has_unit, column.Header)
    def mapping(cell: CompositeCell, column: Any=column) -> FSharpList[FsCell]:
        return to_fs_cells_1(is_term, has_unit, cell)

    cells: Array[FSharpList[FsCell]] = map_2(mapping, column.Cells, None)
    if has_unit:
        def _arrow890(__unit: None=None, column: Any=column) -> IEnumerable_1[FsCell]:
            def _arrow889(__unit: None=None) -> IEnumerable_1[FsCell]:
                def _arrow888(i: int) -> FsCell:
                    return item(0, cells[i])

                return map_1(_arrow888, range_big_int(0, 1, len(column.Cells) - 1))

            return append(singleton(item(0, header)), delay(_arrow889))

        def _arrow893(__unit: None=None, column: Any=column) -> IEnumerable_1[FsCell]:
            def _arrow892(__unit: None=None) -> IEnumerable_1[FsCell]:
                def _arrow891(i_1: int) -> FsCell:
                    return item(1, cells[i_1])

                return map_1(_arrow891, range_big_int(0, 1, len(column.Cells) - 1))

            return append(singleton(item(1, header)), delay(_arrow892))

        def _arrow896(__unit: None=None, column: Any=column) -> IEnumerable_1[FsCell]:
            def _arrow895(__unit: None=None) -> IEnumerable_1[FsCell]:
                def _arrow894(i_2: int) -> FsCell:
                    return item(2, cells[i_2])

                return map_1(_arrow894, range_big_int(0, 1, len(column.Cells) - 1))

            return append(singleton(item(2, header)), delay(_arrow895))

        def _arrow899(__unit: None=None, column: Any=column) -> IEnumerable_1[FsCell]:
            def _arrow898(__unit: None=None) -> IEnumerable_1[FsCell]:
                def _arrow897(i_3: int) -> FsCell:
                    return item(3, cells[i_3])

                return map_1(_arrow897, range_big_int(0, 1, len(column.Cells) - 1))

            return append(singleton(item(3, header)), delay(_arrow898))

        return of_array([to_list(delay(_arrow890)), to_list(delay(_arrow893)), to_list(delay(_arrow896)), to_list(delay(_arrow899))])

    elif is_term:
        def _arrow905(__unit: None=None, column: Any=column) -> IEnumerable_1[FsCell]:
            def _arrow904(__unit: None=None) -> IEnumerable_1[FsCell]:
                def _arrow903(i_4: int) -> FsCell:
                    return item(0, cells[i_4])

                return map_1(_arrow903, range_big_int(0, 1, len(column.Cells) - 1))

            return append(singleton(item(0, header)), delay(_arrow904))

        def _arrow908(__unit: None=None, column: Any=column) -> IEnumerable_1[FsCell]:
            def _arrow907(__unit: None=None) -> IEnumerable_1[FsCell]:
                def _arrow906(i_5: int) -> FsCell:
                    return item(1, cells[i_5])

                return map_1(_arrow906, range_big_int(0, 1, len(column.Cells) - 1))

            return append(singleton(item(1, header)), delay(_arrow907))

        def _arrow911(__unit: None=None, column: Any=column) -> IEnumerable_1[FsCell]:
            def _arrow910(__unit: None=None) -> IEnumerable_1[FsCell]:
                def _arrow909(i_6: int) -> FsCell:
                    return item(2, cells[i_6])

                return map_1(_arrow909, range_big_int(0, 1, len(column.Cells) - 1))

            return append(singleton(item(2, header)), delay(_arrow910))

        return of_array([to_list(delay(_arrow905)), to_list(delay(_arrow908)), to_list(delay(_arrow911))])

    else: 
        def _arrow914(__unit: None=None, column: Any=column) -> IEnumerable_1[FsCell]:
            def _arrow913(__unit: None=None) -> IEnumerable_1[FsCell]:
                def _arrow912(i_7: int) -> FsCell:
                    return item(0, cells[i_7])

                return map_1(_arrow912, range_big_int(0, 1, len(column.Cells) - 1))

            return append(singleton(item(0, header)), delay(_arrow913))

        return singleton_1(to_list(delay(_arrow914)))



__all__ = ["fix_deprecated_ioheader", "from_fs_columns", "to_fs_columns"]

