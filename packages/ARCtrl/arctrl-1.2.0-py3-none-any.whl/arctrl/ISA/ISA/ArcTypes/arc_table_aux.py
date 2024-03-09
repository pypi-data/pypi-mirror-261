from __future__ import annotations
from collections.abc import Callable
from typing import (Any, TypeVar)
from ....fable_modules.fable_library.array_ import (iterate_indexed, map)
from ....fable_modules.fable_library.list import (cons, is_empty, tail as tail_1, head, FSharpList, empty, of_seq, choose, singleton, of_array as of_array_2, map as map_3, length, item, map_indexed, collect, try_pick as try_pick_1, sort_by, append as append_1, zip, exists, pick)
from ....fable_modules.fable_library.map import (of_array, try_find)
from ....fable_modules.fable_library.map_util import (get_item_from_dict, add_to_dict, remove_from_dict)
from ....fable_modules.fable_library.mutable_map import Dictionary
from ....fable_modules.fable_library.option import (some, value as value_9, default_arg, map as map_2)
from ....fable_modules.fable_library.seq import (max_by, try_find_index, filter, to_array, head as head_1, indexed, to_list, try_pick, map as map_1, delay, append, singleton as singleton_1, empty as empty_1)
from ....fable_modules.fable_library.seq2 import (Array_groupBy, List_groupBy)
from ....fable_modules.fable_library.set import (of_array as of_array_1, FSharpSet__Contains)
from ....fable_modules.fable_library.string_ import (to_fail, printf, remove)
from ....fable_modules.fable_library.types import (Array, Int32Array, to_string)
from ....fable_modules.fable_library.util import (IDictionary, compare_primitives, safe_hash, equals, IEnumerable_1, compare, ignore, get_enumerator, dispose, max, number_hash, int32_to_string, string_hash, equal_arrays, array_hash)
from ..helper import (Option_fromValueWithDefault, HashCodes_boxHashSeq, List_tryPickAndRemove)
from ..identifier import create_missing_identifier
from ..JsonTypes.column_index import (ARCtrl_ISA_OntologyAnnotation__OntologyAnnotation_SetColumnIndex_Z524259A4, try_get_parameter_column_index, try_get_component_index, try_get_characteristic_column_index, try_get_factor_column_index)
from ..JsonTypes.component import (Component_fromOptions, Component)
from ..JsonTypes.data import Data
from ..JsonTypes.data_file import DataFile
from ..JsonTypes.factor import Factor
from ..JsonTypes.factor_value import (FactorValue_create_18335379, FactorValue)
from ..JsonTypes.material_attribute import MaterialAttribute_create_Z6C54B221
from ..JsonTypes.material_attribute_value import (MaterialAttributeValue_create_7F714043, MaterialAttributeValue)
from ..JsonTypes.ontology_annotation import OntologyAnnotation
from ..JsonTypes.process import (Process_composeName, Process_make, Process, Process_decomposeName_Z721C83C5, Process_create_Z42860F3E)
from ..JsonTypes.process_input import (ProcessInput_createSource_7888CE42, ProcessInput_createSample_Z6DF16D07, ProcessInput_createMaterial_2363974C, ProcessInput_createImageFile_Z721C83C5, ProcessInput_createRawData_Z721C83C5, ProcessInput_createDerivedData_Z721C83C5, ProcessInput, ProcessInput__isSample, ProcessInput__isSource, ProcessInput__get_Name, ProcessInput_setCharacteristicValues, ProcessInput__isData, ProcessInput__isMaterial, ProcessInput_getCharacteristicValues_102B6859)
from ..JsonTypes.process_output import (ProcessOutput_createSample_Z6DF16D07, ProcessOutput_createMaterial_2363974C, ProcessOutput_createImageFile_Z721C83C5, ProcessOutput_createRawData_Z721C83C5, ProcessOutput_createDerivedData_Z721C83C5, ProcessOutput, ProcessOutput__isSample, ProcessOutput__get_Name, ProcessOutput_setFactorValues, ProcessOutput__isData, ProcessOutput__isMaterial, ProcessOutput_getFactorValues_11830B70)
from ..JsonTypes.process_parameter_value import ProcessParameterValue
from ..JsonTypes.protocol import (Protocol, Protocol_make)
from ..JsonTypes.protocol_parameter import ProtocolParameter
from ..JsonTypes.sample import Sample_create_E50ED22
from ..JsonTypes.source import Source_create_7A281ED9
from ..JsonTypes.value import Value as Value_1
from .composite_cell import CompositeCell
from .composite_column import CompositeColumn
from .composite_header import (CompositeHeader, IOType)

__A = TypeVar("__A")

__B = TypeVar("__B")

def Dictionary_tryFind(key: __A, table: IDictionary[__A, __B]) -> __B | None:
    if key in table:
        return some(get_item_from_dict(table, key))

    else: 
        return None



def get_column_count(headers: Array[CompositeHeader]) -> int:
    return len(headers)


def get_row_count(values: Any) -> int:
    if len(values) == 0:
        return 0

    else: 
        def projection(tuple: tuple[int, int], values: Any=values) -> int:
            return tuple[1]

        class ObjectExpr446:
            @property
            def Compare(self) -> Callable[[int, int], int]:
                return compare_primitives

        return 1 + max_by(projection, values.keys(), ObjectExpr446())[1]



def box_hash_values(col_count: int, values: Any) -> Any:
    hash_1: int = 0
    row_count: int = get_row_count(values) or 0
    for col in range(0, (col_count - 1) + 1, 1):
        for row in range(0, (row_count - 1) + 1, 1):
            hash_1 = (((-1640531527 + safe_hash(get_item_from_dict(values, (col, row)))) + (hash_1 << 6)) + (hash_1 >> 2)) or 0
    return hash_1


def _007CIsUniqueExistingHeader_007C__007C(existing_headers: IEnumerable_1[CompositeHeader], input: CompositeHeader) -> int | None:
    if ((((input.tag == 3) or (input.tag == 2)) or (input.tag == 1)) or (input.tag == 0)) or (input.tag == 13):
        return None

    elif input.tag == 12:
        def _arrow447(h: CompositeHeader, existing_headers: Any=existing_headers, input: Any=input) -> bool:
            return True if (h.tag == 12) else False

        return try_find_index(_arrow447, existing_headers)

    elif input.tag == 11:
        def _arrow448(h_1: CompositeHeader, existing_headers: Any=existing_headers, input: Any=input) -> bool:
            return True if (h_1.tag == 11) else False

        return try_find_index(_arrow448, existing_headers)

    else: 
        def _arrow449(h_2: CompositeHeader, existing_headers: Any=existing_headers, input: Any=input) -> bool:
            return equals(h_2, input)

        return try_find_index(_arrow449, existing_headers)



def try_find_duplicate_unique(new_header: CompositeHeader, existing_headers: IEnumerable_1[CompositeHeader]) -> int | None:
    active_pattern_result: int | None = _007CIsUniqueExistingHeader_007C__007C(existing_headers, new_header)
    if active_pattern_result is not None:
        index: int = active_pattern_result or 0
        return index

    else: 
        return None



def try_find_duplicate_unique_in_array(existing_headers: IEnumerable_1[CompositeHeader]) -> FSharpList[dict[str, Any]]:
    def loop(i_mut: int, duplicate_list_mut: FSharpList[dict[str, Any]], header_list_mut: FSharpList[CompositeHeader], existing_headers: Any=existing_headers) -> FSharpList[dict[str, Any]]:
        while True:
            (i, duplicate_list, header_list) = (i_mut, duplicate_list_mut, header_list_mut)
            (pattern_matching_result, header, tail) = (None, None, None)
            if is_empty(header_list):
                pattern_matching_result = 0

            elif is_empty(tail_1(header_list)):
                pattern_matching_result = 0

            else: 
                pattern_matching_result = 1
                header = head(header_list)
                tail = tail_1(header_list)

            if pattern_matching_result == 0:
                return duplicate_list

            elif pattern_matching_result == 1:
                has_duplicate: int | None = try_find_duplicate_unique(header, tail)
                i_mut = i + 1
                duplicate_list_mut = cons({
                    "HeaderType": header,
                    "Index1": i,
                    "Index2": value_9(has_duplicate)
                }, duplicate_list) if (has_duplicate is not None) else duplicate_list
                header_list_mut = tail
                continue

            break

    def predicate(x: CompositeHeader, existing_headers: Any=existing_headers) -> bool:
        return not x.IsTermColumn

    return loop(0, empty(), of_seq(filter(predicate, existing_headers)))


