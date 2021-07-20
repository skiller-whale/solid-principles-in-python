"""
This exercise additionally imports a new FixedFeeCalculator, which sets a fee
at a fixed amount in one currency. This needs to be converted into the target
currency, so it can be subtracted. Because of this, the calculate method
expects a currency argument.

The FixedFeeCalculator is incompatible with the CurrencyConverter's design.
This means it cannot be substituted for the PercentageFeeCalculator (try running
this script to see what happens)

1. Think about what what a generic interface between FeeCalculators and the
   CurrencyConverter class should look like. At the very least, the interface
   should provide enough data for both the PercentageFeeCalculator and
   FixedFeeCalculator to work with the CurrencyConverter.

   This will probably require you to define a new class that represents the data
   being transferred.

2. Update the CurrencyConverter, PercentageFeeCalculator, and FixedFeeCalculator
   so that they all work with this interface. The CurrencyConverter class should
   work the same way, whichever calculator is passed in.
"""

from converter.currency_converter import CurrencyConverter
from converter.percentage_fee_calculator import PercentageFeeCalculator
from converter.fixed_fee_calculator import FixedFeeCalculator
from converter.xchange import FxService


if __name__ == '__main__':

    fx_service = FxService('www.forexr.us')

    # Use the percentage fee converter to generate a quote:
    percentage_fee_calculator = PercentageFeeCalculator(0.5)
    percentage_fee_converter = CurrencyConverter(fx_service, percentage_fee_calculator)
    quote = percentage_fee_converter.generate_quote("USD", "GBP", 500)

    print("\nQuote from percentage fee converter:")
    print(quote)

    # Use the fixed fee converter to generate a quote:
    fixed_fee_calculator = FixedFeeCalculator(fx_service, 3.50, "GBP")
    fixed_fee_converter = CurrencyConverter(fx_service, fixed_fee_calculator)
    quote = fixed_fee_converter.generate_quote("CAD", "RMB", 300)

    print("\nQuote from fixed fee converter:")
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
