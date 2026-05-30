from typing import Any, Dict, List, Optional
from datetime import datetime


def filter_by_state(data: List[Dict[str, Any]], state: Optional[str] = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    Args:
    data: Список словарей
    state: Значение для фильтрации.По умолчанию 'EXECUTED'.
    Returns:
    Отфильтрованный
    список
    словарей
    """

    # Проверка типа входных данных
    if not isinstance(data, list):
        raise TypeError("Ожидается список, получен другой тип")

    if not data:
        raise ValueError("Пустой список")

    result = []
    for item in data:
        if item.get("state") == state:
            result.append(item)
    return result


def sort_by_date(list_of_dictionaries: list[Dict[str, Any]], sort: bool = True) -> list[Dict[str, Any]]:
    """
    Сортирует список словарей по ключу 'date'.
    """

    if not isinstance(list_of_dictionaries, list):
        raise TypeError("Ожидается список, получен другой тип")

    if not list_of_dictionaries:
        return []

    for item in list_of_dictionaries:
        if "date" in item:
            try:
                datetime.fromisoformat(item["date"])
            except (ValueError, TypeError):
                # Можно либо пропустить, либо выбросить ошибку
                raise ValueError(f"Некорректный формат даты: {item['date']}")

    return sorted(list_of_dictionaries, key=lambda d: d["date"], reverse=sort)
