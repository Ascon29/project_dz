def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """функция, которая принимает список словарей и значение для ключа state (по умолчанию EXECUTED)
    и возвращает новый список, содержащий только те словари, у которых ключ state"""
    return [i for i in data if i.get("state") == state]


def sort_by_date(data: list, rev: bool = True) -> list:
    """функция, которая принимает список словарей и возвращает новый список,
    в котором исходные словари отсортированы по дате.
    Второй параметр задает порядок сортировки (по умолчанию - по убыванию)."""
    return sorted(data, key=lambda x: x["date"], reverse=rev)


# print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#                     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], rev=False))
