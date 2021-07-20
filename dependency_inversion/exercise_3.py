"""
The ComplexFeeCalculator defined in converter.complex_fee_calculator calculates
a fee with a percentage and a fixed component. It works differently to the other
fee calculators, and doesn't match the interface needed by the CurrencyConverter.

1. Look at the ComplexFeeCalculator, think about how its interface is different
   to the other calculators, and why it won't work with the CurrencyConverter.

2. Update the ComplexFeeCalculator so that it satisfies the interface expected
   by the CurrencyConverter. Don't make any changes to the CurrencyConverter.

   (See the bottom of this file for additional hints)

3. Update this exercise script to create an instance of the ComplexFeeCalculator
   class, and use this with the CurrencyConverter to charge a fee of:

       £3.50 (GBP) + 1% of the total converted.

   Try running the script to convert 800 CAD to EUR and check everything works.
"""

from converter.currency_converter import CurrencyConverter
from converter.complex_fee_calculator import ComplexFeeCalculator
from converter.xchange import FxService


if __name__ == '__main__':
    fx_service = FxService('www.cashforforeigncash.biz')

    # TODO: Create a ComplexFeeCalculator instance that will work with the
    # CurrencyConverter class, to charge a fixed fee equivalent to £3.50, and a
    # percentage fee equal to 1% of the total converted.
    calculator = ComplexFeeCalculator(fx_service, 3.50, "GBP")

    currency_converter = CurrencyConverter(fx_service, calculator)
    quote = currency_converter.generate_quote(800, "CAD", "EUR")

    print("\nQuote from more complex converter")
    print(quote)
