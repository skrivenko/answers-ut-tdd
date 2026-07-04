class StringCalculator:
    pass


def add(number: str) -> str:
    numbers = _parse_numbers(number)
    if not numbers:
        return "0"
    result = _sum_numbers(numbers)
    return f"{result:g}"


def _parse_numbers(number: str) -> list[float]:
    if number == "":
        return []
    return [float(p) for p in number.split(",")]


def _sum_numbers(numbers: list[float]) -> float:
    return sum(numbers)

