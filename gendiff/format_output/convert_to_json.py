#!/usr/bin/env python3
import json


def convert_to_json(value):
    return json.dumps(value, sort_keys=True, indent=2)
