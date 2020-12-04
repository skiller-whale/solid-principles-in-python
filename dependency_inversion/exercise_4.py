"""
There is still a tightly coupled dependency in the CurrencyConverter class, the
format_quote function. If you wanted to format the quote differently, there is
no way to do this without significantly changing the class.

Another `simple_format_quote` function is defined in this module. You'll now
update the CurrencyConverter class to allow the injection of this function.

1. Modify the CurrencyConverter class in exercise_1 so a quote formatting
   function is injected, rather than being fixed as the `format_quote` function.

   (HINT: You can specify the `format_quote` function as a default argument
    value, so that you don't need to change any of your other code)

2. Use the DIP to ensure that simple_format_quote can be injected to the
   CurrencyConverter class, and will be used to produce a differently formatted
   output.

3. Modify the code at the bottom of this module so that the converter uses the
   simple_format_quote function instead of the format_quote function.
"""

from util import FxService

from exercise_1 import CurrencyConverter, PercentageFeeCalculator


def simple_format_quote(amount, fees, to_currency):
    """A formatter that just tells you how much you get. Nothing else."""
    return f"Your quote: {amount - fees} {to_currency}"


if __name__ == '__main__':
    fx_service = FxService('www.cashforforeigncash.biz')

    calculator = PercentageFeeCalculator(1.2)
    currency_converter = CurrencyConverter(fx_service, calculator)
    quote = currency_converter.generate_quote("GBP", "YEN", 30)

    print(quote)
