import logging
import sys
from app.commands import Command

class ExitCommand(Command):
    def execute(self, args):
        print("Have a nice day!")
        logging.info("exit the program")
        sys.exit()