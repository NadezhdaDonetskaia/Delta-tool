#!/usr/bin/env python3

def type_of_value(value):
    if value is False:
        result = 'false'
    elif value is True:
        result = 'true'
    elif not value:
        result = 'null'
    else:
        result = f'"{value}"'
    return result


def output_to_json(dict_, spaces_count=0):  # noqa: <error code>
    # нужна ли проверка на пустое значение?
    # if not dict_:
    #     return {}
    result = '{\n'
    sorted_keys = sorted(dict_.keys(),
                         key=lambda x: x[2:] if x[:1] in ('+', '-') else x)
    for key in sorted_keys:
        if key[:2] in ('+ ', '- '):
            if isinstance(dict_[key], dict):
                result += f'{(spaces_count) * " "}"{key}": ' \
                          f'{output_to_json(dict_[key], spaces_count + 2)},\n'
            else:
                value = type_of_value(dict_[key])
                result += f'{(spaces_count) * " "}"{key}": {value},\n'
        else:
            if isinstance(dict_[key], dict):
                result += f'{(spaces_count + 2) * " "}"{key}": ' \
                          f'{output_to_json(dict_[key], spaces_count + 2)},\n'
            else:
                value = type_of_value(dict_[key])
                result += f'{(spaces_count + 2) * " "}"{key}": {value},\n'
    result = result[:-2] + '\n'
    result += ' ' * spaces_count + '}'
    return result
