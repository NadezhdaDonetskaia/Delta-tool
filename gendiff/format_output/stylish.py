#!/usr/bin/env python3
import json

# change name
def type_of_value(value):
    if isinstance(value, bool) or value is None:
        result = json.dumps(value)
    else:
        result = value
    return result


def stylish(dict_, spaces_count=0):
    result = '{\n'
    sorted_keys = sorted(dict_.keys())
    for key in sorted_keys:
        if not isinstance(dict_[key], dict):
            value = type_of_value(dict_[key])
            result += f'{(spaces_count + 4) * " "}{key}: {value}\n'
        elif dict_[key].get('type') == 'unchanged':
            value = type_of_value(dict_[key].get("value"))
            result += f'{(spaces_count + 4) * " "}{key}: {value}\n'
        elif dict_[key].get('type') == 'changed':
            value_del = dict_[key].get('value')[0]
            value_add = dict_[key].get('value')[1]
            result += f'{(spaces_count + 2) * " "}- {key}: ' \
                          f'{type_of_value(value_del)}\n'
            result += f'{(spaces_count + 2) * " "}+ {key}: ' \
                          f'{type_of_value(value_add)}\n'
        elif dict_[key].get('type') == 'deleted':
            value_del = dict_[key].get('value')
            value_del = type_of_value(value_del)
            result += f'{(spaces_count + 2) * " "}- {key}:' \
                          f' {type_of_value(value_del)}\n'
        elif dict_[key].get('type') == 'added':
            value_add = dict_[key].get('value')
            result += f'{(spaces_count + 2) * " "}+ {key}: {value_add}\n'
        else:
            result += f'{(spaces_count + 4) * " "}{key}: ' \
                          f'{stylish(dict_[key], spaces_count + 4)}\n'
    result += ' ' * spaces_count + '}'
    return result
