from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(number:str) -> str:
    number_split = number.split(" ")
    if len(number_split[-1]) == 16:
        mask = get_mask_card_number(number_split[-1])
    else:
        mask = get_mask_account(number_split[-1])

    number_mask = ' '.join(number_split[0:-1]) + ' ' +  mask

    return number_mask