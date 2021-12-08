#!/usr/bin/env python3

def stylish(dict_, spaces_count=0):  # noqa: <error code>
    result = '{\n'
    sorted_keys = sorted(dict_.keys(),
                         key=lambda x: x[2:] if x[:1] in ('+', '-') else x)
    for key in sorted_keys:
        if key[:2] in ('+ ', '- ', '  '):
            if isinstance(dict_[key], dict):
                result += f'{(spaces_count + 2) * " "}{key}: ' \
                          f'{stylish(dict_[key], spaces_count + 4)}\n'
            else:
                if dict_[key] is False:
                    result += f'{(spaces_count + 2) * " "}{key}: false\n'
                elif dict_[key] is True:
                    result += f'{(spaces_count + 2) * " "}{key}: true\n'
                elif dict_[key] is None:
                    result += f'{(spaces_count + 2) * " "}{key}: null\n'
                elif not dict_[key]:
                    result += f'{(spaces_count + 2) * " "}{key}:\n'
                else:
                    result += f'{(spaces_count + 2) * " "}{key}: {dict_[key]}\n'
        else:
            if isinstance(dict_[key], dict):
                result += f'{(spaces_count + 4) * " "}{key}: ' \
                          f'{stylish(dict_[key], spaces_count + 4)}\n'
            else:
                if dict_[key] is False:
                    result += f'{(spaces_count + 4) * " "}{key}: false\n'
                elif dict_[key] is True:
                    result += f'{(spaces_count + 4) * " "}{key}: true\n'
                elif dict_[key] is None:
                    result += f'{(spaces_count + 4) * " "}{key}: null\n'
                elif not dict_[key]:
                    result += f'{(spaces_count + 4) * " "}{key}:\n'
                else:
                    result += f'{(spaces_count + 4) * " "}{key}: {dict_[key]}\n'
    result += ' ' * spaces_count + '}'
    return result
