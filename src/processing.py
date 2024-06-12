def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """функция, которая принимает список словарей и значение для ключа state (по умолчанию EXECUTED)
    и возвращает новый список, содержащий только те словари, у которых ключ state"""
    return [i for i in data if i.get("state") == state]


def sort_by_date(data: list, rev: bool = False) -> list:
    """функция, которая принимает список словарей и возвращает новый список,
    в котором исходные словари отсортированы по дате.
    Второй параметр задает порядок сортировки (по умолчанию - по убыванию)."""
    return sorted(data, key=lambda x: x["date"], reverse=rev)
