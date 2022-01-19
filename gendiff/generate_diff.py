from pathlib import Path
from .format_output import formatting
from .get_difference_representation import get_difference_representation
from .parse import parse


def read_file(file_path):
    with open(file_path) as f:
        file_val = f.read()
    return file_val


def generate_diff(first_path: str, second_path: str, format='stylish') -> str:
    first_file_data = parse(Path(first_path).suffix, read_file(first_path))
    second_file_data = parse(Path(second_path).suffix, read_file(second_path))
    if not isinstance(first_file_data, dict) \
            or not isinstance(second_file_data, dict):
        raise ValueError("File don't be empty!")
    diff = get_difference_representation(first_file_data, second_file_data)
    return formatting(diff, format)
