#!/usr/bin/env python3
from pathlib import Path
from ..format_output import formatting
from .diff_of_dicts import diff_of_dicts
from .parser import parser


def generate_diff(first_path: str, second_path: str, format='stylish') -> str:  # noqa: <error code>
    with open(first_path) as ff:
        first_file = parser(Path(first_path).suffix, ff)
        with open(second_path) as sf:
            second_file = parser(Path(second_path).suffix, sf)
    if not first_file or not second_file:
        raise ValueError("File don't be empty!")
    return formatting(diff_of_dicts(first_file, second_file), format)
