#!/usr/bin/env python3
import json
import yaml
from pathlib import Path
from .scripts.format_output import formatting
from .scripts.diff_of_dicts import diff_of_dicts


def read_file(path: str, val: str) -> dict:
    if Path(path).suffix == '.json':
        return json.load(val)
    if Path(path).suffix in ('.yaml', '.yml'):
        return yaml.safe_load(val)


def generate_diff(first_file: str, second_file: str, format='stylish') -> str:  # noqa: <error code>
    first_file = read_file(first_file, open(first_file))
    second_file = read_file(second_file, open(second_file))
    if not first_file and not second_file:
        return '{}'
    if not first_file or not second_file:
        raise ValueError("File don't be empty!")
    return formatting(diff_of_dicts(first_file, second_file), format)
