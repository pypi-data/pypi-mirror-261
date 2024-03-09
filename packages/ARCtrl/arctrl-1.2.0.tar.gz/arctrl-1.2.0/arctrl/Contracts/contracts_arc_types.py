from __future__ import annotations
from collections.abc import Callable
from typing import Any
from ..fable_modules.fable_library.array_ import equals_with
from ..fable_modules.fable_library.list import FSharpList
from ..fable_modules.fable_library.option import default_arg
from ..fable_modules.fable_library.seq import (to_array, delay, append, collect, singleton, empty)
from ..fable_modules.fable_library.types import Array
from ..fable_modules.fable_library.util import IEnumerable_1
from ..fable_modules.fs_spreadsheet.fs_workbook import FsWorkbook
from ..Contract.contract import (Contract, DTOType, DTO)
from ..FileSystem.file_system_tree import FileSystemTree
from ..FileSystem.path import combine_many
from ..ISA.ISA_Spreadsheet.arc_assay import (to_fs_workbook as to_fs_workbook_1, from_fs_workbook as from_fs_workbook_1)
from ..ISA.ISA_Spreadsheet.arc_investigation import (to_light_fs_workbook, to_fs_workbook, from_fs_workbook)
from ..ISA.ISA_Spreadsheet.arc_study import (ARCtrl_ISA_ArcStudy__ArcStudy_toFsWorkbook_Static_Z2A9662E9, ARCtrl_ISA_ArcStudy__ArcStudy_fromFsWorkbook_Static_32154C9D)
from ..ISA.ISA.ArcTypes.arc_types import (ArcInvestigation, ArcStudy, ArcAssay)
from ..ISA.ISA.identifier import (Study_fileNameFromIdentifier, Assay_fileNameFromIdentifier)
from ..file_system_tree import (create_studies_folder, create_study_folder, create_assay_folder)
from ..path import (get_study_folder_path, get_assay_folder_path)

def _007CStudyPath_007C__007C(input: Array[str]) -> str | None:
    (pattern_matching_result,) = (None,)
    def _arrow1700(x: str, y: str, input: Any=input) -> bool:
        return x == y

    if (len(input) == 3) if (not equals_with(_arrow1700, input, None)) else False:
        if input[0] == "studies":
            if input[2] == "isa.study.xlsx":
                pattern_matching_result = 0

            else: 
                pattern_matching_result = 1


        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        any_study_name: str = input[1]
        return combine_many(input)

    elif pattern_matching_result == 1:
        return None



def _007CAssayPath_007C__007C(input: Array[str]) -> str | None:
    (pattern_matching_result,) = (None,)
    def _arrow1701(x: str, y: str, input: Any=input) -> bool:
        return x == y

    if (len(input) == 3) if (not equals_with(_arrow1701, input, None)) else False:
        if input[0] == "assays":
            if input[2] == "isa.assay.xlsx":
                pattern_matching_result = 0

            else: 
                pattern_matching_result = 1


        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        any_assay_name: str = input[1]
        return combine_many(input)

    elif pattern_matching_result == 1:
        return None



def _007CInvestigationPath_007C__007C(input: Array[str]) -> str | None:
    (pattern_matching_result,) = (None,)
    def _arrow1702(x: str, y: str, input: Any=input) -> bool:
        return x == y

    if (len(input) == 1) if (not equals_with(_arrow1702, input, None)) else False:
        if input[0] == "isa.investigation.xlsx":
            pattern_matching_result = 0

        else: 
            pattern_matching_result = 1


    else: 
        pattern_matching_result = 1

    if pattern_matching_result == 0:
        return combine_many(input)

    elif pattern_matching_result == 1:
        return None



def ARCtrl_ISA_ArcInvestigation__ArcInvestigation_ToCreateContract_6FCE9E49(this: ArcInvestigation, is_light: bool | None=None) -> Contract:
    def _arrow1703(investigation: ArcInvestigation, this: Any=this, is_light: Any=is_light) -> FsWorkbook:
        return to_light_fs_workbook(investigation)

    def _arrow1704(investigation_1: ArcInvestigation, this: Any=this, is_light: Any=is_light) -> FsWorkbook:
        return to_fs_workbook(investigation_1)

    converter: Callable[[ArcInvestigation], FsWorkbook] = _arrow1703 if default_arg(is_light, True) else _arrow1704
    return Contract.create_create("isa.investigation.xlsx", DTOType(2), DTO(0, converter(this)))


def ARCtrl_ISA_ArcInvestigation__ArcInvestigation_ToUpdateContract_6FCE9E49(this: ArcInvestigation, is_light: bool | None=None) -> Contract:
    def _arrow1705(investigation: ArcInvestigation, this: Any=this, is_light: Any=is_light) -> FsWorkbook:
        return to_light_fs_workbook(investigation)

    def _arrow1706(investigation_1: ArcInvestigation, this: Any=this, is_light: Any=is_light) -> FsWorkbook:
        return to_fs_workbook(investigation_1)

    converter: Callable[[ArcInvestigation], FsWorkbook] = _arrow1705 if default_arg(is_light, True) else _arrow1706
    return Contract.create_update("isa.investigation.xlsx", DTOType(2), DTO(0, converter(this)))


