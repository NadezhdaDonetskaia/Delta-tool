#!/usr/bin/env python3


def diff_of_dicts(dict1, dict2):
    result = dict()
    all_keys = set(list(dict1.keys()) + list(dict2.keys()))
    for key in all_keys:
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                result[key] = {
                    'value': dict1[key],
                    'type': 'unchanged',
                }
            elif isinstance(dict1[key], dict) \
                    and isinstance(dict2[key], dict):
                result[key] = diff_of_dicts(dict1[key], dict2[key])
            else:
                result[key] = {
                    'value': (dict1[key], dict2[key]),
                    'type': 'changed',
                }
        elif key in dict1:
            result[key] = {
                'value': dict1[key],
                'type': 'deleted',
            }
        else:
            result[key] = {
                'value': dict2[key],
                'type': 'added',
            }
    return result
