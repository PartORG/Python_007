import pytest

import Utils.utils as utils


def test_random_name_file_length():
    assert len(utils.generate_random_name()) == 20


def test_random_name_format():
    assert utils.generate_random_name().split('.')[1] == 'txt'


def test_random_name_len():
    assert len(utils.generate_random_name().split('.')[0]) == 16
