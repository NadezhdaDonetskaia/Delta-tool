#!/usr/bin/env python3
import json


def convert_to_json(dict_differences):
    return json.dumps(dict_differences, sort_keys=True, indent=2)
