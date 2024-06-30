import os

import requests
from dotenv import load_dotenv

load_dotenv()
url = "https://api.apilayer.com/exchangerates_data/latest"
API_KEY = os.getenv("API_KEY")


def get_rub_transaction(operation):
    """функция, которая принимает на вход транзакцию и возвращает сумму
    транзакции (amount) в рублях, тип данных — float."""

    amount = operation["amount"]
    convert_from = operation["currency"]
    if convert_from == "RUB":
        return float(amount)
    else:
        convert_value = convert_to_rub(convert_from)
        return convert_value * float(amount)


def convert_to_rub(convert_from):
    """функция обращается к внешнему API для получения текущего
    курса валют и конвертации суммы операции в рубли"""

    headers = {"apikey": API_KEY}
    params = {"base": convert_from, "sumbols": "RUB"}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        result = response.json()
        return result["rates"]["RUB"]
    else:
        raise Exception(f"Ошибка. Причина: {response.status_code}")


# example = {'amount': 100, 'currency': 'USD'}
# print(get_rub_transaction(example))
