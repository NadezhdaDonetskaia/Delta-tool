#!/usr/bin/env python3
import os
import pytest
from gendiff import generate_diff


dirname = os.path.dirname(__file__)
first_json_file = os.path.join(dirname, 'fixtures/file1.json')
second_json_file = os.path.join(dirname, 'fixtures/file2.json')
first_yaml_file = os.path.join(dirname, 'fixtures/file1.yml')
second_yaml_file = os.path.join(dirname, 'fixtures/file2.yaml')
first_branching_file = os.path.join(dirname, 'fixtures/file1_branching.json')
second_branching_file = os.path.join(dirname, 'fixtures/file2_branching.json')
first_yaml_branching_file = os.path.join(dirname, 'fixtures/file1_branching.yaml')
second_yaml_branching_file = os.path.join(dirname, 'fixtures/file2_branching.yml')
parameters_mark = [
    (first_json_file, second_json_file, 'stylish', 'fixtures/answer_for_stylish_flat'),
    (first_yaml_file, second_yaml_file, 'stylish', 'fixtures/answer_for_stylish_flat'),
    (first_branching_file, second_branching_file, 'plain', 'fixtures/answer_for_plain_branching'),
    (first_branching_file, second_branching_file, 'stylish', 'fixtures/answer_for_stylish_branching'),
    (first_yaml_branching_file, second_yaml_branching_file, 'stylish', 'fixtures/answer_for_stylish_branching'),
]


@pytest.mark.parametrize(('first_file, second_file, format, answer'), parameters_mark)
def test_generate_diff_json(first_file, second_file, format, answer):
    answer = open(os.path.join(dirname, answer))
    assert generate_diff(first_file, second_file, format) == answer.read()


#  надо ли делать проверку на пустой файл? если да, то какие условия выхода пустого файла?
# empty_f1 = os.path.join(dirname, 'fixtures/empty_file1.json')
# empty_f2 = os.path.join(dirname, 'fixtures/empty_file2.json')
#
#
# def test_is_empty():
#     assert generate_diff(empty_f1, empty_f2) == '{\n}'

