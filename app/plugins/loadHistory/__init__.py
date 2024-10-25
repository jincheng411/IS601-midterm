
from app.commands import Command
from app.history import History

class LoadHistoryCommand(Command):
    def execute(self, args: list):
        """Load history from the CSV file and print a confirmation."""
        History.load_history()
        History.print_history()
