import pytest

from mp_basic_calculator import Calculator


@pytest.fixture
def calculator():
    # All setup for the cart here...
    calculator = Calculator()
    return calculator


def test_memory_reset(calculator):
    assert calculator.add(10) == 10
    assert calculator.multiply(2) == 20
    assert calculator.clean_memory() == 0
