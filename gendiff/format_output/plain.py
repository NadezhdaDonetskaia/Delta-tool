#!/usr/bin/env python3


def type_of_value(value):
    if isinstance(value, (list, tuple, dict, set)):
        result_value = '[complex value]'
    elif isinstance(value, bool):
        if value is True:
            result_value = 'true'
        else:
            result_value = 'false'
    elif value is None:
        result_value = 'null'
    elif isinstance(value, str):
        result_value = f"'{value}'"
    else:
        result_value = value
    return result_value


def plain(dict_, path='', child=False):  # noqa: <error code>
    result = ''
    sorted_keys = sorted(dict_.keys())
    for key in sorted_keys:
        if isinstance(dict_[key], dict):
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
                    result += plain(dict_[key].get('value'), path=path + f'{key}.', child=True)  # noqa: <error code>
            else:
                result += plain(dict_[key], path=path + f'{key}.', child=True)
    if not child:
        result = result[:-1]
    return result
