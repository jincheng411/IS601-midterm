from datetime import datetime
from decimal import Decimal
from unittest.mock import MagicMock, patch
from app.calculation import Calculation
from app.history import History
from app.plugins.clearHistory import ClearHistoryCommand
from app.plugins.loadHistory import LoadHistoryCommand



class TestLoadHistoryCommand:
    @patch.object(History, 'load_history', return_value=None)
    def test_execute_loads_history(self, mock_load):
        command = LoadHistoryCommand()
        command.execute([])  # No arguments needed for this command

        # Assert that the load_history method was called
        mock_load.assert_called_once()


    @patch.object(History, 'history', new_callable=MagicMock)
    def test_print_history_empty(self, mock_history):
        # Test the output when history is empty
        mock_history.return_value = MagicMock()
        mock_history.return_value.empty = True

        output = History.print_history()

        # Check if the output is as expected
        assert output == ""

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
