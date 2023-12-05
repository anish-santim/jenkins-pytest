import pytest
from source import class_functions


@pytest.mark.parametrize("side, areas", [(3, 9), (4, 16)])
def test_multiple_square_areas(side, areas):
    assert class_functions.Square(side).area() == areas
