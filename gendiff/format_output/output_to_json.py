#!/usr/bin/env python3
import json


def output_to_json(dict_, spaces_count=0):  # noqa: <error code>
    result = '{\n'
    sorted_keys = sorted(dict_.keys())
    for key in sorted_keys:
        if isinstance(dict_[key], dict):
            if dict_[key].get('type') == 'unchanged':
                if isinstance(dict_[key].get('value'), dict):
                    value = output_to_json(dict_[key].get("value"), spaces_count + 2)  # noqa: <error code>
                else:
                    value = json.dumps(dict_[key].get('value'))
                result += f'{(spaces_count + 2) * " "}"{key}": {value},\n'
            elif dict_[key].get('type') == 'changed':
                value_del = dict_[key].get('value')[0]
                value_add = dict_[key].get('value')[1]
                if isinstance(value_del, dict):
                    value_del = output_to_json(value_del, spaces_count + 2)
                else:
                    value_del = json.dumps(value_del)
                if isinstance(value_add, dict):
                    value_add = output_to_json(value_add, spaces_count + 2)
                else:
                    value_add = json.dumps(value_add)
                result += f'{(spaces_count + 2) * " "}"- {key}":' \
                          f' {value_del},\n'
                result += f'{(spaces_count + 2) * " "}"+ {key}":' \
                          f' {value_add},\n'
            elif dict_[key].get('type') == 'deleted':
                value_del = dict_[key].get('value')
                if isinstance(value_del, dict):
                    value_del = output_to_json(value_del, spaces_count + 2)
                else:
                    value_del = json.dumps(value_del)
                result += f'{(spaces_count + 2) * " "}"- {key}":' \
                          f' {value_del},\n'
            elif dict_[key].get('type') == 'added':
                value_add = dict_[key].get('value')
                if isinstance(value_add, dict):
                    value_add = output_to_json(value_add, spaces_count + 2)
                else:
                    value_add = json.dumps(value_add)
                result += f'{(spaces_count + 2) * " "}"+ {key}":' \
                          f' {value_add},\n'
            else:
                result += f'{(spaces_count + 2) * " "}"{key}": ' \
                          f'{output_to_json(dict_[key], spaces_count + 2)},\n'
        else:
            value = json.dumps(dict_[key])
            result += f'{(spaces_count + 2) * " "}"{key}": {value},\n'
    result = result[:-2] + '\n'
    result += ' ' * spaces_count + '}'
    return result
