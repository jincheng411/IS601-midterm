'''Test cases for Calculation class'''
from decimal import Decimal
import pytest

from app.calculation import Calculation
from app.operations import add, division, multiply, subtract

@pytest.mark.parametrize("operand_a, operand_b, operation, expected", [
    (Decimal('3'), Decimal('4'), add, Decimal('7')),
    (Decimal('3.4'), Decimal('4.2'), add, Decimal('7.6')),
    (Decimal('0'), Decimal('4'), add, Decimal('4')),
    (Decimal('3'), Decimal('0'), add, Decimal('3')),
    (Decimal('4'), Decimal('3'), subtract, Decimal('1')),
    (Decimal('3'), Decimal('3'), subtract, Decimal('0')),
    (Decimal('2'), Decimal('4'), subtract, Decimal('-2')),
    (Decimal('7.2'), Decimal('4.1'), subtract, Decimal('3.1')),
    (Decimal('3'), Decimal('4'), multiply, Decimal('12')),
    (Decimal('3.4'), Decimal('4.8'), multiply, Decimal('16.32')),
    (Decimal('0'), Decimal('4'), multiply, Decimal('0')),
    (Decimal('3'), Decimal('-4'), multiply, Decimal('-12')),
    (Decimal('12'), Decimal('4'), division, Decimal('3')),
    (Decimal('0'), Decimal('4'), division, Decimal('0')),
    (Decimal('3.8'), Decimal('2'), division, Decimal('1.9')),
])
def test_calculation_operations(operand_a, operand_b, operation, expected):
    '''Test perform method'''
    cal = Calculation(operand_a, operand_b, operation)
    assert cal.perform() == expected

def test_create_calculation():
    '''Test create calculation use factory'''
    cal = Calculation.create(2, 3, division)
    assert isinstance(cal, Calculation)

