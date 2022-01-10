#!/usr/bin/env python3
import json


def type_of_value(value):
    if isinstance(value, bool) or value is None:
        result = json.dumps(value)
    else:
        result = value
    return result


def stylish(dict_, spaces_count=0):  # noqa: <error code>
    result = '{\n'
    sorted_keys = sorted(dict_.keys())
    for key in sorted_keys:
        if isinstance(dict_[key], dict):
            if dict_[key].get('type') == 'unchanged':
                if isinstance(dict_[key].get('value'), dict):
                    value = stylish(dict_[key].get("value"), spaces_count + 4)
                    result += f'{(spaces_count + 4) * " "}{key}: ' \
                              f'{value}\n'
                else:
                    value = type_of_value(dict_[key].get("value"))
                    result += f'{(spaces_count + 4) * " "}{key}: {value}\n'
            elif dict_[key].get('type') == 'changed':
                value_del = dict_[key].get('value')[0]
                value_add = dict_[key].get('value')[1]
                if isinstance(value_del, dict):
                    value_del = stylish(value_del, spaces_count + 4)
                if isinstance(value_add, dict):
                    value_add = stylish(value_add, spaces_count + 4)
                result += f'{(spaces_count + 2) * " "}- {key}: ' \
                          f'{type_of_value(value_del)}\n'
                result += f'{(spaces_count + 2) * " "}+ {key}: ' \
                          f'{type_of_value(value_add)}\n'
            elif dict_[key].get('type') == 'deleted':
                value_del = dict_[key].get('value')
                if isinstance(value_del, dict):
                    value_del = stylish(value_del, spaces_count + 4)
                else:
                    value_del = type_of_value(value_del)
                result += f'{(spaces_count + 2) * " "}- {key}:' \
                          f' {type_of_value(value_del)}\n'
            elif dict_[key].get('type') == 'added':
                value_add = dict_[key].get('value')
                if isinstance(value_add, dict):
                    value_add = stylish(value_add, spaces_count + 4)
                else:
                    value_add = type_of_value(value_add)
                result += f'{(spaces_count + 2) * " "}+ {key}: {value_add}\n'
            else:
                result += f'{(spaces_count + 4) * " "}{key}: ' \
                          f'{stylish(dict_[key], spaces_count + 4)}\n'
        else:
            value = type_of_value(dict_[key])
            result += f'{(spaces_count + 4) * " "}{key}: {value}\n'
    result += ' ' * spaces_count + '}'
    return result
