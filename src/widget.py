from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция проверяет данные являются номером карты или номером счета"""

    if number is None:
        raise ValueError("номер карты не может быть None")

    if isinstance(number, int):
        raise ValueError("Номер должен состоять только из цифр")

    number_split = number.split(" ")

    if not number_split[-1].isdigit():
        raise ValueError("Номер должен состоять только из цифр")

    if not isinstance(number_split[-1], str):
        raise TypeError("Ожидается строка")

    parts = number_split[-1].strip().split(" ")

    if not parts:
        raise ValueError("некорректный формат строки")

    if len(number_split[-1]) != 16 and len(number_split[-1]) != 20:
        raise ValueError("Не является номером карты или счета")

    if len(number_split[-1]) == 16:
        mask = get_mask_card_number(number_split[-1])
    else:
        mask = get_mask_account(number_split[-1])

    number_mask = " ".join(number_split[0:-1]) + " " + mask

    return number_mask


def get_date(date_string: str) -> str:
    """
    Преобразует дату в формат ДД.ММ.ГГГГ без использования datetime.
    """
    try:
        # Разделяем строку по 'T' и берем первую часть (дату)
        date_part = date_string.split("T")[0]

        # Разделяем дату на год, месяц, день
        year, month, day = date_part.split("-")

        # Возвращаем в формате ДД.ММ.ГГГГ
        return f"{day}.{month}.{year}"
    except (IndexError, ValueError):
        raise ValueError("Некорректный формат даты: {date_string}")


def get_datee(date_string: str) -> str:
    """
    Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ.
    """
    if date_string is None:
        raise ValueError("Некорректный формат даты: None")

    if not isinstance(date_string, str):
        raise TypeError("Ожидается строка, получен")

    if not date_string.strip():
        raise ValueError("Некорректный формат даты: пустая строка")

    try:
        # Парсим входную строку в объект datetime
        dt = datetime.fromisoformat(date_string)

        # Преобразуем в нужный формат
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Некорректный формат даты: {date_string}")
