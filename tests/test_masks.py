import pytest
from src.masks import get_mask_account, get_mask_card_number


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
        get_mask_card_number(None)