import pytest

from src.widget import get_data, mask_account_card


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2077-01-29T20:07:07.926541", "29.01.2077"),
    ],
)
def test_get_data(value, expected):
    assert get_data(value) == expected
