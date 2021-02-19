import sys, os; sys.path.append(os.path.dirname(__file__))

from customer_order_data import CustomerOrderData
from invoice_calculator import InvoiceCalculator
from invoice_printer import InvoicePrinter
from logging import log_order


def process_order(order_id, item, amount, card_type):
    order = CustomerOrderData(order_id, item, amount)
    log_order(order)
    calculator = InvoiceCalculator(order.amount, card_type)
    printer = InvoicePrinter(order, calculator)
    printer.print()


if __name__ == '__main__':
    process_order('abc_defghi_jkl', "Lunch", 38.20, 'amex')
    process_order('mno_pqrstu_vwx', "Dinner", 24.99, 'visa')
