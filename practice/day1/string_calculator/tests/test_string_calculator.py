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


def test_add_invalid_format_raises_error():
    with pytest.raises(ValueError) as exc_info:
        add("175.2,\n35")
    assert "Ожидается число, но в позиции 6 найдено '\\n'" in str(exc_info.value)


def test_add_invalid_separator_at_different_position():
    with pytest.raises(ValueError) as exc_info:
        add("1,2,,3")
    assert "Ожидается число, но в позиции 4 найдено ','" in str(exc_info.value)


def test_add_trailing_separator_raises_eof_error():
    with pytest.raises(ValueError) as exc_info:
        add("1,3,")
    assert "Ожидается число, но найдено EOF" in str(exc_info.value)
