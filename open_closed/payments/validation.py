from datetime import date


def validate_card(card):
    if card.expiry_date < date.today():
        raise ValueError("Card has expired")

    if len(card.cvv) != 3:
        raise ValueError("cvv should be 3 digits long")

    if card.card_type == "mastercarp":
        if int(card.number[0]) < 5:
           raise ValueError("mastercarp card numbers must start with 5 or above")

    elif card.card_type == "anchovisa":
        if int(card.number[0]) >= 5:
           raise ValueError("anchovisa card numbers must start with 4 or less")
