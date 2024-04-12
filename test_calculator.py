from calculator import addition
from calculator import division
from calculator import substraction


def test_addition():
    assert addition(1, 2) == 3

def test_substraction():
    assert substraction(7, 5) == 2

def test_division():
    assert division(2, 2) == 1