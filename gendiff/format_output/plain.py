#!/usr/bin/env python3
import json


def transform_value(value):
    if isinstance(value, (list, tuple, dict, set)):
        result_value = '[complex value]'
    elif isinstance(value, bool) or value is None:
        result_value = json.dumps(value)
    elif isinstance(value, str):
        result_value = f"'{value}'"
    else:
        result_value = value
    return result_value


def formation_answer(path, type):
    answer = f"Property '{path}' was "
    if type == 'changed':
        answer += 'updated. '
    elif type == 'deleted':
        answer += 'removed\n'
    elif type == 'added':
        answer += 'added with value: '
    return answer


def plain(dict_, path='', child=False):  # noqa: C901
    result = ''
    sorted_keys = sorted(dict_.keys())
    for key in sorted_keys:
        type = dict_[key].get('type')
        if type == 'unchanged':
            continue
        if dict_[key].get('type') == 'nested':
            new_value = dict_[key].get('value')
            result += plain(new_value, path=f'{path + key}.', child=True)
            continue
        result += formation_answer(f'{path + key}', type)
        if type == 'changed':
            value_del, value_add = dict_[key].get('value')
            value_del = transform_value(value_del)
            value_add = transform_value(value_add)
            result += f'From {value_del} to {value_add}\n'
        elif type == 'added':
            value_add = transform_value(dict_[key].get('value'))
            result += f'{value_add}\n'
    if not child:
        result = result[:-1]
    return result
