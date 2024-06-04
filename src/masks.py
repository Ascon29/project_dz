def return_card_number(card_number: str) -> str:
    """функция, которая принимает строку с номером карты и возвращает его с маской в виде строки"""
    return f"{card_number[-16:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"


def return_account_number(account_number: str) -> str:
    """функция, которая принимает строку с номером счета и возвращает последние 4 цифры в виде строки"""
    return f"**{account_number[-4:]}"
