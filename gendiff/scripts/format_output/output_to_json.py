#!/usr/bin/env python3

def type_of_value(value):
    if value is False:
        result = 'false'
    elif value is True:
        result = 'true'
    elif value is None:
        result = 'null'
    elif not value:
        result = None
    else:
        result = f'"{value}"'
    return result


def output_to_json(dict_, spaces_count=0):  # noqa: <error code>
    result = '{\n'
    sorted_keys = sorted(dict_.keys(),
                         key=lambda x: x[2:] if x[:1] in ('+', '-') else x)
    for key in sorted_keys:
        if key[:2] in ('+ ', '- '):
            if key[:1] == '+':
                pref = '+ '
            else:
                pref = '- '
            if isinstance(dict_[key], dict):
                result += f'{(spaces_count) * " "}{pref}"{key[2:]}": ' \
                          f'{output_to_json(dict_[key], spaces_count + 2)}\n'
            else:
                value = type_of_value(dict_[key])
                if value:
                    result += f'{(spaces_count) * " "}{pref}"{key[2:]}": ' \
                              f'{value},\n'
                else:
                    result += f'{(spaces_count) * " "}{pref}"{key[2:]}":\n'

        else:
            if isinstance(dict_[key], dict):
                result += f'{(spaces_count + 2) * " "}"{key}": ' \
                          f'{output_to_json(dict_[key], spaces_count + 2)}\n'
            else:
                value = type_of_value(dict_[key])
                if value:
                    result += f'{(spaces_count + 2) * " "}"{key}": {value},\n'
                else:
                    result += f'{(spaces_count + 2) * " "}"{key}":\n'
    result += ' ' * spaces_count + '}'
    return result
