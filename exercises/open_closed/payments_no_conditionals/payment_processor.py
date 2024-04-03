class PaymentProcessor:
    def __init__(self, amount, card):
        self.amount = amount
        self.card = card

    def process(self):
        self.card.validate()
        self.card.take_payment(self.amount)
        print("  ", self.amount, "payment taken", "\n")

    def call(self):
        try:
            self.process()
        except Exception as error:
            print("ERROR PROCESSING PAYMENT: ", error)
