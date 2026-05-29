import pytest

from src.processing import *
from tests.conftest import *


def test_filter_by_state_success(sample_data: List[Dict[str, Any]]) -> None:
    """Тест фильтрации по статусу EXECUTED (значение по умолчанию)"""
    result = filter_by_state(sample_data)

    assert all(item["state"] == "EXECUTED" for item in result)
    assert result[0]["id"] == 1
    assert len(result) == 1


def test_filter_by_canceled_state(sample_data):
    """Тест фильтрации по статусу CANCELED"""
    result = filter_by_state(sample_data, state="CANCELED")

    assert len(result) == 1
    assert result[0]["state"] == "CANCELED"
    assert result[0]["id"] == 2



def test_filter_by_state_no_empty_data(empty_data):
    """Тест: пустой список на входе -> пустой список на выходе"""
    with pytest.raises(ValueError):
         filter_by_state(empty_data)

def test_filter_by_state_type_error():
    """Тест: пустой список на входе -> пустой список на выходе"""
    with pytest.raises(TypeError):
         filter_by_state({1:'aбс'})


@pytest.mark.parametrize("test_data", [ (
        [  # Входные данные
            {"id": 414288297, "state": "EXECUTED", "date": "2019-07-03"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"}
        ]
    )
])
def test_sort_date_true(test_data, list_time):
    """Тест: сортировка по убыванию (по умолчанию sort=True)"""
    result = sort_by_date(test_data)
    result_ids = [item["date"] for item in result]
    assert result_ids == list_time



@pytest.mark.parametrize("test_data", [ (
        [  # Входные данные
            {"id": 414288297, "state": "EXECUTED", "date": "2019-07-03"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"}
        ]
    )
])
def test_sort_date_false(test_data, list_time_false):
    """Тест: сортировка по убыванию (по умолчанию sort=True)"""
    result = sort_by_date(test_data, sort=False)
    result_ids = [item["date"] for item in result]
    assert result_ids == list_time_false

def test_sort_with_identical_dates():
    """Тест: несколько элементов с одинаковыми датами"""
    data = [
        {"id": 1, "date": "2024-03-15T10:30:00", "name": "Первый"},
        {"id": 2, "date": "2024-03-15T10:30:00", "name": "Второй"},
        {"id": 3, "date": "2024-03-15T10:30:00", "name": "Третий"}
    ]

    result = sort_by_date(data)

    for item in result:
        assert item["date"] == "2024-03-15T10:30:00"


@pytest.mark.parametrize("invalid_date", [
    "2024/03/15",  # Нестандартный формат
    "15-03-2024",  # ДД-ММ-ГГГГ
    "March 15, 2024",  # Текстовый формат
    "2024-13-45",  # Несуществующая дата
    "not a date",  # Не дата
    "",  # Пустая строка
    "2024-03-15T25:00:00",  # Неверное время
])
def test_sort_with_invalid_date_formats(invalid_date):
    """Параметризованный тест: некорректные форматы дат"""
    data = [
        {"id": 1, "date": "2024-03-15T10:30:00"},
        {"id": 2, "date": invalid_date},
    ]
    with pytest.raises(ValueError):
         sort_by_date(data)



    # # Сравнение строк работает, но порядок может быть неожиданным
    # # Функция не должна падать при любых форматах
    # result = sort_by_date(data)
    #
    # # Результат должен содержать все элементы
    # assert len(result) == 2
    # # Сортировка по строковому представлению
    # assert isinstance(result, list)