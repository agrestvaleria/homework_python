from func import CalculatorMethods


class Calculator(CalculatorMethods):

    @staticmethod
    def validation(x, y):
        assert all(isinstance(number, int) for number in (x, y)), \
            "x or y must be int"
        return True

    def sum(self, x, y):
        self.validation(x, y)
        result = x + y
        print(f"The result is {result}")

    def deduction(self, x, y):
        self.validation(x, y)
        result = x - y
        print(f"The result is {result}")

    def multiplication(self, x, y):
        self.validation(x, y)
        result = x * y
        print(f"The result is {result}")

    def division(self, x, y):
        assert y != 0, 'y must not be 0'
        self.validation(x, y)
        result = x / y
        print(f"The result is {result}")


calculator = Calculator()
calculator.sum(2, 3)
calculator.deduction(4, 4)
calculator.multiplication(0, 5)
calculator.division(5, 0)
