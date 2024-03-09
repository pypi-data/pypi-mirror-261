from typing import Any
from ..fable_modules.fable_library.array_ import (map_indexed, last)
from ..fable_modules.fable_library.string_ import (split as split_1, trim_end, trim_start, join, trim)
from ..fable_modules.fable_library.types import Array

seperators: Array[str] = ["/", "\\"]

def split(path: str) -> Array[str]:
    return split_1(path, seperators, None, 3)


def combine(path1: str, path2: str) -> str:
    return (trim_end(path1, *seperators) + "/") + trim_start(path2, *seperators)


def combine_many(paths: Array[str]) -> str:
    def mapping(i: int, p: str, paths: Any=paths) -> str:
        if i == 0:
            return trim_end(p, *seperators)

        elif i == (len(paths) - 1):
            return trim_start(p, *seperators)

        else: 
            return trim(p, *seperators)


    return join("/", map_indexed(mapping, paths, None))


def get_file_name(path: str) -> str:
    return last(split(path))


def is_file(file_name: str, path: str) -> bool:
    return get_file_name(path) == file_name


__all__ = ["seperators", "split", "combine", "combine_many", "get_file_name", "is_file"]

