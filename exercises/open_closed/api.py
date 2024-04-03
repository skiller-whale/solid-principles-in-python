"""
YOU DON'T NEED TO LOOK AT ANY OF THE CODE IN THIS FILE

This module only exists to provide demo functions that simulate taking payments.
"""

import time


def take_payment(card_type, number, amount):
    display_number = f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:]}"
    print(f"Taking {card_type} payment from <{display_number}>", end='')
    for _ in range(4):
        print('.', end='', flush=True)
        time.sleep(0.2)
    print(' complete.')


def mastercarp_payment(card, amount):
    take_payment("Mastercarp", card.number, amount)


def anchovisa_payment(card, amount):
    take_payment("AnchoVisa", card.number, amount)


def clamex_payment(card, amount):
    take_payment("Clamerican Express", card.number, amount)
