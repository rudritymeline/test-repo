# test_app.py
import pytest
from app import add, subtract, divide

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(5, 2) == 3

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)

# Note: We are skipping test_multiply to demonstrate uncovered code in Codecov
