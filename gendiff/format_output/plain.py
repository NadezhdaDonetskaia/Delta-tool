#!/usr/bin/env python3
import json

# change name
def type_of_value(value):
    if isinstance(value, (list, tuple, dict, set)):
        result_value = '[complex value]'
    elif isinstance(value, bool) or value is None:
        result_value = json.dumps(value)
    elif isinstance(value, str):
        result_value = f"'{value}'"
    else:
        result_value = value
    return result_value


def plain(dict_, path='', child=False):
    result = ''
    sorted_keys = sorted(dict_.keys())
    for key in sorted_keys:
        if dict_[key].get('type') == 'changed':
            value_del = type_of_value(dict_[key].get('value')[0])
            value_add = type_of_value(dict_[key].get('value')[1])
            result += f"Property '{path + key}' was updated. " \
                      f"From {value_del} to {value_add}\n"
        elif dict_[key].get('type') == 'deleted':
            result += f"Property '{path + key}' was removed\n"
        elif dict_[key].get('type') == 'added':
            value_add = type_of_value(dict_[key].get('value'))
            result += f"Property '{path + key}' " \
                      f"was added with value: {value_add}\n"
        elif dict_[key].get('type') == 'unchanged':
            if isinstance(dict_[key].get('value'), dict):
                result += plain(dict_[key].get('value'), path=path + f'{key}.', child=True)
        else:
            result += plain(dict_[key], path=path + f'{key}.', child=True)
    if not child:
        result = result[:-1]
    return result
