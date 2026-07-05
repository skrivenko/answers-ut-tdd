class StringCalculator:

    
    def add(self, input):
        if input == "":
            return "0"
        numbers = input.split(",")
        return str(sum(int(n) for n in numbers))