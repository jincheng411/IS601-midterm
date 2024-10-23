from app.commands import CommandHandler
from app.commands.add import AddCommand
from app.commands.divide import DivideCommand
from app.commands.exit import ExitCommand
from app.commands.multiply import MultiplyCommand
from app.commands.subtract import SubtractCommand

class App():
    def __init__(self):
        self.command_handler = CommandHandler()

    def start(self):
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("substract", SubtractCommand())
        self.command_handler.register_command("divide", DivideCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        print("Welcome to the calculator, type 'exit' to stop.")
        while True:
            user_input = input(">>> ").strip()
            self.command_handler.execute_command(user_input)

