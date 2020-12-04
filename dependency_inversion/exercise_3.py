"""
The ComplexFeeCalculator defined in this module can be used to calculate a fee
with a percentage and a fixed component.

At the moment, this class works quite differently to the other two fee
calculators you've worked with, and does not satisfy the interface required by
the CurrencyConverter.

1. Look at the ComplexFeeCalculator, and think about the ways in which its
   interface is different to the other calculators, and why it would not work
   with the CurrencyConverter.

2. Update the ComplexFeeCalculator so that it satisfies the interface expected
   by the CurrencyConverter. Do not make any changes to the CurrencyConverter
   class.

   See the bottom of this file for additional hints!

3. In the code at the bottom of the script, create an instance of the
   ComplexFeeCalculator class, and use this with the CurrencyConverter to
   charge a fixed fee of £3.50 (GBP) + 1% of the total converted.

   Try running the script to convert 800CAD to EUR and check everything works.
"""

from util import FxService

from exercise_1 import CurrencyConverter


class ComplexFeeCalculator:
    """Charges a fixed fee, plus a percentage of the total

    Example usage:

    >>> calculator = ComplexFeeCalculator(fx_service_instance, 5, "GBP")
    >>> calculator.set_target_currency("EUR")
    >>> calculator.calculate_fee(1000, percentage=1)

    This will calculate the fee in EUR (€) to convert to 1000€. This fee
    includes:
     * The € equivalent of 5 GBP   (the fixed fee)
     * 1% of the total             (the percentage fee)
    """
    def __init__(self, fx_service, fixed_fee_amount, fixed_fee_currency):
        self.fx_service = fx_service
        self.fixed_fee_amount = fixed_fee_amount
        self.fixed_fee_currency = fixed_fee_currency
        self.target_currency = "USD"

    def set_target_currency(self, target_currency):
        self.target_currency = target_currency

    def calculate_fee(self, amount, percentage):
        fixed_fee = self.fx_service.convert(self.fixed_fee_currency,
                                            self.target_currency,
                                            self.fixed_fee_amount)
        percentage_fee = amount * percentage / 100.  # percentage fee
        return round(percentage_fee + fixed_fee, 2)


if __name__ == '__main__':
    fx_service = FxService('www.cashforforeigncash.biz')

    # TODO: Create a ComplexFeeCalculator instance that will work with the
    # CurrencyConverter class, to charge a fixed fee equivalent to £3.50, and a
    # percentage fee equal to 1% of the total converted.
    calculator = ComplexFeeCalculator(fx_service, ...)

    currency_converter = CurrencyConverter(fx_service, calculator)
    quote = currency_converter.generate_quote("CAD", "EUR", 800)

    print("Quote from more complex converter")
    print(quote)



# HINTS

# The CurrencyCalculator class expects to receive a calculator with a well
# defined interface.
#
# Specifically the calculator should:
#
# * Have a method `calculate(amount, target_currency)`
#
# * The `calculate` method should return the fee to convert `amount`, in the
#   `target_currency` specified.


# At first, the ComplexFeeCalculator doesn't satisfy this interface so it will
# need restructuring. You won't need to edit the CurrencyConverter class though.
#
# You'll need to:
#
# 1. Rename the method calculate_fee to calculate
#    (because this is the method name expected by CurrencyConverter)
#
# 2. Move the percentage argument to the __init__ method instead of calculate, and
#    store it as an instance attribute so it can be used in the calculate method.
#    (CurrencyConverter only passes amount and target_currency to calculate)
#
# 3. Accept target_currency as a second argument to the calculate method, and use
#    it to calculate the fixed fee.
