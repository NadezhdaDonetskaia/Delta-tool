#!/usr/bin/env python3
import json
import yaml
from .format_output.stylish import stylish
from .format_output.plain import plain
from .format_output.output_to_json import output_to_json


def is_json(path: str) -> bool:
    return path[-5:] == '.json'


def is_yaml(path: str) -> bool:
    return path[-4:] in ('yaml', '.yml')


def read_file(path: str):
    if is_json(path):
        return json.load(open(path))
    if is_yaml(path):
        return yaml.safe_load(open(path))



def generate_diff(first_file: str, second_file: str, format) -> str:  # noqa: <error code>
    first_file = read_file(first_file)
    second_file = read_file(second_file)

    def diff_of_dicts(dict1, dict2):
        result = dict()
        all_keys = set(list(dict1.keys()) + list(dict2.keys()))
        for key in all_keys:
            if key in dict1 and key in dict2:
                if isinstance(dict1[key], dict)\
                        and isinstance(dict2[key], dict):
                    result[key] = diff_of_dicts(dict1[key], dict2[key])
                else:
                    if dict1[key] == dict2[key]:
                        result[key] = dict1[key]
                    else:
                        result[f'- {key}'] = dict1[key]
                        result[f'+ {key}'] = dict2[key]
            elif key in dict1:
                result[f'- {key}'] = dict1[key]
            else:
                result[f'+ {key}'] = dict2[key]
        return result
    if format == 'stylish':
        return stylish(diff_of_dicts(first_file, second_file))
    elif format == 'plain':
        return plain(diff_of_dicts(first_file, second_file))
    elif format == 'json':
        return output_to_json(diff_of_dicts(first_file, second_file))
