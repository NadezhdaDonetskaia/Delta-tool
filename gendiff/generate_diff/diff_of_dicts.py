#!/usr/bin/env python3


def diff_of_dicts(dict1, dict2):
    result = dict()
    all_keys = set(list(dict1.keys()) + list(dict2.keys()))
    for key in all_keys:
        # про уровни вложенности крутила всяко, не вижу, как можно сделать в один
        # по логике ключ в обоих словарях - значит другой иф на равность
        # можно сделать без второго вложенного иф, но проверки будут двойными и длинными
        # (типо, входит в один, но не входит в другой) - как-то это не красиво(((
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                result[key] = {
                    'value': dict1[key],
                    'type': 'unchanged',
                }
            elif isinstance(dict1[key], dict) \
                    and isinstance(dict2[key], dict):
                # на мой взгляд этот случай отличется:
                # если они не равны, то мы еще не знаем, где именно -> надо идти вглубь
                # зачем нам добавлять сюда ключи типа, если при распаковке мы всё равно будем идти ниже?
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
