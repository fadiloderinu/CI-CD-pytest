import math
import pytest

from myapp.mymodule.funcs import multiply


def test_area_of_square_last_two_digits():
    """
    Validate area calculation for a square where the expected area
    is the last two digits of my student ID (101000478).
    """
    expected = 78
    side = math.sqrt(expected)
    res = multiply(side, side)
    assert res == pytest.approx(expected)
