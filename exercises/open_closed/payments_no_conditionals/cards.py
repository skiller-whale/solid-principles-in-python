from api import mastercarp_payment, anchovisa_payment, clamex_payment
from datetime import date


class Card:
    def __init__(self, card_type, number, expiry_date, cvv):
        self.card_type = card_type
        self.number = number
        self.expiry_date = expiry_date
        self.cvv = cvv

    def validate(self):
        if self.expiry_date < date.today():
            raise ValueError("Card has expired")

        if len(self.cvv) != 3:
            raise ValueError("cvv should be 3 digits long")


class Mastercarp(Card):
    def __init__(self, number, expiry_date, cvv):
        super().__init__("mastercarp", number, expiry_date, cvv)

    def take_payment(self, amount):
        mastercarp_payment(self, amount)

    def validate(self):
        super().validate()
        if int(self.number[0]) < 5:
            raise ValueError("mastercarp card numbers must start with 5 or above")


class AnchoVisa(Card):
    def __init__(self, number, expiry_date, cvv):
        super().__init__("anchovisa", number, expiry_date, cvv)

    def take_payment(self, amount):
        anchovisa_payment(self, amount)

    def validate(self):
        super().validate()
        if int(self.number[0]) >= 5:
            raise ValueError("anchovisa card numbers must start with 4 or less")
