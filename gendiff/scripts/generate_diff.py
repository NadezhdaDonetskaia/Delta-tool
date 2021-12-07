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


def generate_diff(first_file: str, second_file: str) -> str:
    first_file = read_file(first_file)
    second_file = read_file(second_file)

    def dict_to_str(dict_, spaces_count=0):
        result = '{\n'
        for key in dict_:
            if isinstance(dict_[key], dict):
                result += f'{spaces_count*" "}    {key}: {dict_to_str(dict_[key], spaces_count+4)}\n'
            else:
                result += f'{spaces_count*" "}    {key}: {dict_[key]}\n'
        result += ' ' * spaces_count + '}'
        return result

    def diff_to_str(ff: dict, sf: dict, spaces_count=0) -> str:
        accum_keys = ff.copy()
        accum_keys.update(sf)
        accum_keys = [el for el in accum_keys]
        accum_keys.sort()
        result = '{\n'
        for key in accum_keys:
            if key in ff and key in sf:  # если значение не dict!!!
                if ff[key] != sf[key]:
                    if isinstance(ff[key], dict) and isinstance(sf[key], dict):
                        result += f'{spaces_count*" "}    {key}: {diff_to_str(ff[key], sf[key], spaces_count + 4)}\n'
                    else:
                        if isinstance(ff[key], dict):
                            result += f'{spaces_count*" "}  - {key}: {dict_to_str(ff[key], spaces_count + 4)}\n' \
                                      f'{spaces_count*" "}  + {key}: {sf[key]}\n'
                        else:
                            result += f'{spaces_count*" "}  - {key}: {ff[key]}\n' \
                                      f'{spaces_count*" "}  + {key}: {sf[key]}\n'
                else:
                    if isinstance(ff[key], dict):
                        result += f'{spaces_count*" "}    {key}: {dict_to_str(ff[key], spaces_count + 4)}\n'
                    else:
                        result += f'{spaces_count*" "}    {key}: {ff[key]}\n'
            elif key in ff:
                if isinstance(ff[key], dict):
                    result += f'{spaces_count*" "}  - {key}: {dict_to_str(ff[key], spaces_count + 4)}\n'
                else:
                    result += f'{spaces_count*" "}  - {key}: {ff[key]}\n'
            else:
                if isinstance(sf[key], dict):
                    result += f'{spaces_count*" "}  + {key}: {dict_to_str(sf[key], spaces_count + 4)}\n'
                else:
                    result += f'{spaces_count*" "}  + {key}: {sf[key]}\n'
        result += ' ' * spaces_count + '}'
        return result

    return diff_to_str(first_file, second_file)

