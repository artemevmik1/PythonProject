def get_mask_card_number(card_number: str) -> str:
    """
    Функция проверяет размер номера карты на корректность
    и затем маскирует в формате XXXX XX** **** XXXX
    """

    if (len(card_number)) != 16 or not card_number.isdigit():
        raise ValueError("номер карты должен состоять и 16 цифр")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(okaunt_number: str) -> str:
    """
    Функция проверяет размер номера счета на корректность
    и затем маскирует в формате **XXXX
    """

    if okaunt_number is None:
        raise ValueError("номер счета не может быть None")

    if (len(okaunt_number)) != 20 or not okaunt_number.isdigit():
        raise ValueError("номер счета должен состоять и 20 цифр")

    return f"**{okaunt_number[-4:]}"
