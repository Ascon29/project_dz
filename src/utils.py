import json
import os


def get_operations(file_path):
    """функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список."""
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, encoding="utf-8") as file:
            operations = json.load(file)
            if isinstance(operations, list):
                return operations
            else:
                return []
    except json.JSONDecodeError:
        return []
