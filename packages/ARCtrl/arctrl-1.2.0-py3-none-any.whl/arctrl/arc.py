from __future__ import annotations
from collections.abc import Callable
from typing import Any
from .fable_modules.fable_library.array_ import (choose, exactly_one, map, filter, iterate, exists, fold, concat)
from .fable_modules.fable_library.list import FSharpList
from .fable_modules.fable_library.map import of_seq as of_seq_1
from .fable_modules.fable_library.map_util import add_to_dict
from .fable_modules.fable_library.option import (default_arg, value as value_2, map as map_2, bind)
from .fable_modules.fable_library.reflection import (TypeInfo, class_type)
from .fable_modules.fable_library.seq import (to_array, to_list, delay, append, singleton, map as map_1, try_find, find, iterate as iterate_1, empty, collect)
from .fable_modules.fable_library.set import (union_many, of_seq, FSharpSet__Contains)
from .fable_modules.fable_library.types import Array
from .fable_modules.fable_library.util import (IEnumerable_1, to_enumerable, safe_hash, compare_primitives)
from .fable_modules.fs_spreadsheet.Cells.fs_cells_collection import Dictionary_tryGet
from .fable_modules.fs_spreadsheet.fs_workbook import FsWorkbook
from .Contract.contract import (Contract, DTOType, DTO)
from .FileSystem.file_system import FileSystem
from .FileSystem.file_system_tree import FileSystemTree
from .ISA.ISA_Spreadsheet.arc_assay import to_fs_workbook as to_fs_workbook_1
from .ISA.ISA_Spreadsheet.arc_investigation import (to_light_fs_workbook, to_fs_workbook)
from .ISA.ISA_Spreadsheet.arc_study import ARCtrl_ISA_ArcStudy__ArcStudy_toFsWorkbook_Static_Z2A9662E9
from .ISA.ISA.ArcTypes.arc_table import ArcTable
from .ISA.ISA.ArcTypes.arc_tables import ArcTables
from .ISA.ISA.ArcTypes.arc_types import (ArcAssay, ArcStudy, ArcInvestigation)
from .ISA.ISA.identifier import (Study_fileNameFromIdentifier, Assay_fileNameFromIdentifier)
from .Contracts.contracts_arctrl import try_isaread_contract_from_path
from .Contracts.contracts_arc_types import (ARCtrl_ISA_ArcAssay__ArcAssay_tryFromReadContract_Static_7570923F, ARCtrl_ISA_ArcStudy__ArcStudy_tryFromReadContract_Static_7570923F, ARCtrl_ISA_ArcInvestigation__ArcInvestigation_tryFromReadContract_Static_7570923F, ARCtrl_ISA_ArcAssay__ArcAssay_ToDeleteContract, ARCtrl_ISA_ArcInvestigation__ArcInvestigation_ToUpdateContract_6FCE9E49, ARCtrl_ISA_ArcStudy__ArcStudy_ToUpdateContract, ARCtrl_ISA_ArcStudy__ArcStudy_ToCreateContract_6FCE9E49, ARCtrl_ISA_ArcAssay__ArcAssay_ToCreateContract_6FCE9E49, ARCtrl_ISA_ArcAssay__ArcAssay_ToUpdateContract)
from .Contracts.contracts_git import (Init_createInitContract_6DFDD678, gitignore_contract, Init_createAddRemoteContract_Z721C83C5, Clone_createCloneContract_5000466F)
from .file_system_tree import (create_assays_folder, create_assay_folder, create_studies_folder, create_study_folder, create_investigation_file, create_workflows_folder, create_runs_folder)
from .path import (get_assay_folder_path, get_study_folder_path)

def ARCAux_getArcAssaysFromContracts(contracts: Array[Contract]) -> Array[ArcAssay]:
    def chooser(c: Contract, contracts: Any=contracts) -> ArcAssay | None:
        return ARCtrl_ISA_ArcAssay__ArcAssay_tryFromReadContract_Static_7570923F(c)

    return choose(chooser, contracts, None)


