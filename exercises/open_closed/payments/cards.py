class Card:
    def __init__(self, card_type, number, expiry_date, cvv):
        self.card_type = card_type
        self.number = number
        self.expiry_date = expiry_date
        self.cvv = cvv


class Mastercarp(Card):
    def __init__(self, number, expiry_date, cvv):
        super().__init__("mastercarp", number, expiry_date, cvv)


class AnchoVisa(Card):
    def __init__(self, number, expiry_date, cvv):
        super().__init__("anchovisa", number, expiry_date, cvv)
