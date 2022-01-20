import json
import yaml


def parse(data: str, format: str) -> dict:
    if data == '.json':
        return json.loads(format)
    if data in ('.yaml', '.yml'):
        return yaml.safe_load(format)
