import pytest
import sys
import os

# Add the test directory to the path so we can import sample_func
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'test'))

from sample_func import add_numbers, multiply_numbers


def test_add_numbers():
    """Test the add_numbers function."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(10, -5) == 5


def test_multiply_numbers():
    """Test the multiply_numbers function."""
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(-1, 1) == -1
    assert multiply_numbers(0, 5) == 0
    assert multiply_numbers(10, -5) == -50