def SanityChecks_validateColumnIndex(index: int, column_count: int, allow_append: bool) -> None:
    if index < 0:
        raise Exception("Cannot insert CompositeColumn at index < 0.")

    def _arrow450(__unit: None=None, index: Any=index, column_count: Any=column_count, allow_append: Any=allow_append) -> bool:
        x: int = index or 0
        y: int = column_count or 0
        return (compare(x, y) > 0) if allow_append else (compare(x, y) >= 0)

    if _arrow450():
        raise Exception(("Specified index is out of table range! Table contains only " + str(column_count)) + " columns.")



def SanityChecks_validateRowIndex(index: int, row_count: int, allow_append: bool) -> None:
    if index < 0:
        raise Exception("Cannot insert CompositeColumn at index < 0.")

    def _arrow451(__unit: None=None, index: Any=index, row_count: Any=row_count, allow_append: Any=allow_append) -> bool:
        x: int = index or 0
        y: int = row_count or 0
        return (compare(x, y) > 0) if allow_append else (compare(x, y) >= 0)

    if _arrow451():
        raise Exception(("Specified index is out of table range! Table contains only " + str(row_count)) + " rows.")



def SanityChecks_validateColumn(column: CompositeColumn) -> None:
    ignore(column.Validate(True))


def Unchecked_tryGetCellAt(column: int, row: int, cells: Any) -> CompositeCell | None:
    return Dictionary_tryFind((column, row), cells)


def Unchecked_setCellAt(column_index: int, row_index: int, c: CompositeCell, cells: Any) -> None:
    cells[column_index, row_index] = c


def Unchecked_addCellAt(column_index: int, row_index: int, c: CompositeCell, cells: Any) -> None:
    add_to_dict(cells, (column_index, row_index), c)


def Unchecked_moveCellTo(from_col: int, from_row: int, to_col: int, to_row: int, cells: Any) -> None:
    match_value: CompositeCell | None = Dictionary_tryFind((from_col, from_row), cells)
    if match_value is None:
        pass

    else: 
        c: CompositeCell = match_value
        ignore(remove_from_dict(cells, (from_col, from_row)))
        value_1: None = Unchecked_setCellAt(to_col, to_row, c, cells)
        ignore(None)



def Unchecked_removeHeader(index: int, headers: Array[CompositeHeader]) -> None:
    headers.pop(index)


def Unchecked_removeColumnCells(index: int, cells: Any) -> None:
    enumerator: Any = get_enumerator(cells)
    try: 
        while enumerator.System_Collections_IEnumerator_MoveNext():
            active_pattern_result: tuple[tuple[int, int], CompositeCell] = enumerator.System_Collections_Generic_IEnumerator_1_get_Current()
            c: int = active_pattern_result[0][0] or 0
            if c == index:
                ignore(remove_from_dict(cells, (c, active_pattern_result[0][1])))


    finally: 
        dispose(enumerator)



def Unchecked_removeColumnCells_withIndexChange(index: int, column_count: int, row_count: int, cells: Any) -> None:
    for col in range(index, (column_count - 1) + 1, 1):
        for row in range(0, (row_count - 1) + 1, 1):
            if col == index:
                ignore(remove_from_dict(cells, (col, row)))

            elif col > index:
                Unchecked_moveCellTo(col, row, col - 1, row, cells)



def Unchecked_removeRowCells(row_index: int, cells: Any) -> None:
    enumerator: Any = get_enumerator(cells)
    try: 
        while enumerator.System_Collections_IEnumerator_MoveNext():
            active_pattern_result: tuple[tuple[int, int], CompositeCell] = enumerator.System_Collections_Generic_IEnumerator_1_get_Current()
            r: int = active_pattern_result[0][1] or 0
            if r == row_index:
                ignore(remove_from_dict(cells, (active_pattern_result[0][0], r)))


    finally: 
        dispose(enumerator)



def Unchecked_removeRowCells_withIndexChange(row_index: int, column_count: int, row_count: int, cells: Any) -> None:
    for row in range(row_index, (row_count - 1) + 1, 1):
        for col in range(0, (column_count - 1) + 1, 1):
            if row == row_index:
                ignore(remove_from_dict(cells, (col, row)))

            elif row > row_index:
                Unchecked_moveCellTo(col, row, col, row - 1, cells)



def Unchecked_getEmptyCellForHeader(header: CompositeHeader, colum_cell_option: CompositeCell | None=None) -> CompositeCell:
    match_value: bool = header.IsTermColumn
    if match_value:
        (pattern_matching_result,) = (None,)
        if colum_cell_option is None:
            pattern_matching_result = 0

        elif colum_cell_option.tag == 0:
            pattern_matching_result = 0

        elif colum_cell_option.tag == 2:
            pattern_matching_result = 1

        else: 
            pattern_matching_result = 2

        if pattern_matching_result == 0:
            return CompositeCell.empty_term()

        elif pattern_matching_result == 1:
            return CompositeCell.empty_unitized()

        elif pattern_matching_result == 2:
            raise Exception("[extendBodyCells] This should never happen, IsTermColumn header must be paired with either term or unitized cell.")


    else: 
        return CompositeCell.empty_free_text()



def Unchecked_addColumn(new_header: CompositeHeader, new_cells: Array[CompositeCell], index: int, force_replace: bool, only_headers: bool, headers: Array[CompositeHeader], values: Any) -> None:
    number_of_new_columns: int = 1
    index_1: int = index or 0
    has_duplicate_unique: int | None = try_find_duplicate_unique(new_header, headers)
    if (has_duplicate_unique is not None) if (not force_replace) else False:
        raise Exception(((("Invalid new column `" + str(new_header)) + "`. Table already contains header of the same type on index `") + str(value_9(has_duplicate_unique))) + "`")

    if has_duplicate_unique is not None:
        number_of_new_columns = 0
        index_1 = value_9(has_duplicate_unique) or 0

    matchValue: int = get_column_count(headers) or 0
    matchValue_1: int = get_row_count(values) or 0
    start_col_count: int = matchValue or 0
    if has_duplicate_unique is not None:
        Unchecked_removeHeader(index_1, headers)

    headers.insert(index_1, new_header)
    if (has_duplicate_unique is None) if (index_1 < start_col_count) else False:
        def _arrow452(x: int, y: int, new_header: Any=new_header, new_cells: Any=new_cells, index: Any=index, force_replace: Any=force_replace, only_headers: Any=only_headers, headers: Any=headers, values: Any=values) -> int:
            return compare_primitives(x, y)

        last_column_index: int = max(_arrow452, start_col_count - 1, 0) or 0
        for column_index in range(last_column_index, index_1 - 1, -1):
            for row_index in range(0, matchValue_1 + 1, 1):
                Unchecked_moveCellTo(column_index, row_index, column_index + number_of_new_columns, row_index, values)

    if not only_headers:
        if has_duplicate_unique is not None:
            Unchecked_removeColumnCells(index_1, values)

        def _arrow454(tupled_arg: tuple[int, int, CompositeCell], new_header: Any=new_header, new_cells: Any=new_cells, index: Any=index, force_replace: Any=force_replace, only_headers: Any=only_headers, headers: Any=headers, values: Any=values) -> Callable[[Any], None]:
            def _arrow453(values_1: Any) -> None:
                value: None = add_to_dict(values_1, (tupled_arg[0], tupled_arg[1]), tupled_arg[2])
                ignore(None)

            return _arrow453

        def _arrow456(tupled_arg_1: tuple[int, int, CompositeCell], new_header: Any=new_header, new_cells: Any=new_cells, index: Any=index, force_replace: Any=force_replace, only_headers: Any=only_headers, headers: Any=headers, values: Any=values) -> Callable[[Any], None]:
            def _arrow455(cells: Any) -> None:
                Unchecked_setCellAt(tupled_arg_1[0], tupled_arg_1[1], tupled_arg_1[2], cells)

            return _arrow455

        f: Callable[[tuple[int, int, CompositeCell], Any], None] = _arrow454 if (index_1 >= start_col_count) else _arrow456
        def action(row_index_3: int, cell_1: CompositeCell, new_header: Any=new_header, new_cells: Any=new_cells, index: Any=index, force_replace: Any=force_replace, only_headers: Any=only_headers, headers: Any=headers, values: Any=values) -> None:
            f((index_1, row_index_3, cell_1))(values)

        iterate_indexed(action, new_cells)