def ARCtrl_ISA_ArcInvestigation__ArcInvestigation_toCreateContract_Static_6EB1BBBD(inv: ArcInvestigation, is_light: bool | None=None) -> Contract:
    return ARCtrl_ISA_ArcInvestigation__ArcInvestigation_ToCreateContract_6FCE9E49(inv, is_light)


def ARCtrl_ISA_ArcInvestigation__ArcInvestigation_toUpdateContract_Static_6EB1BBBD(inv: ArcInvestigation, is_light: bool | None=None) -> Contract:
    return ARCtrl_ISA_ArcInvestigation__ArcInvestigation_ToUpdateContract_6FCE9E49(inv, is_light)


def ARCtrl_ISA_ArcInvestigation__ArcInvestigation_tryFromReadContract_Static_7570923F(c: Contract) -> ArcInvestigation | None:
    (pattern_matching_result, fsworkbook) = (None, None)
    if c.Operation == "READ":
        if c.DTOType is not None:
            if c.DTOType.tag == 2:
                if c.DTO is not None:
                    if c.DTO.tag == 0:
                        pattern_matching_result = 0
                        fsworkbook = c.DTO.fields[0]

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
        return from_fs_workbook(fsworkbook)

    elif pattern_matching_result == 1:
        return None



def ARCtrl_ISA_ArcStudy__ArcStudy_ToCreateContract_6FCE9E49(this: ArcStudy, WithFolder: bool | None=None) -> Array[Contract]:
    with_folder: bool = default_arg(WithFolder, False)
    path: str = Study_fileNameFromIdentifier(this.Identifier)
    c: Contract = Contract.create_create(path, DTOType(1), DTO(0, ARCtrl_ISA_ArcStudy__ArcStudy_toFsWorkbook_Static_Z2A9662E9(this)))
    def _arrow1710(__unit: None=None, this: Any=this, WithFolder: Any=WithFolder) -> IEnumerable_1[Contract]:
        def _arrow1708(__unit: None=None) -> IEnumerable_1[Contract]:
            folder_fs: FileSystemTree = create_studies_folder([create_study_folder(this.Identifier)])
            def _arrow1707(p: str) -> IEnumerable_1[Contract]:
                return singleton(Contract.create_create(p, DTOType(6))) if (p != path) else empty()

            return collect(_arrow1707, folder_fs.ToFilePaths(False))

        def _arrow1709(__unit: None=None) -> IEnumerable_1[Contract]:
            return singleton(c)

        return append(_arrow1708() if with_folder else empty(), delay(_arrow1709))

    return to_array(delay(_arrow1710))


def ARCtrl_ISA_ArcStudy__ArcStudy_ToUpdateContract(this: ArcStudy) -> Contract:
    path: str = Study_fileNameFromIdentifier(this.Identifier)
    return Contract.create_update(path, DTOType(1), DTO(0, ARCtrl_ISA_ArcStudy__ArcStudy_toFsWorkbook_Static_Z2A9662E9(this)))


def ARCtrl_ISA_ArcStudy__ArcStudy_ToDeleteContract(this: ArcStudy) -> Contract:
    path: str = get_study_folder_path(this.Identifier)
    return Contract.create_delete(path)


def ARCtrl_ISA_ArcStudy__ArcStudy_toDeleteContract_Static_1B3D5E9B(study: ArcStudy) -> Contract:
    return ARCtrl_ISA_ArcStudy__ArcStudy_ToDeleteContract(study)


def ARCtrl_ISA_ArcStudy__ArcStudy_toCreateContract_Static_Z12D8504E(study: ArcStudy, WithFolder: bool | None=None) -> Array[Contract]:
    return ARCtrl_ISA_ArcStudy__ArcStudy_ToCreateContract_6FCE9E49(study, WithFolder)


def ARCtrl_ISA_ArcStudy__ArcStudy_toUpdateContract_Static_1B3D5E9B(study: ArcStudy) -> Contract:
    return ARCtrl_ISA_ArcStudy__ArcStudy_ToUpdateContract(study)


def ARCtrl_ISA_ArcStudy__ArcStudy_tryFromReadContract_Static_7570923F(c: Contract) -> tuple[ArcStudy, FSharpList[ArcAssay]] | None:
    (pattern_matching_result, fsworkbook) = (None, None)
    if c.Operation == "READ":
        if c.DTOType is not None:
            if c.DTOType.tag == 1:
                if c.DTO is not None:
                    if c.DTO.tag == 0:
                        pattern_matching_result = 0
                        fsworkbook = c.DTO.fields[0]

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
        return ARCtrl_ISA_ArcStudy__ArcStudy_fromFsWorkbook_Static_32154C9D(fsworkbook)

    elif pattern_matching_result == 1:
        return None



