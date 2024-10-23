'''Test cases for Calculator class'''
from decimal import Decimal

from app.calculator import Calculator


def test_operation_add():
    '''test add method in calculator class'''
    assert Calculator.add(3, 5) == 8

def test_operation_subtract():
    '''test subtract method in calculator class'''
    assert Calculator.subtract(4, 1) == 3

def test_operation_multiply():
    '''test multiply method in calculator class'''
    assert Calculator.multiply(4, 6) == 24
    assert Calculator.multiply(2, -3) == -6

def test_operation_division():
    '''test division method in calculator class'''
    assert Calculator.division(4, 2) == 2
