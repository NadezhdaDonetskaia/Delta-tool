#!/usr/bin/env python3
import json


def transform_value(value):
    if isinstance(value, bool) or value is None:
        result = json.dumps(value)
    else:
        result = value
    return result


def formation_value(value, spaces):
    if not isinstance(value, dict):
        return transform_value(value)
    keys_ = sorted(value.keys())
    result_value = '{\n'
    for key in keys_:
        val = formation_value(value[key], spaces + 4)
        result_value += f'{" " * (spaces + 4)}{key}: {val}\n'
    result_value += " " * spaces + '}'
    return result_value


def transform_key(type, key):
    if type == 'unchanged':
        return '  ' + str(key)
    elif type == 'changed':
        return '- ' + str(key), '+ ' + str(key)
    elif type == 'deleted':
        return '- ' + str(key)
    else:
        return '+ ' + str(key)


def stylish(dict_, spaces=0):
    result = '{\n'
    sorted_keys = sorted(dict_.keys())
    for key in sorted_keys:
        if not isinstance(dict_[key], dict):
            value = transform_value(dict_[key])
            result += f'{" " * (spaces + 4)}{key}: {value}\n'
        elif dict_[key].get('type') == 'nested':
            val = stylish(dict_[key].get('value'), spaces + 4)
            key = transform_key('unchanged', key)
            result += f'{" " * (spaces + 2)}{key}: {val}\n'
        elif dict_[key].get('type') == 'changed':
            val_del, val_add = dict_[key].get("value")
            val_del = formation_value(val_del, spaces + 4)
            val_add = formation_value(val_add, spaces + 4)
            key_del, key_add = transform_key(dict_[key].get('type'), key)
            result += f'{" " * (spaces + 2)}{key_del}: ' \
                      f'{val_del}\n'
            result += f'{" " * (spaces + 2)}{key_add}: ' \
                      f'{val_add}\n'
        else:
            value = dict_[key].get('value')
            value = formation_value(value, spaces + 4)
            key = transform_key(dict_[key].get('type'), key)
            result += f'{" " * (spaces + 2)}{key}: {value}\n'
    result += " " * spaces + '}'
    return result
