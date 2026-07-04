import pytest

from app.string_calculator import *

def test_add_empty_string_returns_zero():
    calculator = StringCalculator()
    result = calculator.add("")
    assert result == "0"