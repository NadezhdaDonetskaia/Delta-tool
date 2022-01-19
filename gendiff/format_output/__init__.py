from .stylish import stylish
from .plain import plain
from .json import json


def formatting(val, format):
    if format == 'stylish':
        return stylish(val)
    elif format == 'plain':
        return plain(val)
    elif format == 'json':
        return json(val)
