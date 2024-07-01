import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def return_card_number(card_number: str) -> str:
    """функция, которая принимает строку с номером карты и возвращает его с маской в виде строки"""
    logger.info(f"запись маскированной карты {card_number}")
    return f"{card_number[-16:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"


def return_account_number(account_number: str) -> str:
    """функция, которая принимает строку с номером счета и возвращает последние 4 цифры в виде строки"""
    logger.info(f"запись маскированнового счета {account_number}")
    return f"**{account_number[-4:]}"
