#!/usr/bin/env python3

def plain(dict_, path=''):
    result = ''
    sorted_keys = sorted(dict_.keys(),
                         key=lambda x: x[2:] if x[:1] in ('+', '-') else x)
    for key in sorted_keys:
        if key[:1] == '+':
            pass
        elif key[:1] == '-':
            pass
        else:
            pass
    return result
