from masks import return_card_number, return_account_number
from datetime import datetime


def mask_account_card(account_card: str) -> str:
    """функция, которая возвращает строку с маской номера счета или карты"""
    new_str = account_card.split()
    if len(new_str) == 3:
        return f"{new_str[0]} {new_str[1]} {return_card_number(new_str[2])}"
    else:
        return f"{new_str[0]} {return_account_number(new_str[1])}"


def get_data(data: str) -> str:
    """функция, которая возвращает строку даты в формате DD.MM.YY"""
    date_obj = datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")
