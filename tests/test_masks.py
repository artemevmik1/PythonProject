import pytest
from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card

@pytest.mark.parametrize("card, expected", [
    ('8990922113665229', '8990 92** **** 5229'),
    ('1234567890123456', '1234 56** **** 3456'),
    ('9876543210987654', '9876 54** **** 7654')])
def test_valid_card_number(card,expected):
    """Тест корректного номера карты"""
    assert get_mask_card_number(card) == expected


def test_valid_card(number):
    """Тест на номер карты не стандартной длины, с пробелами, с буквами"""
    with pytest.raises(ValueError):
        get_mask_card_number(number)


def test_number_zero(number):
    """Тест на пустой номер карты"""
    with pytest.raises(ValueError):
        mask_account_card(None)


def test_get_mask_account_valid():
    """Тест на соответствие номера правильнйо маскировки"""
    assert get_mask_account('73654108430135874305')== '**4305'
    assert get_mask_account('73654108443243243551') == '**3551'


@pytest.fixture
def account():
    return ['Счет 6468647367 8894779589', 'Счет 646864736788fged9589', '64686473678894779589', 'Счет 6468647367889477', ' ']
def test_get_mask_account(account:str):
    """Проверка работы функции с различными форматами и длинами номеров счетов."""
    with pytest.raises(ValueError):
        get_mask_account(account)



@pytest.mark.parametrize("invalid_account", ["7365410844324351", "7365410844324351321","73654"])
def test_get_mask_account_len_invalid(invalid_account):
    """Проверка работы функции, где номер счета меньше ожидаемой длины."""
    with pytest.raises(ValueError, match="номер счета должен состоять и 20 цифр"):
         get_mask_account(invalid_account)
