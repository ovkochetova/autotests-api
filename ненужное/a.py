import pytest


class TestMathOperations:
    @pytest.mark.parametrize("a,b,expected", [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0)
    ])
    def test_addition(self, a, b, expected):
        assert a + b == expected

    @pytest.mark.parametrize("a,b,expected", [
        (5, 2, 3),
        (10, 5, 5)
    ])
    def test_subtraction(self, a, b, expected):
        assert a - b == expected