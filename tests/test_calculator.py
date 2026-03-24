import pytest
from src.calculator import add, subtract, multiply, divide


# Replaces writing 4 identical test functions
@pytest.mark.parametrize("a, b, expected", [
    (2,   3,   5),    # positive
    (0,   0,   0),    # zeros
    (-1,  1,   0),    # negative
    (100, -50, 50),   # large values
])
def test_add_cases(a, b, expected):
    assert add(a, b) == expected


def test_subtract():
    assert subtract(10, 5) == 5


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
# pytest -v output:
# PASSED  test_add_cases[2-3-5]
# PASSED  test_add_cases[0-0-0]
# PASSED  test_add_cases[-1-1-0]
# PASSED  test_add_cases[100--50-50]
