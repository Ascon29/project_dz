from unittest.mock import mock_open, patch

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


@patch("os.path.exists")
def test_get_operations_with_patch_not_exists(mock_exists):
    mock_exists.return_value = False
    assert get_operations("operations.json") == []


@patch("os.path.exists")
def test_get_operations_with_patch_not_list(mock_exists):
    mock_exists.return_value = True
    m = mock_open(read_data='{"amount": "100", "currency_code": "RUB"}')
    with patch("builtins.open", m) as mocked_open:
        assert get_operations("operations.json") == []
        mocked_open.assert_called_with("operations.json", "r", encoding="utf-8")


@patch("os.path.exists")
def test_get_operations_with_patch_success(mock_exists):
    mock_exists.return_value = True
    m = mock_open(read_data='[{"amount": "100", "currency_code": "RUB"}]')
    with patch("builtins.open", m) as mocked_open:
        assert get_operations("operations.json") == [{"amount": "100", "currency_code": "RUB"}]
        mocked_open.assert_called_with("operations.json", "r", encoding="utf-8")


def test_get_operations_from_csv(test_csv):
    # test_csv == фикстура в модуле conftest.py
    assert get_operations_from_csv("tests/test.csv") == test_csv


def test_get_operations_from_xlsx(test_xlsx):
    # test_xlsx == фикстура в модуле conftest.py
    assert get_operations_from_xlsx("tests/test.xlsx") == test_xlsx


expected_result = [
    {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }
]


@patch("csv.DictReader")
def test_get_data_from_csv_mock(mock_reader):
    mock_reader.return_value = expected_result

    with patch("builtins.open", mock_open()) as mocked_open:
        assert get_operations_from_csv("transactions.csv") == expected_result
        mocked_open.assert_called_with("transactions.csv", "r", encoding="utf-8")

    result = get_operations_from_csv("data/transactions.csv")
    assert result == expected_result


@patch("pandas.read_excel")
def test_get_operations_from_xlsx_mock(mock_reader_excel):
    mock_reader_excel.return_value.to_dict.return_value = expected_result

    with patch("builtins.open", mock_open()) as mocked_open:
        assert get_operations_from_xlsx("transactions_excel.xlsx") == expected_result
        mocked_open.assert_called_with("transactions_excel.xlsx", "rb")

    result = get_operations_from_xlsx("data/transactions_excel.xlsx")
    assert result == expected_result
