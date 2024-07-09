from typing import Dict, Generator, Union


def filter_by_currency(transactions: list, currency: str) -> Generator[Dict[str, Union[str, int, dict]], None, None]:
    """
    функция генератор по очереди возвращает id операции с указанной валютой
    :param transactions: список транзакций.
    :param currency: валюта в виде строки (пример - 'USD')
    :return: 'id' операции.
    """
    for i in transactions:
        if i["operationAmount"]["currency"]["code"] == currency:
            yield i["id"]


def transaction_descriptions(transactions: list) -> Generator[str, None, None]:
    """
    функция генератор по очереди возвращает описание операции
    :param transactions: список транзакций.
    :return: 'description' описание операции.
    """
    for i in transactions:
        yield i["description"]


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """
    функция генерирует номера карт в заданном диапазоне
    :param start: начало генерации (например 1)
    :param stop: онец генерации (например 9999 9999 9999 9999)
    :return: номер карты в виде ХХХХ ХХХХ ХХХХ ХХХХ
    """
    for i in range(start, stop + 1):
        nums = (16 - len(str(i))) * "0" + str(i)
        yield f"{nums[:4]} {nums[4:8]} {nums[8:12]} {nums[12:16]}"
