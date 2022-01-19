import json as js


def json(dict_differences):
    return js.dumps(dict_differences, sort_keys=True, indent=2)
