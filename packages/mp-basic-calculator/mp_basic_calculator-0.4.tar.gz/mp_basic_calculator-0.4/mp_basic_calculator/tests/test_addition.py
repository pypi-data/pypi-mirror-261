import pytest

from mp_basic_calculator import Calculator


@pytest.fixture
def calculator():
    # All setup for the cart here...
    calculator = Calculator()
    return calculator


def test_addition(calculator):
    assert calculator.add(5) == 5
    assert calculator.add(10) == 15
    assert calculator.clean_memory() == 0
    assert calculator.add(10.5) == 10.5
