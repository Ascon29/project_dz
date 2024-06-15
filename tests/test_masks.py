from src.masks import return_card_number, return_account_number


def test_return_card_number(card_number):
    assert return_card_number("4526865425631257") == card_number


def test_return_account_number(account_number):
    assert return_account_number("22003652522239988574") == account_number
