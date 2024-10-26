
import logging
from app.commands import Command
from app.history import History

class ClearHistoryCommand(Command):
    def execute(self, args: list):
        """Clear the history in memory and from the CSV file."""
        History.clear_history()
        logging.warning("History cleared.")
        print("History cleared.")
