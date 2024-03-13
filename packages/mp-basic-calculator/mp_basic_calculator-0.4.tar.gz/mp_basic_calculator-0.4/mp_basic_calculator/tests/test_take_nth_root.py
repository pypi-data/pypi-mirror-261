import pytest

from mp_basic_calculator import Calculator


@pytest.fixture
def calculator():
    # All setup for the cart here...
    calculator = Calculator()
    return calculator


def test_take_nth_root(calculator):
    assert calculator.take_nth_root(25, 2) == 5
    assert calculator.take_nth_root(16, 4) == 2
    assert calculator.take_nth_root(32, 5) == 2
