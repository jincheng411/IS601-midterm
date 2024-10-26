

import logging
import os

from dotenv import load_dotenv
from app.commands import Command
from app.history import History


class DeleteHistoryCommand(Command):
    def execute(self, args: list):
        if len(args) != 1:
            print("Usage: delete <line_number>")
            return
        History.load_history()
        try:
            line_number = int(args[0]) - 1  # Convert to zero-based index
            if line_number < 0 or line_number >= len(History.history):
                print("Invalid line number.")
                print(line_number)
                logging.warning(f"Invalid line number {line_number}")
                return

            # Drop the specified row and reset the index
            History.history = History.history.drop(History.history.index[line_number]).reset_index(drop=True)
            # Save updated history to CSV
            load_dotenv()
            History.history.to_csv(os.path.abspath(os.getenv("CSV_FILE_PATH")), index=False)
            logging.info(f"Deleted line {line_number + 1} from history.")
            print(f"Deleted line {line_number + 1} from history.")

        except ValueError:
            print("Please provide a valid line number.")
            logging.error("Invalid input")
