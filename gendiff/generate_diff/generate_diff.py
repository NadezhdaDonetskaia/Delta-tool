#!/usr/bin/env python3
from pathlib import Path
from ..format_output import formatting
from .get_difference_representation import get_difference_representation
from .parse import parse


def generate_diff(first_path: str, second_path: str, format='stylish') -> str:
    with open(first_path) as ff:
        first_file = parse(Path(first_path).suffix, ff)
        with open(second_path) as sf:
            second_file = parse(Path(second_path).suffix, sf)
    if not first_file or not second_file:
        raise ValueError("File don't be empty!")
    diff = get_difference_representation(first_file, second_file)
    return formatting(diff, format)
