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
    normalized = input.replace("\n", ",")
    return [float(p) for p in normalized.split(",")]


def _sum_numbers(numbers: list[float]) -> float:
    return sum(numbers)


def _format_result(result: float) -> str:
    return f"{result:g}"
