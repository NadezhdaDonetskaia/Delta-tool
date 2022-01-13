#!/usr/bin/env python3


def get_difference_representation(dict1, dict2):
    result = dict()
    all_keys = set(list(dict1.keys()) + list(dict2.keys()))
    for key in all_keys:
        if key not in dict2:
            result[key] = {
                'value': dict1[key],
                'type': 'deleted',
            }
        elif key not in dict1:
            result[key] = {
                'value': dict2[key],
                'type': 'added',
            }
        elif dict1[key] == dict2[key]:
            result[key] = {
                'value': dict1[key],
                'type': 'unchanged',
            }
        elif isinstance(dict1[key], dict) \
                and isinstance(dict2[key], dict):
            result[key] = {
                'value': get_difference_representation(dict1[key], dict2[key]),
                'type': 'nested',
            }
        else:
            result[key] = {
                'value': (dict1[key], dict2[key]),
                'type': 'changed',
            }
    return result
