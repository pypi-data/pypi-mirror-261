from .FileSystem.path import combine

def get_assay_folder_path(assay_identifier: str) -> str:
    return combine("assays", assay_identifier)


def get_study_folder_path(study_identifier: str) -> str:
    return combine("studies", study_identifier)


__all__ = ["get_assay_folder_path", "get_study_folder_path"]

