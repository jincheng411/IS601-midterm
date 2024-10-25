import pandas as pd
from decimal import Decimal
from datetime import datetime
from typing import Callable

from app.calculation import Calculation

class History:
    file_path = 'calculations.csv'
    history = pd.DataFrame(columns=["Datetime", "Number1", "Number2", "Operation", "Result"])

    @classmethod
    def load_history(cls):
        """Load history from a CSV file if it exists."""
        try:
            cls.history = pd.read_csv(cls.file_path, parse_dates=["Datetime"])
        except FileNotFoundError:
            cls.history = pd.DataFrame(columns=["Datetime", "Number1", "Number2", "Operation", "Result"])

    @classmethod
    def save_history(cls):
        """Save the current history to a CSV file."""
        cls.history.to_csv(cls.file_path, index=False)

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a Calculation instance to the history."""
        # Perform the calculation and get the result
        result = calculation.perform()

        # Create a new DataFrame row with all the details
        new_record = pd.DataFrame([{
            "Datetime": datetime.now(),
            "Number1": calculation.a,
            "Number2": calculation.b,
            "Operation": calculation.operation.__name__,
            "Result": result
        }])

        # Concatenate the new row to the history DataFrame
        cls.history = pd.concat([cls.history, new_record], ignore_index=True)
        cls.save_history()

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
        """Return a formatted string of the history."""
        output = ""
        for index, row in cls.history.iterrows():
            output += f"{index + 1}. [{row['Datetime']}] {row['Number1']} {row['Operation']} {row['Number2']} = {row['Result']}\n"
        return output.strip()

    @classmethod
    def get_last_record(cls):
        """Return the last calculation record."""
        if not cls.history.empty:
            return cls.history.iloc[-1]
        return None