def Unchecked_fillMissingCells(headers: Array[CompositeHeader], values: Any) -> None:
    row_count: int = get_row_count(values) or 0
    column_count: int = get_column_count(headers) or 0
    def projection(tuple: tuple[int, int], headers: Any=headers, values: Any=values) -> int:
        return tuple[0]

    class ObjectExpr458:
        @property
        def Equals(self) -> Callable[[int, int], bool]:
            def _arrow457(x: int, y: int) -> bool:
                return x == y

            return _arrow457

        @property
        def GetHashCode(self) -> Callable[[int], int]:
            return number_hash

    class ObjectExpr459:
        @property
        def Compare(self) -> Callable[[int, int], int]:
            return compare_primitives

    column_key_groups: Any = of_array(Array_groupBy(projection, to_array(values.keys()), ObjectExpr458()), ObjectExpr459())
    for column_index in range(0, (column_count - 1) + 1, 1):
        header: CompositeHeader = headers[column_index]
        match_value: Array[tuple[int, int]] | None = try_find(column_index, column_key_groups)
        if match_value is None:
            default_cell_1: CompositeCell = Unchecked_getEmptyCellForHeader(header, None)
            for row_index_1 in range(0, (row_count - 1) + 1, 1):
                Unchecked_addCellAt(column_index, row_index_1, default_cell_1, values)

        elif len(match_value) == row_count:
            col_1: Array[tuple[int, int]] = match_value

        else: 
            col_2: Array[tuple[int, int]] = match_value
            default_cell: CompositeCell = Unchecked_getEmptyCellForHeader(header, get_item_from_dict(values, head_1(col_2)))
            def _arrow460(tuple_1: tuple[int, int], headers: Any=headers, values: Any=values) -> int:
                return tuple_1[1]

            class ObjectExpr461:
                @property
                def Compare(self) -> Callable[[int, int], int]:
                    return compare_primitives

            row_keys: Any = of_array_1(map(_arrow460, col_2, Int32Array), ObjectExpr461())
            for row_index in range(0, (row_count - 1) + 1, 1):
                if not FSharpSet__Contains(row_keys, row_index):
                    Unchecked_addCellAt(column_index, row_index, default_cell, values)




def Unchecked_extendToRowCount(row_count: int, headers: Array[CompositeHeader], values: Any) -> None:
    column_count: int = get_column_count(headers) or 0
    previous_row_count: int = get_row_count(values) or 0
    for column_index in range(0, (column_count - 1) + 1, 1):
        last_value: CompositeCell = get_item_from_dict(values, (column_index, previous_row_count - 1))
        for row_index in range(previous_row_count - 1, (row_count - 1) + 1, 1):
            Unchecked_setCellAt(column_index, row_index, last_value, values)


def Unchecked_addRow(index: int, new_cells: Array[CompositeCell], headers: Array[CompositeHeader], values: Any) -> None:
    row_count: int = get_row_count(values) or 0
    column_count: int = get_column_count(headers) or 0
    increase_row_indices: None
    if index < row_count:
        def _arrow462(x: int, y: int, index: Any=index, new_cells: Any=new_cells, headers: Any=headers, values: Any=values) -> int:
            return compare_primitives(x, y)

        last_row_index: int = max(_arrow462, row_count - 1, 0) or 0
        for row_index in range(last_row_index, index - 1, -1):
            for column_index in range(0, (column_count - 1) + 1, 1):
                Unchecked_moveCellTo(column_index, row_index, column_index, row_index + 1, values)

    else: 
        increase_row_indices = None

    def action(column_index_1: int, cell: CompositeCell, index: Any=index, new_cells: Any=new_cells, headers: Any=headers, values: Any=values) -> None:
        Unchecked_setCellAt(column_index_1, index, cell, values)

    set_new_cells: None = iterate_indexed(action, new_cells)


def Unchecked_addRows(index: int, new_rows: Array[Array[CompositeCell]], headers: Array[CompositeHeader], values: Any) -> None:
    row_count: int = get_row_count(values) or 0
    column_count: int = get_column_count(headers) or 0
    num_new_rows: int = len(new_rows) or 0
    increase_row_indices: None
    if index < row_count:
        def _arrow463(x: int, y: int, index: Any=index, new_rows: Any=new_rows, headers: Any=headers, values: Any=values) -> int:
            return compare_primitives(x, y)

        last_row_index: int = max(_arrow463, row_count - 1, 0) or 0
        for row_index in range(last_row_index, index - 1, -1):
            for column_index in range(0, (column_count - 1) + 1, 1):
                Unchecked_moveCellTo(column_index, row_index, column_index, row_index + num_new_rows, values)

    else: 
        increase_row_indices = None

    current_row_index: int = index or 0
    for idx in range(0, (len(new_rows) - 1) + 1, 1):
        def action(column_index_1: int, cell: CompositeCell, index: Any=index, new_rows: Any=new_rows, headers: Any=headers, values: Any=values) -> None:
            Unchecked_setCellAt(column_index_1, current_row_index, cell, values)

        set_new_cells: None = iterate_indexed(action, new_rows[idx])
        current_row_index = (current_row_index + 1) or 0


def JsonTypes_valueOfCell(value: CompositeCell) -> tuple[Value_1, OntologyAnnotation | None]:
    if value.tag == 0:
        return (Value_1(0, value.fields[0]), None)

    elif value.tag == 2:
        return (Value_1.from_string(value.fields[0]), value.fields[1])

    else: 
        return (Value_1.from_string(value.fields[0]), None)



def JsonTypes_composeComponent(header: CompositeHeader, value: CompositeCell) -> Component:
    pattern_input: tuple[Value_1, OntologyAnnotation | None] = JsonTypes_valueOfCell(value)
    return Component_fromOptions(pattern_input[0], pattern_input[1], header.ToTerm())


def JsonTypes_composeParameterValue(header: CompositeHeader, value: CompositeCell) -> ProcessParameterValue:
    pattern_input: tuple[Value_1, OntologyAnnotation | None] = JsonTypes_valueOfCell(value)
    p: ProtocolParameter = ProtocolParameter.create(None, header.ToTerm())
    return ProcessParameterValue.create(p, pattern_input[0], pattern_input[1])


def JsonTypes_composeFactorValue(header: CompositeHeader, value: CompositeCell) -> FactorValue:
    pattern_input: tuple[Value_1, OntologyAnnotation | None] = JsonTypes_valueOfCell(value)
    return FactorValue_create_18335379(None, Factor.create(None, to_string(header), header.ToTerm()), pattern_input[0], pattern_input[1])


def JsonTypes_composeCharacteristicValue(header: CompositeHeader, value: CompositeCell) -> MaterialAttributeValue:
    pattern_input: tuple[Value_1, OntologyAnnotation | None] = JsonTypes_valueOfCell(value)
    return MaterialAttributeValue_create_7F714043(None, MaterialAttribute_create_Z6C54B221(None, header.ToTerm()), pattern_input[0], pattern_input[1])


def JsonTypes_composeProcessInput(header: CompositeHeader, value: CompositeCell) -> ProcessInput:
    (pattern_matching_result,) = (None,)
    if header.tag == 11:
        if header.fields[0].tag == 0:
            pattern_matching_result = 0

        elif header.fields[0].tag == 1:
            pattern_matching_result = 1

        elif header.fields[0].tag == 5:
            pattern_matching_result = 2

        elif header.fields[0].tag == 4:
            pattern_matching_result = 3

        elif header.fields[0].tag == 2:
            pattern_matching_result = 4

        elif header.fields[0].tag == 3:
            pattern_matching_result = 5

        else: 
            pattern_matching_result = 6


    else: 
        pattern_matching_result = 6

    if pattern_matching_result == 0:
        return ProcessInput_createSource_7888CE42(to_string(value))

    elif pattern_matching_result == 1:
        return ProcessInput_createSample_Z6DF16D07(to_string(value))

    elif pattern_matching_result == 2:
        return ProcessInput_createMaterial_2363974C(to_string(value))

    elif pattern_matching_result == 3:
        return ProcessInput_createImageFile_Z721C83C5(to_string(value))

    elif pattern_matching_result == 4:
        return ProcessInput_createRawData_Z721C83C5(to_string(value))

    elif pattern_matching_result == 5:
        return ProcessInput_createDerivedData_Z721C83C5(to_string(value))

    elif pattern_matching_result == 6:
        return to_fail(printf("Could not parse input header %O"))(header)



