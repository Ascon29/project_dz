import json
import logging
import os

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_operations(file_path):
    """функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список."""
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
