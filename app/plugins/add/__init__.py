from decimal import Decimal
import logging
from app.calculator import Calculator
from app.commands import Command

class AddCommand(Command):
    def execute(self, args: list):
        if len(args) != 2:
            print("Wrong number of arguments: add <num1> <num2>")
            return

        num1 = Decimal(args[0])
        num2 = Decimal(args[1])
        logging.info("Adding %s and %s", num1, num2)
        result = Calculator.add(num1, num2)
        print(f"{num1} + {num2} = {result}.")
