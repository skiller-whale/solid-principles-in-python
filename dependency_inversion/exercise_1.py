"""
The converter.currency_converter module contains a CurrencyConverter class,
which is used to generate quotes for a conversion business.

This class uses:

* An `FxService` object to convert money from one currency to another.
* A `PercentageFeeCalculator` which calculates a fee to deduct.
  (in converter.percentage_fee_calculator).

--------------------------------------------------------------------------------

1. Update the CurrencyConverter class to make it more flexible by allowing
   different currencies to be passed as arguments to generate_quote
   (e.g. from_currency and to_currency)

   Update the usage of CurrencyConverter in this exercise script so the output
   remains the same.

2. Inject an instance of the FxService as a dependency to CurrencyConverter
   instead of creating it in the constructor. The new signature should be:

      def __init__(self, fx_service)

   Update the usage of CurrencyConverter in this exercise script.
   (you'll need to create a new FxService instance and pass it as an argument)

3. Decouple the CurrencyConverter and PercentageFeeCalculator, by injecting a
   fee calculator instance to the constructor. The signature should now be:

      def __init__(self, fx_service, fee_calculator):

   Again, update this exercise script so it runs and produces the same output.
"""

from converter.currency_converter import CurrencyConverter
from converter.percentage_fee_calculator import PercentageFeeCalculator
from converter.xchange import FxService


if __name__ == '__main__':
    # Use the converter to generate a quote:
    converter = CurrencyConverter()
    quote = converter.generate_quote(250)
    print()
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
