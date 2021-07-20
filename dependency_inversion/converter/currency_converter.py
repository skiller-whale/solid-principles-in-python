from .xchange import FxService
from .percentage_fee_calculator import PercentageFeeCalculator


def format_quote(amount, from_currency, to_currency, converted_amount, fees):
    return f"Your quote to convert {amount} {from_currency} into {to_currency}:" \
           f"\n\t{converted_amount} {to_currency} (Fees: {fees} {to_currency})"


class CurrencyConverter:
    """A class to convert between currencies, and charge an appropriate fee"""
    def __init__(self):
        self.fx_service = FxService('www.fx.com')

    def generate_quote(self, amount):
        from_currency = "USD"
        to_currency = "EUR"
        converted_amount = self.fx_service.convert(from_currency, to_currency, amount)
        fees = PercentageFeeCalculator(0.5).calculate(converted_amount)
        return format_quote(amount, from_currency, to_currency, converted_amount, fees)