def ARCtrl_ISA_ArcAssay__ArcAssay_ToCreateContract_6FCE9E49(this: ArcAssay, WithFolder: bool | None=None) -> Array[Contract]:
    with_folder: bool = default_arg(WithFolder, False)
    path: str = Assay_fileNameFromIdentifier(this.Identifier)
    c: Contract = Contract.create_create(path, DTOType(0), DTO(0, to_fs_workbook_1(this)))
    def _arrow1714(__unit: None=None, this: Any=this, WithFolder: Any=WithFolder) -> IEnumerable_1[Contract]:
        def _arrow1712(__unit: None=None) -> IEnumerable_1[Contract]:
            folder_fs: FileSystemTree = create_assay_folder(this.Identifier)
            def _arrow1711(p: str) -> IEnumerable_1[Contract]:
                return singleton(Contract.create_create(p, DTOType(6))) if (p != path) else empty()

            return collect(_arrow1711, folder_fs.ToFilePaths(False))

        def _arrow1713(__unit: None=None) -> IEnumerable_1[Contract]:
            return singleton(c)

        return append(_arrow1712() if with_folder else empty(), delay(_arrow1713))

    return to_array(delay(_arrow1714))


def ARCtrl_ISA_ArcAssay__ArcAssay_ToUpdateContract(this: ArcAssay) -> Contract:
    path: str = Assay_fileNameFromIdentifier(this.Identifier)
    return Contract.create_update(path, DTOType(0), DTO(0, to_fs_workbook_1(this)))


def ARCtrl_ISA_ArcAssay__ArcAssay_ToDeleteContract(this: ArcAssay) -> Contract:
    path: str = get_assay_folder_path(this.Identifier)
    return Contract.create_delete(path)


def ARCtrl_ISA_ArcAssay__ArcAssay_toDeleteContract_Static_1C75D08D(assay: ArcAssay) -> Contract:
    return ARCtrl_ISA_ArcAssay__ArcAssay_ToDeleteContract(assay)


def ARCtrl_ISA_ArcAssay__ArcAssay_toCreateContract_Static_Z3B1E839C(assay: ArcAssay, WithFolder: bool | None=None) -> Array[Contract]:
    return ARCtrl_ISA_ArcAssay__ArcAssay_ToCreateContract_6FCE9E49(assay, WithFolder)


def ARCtrl_ISA_ArcAssay__ArcAssay_toUpdateContract_Static_1C75D08D(assay: ArcAssay) -> Contract:
    return ARCtrl_ISA_ArcAssay__ArcAssay_ToUpdateContract(assay)


def ARCtrl_ISA_ArcAssay__ArcAssay_tryFromReadContract_Static_7570923F(c: Contract) -> ArcAssay | None:
    (pattern_matching_result, fsworkbook) = (None, None)
    if c.Operation == "READ":
        if c.DTOType is not None:
            if c.DTOType.tag == 0:
                if c.DTO is not None:
                    if c.DTO.tag == 0:
                        pattern_matching_result = 0
                        fsworkbook = c.DTO.fields[0]

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
        return from_fs_workbook_1(fsworkbook)

    elif pattern_matching_result == 1:
        return None



__all__ = ["_007CStudyPath_007C__007C", "_007CAssayPath_007C__007C", "_007CInvestigationPath_007C__007C", "ARCtrl_ISA_ArcInvestigation__ArcInvestigation_ToCreateContract_6FCE9E49", "ARCtrl_ISA_ArcInvestigation__ArcInvestigation_ToUpdateContract_6FCE9E49", "ARCtrl_ISA_ArcInvestigation__ArcInvestigation_toCreateContract_Static_6EB1BBBD", "ARCtrl_ISA_ArcInvestigation__ArcInvestigation_toUpdateContract_Static_6EB1BBBD", "ARCtrl_ISA_ArcInvestigation__ArcInvestigation_tryFromReadContract_Static_7570923F", "ARCtrl_ISA_ArcStudy__ArcStudy_ToCreateContract_6FCE9E49", "ARCtrl_ISA_ArcStudy__ArcStudy_ToUpdateContract", "ARCtrl_ISA_ArcStudy__ArcStudy_ToDeleteContract", "ARCtrl_ISA_ArcStudy__ArcStudy_toDeleteContract_Static_1B3D5E9B", "ARCtrl_ISA_ArcStudy__ArcStudy_toCreateContract_Static_Z12D8504E", "ARCtrl_ISA_ArcStudy__ArcStudy_toUpdateContract_Static_1B3D5E9B", "ARCtrl_ISA_ArcStudy__ArcStudy_tryFromReadContract_Static_7570923F", "ARCtrl_ISA_ArcAssay__ArcAssay_ToCreateContract_6FCE9E49", "ARCtrl_ISA_ArcAssay__ArcAssay_ToUpdateContract", "ARCtrl_ISA_ArcAssay__ArcAssay_ToDeleteContract", "ARCtrl_ISA_ArcAssay__ArcAssay_toDeleteContract_Static_1C75D08D", "ARCtrl_ISA_ArcAssay__ArcAssay_toCreateContract_Static_Z3B1E839C", "ARCtrl_ISA_ArcAssay__ArcAssay_toUpdateContract_Static_1C75D08D", "ARCtrl_ISA_ArcAssay__ArcAssay_tryFromReadContract_Static_7570923F"]