def ARCAux_getArcStudiesFromContracts(contracts: Array[Contract]) -> Array[tuple[ArcStudy, FSharpList[ArcAssay]]]:
    def chooser(c: Contract, contracts: Any=contracts) -> tuple[ArcStudy, FSharpList[ArcAssay]] | None:
        return ARCtrl_ISA_ArcStudy__ArcStudy_tryFromReadContract_Static_7570923F(c)

    return choose(chooser, contracts, None)


def ARCAux_getArcInvestigationFromContracts(contracts: Array[Contract]) -> ArcInvestigation:
    def chooser(c: Contract, contracts: Any=contracts) -> ArcInvestigation | None:
        return ARCtrl_ISA_ArcInvestigation__ArcInvestigation_tryFromReadContract_Static_7570923F(c)

    return exactly_one(choose(chooser, contracts, None))


def ARCAux_updateFSByISA(isa: ArcInvestigation | None, fs: FileSystem) -> FileSystem:
    pattern_input: tuple[Array[str], Array[str]]
    if isa is None:
        pattern_input = ([], [])

    else: 
        inv: ArcInvestigation = isa
        pattern_input = (to_array(inv.StudyIdentifiers), to_array(inv.AssayIdentifiers))

    def _arrow1780(assay_name: str, isa: Any=isa, fs: Any=fs) -> FileSystemTree:
        return create_assay_folder(assay_name)

    assays: FileSystemTree = create_assays_folder(map(_arrow1780, pattern_input[1], None))
    def _arrow1781(study_name: str, isa: Any=isa, fs: Any=fs) -> FileSystemTree:
        return create_study_folder(study_name)

    studies: FileSystemTree = create_studies_folder(map(_arrow1781, pattern_input[0], None))
    investigation: FileSystemTree = create_investigation_file()
    tree_1: FileSystem
    tree: FileSystemTree = FileSystemTree.create_root_folder([investigation, assays, studies])
    tree_1 = FileSystem.create(tree = tree)
    return fs.Union(tree_1)


def ARCAux_updateFSByCWL(cwl: None | None, fs: FileSystem) -> FileSystem:
    workflows: FileSystemTree = create_workflows_folder([])
    runs: FileSystemTree = create_runs_folder([])
    tree_1: FileSystem
    tree: FileSystemTree = FileSystemTree.create_root_folder([workflows, runs])
    tree_1 = FileSystem.create(tree = tree)
    return fs.Union(tree_1)


def _expr1826() -> TypeInfo:
    return class_type("ARCtrl.ARC", None, ARC)


