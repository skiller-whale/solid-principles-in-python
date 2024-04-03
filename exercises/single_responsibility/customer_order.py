from datetime import datetime
import pathlib
import textwrap


class CustomerOrder:
    CARD_FEE_RATES = { 'visa': 0.015, 'mastercard': 0.01, 'amex': 0.03 }
    INVOICE_WIDTH = 40
    SALES_TAX = 0.2

    def __init__(self, order_id, item_name, amount):
        self.order_id = order_id
        self.item_name = item_name
        self.amount = amount

    @property
    def _invoice_number(self):
        return "INV-" + self.order_id.replace('_', '-')

    def _format_order(self):
        return f"{self.item_name} | {self.amount}"

    def _format_value(self, key, value):
        return f'{key}:'.ljust(self.INVOICE_WIDTH - 12) + f'{value:.2f}'.rjust(12)

    def get_sales_tax(self):
        """Calculate the amount of sales tax required"""
        return self.SALES_TAX * self.amount

    def get_card_fees(self, card_type):
        """Calculate the fees to pay on a card"""
        return self.CARD_FEE_RATES[card_type] * self.amount

    def get_total_cost(self, card_type):
        """Calculate the total cost paid"""
        return self.amount + self.get_sales_tax() + self.get_card_fees(card_type)

    def log_order(self):
        """Saves a record of the order to file"""
        filename = pathlib.Path(__file__).parent / '_invoices' / self._invoice_number
        with open(filename, 'w') as file:
            file.write(self._format_order())

    def print_invoice(self, card_type):
        """Print out an invoice for a customer paying with a card of `card_type`"""
        bar = '-' * self.INVOICE_WIDTH
        print(textwrap.dedent(f"""\n
            {"INVOICE".center(self.INVOICE_WIDTH)}
            {bar}
            {datetime.now().strftime('%H:%M%p %y-%h-%d').rjust(self.INVOICE_WIDTH)}
            {f"No: {self._invoice_number}".rjust(self.INVOICE_WIDTH)}
            {bar}
            {self._format_order()}
            {bar}
            {self._format_value('Sub Total', self.amount)}
            {self._format_value(f'Sales Tax ({self.SALES_TAX}%)', self.get_sales_tax())}
            {self._format_value('Card Fees', self.get_card_fees(card_type))}
            {self._format_value('Total', self.get_total_cost(card_type))}
            {bar}
            """))


def process_order(order_id, item, amount, card):
    order = CustomerOrder(order_id, item, amount)
    order.log_order()
    order.print_invoice(card)


if __name__ == '__main__':
    process_order('abc_defghi_jkl', "Lunch", 38.20, 'amex')
    process_order('mno_pqrstu_vwx', "Dinner", 24.99, 'visa')
