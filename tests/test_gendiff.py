#!/usr/bin/env python3
import os
from gendiff import generate_diff


dirname = os.path.dirname(__file__)
first_json_file = os.path.join(dirname, 'fixtures/file1.json')
second_json_file = os.path.join(dirname, 'fixtures/file2.json')


def test_generate_diff_json():
    answer = open(os.path.join(dirname, 'fixtures/answer'))
    assert generate_diff(first_json_file, second_json_file) == answer.read()


first_yaml_file = os.path.join(dirname, 'fixtures/file1.yml')
second_yaml_file = os.path.join(dirname, 'fixtures/file2.yaml')


def test_generate_diff_yaml():
    answer = open(os.path.join(dirname, 'fixtures/answer'))
    assert generate_diff(first_yaml_file, second_yaml_file) == answer.read()
