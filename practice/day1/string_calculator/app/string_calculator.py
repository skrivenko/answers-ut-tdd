class StringCalculator:

    
    def add(self, input):
        if input == "":
            return "0"
        numbers = input.split(",")
        total = sum(float(n) for n in numbers)
        return f"{total:g}"