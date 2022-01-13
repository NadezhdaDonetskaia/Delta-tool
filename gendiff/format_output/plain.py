#!/usr/bin/env python3
import json


def stringify(value):
    if isinstance(value, (list, tuple, dict, set)):
        result_value = '[complex value]'
    elif isinstance(value, bool) or value is None:
        result_value = json.dumps(value)
    elif isinstance(value, str):
        result_value = f"'{value}'"
    else:
        result_value = value
    return result_value


def get_report_diff(path, type):
    report = f"Property '{path}' was "
    if type == 'changed':
        report += 'updated. '
    elif type == 'deleted':
        report += 'removed\n'
    elif type == 'added':
        report += 'added with value: '
    return report


def plain_deep(dict_level, path='', child=False):  # noqa: C901
    result = ''
    sorted_keys = sorted(dict_level.keys())
    for key in sorted_keys:
        type = dict_level[key].get('type')
        if type == 'unchanged':
            continue
        if dict_level[key].get('type') == 'nested':
            new_value = dict_level[key].get('value')
            result += plain_deep(new_value, path=f'{path + key}.', child=True)
            continue
        result += get_report_diff(f'{path + key}', type)
        if type == 'changed':
            value_del, value_add = dict_level[key].get('value')
            value_del = stringify(value_del)
            value_add = stringify(value_add)
            result += f'From {value_del} to {value_add}\n'
        elif type == 'added':
            value_add = stringify(dict_level[key].get('value'))
            result += f'{value_add}\n'
    if not child:
        result = result[:-1]
    return result


def plain(dict_):
    return plain_deep(dict_, path='')
