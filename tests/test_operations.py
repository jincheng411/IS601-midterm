'''My operations Test'''

from app.operations import add, division, multiply, subtract

def test_addition():
    '''Test that addition function works '''
    assert add(2,2) == 4

def test_subtraction():
    '''Test that subtraction function works '''
    assert subtract(2,2) == 0

def test_multiplication():
    '''Test that multiply function works '''
    assert multiply(2,3) == 6

def test_division():
    '''Test that division function works '''
    assert division(6,2) == 3
