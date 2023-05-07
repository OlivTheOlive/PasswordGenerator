
class PositiveNumberConstructor:
    def __init__(self, input_num):
        if not isinstance(input_num, (int, float)):
            raise TypeError("Input must be a number")
        elif input_num <= 0:
            raise ValueError("Input must be a positive number")
        else:
            self.input_num = input_num

