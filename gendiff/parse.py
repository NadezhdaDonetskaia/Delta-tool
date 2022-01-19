import json
import yaml


def parse(extension: str, open_file: str) -> dict:
    if extension == '.json':
        return json.loads(open_file)
    if extension in ('.yaml', '.yml'):
        return yaml.safe_load(open_file)
