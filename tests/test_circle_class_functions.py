import pytest
from source import class_functions


class TestCircle:

    def setup_method(self, method):
        self.circle = class_functions.Circle(7)

    def test_area(self):
        assert self.circle.area() == 153.94
