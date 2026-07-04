import pytest

from app.string_calculator import *


def test_add_empty_string_returns_zero():
    calculator = StringCalculator()
    result = calculator.add("")
    assert result == "0"


def test_add_single_number_returns_same_number():
    calculator = StringCalculator()
    result = calculator.add("1")
    assert result == "1"


def test_add_two_numbers_returns_sum():
    calculator = StringCalculator()
    result = calculator.add("1.1,2.2")
    assert result== "3.3"