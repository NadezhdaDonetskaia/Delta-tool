#!/usr/bin/env python3
import json
import yaml
from pathlib import Path
from ..format_output import formatting
from .diff_of_dicts import diff_of_dicts


def read_file(path: str, val: str) -> dict:
    if Path(path).suffix == '.json':
        return json.load(val)
    if Path(path).suffix in ('.yaml', '.yml'):
        return yaml.safe_load(val)


def generate_diff(first_path: str, second_path: str, format='stylish') -> str:  # noqa: <error code>
    with open(first_path) as ff:
        first_file = read_file(first_path, ff)
        with open(second_path) as sf:
            second_file = read_file(second_path, sf)
    if not first_file or not second_file:
        raise ValueError("File don't be empty!")
    return formatting(diff_of_dicts(first_file, second_file), format)
