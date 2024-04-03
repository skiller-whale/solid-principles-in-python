class InvoiceCalculator:
    CARD_FEE_RATES = { 'visa': 0.015, 'mastercard': 0.01, 'amex': 0.03 }
    SALES_TAX = 0.2

    def __init__(self, amount, card_type):
        self.amount = amount
        self.card_type = card_type

    @property
    def total(self):
        return round(self.amount + self.sales_tax + self.card_fees, 2)

    @property
    def sales_tax(self):
        return round(self.amount * self.SALES_TAX, 2)

    @property
    def card_fees(self):
        return round(self.amount * self.CARD_FEE_RATES[self.card_type], 2)
