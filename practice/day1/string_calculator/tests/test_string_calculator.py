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


def test_add_invalid_newline_position_raises_error():
    calculator = StringCalculator()
    import pytest
    with pytest.raises(ValueError) as exc_info:
        calculator.add("175.2,\n35")
    assert str(exc_info.value) == r"Ожидается число, но в позиции 6 найдено '\n'"
