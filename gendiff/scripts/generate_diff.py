#!/usr/bin/env python3
import json


def generate_diff(first_file, second_file) -> str:
    first_file = json.load(open(first_file))
    second_file = json.load(open(second_file))
    accum_keys = first_file.copy()
    accum_keys.update(second_file)
    accum_keys = [el for el in accum_keys]
    accum_keys.sort()
    result = '{\n'
    for key in accum_keys:
        if key in first_file and key in second_file:
            if first_file[key] != second_file[key]:
                result += f'    - {key}: {first_file[key]}\n    ' \
                          f'+ {key}: {second_file[key]}\n'
            else:
                result += f'      {key}: {first_file[key]}\n'
        elif key in first_file:
            result += f'    - {key}: {first_file[key]}\n'
        else:
            result += f'    + {key}: {second_file[key]}\n'
    result += '}'
    return result
