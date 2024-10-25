'''test cases for commands'''

import pytest

from app.commands import CommandHandler
from app.plugins.add import AddCommand
from app.plugins.divide import DivideCommand
from app.plugins.menu import MenuCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.subtract import SubtractCommand

@pytest.fixture
def command_handler():
    handler = CommandHandler()
    handler.register_command('add', AddCommand())
    handler.register_command('subtract', SubtractCommand())
    handler.register_command('multiply', MultiplyCommand())
    handler.register_command('divide', DivideCommand())
    handler.register_command('menu', MenuCommand())
    return handler

def test_add_command_output(capsys, command_handler):
    """Test AddCommand with valid input."""
    command_handler.execute_command('add 5 3')
    captured = capsys.readouterr()
    assert "5 + 3 = 8.\n" in captured.out

def test_add_command_missing_arguments(capsys, command_handler):
    """Test AddCommand with invalid number of arguments."""
    command_handler.execute_command('add 2')
    captured = capsys.readouterr()
    assert "Wrong number of arguments: add <num1> <num2>\n" in captured.out

# def test_add_command():
#     add_command = AddCommand()
#     result = add_command.execute(['1', '4'])
#     print(add_command.execute(['1', '3']))
#     assert result == None

def test_subtract_command_output(capsys, command_handler):
    """Test SubtractCommand with valid input."""
    command_handler.execute_command('subtract 10 5')
    captured = capsys.readouterr()
    assert "10 - 5 = 5.\n" in captured.out

def test_subtract_command_missing_arguments(capsys, command_handler):
    """Test SubtractCommand with missing arguments."""
    command_handler.execute_command('subtract 10')
    captured = capsys.readouterr()
    assert "Wrong number of arguments: subtract <num1> <num2>\n" in captured.out

def test_multiply_command_output(capsys, command_handler):
    """Test MultiplyCommand with valid input."""
    command_handler.execute_command('multiply 10 5')
    captured = capsys.readouterr()
    assert "10 * 5 = 50.\n" in captured.out

def test_multiply_command_missing_arguments(capsys, command_handler):
    """Test SubtractCommand with missing arguments."""
    command_handler.execute_command('multiply 10')
    captured = capsys.readouterr()
    assert "Wrong number of arguments: multiply <num1> <num2>\n" in captured.out

def test_divide_command_output(capsys, command_handler):
    """Test DivideCommand with valid input."""
    command_handler.execute_command('divide 10 5')
    captured = capsys.readouterr()
    assert "10 / 5 = 2.\n" in captured.out

def test_divide_command_missing_arguments(capsys, command_handler):
    """Test DivideCommand with missing arguments."""
    command_handler.execute_command('divide 10')
    captured = capsys.readouterr()
    assert "Wrong number of arguments: divide <num1> <num2>\n" in captured.out

def test_divide_command_divide_by_zero(capsys, command_handler):
    """Test DivideCommand raise divide by zero error"""
    # with pytest.raises(ZeroDivisionError):
    #     command_handler.execute_command('divide 10 0')
    command_handler.execute_command('divide 10 0')
    captured = capsys.readouterr()
    assert "Error: Division by zero.\n" in captured.out

def test_menu_command(capsys, command_handler):
    """Test DivideCommand raise divide by zero error"""
    # with pytest.raises(ZeroDivisionError):
    #     command_handler.execute_command('divide 10 0')
    command_handler.execute_command('menu')
    captured = capsys.readouterr()
    assert "-----------Menu:-----------\nadd <num1> <num2>\nsubtract <num1> <num2>\nmultiply <num1> <num2>\ndivide <num1> <num2>\n" in captured.out

def test_unknown_command(capsys, command_handler):
    """Test an unknown command."""
    command_handler.execute_command('abc 10 5')
    captured = capsys.readouterr()
    assert "No such command: abc\n" in captured.out