def JsonTypes_composeProcessOutput(header: CompositeHeader, value: CompositeCell) -> ProcessOutput:
    (pattern_matching_result,) = (None,)
    if header.tag == 12:
        if header.fields[0].tag == 1:
            pattern_matching_result = 0

        elif header.fields[0].tag == 5:
            pattern_matching_result = 1

        elif header.fields[0].tag == 4:
            pattern_matching_result = 2

        elif header.fields[0].tag == 2:
            pattern_matching_result = 3

        elif header.fields[0].tag == 3:
            pattern_matching_result = 4

        else: 
            pattern_matching_result = 5


    else: 
        pattern_matching_result = 5

    if pattern_matching_result == 0:
        return ProcessOutput_createSample_Z6DF16D07(to_string(value))

    elif pattern_matching_result == 1:
        return ProcessOutput_createMaterial_2363974C(to_string(value))

    elif pattern_matching_result == 2:
        return ProcessOutput_createImageFile_Z721C83C5(to_string(value))

    elif pattern_matching_result == 3:
        return ProcessOutput_createRawData_Z721C83C5(to_string(value))

    elif pattern_matching_result == 4:
        return ProcessOutput_createDerivedData_Z721C83C5(to_string(value))

    elif pattern_matching_result == 5:
        return to_fail(printf("Could not parse output header %O"))(header)



def JsonTypes_cellOfValue(value: Value_1 | None=None, unit: OntologyAnnotation | None=None) -> CompositeCell:
    value_2: Value_1 = default_arg(value, Value_1(3, ""))
    if value_2.tag == 3:
        if unit is not None:
            u: OntologyAnnotation = unit
            return CompositeCell(2, value_2.fields[0], u)

        else: 
            return CompositeCell(1, value_2.fields[0])


    elif value_2.tag == 2:
        if unit is None:
            return CompositeCell(1, to_string(value_2.fields[0]))

        else: 
            u_1: OntologyAnnotation = unit
            return CompositeCell(2, to_string(value_2.fields[0]), u_1)


    elif value_2.tag == 1:
        if unit is None:
            return CompositeCell(1, int32_to_string(value_2.fields[0]))

        else: 
            u_2: OntologyAnnotation = unit
            return CompositeCell(2, int32_to_string(value_2.fields[0]), u_2)


    elif unit is None:
        return CompositeCell(0, value_2.fields[0])

    else: 
        return to_fail(printf("Could not parse value %O with unit %O"))(value_2)(unit)



def JsonTypes_decomposeComponent(c: Component) -> tuple[CompositeHeader, CompositeCell]:
    return (CompositeHeader(0, value_9(c.ComponentType)), JsonTypes_cellOfValue(c.ComponentValue, c.ComponentUnit))


def JsonTypes_decomposeParameterValue(ppv: ProcessParameterValue) -> tuple[CompositeHeader, CompositeCell]:
    return (CompositeHeader(3, value_9(value_9(ppv.Category).ParameterName)), JsonTypes_cellOfValue(ppv.Value, ppv.Unit))


def JsonTypes_decomposeFactorValue(fv: FactorValue) -> tuple[CompositeHeader, CompositeCell]:
    return (CompositeHeader(2, value_9(value_9(fv.Category).FactorType)), JsonTypes_cellOfValue(fv.Value, fv.Unit))


def JsonTypes_decomposeCharacteristicValue(cv: MaterialAttributeValue) -> tuple[CompositeHeader, CompositeCell]:
    return (CompositeHeader(1, value_9(value_9(cv.Category).CharacteristicType)), JsonTypes_cellOfValue(cv.Value, cv.Unit))


def JsonTypes_decomposeProcessInput(pi: ProcessInput) -> tuple[CompositeHeader, CompositeCell]:
    if pi.tag == 1:
        return (CompositeHeader(11, IOType(1)), CompositeCell(1, default_arg(pi.fields[0].Name, "")))

    elif pi.tag == 3:
        return (CompositeHeader(11, IOType(5)), CompositeCell(1, default_arg(pi.fields[0].Name, "")))

    elif pi.tag == 2:
        d: Data = pi.fields[0]
        data_type: DataFile = value_9(d.DataType)
        if data_type.tag == 0:
            return (CompositeHeader(11, IOType(2)), CompositeCell(1, default_arg(d.Name, "")))

        elif data_type.tag == 1:
            return (CompositeHeader(11, IOType(3)), CompositeCell(1, default_arg(d.Name, "")))

        else: 
            return (CompositeHeader(11, IOType(4)), CompositeCell(1, default_arg(d.Name, "")))


    else: 
        return (CompositeHeader(11, IOType(0)), CompositeCell(1, default_arg(pi.fields[0].Name, "")))



def JsonTypes_decomposeProcessOutput(po: ProcessOutput) -> tuple[CompositeHeader, CompositeCell]:
    if po.tag == 2:
        return (CompositeHeader(12, IOType(5)), CompositeCell(1, default_arg(po.fields[0].Name, "")))

    elif po.tag == 1:
        d: Data = po.fields[0]
        data_type: DataFile = value_9(d.DataType)
        if data_type.tag == 0:
            return (CompositeHeader(12, IOType(2)), CompositeCell(1, default_arg(d.Name, "")))

        elif data_type.tag == 1:
            return (CompositeHeader(12, IOType(3)), CompositeCell(1, default_arg(d.Name, "")))

        else: 
            return (CompositeHeader(12, IOType(4)), CompositeCell(1, default_arg(d.Name, "")))


    else: 
        return (CompositeHeader(12, IOType(1)), CompositeCell(1, default_arg(po.fields[0].Name, "")))



def ProcessParsing_tryComponentGetter(general_i: int, value_i: int, value_header: CompositeHeader) -> Callable[[Any, int], Component] | None:
    if value_header.tag == 0:
        cat: CompositeHeader = CompositeHeader(0, ARCtrl_ISA_OntologyAnnotation__OntologyAnnotation_SetColumnIndex_Z524259A4(value_header.fields[0], value_i))
        def Value(matrix: Any, general_i: Any=general_i, value_i: Any=value_i, value_header: Any=value_header) -> Callable[[int], Component]:
            def _arrow464(i: int, matrix: Any=matrix) -> Component:
                return JsonTypes_composeComponent(cat, get_item_from_dict(matrix, (general_i, i)))

            return _arrow464

        return Value

    else: 
        return None



def ProcessParsing_tryParameterGetter(general_i: int, value_i: int, value_header: CompositeHeader) -> Callable[[Any, int], ProcessParameterValue] | None:
    if value_header.tag == 3:
        cat: CompositeHeader = CompositeHeader(3, ARCtrl_ISA_OntologyAnnotation__OntologyAnnotation_SetColumnIndex_Z524259A4(value_header.fields[0], value_i))
        def Value(matrix: Any, general_i: Any=general_i, value_i: Any=value_i, value_header: Any=value_header) -> Callable[[int], ProcessParameterValue]:
            def _arrow465(i: int, matrix: Any=matrix) -> ProcessParameterValue:
                return JsonTypes_composeParameterValue(cat, get_item_from_dict(matrix, (general_i, i)))

            return _arrow465

        return Value

    else: 
        return None



def ProcessParsing_tryFactorGetter(general_i: int, value_i: int, value_header: CompositeHeader) -> Callable[[Any, int], FactorValue] | None:
    if value_header.tag == 2:
        cat: CompositeHeader = CompositeHeader(2, ARCtrl_ISA_OntologyAnnotation__OntologyAnnotation_SetColumnIndex_Z524259A4(value_header.fields[0], value_i))
        def Value(matrix: Any, general_i: Any=general_i, value_i: Any=value_i, value_header: Any=value_header) -> Callable[[int], FactorValue]:
            def _arrow466(i: int, matrix: Any=matrix) -> FactorValue:
                return JsonTypes_composeFactorValue(cat, get_item_from_dict(matrix, (general_i, i)))

            return _arrow466

        return Value

    else: 
        return None



def ProcessParsing_tryCharacteristicGetter(general_i: int, value_i: int, value_header: CompositeHeader) -> Callable[[Any, int], MaterialAttributeValue] | None:
    if value_header.tag == 1:
        cat: CompositeHeader = CompositeHeader(1, ARCtrl_ISA_OntologyAnnotation__OntologyAnnotation_SetColumnIndex_Z524259A4(value_header.fields[0], value_i))
        def Value(matrix: Any, general_i: Any=general_i, value_i: Any=value_i, value_header: Any=value_header) -> Callable[[int], MaterialAttributeValue]:
            def _arrow467(i: int, matrix: Any=matrix) -> MaterialAttributeValue:
                return JsonTypes_composeCharacteristicValue(cat, get_item_from_dict(matrix, (general_i, i)))

            return _arrow467

        return Value

    else: 
        return None



def ProcessParsing_tryGetProtocolTypeGetter(general_i: int, header: CompositeHeader) -> Callable[[Any, int], OntologyAnnotation] | None:
    if header.tag == 4:
        def Value(matrix: Any, general_i: Any=general_i, header: Any=header) -> Callable[[int], OntologyAnnotation]:
            def _arrow468(i: int, matrix: Any=matrix) -> OntologyAnnotation:
                return get_item_from_dict(matrix, (general_i, i)).AsTerm

            return _arrow468

        return Value

    else: 
        return None



