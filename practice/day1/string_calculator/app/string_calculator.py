class StringCalculator:
    pass


def add(input: str) -> str:
    numbers = _parse_numbers(input)
    if not numbers:
        return "0"
    result = _sum_numbers(numbers)
    return _format_result(result)


def _parse_numbers(input: str) -> list[float]:
    if input == "":
        return []
    parts = input.replace("\n", ",").split(",")
    return _convert_parts_to_numbers(input, parts)


def _convert_parts_to_numbers(input: str, parts: list[str]) -> list[float]:
    result = []
    pos = 0
    for part in parts:
        _validate_part(input, part, pos)
        result.append(float(part))
        pos += len(part) + 1
    return result


def _validate_part(input: str, part: str, pos: int) -> None:
    if part == "":
        if pos >= len(input):
            raise ValueError("Ожидается число, но найдено EOF")
        char = _get_char_at_position(input, pos)
        raise ValueError(f"Ожидается число, но в позиции {pos} найдено '{char}'")


def _get_char_at_position(input: str, pos: int) -> str:
    if pos < len(input):
        ch = input[pos]
        return "\\n" if ch == "\n" else ch
    return "\\n"


def _sum_numbers(numbers: list[float]) -> float:
    return sum(numbers)


def _format_result(result: float) -> str:
    return f"{result:g}"
