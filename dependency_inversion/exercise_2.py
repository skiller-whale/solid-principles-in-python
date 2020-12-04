"""
This module imports code from exercise_1, and adds a new FixedFeeCalculator.

This calculator applies fee as a fixed amount in one currency. However, this
needs to be converted into whatever currency is being provided. Because of this,
the FixedFeeCalculator.calculate method expects a currency argument.

This means that the FixedFeeCalculator is incompatible with how the 
CurrencyConverter is currently designed to calculate the fee for a 
conversion, so cannot be substituted for the PercentageFeeCalculator 
(try running this script to see what happens)

1. Think about the 'interface' for a generic FeeCalculator that could work with
   the CurrencyConverter class. This interface should allow both the
   PercentageFeeCalculator and FixedFeeCalculator to work with the
   CurrencyConverter.

2. Update the CurrencyConverter, PercentageFeeCalculator, and FixedFeeCalculator
   classes so that they all expect / satisfy this interface. The
   CurrencyConverter class should work the same way, whichever calculator is
   passed in.
"""


from util import FxService
from exercise_1 import CurrencyConverter, PercentageFeeCalculator


class FixedFeeCalculator:
    def __init__(self, fx_service, fee_amount=5, fee_currency="USD"):
        self.fee_amount = fee_amount
        self.fee_currency = fee_currency
        self.fx_service = fx_service

    def calculate(self, target_currency):
        return self.fx_service.convert(
            self.fee_currency,
            target_currency, self.fee_amount
         )


if __name__ == '__main__':

    fx_service = FxService('www.forexr.us')

    # Use the percentage fee converter to generate a quote:
    percentage_fee_calculator = PercentageFeeCalculator(0.5)
    percentage_fee_converter = CurrencyConverter(fx_service, percentage_fee_calculator)
    quote = percentage_fee_converter.generate_quote("USD", "GBP", 500)

    print("\nQuote from percentage fee converter:")
    print(quote)
    print()

    # Use the fixed fee converter to generate a quote:
    fixed_fee_calculator = FixedFeeCalculator(fx_service, 3.50, "GBP")
    fixed_fee_converter = CurrencyConverter(fx_service, fixed_fee_calculator)
    quote = fixed_fee_converter.generate_quote("CAD", "RMB", 300)

    print("Quote from fixed fee converter:")
    print(quote)


"""
OPTIONAL EXTRA

3. The fixed fee calculator needs access to an FxService to perform the
   conversion. At the moment, this is provided through injection to the
   constructor.

   How could you change the interface between the CurrencyConverter and its
   fee calculator to guarantee that the same converter is always used for the
   conversion, and for fee calculation?
"""
