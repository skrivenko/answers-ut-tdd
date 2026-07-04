import pytest
from string_calculator import add


def test_add_empty_string_returns_zero():
    assert add("") == "0"


def test_add_single_number_returns_same_number():
    assert add("1") == "1"


def test_add_two_numbers_returns_sum():
    assert add("1.1,2.2") == "3.3"


def test_add_newline_as_separator():
    assert add("1\n2,3") == "6"
