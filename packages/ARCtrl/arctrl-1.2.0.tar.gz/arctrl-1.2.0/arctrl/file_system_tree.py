from __future__ import annotations
from .fable_modules.fable_library.array_ import append
from .fable_modules.fable_library.types import Array
from .FileSystem.file_system_tree import FileSystemTree

def create_git_keep_file(__unit: None=None) -> FileSystemTree:
    return FileSystemTree.create_file(".gitkeep")


def create_readme_file(__unit: None=None) -> FileSystemTree:
    return FileSystemTree.create_file("README.md")


def create_empty_folder(name: str) -> FileSystemTree:
    return FileSystemTree.create_folder(name, [create_git_keep_file()])


def create_assay_folder(assay_name: str) -> FileSystemTree:
    dataset: FileSystemTree = create_empty_folder("dataset")
    protocols: FileSystemTree = create_empty_folder("protocols")
    readme: FileSystemTree = create_readme_file()
    assay_file: FileSystemTree = FileSystemTree.create_file("isa.assay.xlsx")
    return FileSystemTree.create_folder(assay_name, [dataset, protocols, assay_file, readme])


def create_study_folder(study_name: str) -> FileSystemTree:
    resources: FileSystemTree = create_empty_folder("resources")
    protocols: FileSystemTree = create_empty_folder("protocols")
    readme: FileSystemTree = create_readme_file()
    study_file: FileSystemTree = FileSystemTree.create_file("isa.study.xlsx")
    return FileSystemTree.create_folder(study_name, [resources, protocols, study_file, readme])


def create_investigation_file(__unit: None=None) -> FileSystemTree:
    return FileSystemTree.create_file("isa.investigation.xlsx")


def create_assays_folder(assays: Array[FileSystemTree]) -> FileSystemTree:
    return FileSystemTree.create_folder("assays", append([create_git_keep_file()], assays, None))


def create_studies_folder(studies: Array[FileSystemTree]) -> FileSystemTree:
    return FileSystemTree.create_folder("studies", append([create_git_keep_file()], studies, None))


def create_workflows_folder(workflows: Array[FileSystemTree]) -> FileSystemTree:
    return FileSystemTree.create_folder("workflows", append([create_git_keep_file()], workflows, None))


def create_runs_folder(runs: Array[FileSystemTree]) -> FileSystemTree:
    return FileSystemTree.create_folder("runs", append([create_git_keep_file()], runs, None))


__all__ = ["create_git_keep_file", "create_readme_file", "create_empty_folder", "create_assay_folder", "create_study_folder", "create_investigation_file", "create_assays_folder", "create_studies_folder", "create_workflows_folder", "create_runs_folder"]

