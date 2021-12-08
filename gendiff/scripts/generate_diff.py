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


def stylish(dict_, spaces_count=0):
    result = '{\n'
    sorted_keys = sorted(dict_.keys(), key=lambda x: x[2:] if x[:1] in ('+', '-') else x)
    for key in sorted_keys:
        if key[:2] in ('+ ', '- ', '  '):
            if isinstance(dict_[key], dict):
                result += f'{(spaces_count + 2) * " "}{key}: {stylish(dict_[key], spaces_count + 4)}\n'
            else:
                if dict_[key] is False:
                    result += f'{(spaces_count + 2) * " "}{key}: false\n'
                elif dict_[key] is True:
                    result += f'{(spaces_count + 2) * " "}{key}: true\n'
                elif dict_[key] is None:
                    result += f'{(spaces_count + 2) * " "}{key}: null\n'
                elif not dict_[key]:
                    result += f'{(spaces_count + 2) * " "}{key}:\n'
                else:
                    result += f'{(spaces_count + 2) * " "}{key}: {dict_[key]}\n'
        else:
            if isinstance(dict_[key], dict):
                result += f'{(spaces_count + 4) * " "}{key}: {stylish(dict_[key], spaces_count + 4)}\n'
            else:
                if dict_[key] is False:
                    result += f'{(spaces_count + 4) * " "}{key}: false\n'
                elif dict_[key] is True:
                    result += f'{(spaces_count + 4) * " "}{key}: true\n'
                elif dict_[key] is None:
                    result += f'{(spaces_count + 4) * " "}{key}: null\n'
                elif not dict_[key]:
                    result += f'{(spaces_count + 4) * " "}{key}:\n'
                else:
                    result += f'{(spaces_count + 4) * " "}{key}: {dict_[key]}\n'
    result += ' ' * spaces_count + '}'
    return result


def generate_diff(first_file: str, second_file: str) -> str:
    first_file = read_file(first_file)
    second_file = read_file(second_file)

    def diff_of_dicts(dict1, dict2):
        result = dict()
        all_keys = set(list(dict1.keys()) + list(dict2.keys()))
        for key in all_keys:
            if key in dict1 and key in dict2:
                if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
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
    return stylish(diff_of_dicts(first_file, second_file))
