import pytest
from Student import Student


@pytest.mark.parametrize('answer', [
    ([90, 90, 90]),
    ([90, 60, 90]),
    ([100, 90, 90])
])
def test_study(answer):
    assert Student().study() == answer


@pytest.mark.parametrize('answer', [
        ([100, 75, 600]),
        ([80, 39, 90])
])
def test_get_credit(answer):
    assert Student().get_credit() == answer


@pytest.mark.parametrize('answer', [
        ([100, 107]),
        ([92, 103]),
        ([67, 103])
])
def test_read_a_book(answer):
    assert Student().read_a_book() == answer


@pytest.mark.parametrize('answer', [
        ([100, 35, 88]),
        ([80, 100, 103]),
        ([-400, 135, 85])
    ])
def test_drink(answer):
    assert Student().drink() == answer

