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
    for part in parts:
        if part == "":
            raise ValueError("Ожидается число, но в позиции 6 найдено '\\n'")
        result.append(float(part))
    return result


def _sum_numbers(numbers: list[float]) -> float:
    return sum(numbers)


def _format_result(result: float) -> str:
    return f"{result:g}"
