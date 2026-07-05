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


@pytest.mark.parametrize("input,expected_error,description", [
    ("175.2,\n35", r"Ожидается число, но в позиции 6 найдено '\n'", "newline right after comma"),
    ("1,2\n,3", r"Ожидается число, но в позиции 4 найдено ','", "comma right after newline"),
])
def test_string_calculator_add_raises_error(input, expected_error, description):
    calculator = StringCalculator()
    with pytest.raises(ValueError) as exc_info:
        calculator.add(input)
    assert str(exc_info.value) == expected_error, description
