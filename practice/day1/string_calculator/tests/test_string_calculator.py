from app.string_calculator import StringCalculator


def test_add_empty_string_returns_zero():
    calculator = StringCalculator()
    result = calculator.add("")
    assert result == "0"


def test_add_single_number_returns_itself():
    calculator = StringCalculator()
    result = calculator.add("1")
    assert result == "1"