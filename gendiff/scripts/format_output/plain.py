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
    else:
        result_value = f"'{value}'"
    return result_value


def plain(dict_, path=''):
    result = ''
    sorted_keys = sorted(dict_.keys(),
                         key=lambda x: x[2:] if x[:1] in ('+', '-') else x)
    for key in sorted_keys:
        if key[:1] == '-' and f'+{key[1:]}' in dict_:
            value1 = type_of_value(dict_[key])
            value2 = type_of_value(dict_[f'+{key[1:]}'])
            result += f"Property '{path + key[2:]}' was updated. From {value1} to {value2}\n"
        elif key[:1] == '-':
            result += f"Property '{path + key[2:]}' was removed\n"
        elif key[:1] == '+' and f'-{key[1:]}' not in dict_:
            value = type_of_value(dict_[key])
            result += f"Property '{path + key[2:]}' was added with value: {value}\n"
        else:
            if isinstance(dict_[key], dict):
                result += plain(dict_[key], path=path+f'{key}.')
    return result
