import pytest


@pytest.mark.parametrize("input1, input2, input3", [(4, 3, 2), (7, 6, 13)])
def test_add(input1, input2, input3):
    assert input1 + input2 == input3
