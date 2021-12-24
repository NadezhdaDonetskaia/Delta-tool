from .stylish import stylish
from .plain import plain
from .output_to_json import output_to_json


def formatting(val, format):
    if format == 'stylish':
        return stylish(val)
    elif format == 'plain':
        return plain(val)
    elif format == 'json':
        return output_to_json(val)