def ProcessParsing_tryGetProtocolREFGetter(general_i: int, header: CompositeHeader) -> Callable[[Any, int], str] | None:
    if header.tag == 8:
        def Value(matrix: Any, general_i: Any=general_i, header: Any=header) -> Callable[[int], str]:
            def _arrow469(i: int, matrix: Any=matrix) -> str:
                return get_item_from_dict(matrix, (general_i, i)).AsFreeText

            return _arrow469

        return Value

    else: 
        return None



def ProcessParsing_tryGetProtocolDescriptionGetter(general_i: int, header: CompositeHeader) -> Callable[[Any, int], str] | None:
    if header.tag == 5:
        def Value(matrix: Any, general_i: Any=general_i, header: Any=header) -> Callable[[int], str]:
            def _arrow470(i: int, matrix: Any=matrix) -> str:
                return get_item_from_dict(matrix, (general_i, i)).AsFreeText

            return _arrow470

        return Value

    else: 
        return None



def ProcessParsing_tryGetProtocolURIGetter(general_i: int, header: CompositeHeader) -> Callable[[Any, int], str] | None:
    if header.tag == 6:
        def Value(matrix: Any, general_i: Any=general_i, header: Any=header) -> Callable[[int], str]:
            def _arrow471(i: int, matrix: Any=matrix) -> str:
                return get_item_from_dict(matrix, (general_i, i)).AsFreeText

            return _arrow471

        return Value

    else: 
        return None



def ProcessParsing_tryGetProtocolVersionGetter(general_i: int, header: CompositeHeader) -> Callable[[Any, int], str] | None:
    if header.tag == 7:
        def Value(matrix: Any, general_i: Any=general_i, header: Any=header) -> Callable[[int], str]:
            def _arrow472(i: int, matrix: Any=matrix) -> str:
                return get_item_from_dict(matrix, (general_i, i)).AsFreeText

            return _arrow472

        return Value

    else: 
        return None



def ProcessParsing_tryGetInputGetter(general_i: int, header: CompositeHeader) -> Callable[[Any, int], ProcessInput] | None:
    if header.tag == 11:
        def Value(matrix: Any, general_i: Any=general_i, header: Any=header) -> Callable[[int], ProcessInput]:
            def _arrow473(i: int, matrix: Any=matrix) -> ProcessInput:
                return JsonTypes_composeProcessInput(header, get_item_from_dict(matrix, (general_i, i)))

            return _arrow473

        return Value

    else: 
        return None



def ProcessParsing_tryGetOutputGetter(general_i: int, header: CompositeHeader) -> Callable[[Any, int], ProcessOutput] | None:
    if header.tag == 12:
        def Value(matrix: Any, general_i: Any=general_i, header: Any=header) -> Callable[[int], ProcessOutput]:
            def _arrow474(i: int, matrix: Any=matrix) -> ProcessOutput:
                return JsonTypes_composeProcessOutput(header, get_item_from_dict(matrix, (general_i, i)))

            return _arrow474

        return Value

    else: 
        return None



