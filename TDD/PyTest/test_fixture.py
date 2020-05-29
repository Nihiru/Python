"""
:Fixtures are used when we want to run some code before every test method
:Fixtures are used to preset configurations
"""
import pytest


@pytest.fixture
def view():
    a = 25
    b = 30
    c = 35
    return [a, b, c]


def test_compareWithA(view):
    z = 35
    assert view[0] == z


def test_compareWithB(view):
    x = 25
    assert view[0] == x


def test_compareWithC(view):
    y = 20
    assert view[0] == y
