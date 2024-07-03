def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """
    функция, фильтрующая список словарей по ключу state (по умолчанию EXECUTED).
    Возвращает новый список, содержащий только те словари, у которых ключ state.
    :param data: список словарей
    :param state:  ключ для фильтрации (optional)
    :return: отфильтрованный список по ключу state.
    """
    return [i for i in data if i.get("state") == state]


def sort_by_date(data: list, rev: bool = True) -> list:
    """
    функция принимает список словарей и возвращает новый список,
    в котором исходные словари отсортированы по дате.
    Второй параметр задает порядок сортировки (по умолчанию - по убыванию).
    :param data: список словарей.
    :param rev: ключ для порядка сортировки (по возрастанию или по убыванию)
    :return: отсортированный список по ключу rev.
    """
    return sorted(data, key=lambda x: x["date"], reverse=rev)


# print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#                     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], rev=False))
