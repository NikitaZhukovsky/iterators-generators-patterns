class Calculator:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate(self, first_number, second_number):
        if self.strategy:
            return self.strategy.execute(first_number, second_number)
        else:
            raise ValueError("Такой стратегии нет!")


class Addition:
    @staticmethod
    def execute(first_number, second_number):
        if isinstance(first_number, (int, float)) and isinstance(second_number, (int, float)):
            return first_number * second_number
        else:
            print("Неверный ввод")


class Subtraction:
    @staticmethod
    def execute(first_number, second_number):
        if isinstance(first_number, (int, float)) and isinstance(second_number, (int, float)):
            return first_number * second_number
        else:
            print("Неверный ввод")


class Multiplication:
    @staticmethod
    def execute(first_number, second_number):
        if isinstance(first_number, (int, float)) and isinstance(second_number, (int, float)):
            return first_number * second_number
        else:
            print("Неверный ввод")


class Division:
    @staticmethod
    def execute(first_number, second_number):
        if isinstance(first_number, (int, float)) and isinstance(second_number, (int, float)):
            if second_number != 0:
                return first_number / second_number
            else:
                raise ZeroDivisionError("Деление на 0!")
        else:
            print("Неверный ввод")


calculator = Calculator()

calculator.set_strategy(Addition())
result = calculator.calculate(5, 3)
print(f"Сумма чисел: {result}")


calculator.set_strategy(Subtraction())
result = calculator.calculate(10, 4)
print(f"Разность чисел: {result}")


calculator.set_strategy(Multiplication())
result = calculator.calculate(7, 2)
print(f"Произведение чисел: {result}")


calculator.set_strategy(Division())
result = calculator.calculate(15, 3)
print(f"Частное чисел: {result}")
