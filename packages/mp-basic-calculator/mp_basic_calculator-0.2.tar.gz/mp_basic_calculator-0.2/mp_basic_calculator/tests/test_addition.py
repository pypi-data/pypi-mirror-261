import pytest

from mp_basic_calculator import Calculator


@pytest.fixture
def calculator():
    # All setup for the cart here...
    calculator = Calculator()
    return calculator


def test_addition(calculator):
    assert calculator.addition(5) == 5
    assert calculator.addition(10) == 15
    assert calculator.clean_memory() == 0
    assert calculator.addition(10.5) == 10.5