def ProcessParsing_getProcessGetter(process_name_root: str, headers: IEnumerable_1[CompositeHeader]) -> Callable[[Any, int], Process]:
    headers_1: IEnumerable_1[tuple[int, CompositeHeader]] = indexed(headers)
    def predicate(arg: tuple[int, CompositeHeader], process_name_root: Any=process_name_root, headers: Any=headers) -> bool:
        return arg[1].IsCvParamColumn

    value_headers: FSharpList[tuple[int, tuple[int, CompositeHeader]]] = to_list(indexed(filter(predicate, headers_1)))
    def chooser(tupled_arg: tuple[int, tuple[int, CompositeHeader]], process_name_root: Any=process_name_root, headers: Any=headers) -> Callable[[Any, int], MaterialAttributeValue] | None:
        _arg: tuple[int, CompositeHeader] = tupled_arg[1]
        return ProcessParsing_tryCharacteristicGetter(_arg[0], tupled_arg[0], _arg[1])

    char_getters: FSharpList[Callable[[Any, int], MaterialAttributeValue]] = choose(chooser, value_headers)
    def chooser_1(tupled_arg_1: tuple[int, tuple[int, CompositeHeader]], process_name_root: Any=process_name_root, headers: Any=headers) -> Callable[[Any, int], FactorValue] | None:
        _arg_1: tuple[int, CompositeHeader] = tupled_arg_1[1]
        return ProcessParsing_tryFactorGetter(_arg_1[0], tupled_arg_1[0], _arg_1[1])

    factor_value_getters: FSharpList[Callable[[Any, int], FactorValue]] = choose(chooser_1, value_headers)
    def chooser_2(tupled_arg_2: tuple[int, tuple[int, CompositeHeader]], process_name_root: Any=process_name_root, headers: Any=headers) -> Callable[[Any, int], ProcessParameterValue] | None:
        _arg_2: tuple[int, CompositeHeader] = tupled_arg_2[1]
        return ProcessParsing_tryParameterGetter(_arg_2[0], tupled_arg_2[0], _arg_2[1])

    parameter_value_getters: FSharpList[Callable[[Any, int], ProcessParameterValue]] = choose(chooser_2, value_headers)
    def chooser_3(tupled_arg_3: tuple[int, tuple[int, CompositeHeader]], process_name_root: Any=process_name_root, headers: Any=headers) -> Callable[[Any, int], Component] | None:
        _arg_3: tuple[int, CompositeHeader] = tupled_arg_3[1]
        return ProcessParsing_tryComponentGetter(_arg_3[0], tupled_arg_3[0], _arg_3[1])

    component_getters: FSharpList[Callable[[Any, int], Component]] = choose(chooser_3, value_headers)
    def chooser_4(tupled_arg_4: tuple[int, CompositeHeader], process_name_root: Any=process_name_root, headers: Any=headers) -> Callable[[Any, int], OntologyAnnotation] | None:
        return ProcessParsing_tryGetProtocolTypeGetter(tupled_arg_4[0], tupled_arg_4[1])

    protocol_type_getter: Callable[[Any, int], OntologyAnnotation] | None = try_pick(chooser_4, headers_1)
    def chooser_5(tupled_arg_5: tuple[int, CompositeHeader], process_name_root: Any=process_name_root, headers: Any=headers) -> Callable[[Any, int], str] | None:
        return ProcessParsing_tryGetProtocolREFGetter(tupled_arg_5[0], tupled_arg_5[1])

    protocol_refgetter: Callable[[Any, int], str] | None = try_pick(chooser_5, headers_1)
    def chooser_6(tupled_arg_6: tuple[int, CompositeHeader], process_name_root: Any=process_name_root, headers: Any=headers) -> Callable[[Any, int], str] | None:
        return ProcessParsing_tryGetProtocolDescriptionGetter(tupled_arg_6[0], tupled_arg_6[1])

    protocol_description_getter: Callable[[Any, int], str] | None = try_pick(chooser_6, headers_1)
    def chooser_7(tupled_arg_7: tuple[int, CompositeHeader], process_name_root: Any=process_name_root, headers: Any=headers) -> Callable[[Any, int], str] | None:
        return ProcessParsing_tryGetProtocolURIGetter(tupled_arg_7[0], tupled_arg_7[1])

    protocol_urigetter: Callable[[Any, int], str] | None = try_pick(chooser_7, headers_1)
    def chooser_8(tupled_arg_8: tuple[int, CompositeHeader], process_name_root: Any=process_name_root, headers: Any=headers) -> Callable[[Any, int], str] | None:
        return ProcessParsing_tryGetProtocolVersionGetter(tupled_arg_8[0], tupled_arg_8[1])

    protocol_version_getter: Callable[[Any, int], str] | None = try_pick(chooser_8, headers_1)
    input_getter_1: Callable[[Any, int], FSharpList[ProcessInput]]
    def chooser_9(tupled_arg_9: tuple[int, CompositeHeader], process_name_root: Any=process_name_root, headers: Any=headers) -> Callable[[Any, int], ProcessInput] | None:
        return ProcessParsing_tryGetInputGetter(tupled_arg_9[0], tupled_arg_9[1])

    match_value: Callable[[Any, int], ProcessInput] | None = try_pick(chooser_9, headers_1)
    if match_value is None:
        def _arrow476(matrix_1: Any, process_name_root: Any=process_name_root, headers: Any=headers) -> Callable[[int], FSharpList[ProcessInput]]:
            def _arrow475(i_1: int) -> FSharpList[ProcessInput]:
                def mapping_1(f_1: Callable[[Any, int], MaterialAttributeValue]) -> MaterialAttributeValue:
                    return f_1(matrix_1)(i_1)

                return singleton(ProcessInput(0, Source_create_7A281ED9(None, ((("" + process_name_root) + "_Input_") + str(i_1)) + "", to_list(map_1(mapping_1, char_getters)))))

            return _arrow475

        input_getter_1 = _arrow476

    else: 
        input_getter: Callable[[Any, int], ProcessInput] = match_value
        def _arrow478(matrix: Any, process_name_root: Any=process_name_root, headers: Any=headers) -> Callable[[int], FSharpList[ProcessInput]]:
            def _arrow477(i: int) -> FSharpList[ProcessInput]:
                def mapping(f: Callable[[Any, int], MaterialAttributeValue]) -> MaterialAttributeValue:
                    return f(matrix)(i)

                chars: FSharpList[MaterialAttributeValue] = to_list(map_1(mapping, char_getters))
                input: ProcessInput = input_getter(matrix)(i)
                return of_array_2([input, ProcessInput_createSample_Z6DF16D07(ProcessInput__get_Name(input), chars)]) if ((not is_empty(chars)) if (not (True if ProcessInput__isSample(input) else ProcessInput__isSource(input))) else False) else singleton(ProcessInput_setCharacteristicValues(chars, input))

            return _arrow477

        input_getter_1 = _arrow478

    output_getter_1: Callable[[Any, int], FSharpList[ProcessOutput]]
    def chooser_10(tupled_arg_10: tuple[int, CompositeHeader], process_name_root: Any=process_name_root, headers: Any=headers) -> Callable[[Any, int], ProcessOutput] | None:
        return ProcessParsing_tryGetOutputGetter(tupled_arg_10[0], tupled_arg_10[1])

    match_value_1: Callable[[Any, int], ProcessOutput] | None = try_pick(chooser_10, headers_1)
    if match_value_1 is None:
        def _arrow480(matrix_3: Any, process_name_root: Any=process_name_root, headers: Any=headers) -> Callable[[int], FSharpList[ProcessOutput]]:
            def _arrow479(i_3: int) -> FSharpList[ProcessOutput]:
                def mapping_3(f_3: Callable[[Any, int], FactorValue]) -> FactorValue:
                    return f_3(matrix_3)(i_3)

                return singleton(ProcessOutput(0, Sample_create_E50ED22(None, ((("" + process_name_root) + "_Output_") + str(i_3)) + "", None, to_list(map_1(mapping_3, factor_value_getters)))))

            return _arrow479

        output_getter_1 = _arrow480

    else: 
        output_getter: Callable[[Any, int], ProcessOutput] = match_value_1
        def _arrow482(matrix_2: Any, process_name_root: Any=process_name_root, headers: Any=headers) -> Callable[[int], FSharpList[ProcessOutput]]:
            def _arrow481(i_2: int) -> FSharpList[ProcessOutput]:
                def mapping_2(f_2: Callable[[Any, int], FactorValue]) -> FactorValue:
                    return f_2(matrix_2)(i_2)

                factors: FSharpList[FactorValue] = to_list(map_1(mapping_2, factor_value_getters))
                output: ProcessOutput = output_getter(matrix_2)(i_2)
                return of_array_2([output, ProcessOutput_createSample_Z6DF16D07(ProcessOutput__get_Name(output), None, factors)]) if ((not is_empty(factors)) if (not ProcessOutput__isSample(output)) else False) else singleton(ProcessOutput_setFactorValues(factors, output))

            return _arrow481

        output_getter_1 = _arrow482

    def _arrow484(matrix_4: Any, process_name_root: Any=process_name_root, headers: Any=headers) -> Callable[[int], Process]:
        def _arrow483(i_4: int) -> Process:
            def mapping_4(p: str) -> str:
                return Process_composeName(p, i_4)

            pn: str | None = map_2(mapping_4, Option_fromValueWithDefault("", process_name_root))
            def mapping_5(f_4: Callable[[Any, int], ProcessParameterValue]) -> ProcessParameterValue:
                return f_4(matrix_4)(i_4)

            paramvalues: FSharpList[ProcessParameterValue] | None = Option_fromValueWithDefault(empty(), map_3(mapping_5, parameter_value_getters))
            def mapping_7(list_6: FSharpList[ProcessParameterValue]) -> FSharpList[ProtocolParameter]:
                def mapping_6(pv: ProcessParameterValue, list_6: Any=list_6) -> ProtocolParameter:
                    return value_9(pv.Category)

                return map_3(mapping_6, list_6)

            parameters: FSharpList[ProtocolParameter] | None = map_2(mapping_7, paramvalues)
            protocol: Protocol | None
            def mapping_8(f_5: Callable[[Any, int], str]) -> str:
                return f_5(matrix_4)(i_4)

            def mapping_9(f_6: Callable[[Any, int], OntologyAnnotation]) -> OntologyAnnotation:
                return f_6(matrix_4)(i_4)

            def mapping_10(f_7: Callable[[Any, int], str]) -> str:
                return f_7(matrix_4)(i_4)

            def mapping_11(f_8: Callable[[Any, int], str]) -> str:
                return f_8(matrix_4)(i_4)

            def mapping_12(f_9: Callable[[Any, int], str]) -> str:
                return f_9(matrix_4)(i_4)

            def mapping_13(f_10: Callable[[Any, int], Component]) -> Component:
                return f_10(matrix_4)(i_4)

            p_1: Protocol = Protocol_make(None, map_2(mapping_8, protocol_refgetter), map_2(mapping_9, protocol_type_getter), map_2(mapping_10, protocol_description_getter), map_2(mapping_11, protocol_urigetter), map_2(mapping_12, protocol_version_getter), parameters, Option_fromValueWithDefault(empty(), map_3(mapping_13, component_getters)), None)
            (pattern_matching_result,) = (None,)
            if p_1.Name is None:
                if p_1.ProtocolType is None:
                    if p_1.Description is None:
                        if p_1.Uri is None:
                            if p_1.Version is None:
                                if p_1.Components is None:
                                    pattern_matching_result = 0

                                else: 
                                    pattern_matching_result = 1


                            else: 
                                pattern_matching_result = 1


                        else: 
                            pattern_matching_result = 1


                    else: 
                        pattern_matching_result = 1


                else: 
                    pattern_matching_result = 1


            else: 
                pattern_matching_result = 1

            if pattern_matching_result == 0:
                protocol = None

            elif pattern_matching_result == 1:
                protocol = p_1

            pattern_input: tuple[FSharpList[ProcessInput], FSharpList[ProcessOutput]]
            inputs: FSharpList[ProcessInput] = input_getter_1(matrix_4)(i_4)
            outputs: FSharpList[ProcessOutput] = output_getter_1(matrix_4)(i_4)
            pattern_input = ((of_array_2([item(0, inputs), item(0, inputs)]), outputs)) if ((length(outputs) == 2) if (length(inputs) == 1) else False) else (((inputs, of_array_2([item(0, outputs), item(0, outputs)]))) if ((length(outputs) == 1) if (length(inputs) == 2) else False) else ((inputs, outputs)))
            return Process_make(None, pn, protocol, paramvalues, None, None, None, None, pattern_input[0], pattern_input[1], None)

        return _arrow483

    return _arrow484


def ProcessParsing_groupProcesses(ps: FSharpList[Process]) -> FSharpList[tuple[str, FSharpList[Process]]]:
    def projection(x: Process, ps: Any=ps) -> str:
        if (Process_decomposeName_Z721C83C5(value_9(x.Name))[1] is not None) if (x.Name is not None) else False:
            return Process_decomposeName_Z721C83C5(value_9(x.Name))[0]

        elif (value_9(x.ExecutesProtocol).Name is not None) if (x.ExecutesProtocol is not None) else False:
            return value_9(value_9(x.ExecutesProtocol).Name)

        elif (value_9(x.Name).find("_") >= 0) if (x.Name is not None) else False:
            last_under_score_index: int = value_9(x.Name).rfind("_") or 0
            return remove(value_9(x.Name), last_under_score_index)

        elif x.Name is not None:
            return value_9(x.Name)

        elif (value_9(x.ExecutesProtocol).ID is not None) if (x.ExecutesProtocol is not None) else False:
            return value_9(value_9(x.ExecutesProtocol).ID)

        else: 
            return create_missing_identifier()


    class ObjectExpr486:
        @property
        def Equals(self) -> Callable[[str, str], bool]:
            def _arrow485(x_1: str, y: str) -> bool:
                return x_1 == y

            return _arrow485

        @property
        def GetHashCode(self) -> Callable[[str], int]:
            return string_hash

    return List_groupBy(projection, ps, ObjectExpr486())


