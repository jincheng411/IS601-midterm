import logging
import os
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime
from app.calculation import Calculation

class History:
    # Load environment variables from .env file
    load_dotenv()
    file_path = os.getenv("CSV_FILE_PATH")
    history = pd.DataFrame(columns=["Datetime", "Number1", "Number2", "Operation", "Result"])

    @classmethod
    def load_history(cls):
        """Load history from a CSV file if it exists."""
        try:
            cls.history = pd.read_csv(cls.file_path, parse_dates=["Datetime"])
        except FileNotFoundError:
            logging.error("History file not found. Starting with an empty history.")
            print("History file not found. Starting with an empty history.")

    @classmethod
    def save_history(cls):
        """Save the current history to a CSV file."""
        cls.history.to_csv(cls.file_path, index=False)
        logging.info("save to csv")

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a Calculation instance to the history."""
        # Perform the calculation and get the result
        result = calculation.perform()

        # Create a new DataFrame row with all the details
        new_record = pd.DataFrame([{
            "Datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Number1": calculation.a,
            "Number2": calculation.b,
            "Operation": calculation.operation.__name__,
            "Result": result
        }])

        # Concatenate the new row to the history DataFrame
        if not new_record.isna().all(axis=None):
            # Concatenate the new row to the history DataFrame if it has valid data
            cls.history = pd.concat([cls.history, new_record], ignore_index=True)
            cls.save_history()
            logging.info("save to history list")
    @classmethod
    def get_history(cls) -> pd.DataFrame:
        """Return the entire calculation history."""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clear the history both in memory and in the CSV file."""
        cls.history = pd.DataFrame(columns=["Datetime", "Number1", "Number2", "Operation", "Result"])
        cls.save_history()

    @classmethod
    def print_history(cls):
        if cls.history.empty:
            return "No history to display."

        # Format the headers as CSV-like output
        output = "Datetime,Number1,Number2,Operation,Result\n"
        for _, row in cls.history.iterrows():
            output += f"{row['Datetime']},{row['Number1']},{row['Number2']},{row['Operation']},{row['Result']}\n"
        print(output.strip())
        return output.strip()

    @classmethod
    def get_last_record(cls):
        """Return the last calculation record."""
        if not cls.history.empty:
            return cls.history.iloc[-1]
        return None