class ARC:
    def __init__(self, isa: ArcInvestigation | None=None, cwl: None | None=None, fs: FileSystem | None=None) -> None:
        self.cwl: None | None = cwl
        self._isa: ArcInvestigation | None = isa
        self._cwl: None | None = self.cwl
        self._fs: FileSystem = ARCAux_updateFSByCWL(self.cwl, ARCAux_updateFSByISA(isa, default_arg(fs, FileSystem.create(tree = FileSystemTree(1, "", [])))))

    @property
    def ISA(self, __unit: None=None) -> ArcInvestigation | None:
        this: ARC = self
        return this._isa

    @ISA.setter
    def ISA(self, new_isa: ArcInvestigation | None=None) -> None:
        this: ARC = self
        this._isa = new_isa
        this.UpdateFileSystem()

    @property
    def CWL(self, __unit: None=None) -> None | None:
        this: ARC = self
        return this.cwl

    @property
    def FileSystem(self, __unit: None=None) -> FileSystem:
        this: ARC = self
        return this._fs

    @FileSystem.setter
    def FileSystem(self, fs: FileSystem) -> None:
        this: ARC = self
        this._fs = fs

    def RemoveAssay(self, assay_identifier: str) -> Array[Contract]:
        this: ARC = self
        isa: ArcInvestigation
        match_value: ArcInvestigation | None = this.ISA
        if match_value is None:
            raise Exception("Cannot remove assay from null ISA value.")

        else: 
            isa = match_value

        assay: ArcAssay = isa.GetAssay(assay_identifier)
        studies: Array[ArcStudy] = assay.StudiesRegisteredIn
        isa.RemoveAssay(assay_identifier)
        paths: Array[str] = this.FileSystem.Tree.ToFilePaths()
        assay_folder_path: str = get_assay_folder_path(assay_identifier)
        def predicate(p: str) -> bool:
            return not (p.find(assay_folder_path) == 0)

        filtered_paths: Array[str] = filter(predicate, paths)
        this.SetFilePaths(filtered_paths)
        def _arrow1784(__unit: None=None) -> IEnumerable_1[Contract]:
            def _arrow1783(__unit: None=None) -> IEnumerable_1[Contract]:
                def _arrow1782(__unit: None=None) -> IEnumerable_1[Contract]:
                    return map_1(ARCtrl_ISA_ArcStudy__ArcStudy_ToUpdateContract, studies)

                return append(singleton(ARCtrl_ISA_ArcInvestigation__ArcInvestigation_ToUpdateContract_6FCE9E49(isa)), delay(_arrow1782))

            return append(singleton(ARCtrl_ISA_ArcAssay__ArcAssay_ToDeleteContract(assay)), delay(_arrow1783))

        return list(to_list(delay(_arrow1784)))

    def RemoveStudy(self, study_identifier: str) -> Array[Contract]:
        this: ARC = self
        isa: ArcInvestigation
        match_value: ArcInvestigation | None = this.ISA
        if match_value is None:
            raise Exception("Cannot remove study from null ISA value.")

        else: 
            isa = match_value

        isa.RemoveStudy(study_identifier)
        paths: Array[str] = this.FileSystem.Tree.ToFilePaths()
        study_folder_path: str = get_study_folder_path(study_identifier)
        def predicate(p: str) -> bool:
            return not (p.find(study_folder_path) == 0)

        filtered_paths: Array[str] = filter(predicate, paths)
        this.SetFilePaths(filtered_paths)
        return list(to_enumerable([Contract.create_delete(study_folder_path), ARCtrl_ISA_ArcInvestigation__ArcInvestigation_ToUpdateContract_6FCE9E49(isa)]))

    @staticmethod
    def from_file_paths(file_paths: Array[str]) -> ARC:
        return ARC(None, None, FileSystem.from_file_paths(file_paths))

    def SetFilePaths(self, file_paths: Array[str]) -> None:
        this: ARC = self
        tree: FileSystemTree = FileSystemTree.from_file_paths(file_paths)
        this._fs = FileSystem(tree, this._fs.History)

    def GetReadContracts(self, __unit: None=None) -> Array[Contract]:
        this: ARC = self
        return choose(try_isaread_contract_from_path, this._fs.Tree.ToFilePaths(), None)

    def SetISAFromContracts(self, contracts: Array[Contract]) -> None:
        this: ARC = self
        investigation: ArcInvestigation = ARCAux_getArcInvestigationFromContracts(contracts)
        def mapping(tuple: tuple[ArcStudy, FSharpList[ArcAssay]]) -> ArcStudy:
            return tuple[0]

        studies: Array[ArcStudy] = map(mapping, ARCAux_getArcStudiesFromContracts(contracts), None)
        assays: Array[ArcAssay] = ARCAux_getArcAssaysFromContracts(contracts)
        def action(ai: str) -> None:
            def predicate(a: ArcAssay, ai: Any=ai) -> bool:
                return a.Identifier == ai

            if not exists(predicate, assays):
                investigation.DeleteAssay(ai)


        iterate(action, investigation.AssayIdentifiers)
        def action_1(si: str) -> None:
            def predicate_1(s: ArcStudy, si: Any=si) -> bool:
                return s.Identifier == si

            if not exists(predicate_1, studies):
                investigation.DeleteStudy(si)


        iterate(action_1, investigation.StudyIdentifiers)
        def action_2(study: ArcStudy) -> None:
            def predicate_2(s_1: ArcStudy, study: Any=study) -> bool:
                return s_1.Identifier == study.Identifier

            registered_study_opt: ArcStudy | None = try_find(predicate_2, investigation.Studies)
            if registered_study_opt is None:
                investigation.AddStudy(study)

            else: 
                registered_study: ArcStudy = registered_study_opt
                registered_study.UpdateReferenceByStudyFile(study, True)

            study.StaticHash = study.GetLightHashCode() or 0

        iterate(action_2, studies)
        def action_3(assay: ArcAssay) -> None:
            def predicate_3(a_1: ArcAssay, assay: Any=assay) -> bool:
                return a_1.Identifier == assay.Identifier

            registered_assay_opt: ArcAssay | None = try_find(predicate_3, investigation.Assays)
            if registered_assay_opt is None:
                investigation.AddAssay(assay)

            else: 
                registered_assay: ArcAssay = registered_assay_opt
                registered_assay.UpdateReferenceByAssayFile(assay, True)

            def predicate_4(a_2: ArcAssay, assay: Any=assay) -> bool:
                return a_2.Identifier == assay.Identifier

            assay_1: ArcAssay = find(predicate_4, investigation.Assays)
            updated_tables: ArcTables
            array_6: Array[ArcStudy] = assay_1.StudiesRegisteredIn
            def folder(tables: ArcTables, study_1: ArcStudy, assay: Any=assay) -> ArcTables:
                return ArcTables.update_reference_tables_by_sheets(ArcTables(study_1.Tables), tables, False)

            updated_tables = fold(folder, ArcTables(assay_1.Tables), array_6)
            assay_1.Tables = updated_tables.Tables

        iterate(action_3, assays)
        def action_4(a_3: ArcAssay) -> None:
            a_3.StaticHash = safe_hash(a_3) or 0

        iterate_1(action_4, investigation.Assays)
        def action_5(s_2: ArcStudy) -> None:
            s_2.StaticHash = s_2.GetLightHashCode() or 0

        iterate_1(action_5, investigation.Studies)
        investigation.StaticHash = investigation.GetLightHashCode() or 0
        this.ISA = investigation

    def UpdateFileSystem(self, __unit: None=None) -> None:
        this: ARC = self
        new_fs: FileSystem
        fs: FileSystem = ARCAux_updateFSByISA(this._isa, this._fs)
        new_fs = ARCAux_updateFSByCWL(this._cwl, fs)
        this._fs = new_fs

    def GetWriteContracts(self, is_light: bool | None=None) -> Array[Contract]:
        this: ARC = self
        is_light_1: bool = default_arg(is_light, True)
        workbooks: Any = dict([])
        match_value: ArcInvestigation | None = this.ISA
        if match_value is None:
            add_to_dict(workbooks, "isa.investigation.xlsx", (DTOType(2), to_light_fs_workbook(ArcInvestigation.create("MISSING_IDENTIFIER_"))))

        else: 
            inv: ArcInvestigation = match_value
            add_to_dict(workbooks, "isa.investigation.xlsx", (DTOType(2), (to_light_fs_workbook if is_light_1 else to_fs_workbook)(inv)))
            inv.StaticHash = inv.GetLightHashCode() or 0
            def action(s: ArcStudy) -> None:
                s.StaticHash = s.GetLightHashCode() or 0
                add_to_dict(workbooks, Study_fileNameFromIdentifier(s.Identifier), (DTOType(1), ARCtrl_ISA_ArcStudy__ArcStudy_toFsWorkbook_Static_Z2A9662E9(s)))

            iterate_1(action, inv.Studies)
            def action_1(a: ArcAssay) -> None:
                a.StaticHash = safe_hash(a) or 0
                add_to_dict(workbooks, Assay_fileNameFromIdentifier(a.Identifier), (DTOType(0), to_fs_workbook_1(a)))

            iterate_1(action_1, inv.Assays)

        def mapping(fp: str) -> Contract:
            match_value_1: tuple[DTOType, FsWorkbook] | None = Dictionary_tryGet(fp, workbooks)
            if match_value_1 is None:
                return Contract.create_create(fp, DTOType(6))

            else: 
                wb: FsWorkbook = match_value_1[1]
                dto: DTOType = match_value_1[0]
                return Contract.create_create(fp, dto, DTO(0, wb))


        return map(mapping, this._fs.Tree.ToFilePaths(True), None)

    def GetUpdateContracts(self, is_light: bool | None=None) -> Array[Contract]:
        this: ARC = self
        is_light_1: bool = default_arg(is_light, True)
        match_value: ArcInvestigation | None = this.ISA
        def _arrow1785(__unit: None=None) -> bool:
            inv: ArcInvestigation = match_value
            return inv.StaticHash == 0

        def _arrow1786(__unit: None=None) -> Array[Contract]:
            inv_1: ArcInvestigation = match_value
            return this.GetWriteContracts(is_light_1)

        def _arrow1794(__unit: None=None) -> Array[Contract]:
            inv_2: ArcInvestigation = match_value
            def _arrow1793(__unit: None=None) -> IEnumerable_1[Contract]:
                hash_1: int = inv_2.GetLightHashCode() or 0
                def _arrow1792(__unit: None=None) -> IEnumerable_1[Contract]:
                    inv_2.StaticHash = hash_1 or 0
                    def _arrow1788(s: ArcStudy) -> IEnumerable_1[Contract]:
                        hash_2: int = s.GetLightHashCode() or 0
                        def _arrow1787(__unit: None=None) -> IEnumerable_1[Contract]:
                            s.StaticHash = hash_2 or 0
                            return empty()

                        return append(ARCtrl_ISA_ArcStudy__ArcStudy_ToCreateContract_6FCE9E49(s, True) if (s.StaticHash == 0) else (singleton(ARCtrl_ISA_ArcStudy__ArcStudy_ToUpdateContract(s)) if (s.StaticHash != hash_2) else empty()), delay(_arrow1787))

                    def _arrow1791(__unit: None=None) -> IEnumerable_1[Contract]:
                        def _arrow1790(a: ArcAssay) -> IEnumerable_1[Contract]:
                            hash_3: int = safe_hash(a) or 0
                            def _arrow1789(__unit: None=None) -> IEnumerable_1[Contract]:
                                a.StaticHash = hash_3 or 0
                                return empty()

                            return append(ARCtrl_ISA_ArcAssay__ArcAssay_ToCreateContract_6FCE9E49(a, True) if (a.StaticHash == 0) else (singleton(ARCtrl_ISA_ArcAssay__ArcAssay_ToUpdateContract(a)) if (a.StaticHash != hash_3) else empty()), delay(_arrow1789))

                        return collect(_arrow1790, inv_2.Assays)

                    return append(collect(_arrow1788, inv_2.Studies), delay(_arrow1791))

                return append(singleton(ARCtrl_ISA_ArcInvestigation__ArcInvestigation_ToUpdateContract_6FCE9E49(inv_2, is_light_1)) if (inv_2.StaticHash != hash_1) else empty(), delay(_arrow1792))

            return to_array(delay(_arrow1793))

        return (_arrow1786() if _arrow1785() else _arrow1794()) if (match_value is not None) else this.GetWriteContracts(is_light_1)

    def GetGitInitContracts(self, branch: str | None=None, repository_address: str | None=None, default_gitignore: bool | None=None) -> Array[Contract]:
        default_gitignore_1: bool = default_arg(default_gitignore, False)
        def _arrow1797(__unit: None=None) -> IEnumerable_1[Contract]:
            def _arrow1796(__unit: None=None) -> IEnumerable_1[Contract]:
                def _arrow1795(__unit: None=None) -> IEnumerable_1[Contract]:
                    return singleton(Init_createAddRemoteContract_Z721C83C5(value_2(repository_address))) if (repository_address is not None) else empty()

                return append(singleton(gitignore_contract) if default_gitignore_1 else empty(), delay(_arrow1795))

            return append(singleton(Init_createInitContract_6DFDD678(branch)), delay(_arrow1796))

        return to_array(delay(_arrow1797))

    @staticmethod
    def get_clone_contract(remote_url: str, merge: bool | None=None, branch: str | None=None, token: tuple[str, str] | None=None, nolfs: bool | None=None) -> Contract:
        return Clone_createCloneContract_5000466F(remote_url, merge, branch, token, nolfs)

    def Copy(self, __unit: None=None) -> ARC:
        this: ARC = self
        def mapping(i: ArcInvestigation) -> ArcInvestigation:
            return i.Copy()

        isa_copy: ArcInvestigation | None = map_2(mapping, this._isa)
        fs_copy: FileSystem = this._fs.Copy()
        return ARC(isa_copy, this._cwl, fs_copy)

    def GetRegisteredPayload(self, IgnoreHidden: bool | None=None) -> FileSystemTree:
        this: ARC = self
        def mapping_1(isa: ArcInvestigation) -> Array[ArcStudy]:
            return isa.Studies[:]

        def mapping(i: ArcInvestigation) -> ArcInvestigation:
            return i.Copy()

        registered_studies: Array[ArcStudy] = default_arg(map_2(mapping_1, map_2(mapping, this._isa)), [])
        def mapping_2(s: ArcStudy) -> Array[ArcAssay]:
            return s.RegisteredAssays[:]

        registered_assays: Array[ArcAssay] = concat(map(mapping_2, registered_studies, None), None)
        class ObjectExpr1798:
            @property
            def Compare(self) -> Callable[[str, str], int]:
                return compare_primitives

        def mapping_3(s_1: ArcStudy) -> Any:
            study_foldername: str = ((("" + "studies") + "/") + s_1.Identifier) + ""
            def _arrow1805(__unit: None=None, s_1: Any=s_1) -> IEnumerable_1[str]:
                def _arrow1804(__unit: None=None) -> IEnumerable_1[str]:
                    def _arrow1803(__unit: None=None) -> IEnumerable_1[str]:
                        def _arrow1802(table: ArcTable) -> IEnumerable_1[str]:
                            def _arrow1801(kv: Any) -> IEnumerable_1[str]:
                                text_value: str = kv[1].ToFreeTextCell().AsFreeText
                                def _arrow1800(__unit: None=None) -> IEnumerable_1[str]:
                                    def _arrow1799(__unit: None=None) -> IEnumerable_1[str]:
                                        return singleton(((((("" + study_foldername) + "/") + "protocols") + "/") + text_value) + "")

                                    return append(singleton(((((("" + study_foldername) + "/") + "resources") + "/") + text_value) + ""), delay(_arrow1799))

                                return append(singleton(text_value), delay(_arrow1800))

                            return collect(_arrow1801, table.Values)

                        return collect(_arrow1802, s_1.Tables)

                    return append(singleton(((("" + study_foldername) + "/") + "README.md") + ""), delay(_arrow1803))

                return append(singleton(((("" + study_foldername) + "/") + "isa.study.xlsx") + ""), delay(_arrow1804))

            class ObjectExpr1806:
                @property
                def Compare(self) -> Callable[[str, str], int]:
                    return compare_primitives

            return of_seq(to_list(delay(_arrow1805)), ObjectExpr1806())

        class ObjectExpr1807:
            @property
            def Compare(self) -> Callable[[str, str], int]:
                return compare_primitives

        def mapping_4(a: ArcAssay) -> Any:
            assay_foldername: str = ((("" + "assays") + "/") + a.Identifier) + ""
            def _arrow1814(__unit: None=None, a: Any=a) -> IEnumerable_1[str]:
                def _arrow1813(__unit: None=None) -> IEnumerable_1[str]:
                    def _arrow1812(__unit: None=None) -> IEnumerable_1[str]:
                        def _arrow1811(table_1: ArcTable) -> IEnumerable_1[str]:
                            def _arrow1810(kv_1: Any) -> IEnumerable_1[str]:
                                text_value_1: str = kv_1[1].ToFreeTextCell().AsFreeText
                                def _arrow1809(__unit: None=None) -> IEnumerable_1[str]:
                                    def _arrow1808(__unit: None=None) -> IEnumerable_1[str]:
                                        return singleton(((((("" + assay_foldername) + "/") + "protocols") + "/") + text_value_1) + "")

                                    return append(singleton(((((("" + assay_foldername) + "/") + "dataset") + "/") + text_value_1) + ""), delay(_arrow1808))

                                return append(singleton(text_value_1), delay(_arrow1809))

                            return collect(_arrow1810, table_1.Values)

                        return collect(_arrow1811, a.Tables)

                    return append(singleton(((("" + assay_foldername) + "/") + "README.md") + ""), delay(_arrow1812))

                return append(singleton(((("" + assay_foldername) + "/") + "isa.assay.xlsx") + ""), delay(_arrow1813))

            class ObjectExpr1815:
                @property
                def Compare(self) -> Callable[[str, str], int]:
                    return compare_primitives

            return of_seq(to_list(delay(_arrow1814)), ObjectExpr1815())

        class ObjectExpr1816:
            @property
            def Compare(self) -> Callable[[str, str], int]:
                return compare_primitives

        class ObjectExpr1817:
            @property
            def Compare(self) -> Callable[[str, str], int]:
                return compare_primitives

        include_files: Any = union_many(to_enumerable([of_seq(to_enumerable(["isa.investigation.xlsx", "README.md"]), ObjectExpr1798()), union_many(map(mapping_3, registered_studies, None), ObjectExpr1807()), union_many(map(mapping_4, registered_assays, None), ObjectExpr1816())]), ObjectExpr1817())
        ignore_hidden: bool = default_arg(IgnoreHidden, True)
        fs_copy: FileSystem = this._fs.Copy()
        def binder(tree_1: FileSystemTree) -> FileSystemTree | None:
            if ignore_hidden:
                def _arrow1818(n_1: str, tree_1: Any=tree_1) -> bool:
                    return not (n_1.find(".") == 0)

                return FileSystemTree.filter_folders(_arrow1818)(tree_1)

            else: 
                return tree_1


        def _arrow1820(__unit: None=None) -> FileSystemTree | None:
            tree: FileSystemTree
            def predicate(p: str) -> bool:
                if True if (p.find("workflows") == 0) else (p.find("runs") == 0):
                    return True

                else: 
                    return FSharpSet__Contains(include_files, p)


            paths: Array[str] = filter(predicate, FileSystemTree.to_file_paths()(fs_copy.Tree))
            tree = FileSystemTree.from_file_paths(paths)
            def _arrow1819(n: str) -> bool:
                return not (n.find(".") == 0)

            return FileSystemTree.filter_files(_arrow1819)(tree) if ignore_hidden else tree

        return default_arg(bind(binder, _arrow1820()), FileSystemTree.from_file_paths([]))

    def GetAdditionalPayload(self, IgnoreHidden: bool | None=None) -> FileSystemTree:
        this: ARC = self
        ignore_hidden: bool = default_arg(IgnoreHidden, True)
        class ObjectExpr1821:
            @property
            def Compare(self) -> Callable[[str, str], int]:
                return compare_primitives

        registered_payload: Any = of_seq(FileSystemTree.to_file_paths()(this.GetRegisteredPayload()), ObjectExpr1821())
        def binder(tree_1: FileSystemTree) -> FileSystemTree | None:
            if ignore_hidden:
                def _arrow1822(n_1: str, tree_1: Any=tree_1) -> bool:
                    return not (n_1.find(".") == 0)

                return FileSystemTree.filter_folders(_arrow1822)(tree_1)

            else: 
                return tree_1


        def _arrow1824(__unit: None=None) -> FileSystemTree | None:
            tree: FileSystemTree
            def predicate(p: str) -> bool:
                return not FSharpSet__Contains(registered_payload, p)

            paths: Array[str] = filter(predicate, FileSystemTree.to_file_paths()(this._fs.Copy().Tree))
            tree = FileSystemTree.from_file_paths(paths)
            def _arrow1823(n: str) -> bool:
                return not (n.find(".") == 0)

            return FileSystemTree.filter_files(_arrow1823)(tree) if ignore_hidden else tree

        return default_arg(bind(binder, _arrow1824()), FileSystemTree.from_file_paths([]))

    @staticmethod
    def DefaultContracts() -> Any:
        class ObjectExpr1825:
            @property
            def Compare(self) -> Callable[[str, str], int]:
                return compare_primitives

        return of_seq_1(to_enumerable([(".gitignore", gitignore_contract)]), ObjectExpr1825())


ARC_reflection = _expr1826

def ARC__ctor_81B80F4(isa: ArcInvestigation | None=None, cwl: None | None=None, fs: FileSystem | None=None) -> ARC:
    return ARC(isa, cwl, fs)


__all__ = ["ARCAux_getArcAssaysFromContracts", "ARCAux_getArcStudiesFromContracts", "ARCAux_getArcInvestigationFromContracts", "ARCAux_updateFSByISA", "ARCAux_updateFSByCWL", "ARC_reflection"]

