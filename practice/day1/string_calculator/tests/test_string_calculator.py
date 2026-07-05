import pytest
from app.string_calculator import StringCalculator


@pytest.mark.parametrize("input,expected,description", [
    ("", "0", "empty string returns zero"),
    ("1", "1", "single number returns itself"),
    ("1,2", "3", "two numbers return sum"),
    ("1.1,2.2,3.3", "6.6", "three float numbers return sum"),
    ("1\n2,3", "6", "newline and comma delimiters"),
])
def test_string_calculator_add(input, expected, description):
    calculator = StringCalculator()
    result = calculator.add(input)
    assert result == expected, description
