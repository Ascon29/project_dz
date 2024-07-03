from datetime import datetime

from src.masks import return_account_number, return_card_number


def mask_account_card(account_card: str) -> str:
    """
    функция, которая возвращает строку с маской номера счета или карты
    :param account_card: Номер счета или карты в виде строки.
    :return: Маскированный номер счетаили карты.
    """
    new_str = account_card.split()
    if len(new_str) == 3:
        return f"{new_str[0]} {new_str[1]} {return_card_number(new_str[2])}"
    elif len(new_str[-1]) == 16:
        return f"{new_str[0]} {return_card_number(new_str[1])}"
    else:
        return f"{new_str[0]} {return_account_number(new_str[1])}"


def get_data(data: str) -> str:
    """
    функция, которая возвращает строку даты в формате DD.MM.YY
    :param data: полная дата и время в виде строки.
    :return: дата в виде 'DD.MM.YY.
    """
    date_obj = datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")
