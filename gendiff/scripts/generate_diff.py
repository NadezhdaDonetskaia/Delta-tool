#!/usr/bin/env python3
import json
import yaml


def is_json(path: str) -> bool:
    return path[-5:] == '.json'


def is_yaml(path: str) -> bool:
    return path[-4:] in ('yaml', '.yml')


def read_file(path: str):
    if is_json(path):
        return json.load(open(path))
    if is_yaml(path):
        return yaml.safe_load(open(path))


def generate_diff(first_file: str, second_file: str, spaces_count=0) -> str:
    first_file = read_file(first_file)
    second_file = read_file(second_file)
    accum_keys = first_file.copy()
    accum_keys.update(second_file)
    accum_keys = [el for el in accum_keys]
    accum_keys.sort()
    result = '{\n'
    for key in accum_keys:
        if key in first_file and key in second_file:
            if first_file[key] != second_file[key]:
                result += f'{spaces_count*" "}  - {key}: {first_file[key]}\n' \
                          f'{spaces_count*" "}  + {key}: {second_file[key]}\n'
            else:
                result += f'{spaces_count*" "}    {key}: {first_file[key]}\n'
        elif key in first_file:
            result += f'{spaces_count*" "}  - {key}: {first_file[key]}\n'
        else:
            result += f'{spaces_count*" "}  + {key}: {second_file[key]}\n'
    result += '}'
    return result
