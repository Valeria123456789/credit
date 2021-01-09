import pytest
from Magistrant import Magistrant


@pytest.mark.parametrize('answer', [
    ([0, 70, 100, 130]),
    ([100, 120, 1100, 70]),
    ([100, 190, 9, 55])
])
def test_get_credit(answer):
    assert Magistrant().get_credit() == answer


@pytest.mark.parametrize('answer', [
        ([0, 140]),
        ([-32, 120]),
])
def test_study(answer):
    assert Magistrant().study() == answer