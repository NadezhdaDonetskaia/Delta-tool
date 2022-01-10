from .stylish import stylish
from .plain import plain
from .convert_to_json import convert_to_json


def formatting(val, format):
    if format == 'stylish':
        return stylish(val)
    elif format == 'plain':
        return plain(val)
    elif format == 'json':
        return convert_to_json(val)
