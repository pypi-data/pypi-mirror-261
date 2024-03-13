import pytest

from mp_basic_calculator import Calculator


@pytest.fixture
def calculator():
    # All setup for the cart here...
    calculator = Calculator()
    return calculator


def test_subtraction(calculator):
    assert calculator.subtract(5) == -5
    assert calculator.subtract(-10) == 5
    assert calculator.clean_memory() == 0
    assert calculator.subtract(10.5) == -10.5
