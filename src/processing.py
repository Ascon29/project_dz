import re
from collections import Counter


def filter_by_state(operations: list, state: str = "EXECUTED") -> list:
    """
    функция, фильтрующая список словарей по ключу state (по умолчанию EXECUTED).
    Возвращает новый список, содержащий только те словари, у которых ключ state.
    :param operations: список словарей
    :param state:  ключ для фильтрации (optional)
    :return: отфильтрованный список по ключу 'state'.
    """
    return [i for i in operations if i.get("state") == state]


def sort_by_date(operations: list, rev: bool = True) -> list:
    """
    функция принимает список словарей и возвращает новый список,
    в котором исходные словари отсортированы по дате.
    Второй параметр задает порядок сортировки (по умолчанию - по убыванию).
    :param operations: список словарей.
    :param rev: ключ для порядка сортировки (по возрастанию или по убыванию)
    :return: отсортированный список по ключу 'rev'.
    """
    return sorted(operations, key=lambda x: x["date"], reverse=rev)


def sort_by_input(operations, input_word):
    """
    принимает список словарей с данными о банковских операциях и строку поиска.
    возвращает список словарей, у которых в описании 'description' есть данная строка
    :param operations: список словарей
    :param input_word: ввод пользователя
    :return: отфильтрованный список по ключу 'description'
    """
    result = []
    for i in operations:
        pattern = input_word.lower()
        match = re.search(pattern, i.get("description"), flags=re.IGNORECASE)
        if match:
            if match.group().lower() == pattern:
                result.append(i)
    return result


def get_count_description(operations, descriptions):
    """
    принимает список словарей с данными о банковских операциях и список категорий операций
    возвращает словарь, в котором ключи — названия категорий,
    а значения — количество операций в каждой категории.
    :param operations: список словарей
    :param descriptions: список категорий
    :return: словарь {'название категории': 'колличество операций по данной категории'}
    """

    # убираем операции, описание которых нет в списке описаний
    filtered_operations = [operation for operation in operations if operation["description"] in descriptions]

    # создаем новый список описаний операций
    filtered_description = [description["description"] for description in filtered_operations]

    counter = Counter(filtered_description)
    return dict(counter)


if __name__ == "__main__":
    operations = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 596171168,
            "state": "EXECUTED",
            "date": "2018-07-11T02:26:18.671407",
            "operationAmount": {"amount": "79931.03", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 72082042523231456215",
        },
    ]
    x = input()
    descriptions = ["Открытие вклада", "Перевод с карты на карту", "Перевод со счета на счет"]
    print(sort_by_input(operations, x))
    print(get_count_description(operations, descriptions))
