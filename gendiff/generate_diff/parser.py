#!/usr/bin/env python3
import json
import yaml
from typing import TextIO


def parser(extension: str, open_file: TextIO) -> dict:
    if extension == '.json':
        return json.load(open_file)
    if extension in ('.yaml', '.yml'):
        return yaml.safe_load(open_file)
