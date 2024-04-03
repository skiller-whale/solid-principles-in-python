from api import mastercarp_payment, anchovisa_payment, clamex_payment
from validation import validate_card


class PaymentProcessor:
    def __init__(self, amount, card):
        self.amount = amount
        self.card = card

    def process(self):
        validate_card(self.card)

        if self.card.card_type == "mastercarp":
            mastercarp_payment(self.card, self.amount)

        elif self.card.card_type == "anchovisa":
            anchovisa_payment(self.card, self.amount)

        else:
            raise ValueError("Unknown Card Type")

        print("  ", self.amount, "payment taken", "\n")

    def call(self):
        try:
            self.process()
        except Exception as error:
            print("ERROR PROCESSING PAYMENT: ", error)
