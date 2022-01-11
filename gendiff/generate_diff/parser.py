#!/usr/bin/env python3
import json
import yaml


def parser(extension: str, val: str) -> dict:
    if extension == '.json':
        return json.load(val)
    if extension in ('.yaml', '.yml'):
        return yaml.safe_load(val)
