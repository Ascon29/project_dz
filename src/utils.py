import csv
import json
import logging
import os

import pandas as pd

from config import LOGS_UTILS_DIR

logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(LOGS_UTILS_DIR, "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_operations(file_path):
    """
    функция принимает путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список.
    :param file_path: путь до JSON-файла.
    :return: list с данными о транзакциях.
    """
    logger.info(f"попытка открыть файл {file_path}")
    if not os.path.exists(file_path):
        logger.warning(f"файл {file_path} отсуствует")
        return []
    try:
        logger.info(f"открытие файла {file_path}")
        with open(file_path, "r", encoding="utf-8") as file:
            operations = json.load(file)
            logger.info(f"запись информации {operations}")
            if isinstance(operations, list):
                return operations
            else:
                logger.warning(f"файл {file_path} содержит не список(list")
                return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка {json.JSONDecodeError}")
        return []


def get_operations_from_csv(file_path):
    """функция принимает путь до CSV файла и возвращает список с данными
    о финансовых транзакциях
    :param file_path: путь до CSV файла.
    :return: list с данными о транзакцих
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            result = []
            for row in reader:
                result.append(row)
            return result
    except FileNotFoundError as ex:
        return f"{ex}: Файл не найден"


def get_operations_from_xlsx(file_path):
    """функция принимает путь до XLSX файла и возвращает список с данными
    о финансовых транзакциях
    :param file_path: путь до XLSX файла.
    :return: list с данными о транзакцих
    """
    try:
        with open(file_path, "rb") as file:
            operations = pd.read_excel(file).to_dict("records")
            return operations
    except FileNotFoundError as ex:
        return f"{ex}: Файл не найден"


# print(get_operations('data/operations.json'))
# print(get_operations_from_csv('../data/transactions.csv'))
# print(get_operations_from_xlsx('data/transactions_excel.xlsx'))
