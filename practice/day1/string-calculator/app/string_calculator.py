class StringCalculator:

    def add(self, input: str) -> str:
        numbers = self._parse_numbers(input)
        if not numbers:
            return "0"
        result = self._sum_numbers(numbers)
        return self._format_result(result)

    def _parse_numbers(self, input: str) -> list[float]:
        if input == "":
            return []
        return [float(p) for p in input.split(",")]

    def _sum_numbers(self, numbers: list[float]) -> float:
        return sum(numbers)

    def _format_result(self, result: float) -> str:
        return f"{result:g}"
