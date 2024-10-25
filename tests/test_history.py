
from decimal import Decimal
from unittest.mock import MagicMock, patch
from app.history import History
import pandas as pd
from app.plugins.clearHistory import ClearHistoryCommand
from app.plugins.loadHistory import LoadHistoryCommand



class TestLoadHistoryCommand:
    @patch.object(History, 'load_history', return_value=None)
    def test_execute_loads_history(self, mock_load):
        command = LoadHistoryCommand()
        command.execute([])  # No arguments needed for this command

        # Assert that the load_history method was called
        mock_load.assert_called_once()

    @patch.object(History, 'load_history', return_value=None)
    def test_execute_loads_history(self, mock_load):
        command = LoadHistoryCommand()
        command.execute([])  # No arguments needed for this command

        # Assert that the load_history method was called
        mock_load.assert_called_once()


    @patch.object(History, 'clear_history', return_value=None)
    def test_execute_clears_history(self, mock_clear):
        command = ClearHistoryCommand()
        command.execute([])  # No arguments needed for this command

        # Assert that the clear_history method was called
        mock_clear.assert_called_once()

    @patch.object(History, 'clear_history', return_value=None)
    def test_execute_clears_history_when_already_empty(self, mock_clear):
        # Assume clear_history is called when history is already empty
        command = ClearHistoryCommand()
        command.execute([])  # No arguments needed for this command

        # Assert that clear_history method was called even if it was already empty
        mock_clear.assert_called_once()

    def test_print_history_csv_format(self):
        # Set up sample history data
        sample_data = pd.DataFrame({
            'Datetime': ['2024-10-10 10:00:00'],
            'Number1': [Decimal('10')],
            'Number2': [Decimal('5')],
            'Operation': ['add'],
            'Result': [Decimal('15')]
        })
        History.history = sample_data

        # Expected CSV-like output
        expected_output = (
            "Datetime,Number1,Number2,Operation,Result\n"
            "2024-10-10 10:00:00,10,5,add,15"
        )

        # Assert output matches expected CSV format
        assert History.print_history() == expected_output
