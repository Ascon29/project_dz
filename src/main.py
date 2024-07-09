from config import DATA_DIR
from src.processing import filter_by_state, sort_by_date, sort_by_input
from src.utils import get_operations, get_operations_from_csv, get_operations_from_xlsx
from src.widget import get_data, mask_account_card


def main():
    """функция отвечает за основную логику проекта и связывает функциональности модулей между собой"""

    # приветствие и выбор тип файла для работы
    print(
        """Программа: Привет! Добро пожаловать в программу работы
с банковскими транзакциями."""
    )
    while True:
        menu_choise = input(
            """Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла

"""
        )
        if menu_choise in ["1", "2", "3"]:
            break
        else:
            print("Неправильный ввод\n")

    if menu_choise == "1":
        print("Для обработки выбран JSON-файл.\n")
        transactions_data = get_operations(DATA_DIR + "/operations.json")
    elif menu_choise == "2":
        print("Для обработки выбран CSV-файл.\n")
        transactions_data = get_operations_from_csv(DATA_DIR + "/transactions.csv")
    elif menu_choise == "3":
        print("Для обработки выбран XLSX-файл.\n")
        transactions_data = get_operations_from_xlsx(DATA_DIR + "/transactions_excel.xlsx")

    # выбор фильтации по статусу транзакции
    while True:
        status_choise = input(
            """Программа: Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING

"""
        ).upper()
        if status_choise in ["EXECUTED", "CANCELED", "PENDING"]:
            break
        else:
            print(f'Статус операции "{status_choise}" недоступен.\n')

    print(f'Операции отфильтрованы по статусу "{status_choise}"\n')
    filtered_transactions_data = filter_by_state(transactions_data, status_choise)

    # ряд вопросов с однотипными ответами. реализую через список вопросов
    questions = [
        "Отсортировать операции по дате? Да/Нет\n",
        "Отсортировать по возрастанию? Да/Нет\n",
        "Выводить только рублевые тразакции? Да/Нет\n",
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n",
    ]
    answers = []

    for i in questions:
        while True:
            user_input = input(i).lower()
            if user_input in ["да", "нет"]:
                answers.append(user_input)
                break
            else:
                print("Неправильный ввод\n")

    if answers[0] == "да":  # выбрана фильтация по дате
        if answers[1] == "да":  # если выбрана фильтация по возрастанию
            sorted_transactions_by_date = sort_by_date(filtered_transactions_data, rev=False)
        else:  # если выбрана по убыванию
            sorted_transactions_by_date = sort_by_date(filtered_transactions_data)
    else:  # фильтация по дате не выбрана
        sorted_transactions_by_date = filtered_transactions_data

    # фильтрация по рублевым транзакциям
    if answers[2] == "да":
        filtered_by_rub = [
            transaction for transaction in sorted_transactions_by_date if transaction["currency_code"] == "RUB"
        ]
    else:
        filtered_by_rub = sorted_transactions_by_date

    # фильтация по определенному слову в описании
    if answers[3] == "да":
        word_for_filter = input("Введите слово для фильтрации\n")
        filtered_by_word = sort_by_input(filtered_by_rub, word_for_filter)
    else:
        filtered_by_word = filtered_by_rub

    len_transactions = len(filtered_by_word)
    print("Распечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len_transactions}\n")

    # итог работы программы
    if len_transactions > 0:
        for i in filtered_by_word:
            if i["description"] == "Открытие вклада":
                print(
                    f"""{get_data(i["date"])} {i["description"]}\n
                {mask_account_card(i["to"])}\n
                Сумма: {i["amount"]} {i["currency_name"]}\n"""
                )
            else:
                print(
                    f"""{get_data(i["date"])} {i["description"]}\n
                {mask_account_card(i["from"])} -> {mask_account_card(i["to"])}\n
                Сумма: {i["amount"]} {i["currency_name"]}\n"""
                )
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
