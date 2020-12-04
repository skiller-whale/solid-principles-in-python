"""
This module contains a CurrencyConverter class, which is used to generate
quotes for a currency conversion business. This class uses:
* An `FxService` object to convert money from one currency to another.
* A `PercentageFeeCalculator` to calculate a fee to deduct.

--------------------------------------------------------------------------------

1. First, make the CurrencyConverter more flexible by allowing different
   currencies to be passed to generate_quote as method parameters (e.g.
   from_currency and to_currency)

   Update the usage of CurrencyConverter at the bottom of the file as well.

2. Instead of creating a new FxService in the constructor of
   CurrencyConverter, pass in the fx_service object as an argument
   (Dependency Injection).

   Update the usage of CurrencyConverter at the bottom of the file as well
   (you'll need to create a new FxService instance and pass it as an argument)

3. Decouple the CurrencyConverter and PercentageFeeCalculator. Afterwards, you
   should be able to pass an instance of the PercentageFeeCalculator into the
   CurrencyConverter __init__ method, and use this to calculate conversion fees.
"""

from util import FxService, format_quote


class CurrencyConverter:
    def __init__(self):
        self.fx_service = FxService('www.fx.com')

    def generate_quote(self, amount):
        from_currency = "USD"
        to_currency = "EUR"
        converted_amount = self.fx_service.convert(from_currency, to_currency, amount)
        fees = PercentageFeeCalculator(0.5).calculate(converted_amount)
        return format_quote(amount, from_currency, to_currency, converted_amount, fees)


class PercentageFeeCalculator:
    def __init__(self, percentage_fee):
        self.fee_ratio = percentage_fee / 100.

    def calculate(self, amount):
        return round(amount * self.fee_ratio, 2)


if __name__ == '__main__':

    # Use the converter to generate a quote:
    converter = CurrencyConverter()
    quote = converter.generate_quote(250)

    print(quote)



# HINTS FOR REFACTORING (in exercise part 3)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# To use dependency injection with the PercentageFeeCalculator, you can refactor
# in 2 stages:
#
#  1. Instead of creating a PercentageFeeCalculator instance in the
#    generate_quote method of CurrencyConverter, do it in the __init__ method.
#    (and assign it to e.g. self.fee_calculator).
#
#    Use self.fee_calculator in the generate_quote method instead of creating a
#    new PercentageFeeCalculator
#
#  2. Then, create a PercentageFeeCalculator instance outside the
#     CurrencyConverter and pass it in as an argument to __init__ (like you did
#     for the FxService).
