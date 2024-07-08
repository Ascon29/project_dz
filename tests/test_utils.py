# import json
from unittest.mock import patch

# import os
import pytest
from src.utils import get_operations, get_operations_from_csv, get_operations_from_xlsx


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


def test_get_operations_from_csv(test_csv):
    # test_csv == фикстура в модуле conftest.py
    assert get_operations_from_csv("tests/test.csv") == test_csv


def test_get_operations_from_xlsx(test_xlsx):
    # test_xlsx == фикстура в модуле conftest.py
    assert get_operations_from_xlsx("tests/test.xlsx") == test_xlsx


expected_result = [
    {
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "SoL",
        "currency_code": "PEN",
        "from": "Счет 58803664651298323391",
        "to": "Счет 39746506635466619397",
        "description": "Перевод организации",
    }
]


@patch("csv.reader")
def test_get_data_from_csv_mock(mock_reader):
    mock_reader.return_value = iter(
        [
            ["id", "state", "date", "amount", "currency_name", "currency_code", "from", "to", "description"],
            [
                "650703",
                "EXECUTED",
                "2023-09-05T11:30:32Z",
                "16210",
                "SoL",
                "PEN",
                "Счет 58803664651298323391",
                "Счет 39746506635466619397",
                "Перевод организации",
            ],
        ]
    )

    result = get_operations_from_csv("data/transactions.csv")
    assert result == expected_result


# def test_get_operations_from_xlsx_mock():
#     with patch('builtins.open') as mock_open:
#         mock_open = [
#             {
#                 "id": "650703",
#                 "state": "EXECUTED",
#                 "date": "2023-09-05T11:30:32Z",
#                 "amount": "16210",
#                 "currency_name": "SoL",
#                 "currency_code": "PEN",
#                 "from": "Счет 58803664651298323391",
#                 "to": "Счет 39746506635466619397",
#                 "description": "Перевод организации"
#             }
#         ]
#         assert get_operations_from_xlsx(mock_open) == expected_result
