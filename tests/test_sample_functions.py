import pytest
from source import sample_functions


def test_add():
    res = sample_functions.add(3, 4)
    assert res == 7


