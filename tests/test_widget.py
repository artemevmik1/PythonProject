import pytest
from src.widget import mask_account_card


@pytest.mark.parametrize("input_data, expected", [
        # Тесты для карт (16 цифр)
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 1234567812345678", "MasterCard 1234 56** **** 5678"),
        ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
        ("МИР 1234567890123456", "МИР 1234 56** **** 3456"),
        ("Карта 1111222233334444", "Карта 1111 22** **** 4444"),

        # Тесты для счетов
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Счет 11111111111111111111", "Счет **1111"),
        ("Расчетный счет 98765432109876543210", "Расчетный счет **3210"),

        # Тесты без названия
        ("7000792289606361", " 7000 79** **** 6361"),
        ("73654108430135874305", " **4305")])
def test_mask_account_card(input_data, expected):
        """проверка, что функция корректно распознает и применяет нужный тип маскировки в зависимости от типа входных данных (карта или счет).."""
        assert mask_account_card(input_data) == expected



def test_mask_account_card_empty():
        """Тест: пустая строка"""
        with pytest.raises(ValueError):
                mask_account_card("")


@pytest.mark.parametrize("card_valid", ['Счет 646864  7367 8894779589', 'Счет 646864736788fged9589', 'Счет 646864736734889477', ' ', 121232431, 'sdfadgergWE'])
def test_mask_account_card_invalid(card_valid):
    """Тестирование функции на обработку некорректных входных данных и
     проверка ее устойчивости к ошибкам."""
    with pytest.raises(ValueError):
         mask_account_card(card_valid)
