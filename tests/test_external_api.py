from unittest.mock import patch

import pytest

from src.external_api import convert_to_rub, get_rub_transaction


@patch("requests.get")
def test_convert_to_rub(mock_request):
    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = {"rates": {"RUB": 100}}
    assert convert_to_rub("USD") == 100


@patch("requests.get")
def test_convert_to_rub_error(mock_request):
    mock_request.return_value.status_code = 400
    mock_request.return_value.json.return_value = {"rates": {"RUB": 100}}
    with pytest.raises(Exception):
        convert_to_rub("USD")


def test_get_rub_transaction():
    assert get_rub_transaction({"amount": 100, "currency": "RUB"}) == 100.0


# def test_get_rub_transaction_usd():
#     with patch('convert_to_rub') as mock_convert:
#         mock_convert.return_value = 85.5
#         assert get_rub_transaction({'amount': 100, 'currency': 'USD'}) == 85.5
