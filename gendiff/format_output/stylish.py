#!/usr/bin/env python3
import json


def transform_value(value):
    if isinstance(value, bool) or value is None:
        result = json.dumps(value)
    else:
        result = value
    return result


def formation_value(value, deep):
    if not isinstance(value, dict):
        return transform_value(value)
    keys_ = sorted(value.keys())
    result_value = '{\n'
    for key in keys_:
        val = formation_value(value[key], deep + 1)
        result_value += f'{" " * (deep * 4)}{key}: {val}\n'
    result_value += " " * (deep - 1) * 4 + '}'
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


def stylish_deep(dict_level, deep):
    result = '{\n'
    sorted_keys = sorted(dict_level.keys())
    for key in sorted_keys:
        if not isinstance(dict_level[key], dict):
            value = transform_value(dict_level[key])
            result += f'{" " * (deep * 4)}{key}: {value}\n'
        elif dict_level[key].get('type') == 'nested':
            val = stylish_deep(dict_level[key].get('value'), deep + 1)
            key = transform_key('unchanged', key)
            result += f'{" " * (deep * 4 - 2)}{key}: {val}\n'
        elif dict_level[key].get('type') == 'changed':
            val_del, val_add = dict_level[key].get("value")
            val_del = formation_value(val_del, deep + 1)
            val_add = formation_value(val_add, deep + 1)
            key_del, key_add = transform_key(dict_level[key].get('type'), key)
            result += f'{" " * (deep * 4 - 2)}{key_del}: ' \
                      f'{val_del}\n'
            result += f'{" " * (deep * 4 - 2)}{key_add}: ' \
                      f'{val_add}\n'
        else:
            value = dict_level[key].get('value')
            value = formation_value(value, deep + 1)
            key = transform_key(dict_level[key].get('type'), key)
            result += f'{" " * (deep * 4 - 2)}{key}: {value}\n'
    result += " " * (deep - 1) * 4 + '}'
    return result


def stylish(dict_):
    return stylish_deep(dict_, 1)
