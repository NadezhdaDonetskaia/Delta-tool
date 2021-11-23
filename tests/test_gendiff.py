#!/usr/bin/env python3
import os
from pathlib import Path
from gendiff import generate_diff


dirname = os.path.dirname(__file__)
first_file = os.path.join(dirname, 'fixtures/file1.json')
second_file = os.path.join(dirname, 'fixtures/file2.json')
print(first_file)


def test_generate_diff():
    answer = open(os.path.join(dirname, 'fixtures/answer_true'))
    assert generate_diff(first_file, second_file) == answer.read()
