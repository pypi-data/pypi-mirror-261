import pytest

from mp_basic_calculator import Calculator


@pytest.fixture
def calculator():
    # All setup for the cart here...
    calculator = Calculator()
    return calculator


def test_division(calculator):
    assert calculator.divide(10) == 10
    assert calculator.divide(2) == 5
    assert calculator.clean_memory() == 0
    assert calculator.multiply(10.5) == 10.5
