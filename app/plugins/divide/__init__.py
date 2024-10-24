from decimal import Decimal
from app.calculator import Calculator
from app.commands import Command


class DivideCommand(Command):
        def execute(self, args: list):
            if len(args) != 2:
                print("Wrong number of arguments: divide <num1> <num2>")
                return
            try:
                num1 = Decimal(args[0])
                num2 = Decimal(args[1])
                result = Calculator.division(num1, num2)
                print(f"{num1} / {num2} = {result}.")
            except ZeroDivisionError:
                print("Error: Division by zero.")
