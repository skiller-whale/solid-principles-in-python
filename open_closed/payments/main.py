"""Run this script to check the rest of the code works as expected"""


import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from datetime import date

from cards import Mastercarp, AnchoVisa
from payment_processor import PaymentProcessor


if __name__ == '__main__':
    card_1 = Mastercarp('9988776655443322', date(2023, 12, 15), '143')
    PaymentProcessor(23.15, card_1).call()

    card_2 = AnchoVisa('0123456789101112', date(2022, 3, 1), '992')
    PaymentProcessor(250.00, card_2).call()

    # from cards import ClamericanExpress
    # card_3 = ClamericanExpress('2468135746803579', date(2024, 8, 13), '8264')
    # PaymentProcessor(92.99, card_3).call()
