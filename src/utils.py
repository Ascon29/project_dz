import json
import logging
import os
import pandas as pd
import csv

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/utils.log", "w")
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
        with open(file_path, encoding="utf-8") as file:
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
    '''функция принимает путь до CSV файла и возвращает список с данными
    о финансовых транзакциях
    :param file_path: путь до CSV файла.
    :return: list с данными о транзакцих
    '''
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        header = next(reader)
        result = []
        for row in reader:
            row_dict = dict()
            for index, item in enumerate(header):
                row_dict[item] = row[index]
            result.append(row_dict)
    return result


def get_operations_from_xlsx(file_path):
    '''функция принимает путь до XLSX файла и возвращает список с данными
    о финансовых транзакциях
    :param file_path: путь до XLSX файла.
    :return: list с данными о транзакцих
    '''
    operations = pd.read_excel(file_path).to_json(orient='records')
    return json.loads(operations)

# print(get_operations_from_csv('data/transactions.csv'))
# print(get_operations_from_xlsx('data/transactions_excel.xlsx'))
