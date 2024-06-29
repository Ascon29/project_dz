# import json
# from unittest.mock import patch

import pytest

from src.utils import get_operations


@pytest.mark.parametrize(
    "x, expected",
    [
        (
            "tests/oper.json",
            [
                {
                    "id": 441945886,
                    "state": "EXECUTED",
                    "date": "2019-08-26T10:50:58.294041",
                    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "to": "Счет 64686473678894779589",
                }
            ],
        ),
        ("", []),
        ("tests/oper_empty.json", []),
        ("oper_not_list.json", []),
    ],
)
def test_get_operations(x, expected):
    assert get_operations(x) == expected


# @patch('os.path.exists')
# def test_get_operations(mock_exists):
#     mock_exists.return_value = False
#     assert get_operations('data/data.json') == []
