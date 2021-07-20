"""
There is still a tightly coupled dependency in the CurrencyConverter class, the
format_quote function. If you want to format the quote differently, there is
no way to do this without awkward changes to the class.

You'll now update the CurrencyConverter class to allow injection of an alternate
formatting function.

1. Modify the CurrencyConverter class so a quote formatting function is
   injected, instead of tight coupling to the `format_quote` function.

   (HINT: You can specify the `format_quote` function as the default value for
    the formatter argument, so that you don't need to change other uses)

2. Apply the DIP to think about the interface between the CurrencyConverter and
   the quote formatter function.

   Modify the format_quote method and the CurrencyConverter class to fit this
   interface, and run this exercise script to check that everything still works.

3. Modify the code at the bottom of this exercise script so that the converter
   uses the simple_format_quote function instead of the format_quote function.

   Run this script and check that the output has changed as expected.
"""

from converter.currency_converter import CurrencyConverter, format_quote
from converter.percentage_fee_calculator import PercentageFeeCalculator
from converter.xchange import FxService


def simple_format_quote(amount, fees, to_currency):
    """A formatter that just tells you how much you get. Nothing else."""
    return f"Your quote: {amount - fees:.2f} {to_currency}"


if __name__ == '__main__':
    fx_service = FxService('www.cashforforeigncash.biz')

    calculator = PercentageFeeCalculator(1.2)
    currency_converter = CurrencyConverter(fx_service, calculator)
    quote = currency_converter.generate_quote("GBP", "YEN", 30)

    print('\n', quote)
