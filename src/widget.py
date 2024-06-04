from masks import return_card_number, return_account_number

def mask_account_card(account_card: str) -> str:
    '''функция, которая возвращает строку с маской номера счета или карты'''
    new_str = account_card.split()
    if len(new_str) == 3:
        return f'{new_str[0]} {new_str[1]} {return_card_number(new_str[2])}'
    else:
        return f'{new_str[0]} {return_account_number(new_str[1])}'


def get_data(data: str) -> str:
    pass


x = 'Счет 73654108430135874305'
print(mask_account_card(x))

# Maestro 1596837868705199
# Счет 64686473678894779589
# MasterCard 7158300734726758
# Счет 35383033474447895560
# Visa Classic 6831982476737658
# Visa Platinum 8990922113665229
# Visa Gold 5999414228426353
# Счет 73654108430135874305