
from decimal import Decimal
from unittest.mock import MagicMock, patch
from app.history import History
import pandas as pd
from app.plugins.clearHistory import ClearHistoryCommand
from app.plugins.deleteHistory import DeleteHistoryCommand
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


class TestDeleteHistoryCommand:
    def setup_method(self):
        # Set up sample history data for testing
        History.history = pd.DataFrame({
            'Datetime': ['2024-10-10 10:00:00', '2024-10-11 11:00:00'],
            'Number1': [Decimal('10'), Decimal('20')],
            'Number2': [Decimal('5'), Decimal('10')],
            'Operation': ['add', 'subtract'],
            'Result': [Decimal('15'), Decimal('10')]
        })

    def test_delete_valid_line(self, capsys):
        command = DeleteHistoryCommand()
        command.execute(["1"])

        # Capture and verify output
        captured = capsys.readouterr()
        assert "Deleted line 1 from history." in captured.out
        assert len(History.history) == 1
        assert History.history.iloc[0]['Result'] == Decimal('10')

    # def test_delete_invalid_line(self, capsys):
    #     command = DeleteHistoryCommand()
    #     command.execute(["5"])

    #     # Capture and verify output for invalid line number
    #     captured = capsys.readouterr()
    #     assert "Invalid line number." in captured.out
    #     assert len(History.history) == 2

    # def test_delete_non_integer_input(self, capsys):
    #     command = DeleteHistoryCommand()
    #     command.execute(["abc"])

    #     # Capture and verify output for non-integer input
    #     captured = capsys.readouterr()
    #     assert "Please provide a valid line number." in captured.out
    #     assert len(History.history) == 2