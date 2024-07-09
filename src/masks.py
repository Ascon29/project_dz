import logging

from config import LOGS_MASKS_DIR

logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(LOGS_MASKS_DIR, "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def return_card_number(card_number: str) -> str:
    """
    Принимает строку с номером карты и возвращает его с маской в виде строки
    :param card_number: Номер карты в виде строки.
    :return: Маскированный номер карты.
    """
    logger.info(f"запись маскированной карты {card_number}")
    return f"{card_number[-16:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"


def return_account_number(account_number: str) -> str:
    """
    Принимает строку с номером счета и возвращает его с маской в виде строки
    :param account_number: Номер счета в виде строки.
    :return: Маскированный номер счета.
    """
    logger.info(f"запись маскированнового счета {account_number}")
    return f"**{account_number[-4:]}"