def ProcessParsing_mergeIdenticalProcesses(processes: FSharpList[Process]) -> FSharpList[Process]:
    def projection(x: Process, processes: Any=processes) -> tuple[str, Protocol | None, Any | None]:
        if (Process_decomposeName_Z721C83C5(value_9(x.Name))[1] is not None) if (x.Name is not None) else False:
            def mapping(a: FSharpList[ProcessParameterValue], x: Any=x) -> Any:
                return HashCodes_boxHashSeq(a)

            return (Process_decomposeName_Z721C83C5(value_9(x.Name))[0], x.ExecutesProtocol, map_2(mapping, x.ParameterValues))

        elif (value_9(x.ExecutesProtocol).Name is not None) if (x.ExecutesProtocol is not None) else False:
            def mapping_1(a_1: FSharpList[ProcessParameterValue], x: Any=x) -> Any:
                return HashCodes_boxHashSeq(a_1)

            return (value_9(value_9(x.ExecutesProtocol).Name), x.ExecutesProtocol, map_2(mapping_1, x.ParameterValues))

        else: 
            def mapping_2(a_2: FSharpList[ProcessParameterValue], x: Any=x) -> Any:
                return HashCodes_boxHashSeq(a_2)

            return (create_missing_identifier(), x.ExecutesProtocol, map_2(mapping_2, x.ParameterValues))


    class ObjectExpr487:
        @property
        def Equals(self) -> Callable[[tuple[str, Protocol | None, Any | None], tuple[str, Protocol | None, Any | None]], bool]:
            return equal_arrays

        @property
        def GetHashCode(self) -> Callable[[tuple[str, Protocol | None, Any | None]], int]:
            return array_hash

    l: FSharpList[tuple[tuple[str, Protocol | None, Any | None], FSharpList[Process]]] = List_groupBy(projection, processes, ObjectExpr487())
    def mapping_5(i: int, tupled_arg: tuple[tuple[str, Protocol | None, Any | None], FSharpList[Process]], processes: Any=processes) -> Process:
        _arg: tuple[str, Protocol | None, Any | None] = tupled_arg[0]
        processes_1: FSharpList[Process] = tupled_arg[1]
        n: str = _arg[0]
        p_vs: FSharpList[ProcessParameterValue] | None = item(0, processes_1).ParameterValues
        def mapping_3(p: Process, i: Any=i, tupled_arg: Any=tupled_arg) -> FSharpList[ProcessInput]:
            return default_arg(p.Inputs, empty())

        inputs: FSharpList[ProcessInput] | None = Option_fromValueWithDefault(empty(), collect(mapping_3, processes_1))
        def mapping_4(p_1: Process, i: Any=i, tupled_arg: Any=tupled_arg) -> FSharpList[ProcessOutput]:
            return default_arg(p_1.Outputs, empty())

        outputs: FSharpList[ProcessOutput] | None = Option_fromValueWithDefault(empty(), collect(mapping_4, processes_1))
        return Process_create_Z42860F3E(None, Process_composeName(n, i) if (length(l) > 1) else n, _arg[1], p_vs, None, None, None, None, inputs, outputs)

    return map_indexed(mapping_5, l)


def ProcessParsing_processToRows(p: Process) -> FSharpList[FSharpList[tuple[CompositeHeader, CompositeCell]]]:
    def mapping(ppv: ProcessParameterValue, p: Any=p) -> tuple[tuple[CompositeHeader, CompositeCell], int | None]:
        return (JsonTypes_decomposeParameterValue(ppv), try_get_parameter_column_index(ppv))

    pvs: FSharpList[tuple[tuple[CompositeHeader, CompositeCell], int | None]] = map_3(mapping, default_arg(p.ParameterValues, empty()))
    components: FSharpList[tuple[tuple[CompositeHeader, CompositeCell], int | None]]
    match_value: Protocol | None = p.ExecutesProtocol
    def mapping_1(ppv_1: Component, p: Any=p) -> tuple[tuple[CompositeHeader, CompositeCell], int | None]:
        return (JsonTypes_decomposeComponent(ppv_1), try_get_component_index(ppv_1))

    components = empty() if (match_value is None) else map_3(mapping_1, default_arg(match_value.Components, empty()))
    prot_vals: FSharpList[tuple[CompositeHeader, CompositeCell]]
    match_value_1: Protocol | None = p.ExecutesProtocol
    if match_value_1 is None:
        prot_vals = empty()

    else: 
        prot_1: Protocol = match_value_1
        def _arrow492(__unit: None=None, p: Any=p) -> IEnumerable_1[tuple[CompositeHeader, CompositeCell]]:
            def _arrow491(__unit: None=None) -> IEnumerable_1[tuple[CompositeHeader, CompositeCell]]:
                def _arrow490(__unit: None=None) -> IEnumerable_1[tuple[CompositeHeader, CompositeCell]]:
                    def _arrow489(__unit: None=None) -> IEnumerable_1[tuple[CompositeHeader, CompositeCell]]:
                        def _arrow488(__unit: None=None) -> IEnumerable_1[tuple[CompositeHeader, CompositeCell]]:
                            return singleton_1((CompositeHeader(7), CompositeCell(1, value_9(prot_1.Version)))) if (prot_1.Version is not None) else empty_1()

                        return append(singleton_1((CompositeHeader(6), CompositeCell(1, value_9(prot_1.Uri)))) if (prot_1.Uri is not None) else empty_1(), delay(_arrow488))

                    return append(singleton_1((CompositeHeader(5), CompositeCell(1, value_9(prot_1.Description)))) if (prot_1.Description is not None) else empty_1(), delay(_arrow489))

                return append(singleton_1((CompositeHeader(4), CompositeCell(0, value_9(prot_1.ProtocolType)))) if (prot_1.ProtocolType is not None) else empty_1(), delay(_arrow490))

            return append(singleton_1((CompositeHeader(8), CompositeCell(1, value_9(prot_1.Name)))) if (prot_1.Name is not None) else empty_1(), delay(_arrow491))

        prot_vals = to_list(delay(_arrow492))

    def mapping_5(tupled_arg_1: tuple[tuple[str, str], FSharpList[tuple[ProcessInput, ProcessOutput]]], p: Any=p) -> FSharpList[tuple[CompositeHeader, CompositeCell]]:
        ios: FSharpList[tuple[ProcessInput, ProcessOutput]] = tupled_arg_1[1]
        def chooser(tupled_arg_2: tuple[ProcessInput, ProcessOutput], tupled_arg_1: Any=tupled_arg_1) -> ProcessInput | None:
            i_2: ProcessInput = tupled_arg_2[0]
            if True if ProcessInput__isSource(i_2) else ProcessInput__isSample(i_2):
                return i_2

            else: 
                return None


        input_for_charas: ProcessInput = default_arg(try_pick_1(chooser, ios), head(ios)[0])
        def chooser_1(tupled_arg_3: tuple[ProcessInput, ProcessOutput], tupled_arg_1: Any=tupled_arg_1) -> ProcessInput | None:
            i_3: ProcessInput = tupled_arg_3[0]
            if True if ProcessInput__isData(i_3) else ProcessInput__isMaterial(i_3):
                return i_3

            else: 
                return None


        input_for_type: ProcessInput = default_arg(try_pick_1(chooser_1, ios), head(ios)[0])
        def mapping_2(cv: MaterialAttributeValue, tupled_arg_1: Any=tupled_arg_1) -> tuple[tuple[CompositeHeader, CompositeCell], int | None]:
            return (JsonTypes_decomposeCharacteristicValue(cv), try_get_characteristic_column_index(cv))

        chars: FSharpList[tuple[tuple[CompositeHeader, CompositeCell], int | None]] = map_3(mapping_2, ProcessInput_getCharacteristicValues_102B6859(input_for_charas))
        def chooser_2(tupled_arg_4: tuple[ProcessInput, ProcessOutput], tupled_arg_1: Any=tupled_arg_1) -> ProcessOutput | None:
            o_4: ProcessOutput = tupled_arg_4[1]
            if ProcessOutput__isSample(o_4):
                return o_4

            else: 
                return None


        output_for_factors: ProcessOutput = default_arg(try_pick_1(chooser_2, ios), head(ios)[1])
        def chooser_3(tupled_arg_5: tuple[ProcessInput, ProcessOutput], tupled_arg_1: Any=tupled_arg_1) -> ProcessOutput | None:
            o_5: ProcessOutput = tupled_arg_5[1]
            if True if ProcessOutput__isData(o_5) else ProcessOutput__isMaterial(o_5):
                return o_5

            else: 
                return None


        output_for_type: ProcessOutput = default_arg(try_pick_1(chooser_3, ios), head(ios)[1])
        def mapping_4(tuple_5: tuple[tuple[CompositeHeader, CompositeCell], int | None], tupled_arg_1: Any=tupled_arg_1) -> tuple[CompositeHeader, CompositeCell]:
            return tuple_5[0]

        def projection_1(arg: tuple[tuple[CompositeHeader, CompositeCell], int | None], tupled_arg_1: Any=tupled_arg_1) -> int:
            return default_arg(arg[1], 10000)

        def mapping_3(fv: FactorValue, tupled_arg_1: Any=tupled_arg_1) -> tuple[tuple[CompositeHeader, CompositeCell], int | None]:
            return (JsonTypes_decomposeFactorValue(fv), try_get_factor_column_index(fv))

        class ObjectExpr493:
            @property
            def Compare(self) -> Callable[[int, int], int]:
                return compare_primitives

        vals: FSharpList[tuple[CompositeHeader, CompositeCell]] = map_3(mapping_4, sort_by(projection_1, append_1(chars, append_1(components, append_1(pvs, map_3(mapping_3, ProcessOutput_getFactorValues_11830B70(output_for_factors))))), ObjectExpr493()))
        def _arrow497(__unit: None=None, tupled_arg_1: Any=tupled_arg_1) -> IEnumerable_1[tuple[CompositeHeader, CompositeCell]]:
            def _arrow496(__unit: None=None) -> IEnumerable_1[tuple[CompositeHeader, CompositeCell]]:
                def _arrow495(__unit: None=None) -> IEnumerable_1[tuple[CompositeHeader, CompositeCell]]:
                    def _arrow494(__unit: None=None) -> IEnumerable_1[tuple[CompositeHeader, CompositeCell]]:
                        return singleton_1(JsonTypes_decomposeProcessOutput(output_for_type))

                    return append(vals, delay(_arrow494))

                return append(prot_vals, delay(_arrow495))

            return append(singleton_1(JsonTypes_decomposeProcessInput(input_for_type)), delay(_arrow496))

        return to_list(delay(_arrow497))

    def projection(tupled_arg: tuple[ProcessInput, ProcessOutput], p: Any=p) -> tuple[str, str]:
        return (ProcessInput__get_Name(tupled_arg[0]), ProcessOutput__get_Name(tupled_arg[1]))

    def _arrow498(__unit: None=None, p: Any=p) -> FSharpList[tuple[ProcessInput, ProcessOutput]]:
        list_4: FSharpList[ProcessOutput] = default_arg(p.Outputs, empty())
        return zip(default_arg(p.Inputs, empty()), list_4)

    class ObjectExpr499:
        @property
        def Equals(self) -> Callable[[tuple[str, str], tuple[str, str]], bool]:
            return equal_arrays

        @property
        def GetHashCode(self) -> Callable[[tuple[str, str]], int]:
            return array_hash

    return map_3(mapping_5, List_groupBy(projection, _arrow498(), ObjectExpr499()))


