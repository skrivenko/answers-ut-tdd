import pytest
from app.string_calculator import StringCalculator


@pytest.mark.parametrize("input,expected,description", [
    ("", "0", "empty_string_returns_zero"),
    ("1", "1", "single_number_returns_itself"),
    ("1,2", "3", "two_numbers_return_sum"),
    ("1.1,2.2,3.3", "6.6", "three_float_numbers_return_sum"),
], ids=["empty_string_returns_zero", "single_number_returns_itself", "two_numbers_return_sum", "three_float_numbers_return_sum"])
def test_string_calculator_add(input, expected, description):
    calculator = StringCalculator()
    result = calculator.add(input)
    assert result == expected, description
