class StringCalculator:

    
    def add(self, input):
        if input == "":
            return "0"
        numbers = self._parse_numbers(input)
        total_sum = sum(float(n) for n in numbers)
        return self._format_result(total_sum)

    
    def _parse_numbers(self, input):
        input = input.replace("\n", ",")
        return input.split(",")

    
    def _format_result(self, value):
        return f"{value:g}"