def ProcessParsing_compositeHeaderEqual(ch1: CompositeHeader, ch2: CompositeHeader) -> bool:
    return to_string(ch1) == to_string(ch2)


def ProcessParsing_alignByHeaders(keep_order: bool, rows: FSharpList[FSharpList[tuple[CompositeHeader, CompositeCell]]]) -> tuple[Array[CompositeHeader], Any]:
    headers: Array[CompositeHeader] = []
    class ObjectExpr500:
        @property
        def Equals(self) -> Callable[[tuple[int, int], tuple[int, int]], bool]:
            return equal_arrays

        @property
        def GetHashCode(self) -> Callable[[tuple[int, int]], int]:
            return array_hash

    values: Any = Dictionary([], ObjectExpr500())
    def loop(col_i_mut: int, rows_2_mut: FSharpList[FSharpList[tuple[CompositeHeader, CompositeCell]]], keep_order: Any=keep_order, rows: Any=rows) -> tuple[Array[CompositeHeader], Any]:
        while True:
            (col_i, rows_2) = (col_i_mut, rows_2_mut)
            def _arrow501(arg: FSharpList[tuple[CompositeHeader, CompositeCell]], col_i: Any=col_i, rows_2: Any=rows_2) -> bool:
                return not is_empty(arg)

            if not exists(_arrow501, rows_2):
                return (headers, values)

            else: 
                def _arrow502(l: FSharpList[tuple[CompositeHeader, CompositeCell]], col_i: Any=col_i, rows_2: Any=rows_2) -> tuple[CompositeHeader, CompositeCell] | None:
                    return None if is_empty(l) else head(l)

                first_elem: CompositeHeader = pick(_arrow502, rows_2)[0]
                (headers.append(first_elem))
                col_i_mut = col_i + 1
                def mapping(row_i: int, l_1: FSharpList[tuple[CompositeHeader, CompositeCell]], col_i: Any=col_i, rows_2: Any=rows_2) -> FSharpList[tuple[CompositeHeader, CompositeCell]]:
                    if keep_order:
                        if not is_empty(l_1):
                            if ProcessParsing_compositeHeaderEqual(head(l_1)[0], first_elem):
                                add_to_dict(values, (col_i, row_i), head(l_1)[1])
                                return tail_1(l_1)

                            else: 
                                return l_1


                        else: 
                            return empty()


                    else: 
                        def f(tupled_arg: tuple[CompositeHeader, CompositeCell], row_i: Any=row_i, l_1: Any=l_1) -> CompositeCell | None:
                            if ProcessParsing_compositeHeaderEqual(tupled_arg[0], first_elem):
                                return tupled_arg[1]

                            else: 
                                return None


                        pattern_input: tuple[CompositeCell | None, FSharpList[tuple[CompositeHeader, CompositeCell]]] = List_tryPickAndRemove(f, l_1)
                        new_l: FSharpList[tuple[CompositeHeader, CompositeCell]] = pattern_input[1]
                        first_match: CompositeCell | None = pattern_input[0]
                        if first_match is None:
                            return new_l

                        else: 
                            add_to_dict(values, (col_i, row_i), first_match)
                            return new_l



                rows_2_mut = map_indexed(mapping, rows_2)
                continue

            break

    return loop(0, rows)


__all__ = ["Dictionary_tryFind", "get_column_count", "get_row_count", "box_hash_values", "_007CIsUniqueExistingHeader_007C__007C", "try_find_duplicate_unique", "try_find_duplicate_unique_in_array", "SanityChecks_validateColumnIndex", "SanityChecks_validateRowIndex", "SanityChecks_validateColumn", "Unchecked_tryGetCellAt", "Unchecked_setCellAt", "Unchecked_addCellAt", "Unchecked_moveCellTo", "Unchecked_removeHeader", "Unchecked_removeColumnCells", "Unchecked_removeColumnCells_withIndexChange", "Unchecked_removeRowCells", "Unchecked_removeRowCells_withIndexChange", "Unchecked_getEmptyCellForHeader", "Unchecked_addColumn", "Unchecked_fillMissingCells", "Unchecked_extendToRowCount", "Unchecked_addRow", "Unchecked_addRows", "JsonTypes_valueOfCell", "JsonTypes_composeComponent", "JsonTypes_composeParameterValue", "JsonTypes_composeFactorValue", "JsonTypes_composeCharacteristicValue", "JsonTypes_composeProcessInput", "JsonTypes_composeProcessOutput", "JsonTypes_cellOfValue", "JsonTypes_decomposeComponent", "JsonTypes_decomposeParameterValue", "JsonTypes_decomposeFactorValue", "JsonTypes_decomposeCharacteristicValue", "JsonTypes_decomposeProcessInput", "JsonTypes_decomposeProcessOutput", "ProcessParsing_tryComponentGetter", "ProcessParsing_tryParameterGetter", "ProcessParsing_tryFactorGetter", "ProcessParsing_tryCharacteristicGetter", "ProcessParsing_tryGetProtocolTypeGetter", "ProcessParsing_tryGetProtocolREFGetter", "ProcessParsing_tryGetProtocolDescriptionGetter", "ProcessParsing_tryGetProtocolURIGetter", "ProcessParsing_tryGetProtocolVersionGetter", "ProcessParsing_tryGetInputGetter", "ProcessParsing_tryGetOutputGetter", "ProcessParsing_getProcessGetter", "ProcessParsing_groupProcesses", "ProcessParsing_mergeIdenticalProcesses", "ProcessParsing_processToRows", "ProcessParsing_compositeHeaderEqual", "ProcessParsing_alignByHeaders"]

