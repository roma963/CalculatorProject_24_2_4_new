import pytest
from calculator import Calculator
calc = Calculator()
def test_add_positive():
    assert calc.add(2, 3) == 5
def test_subtract_positive():
    assert calc.subtract(5, 2) == 3
def test_multiply_positive():
    assert calc.multiply(4, 6) == 24
def test_divide_positive():
    assert calc.divide(10, 2) == 5
def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)
