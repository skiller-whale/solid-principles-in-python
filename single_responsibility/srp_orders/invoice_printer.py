import textwrap
from datetime import datetime


class InvoicePrinter:
    WIDTH = 40

    def __init__(self, order, invoice_calculator):
        self.order = order
        self.invoice_calculator = invoice_calculator

    def _format_value(self, key, value):
        return f'{key}:'.ljust(self.WIDTH - 12) + f'{value:.2f}'.rjust(12)

    @property
    def _invoice_number(self):
        return "INV-" + self.order.order_id.replace('_', '-')

    def print(self):
        bar = '-' * self.WIDTH
        print(textwrap.dedent(f"""\n
            {"INVOICE".center(self.WIDTH)}
            {bar}
            {datetime.now().strftime('%H:%M%p %y-%h-%d').rjust(self.WIDTH)}
            {f"No: {self._invoice_number}".rjust(self.WIDTH)}
            {bar}
            {self.order.item_name} | {self.order.amount}
            {bar}
            {self._format_value('Sub Total', self.invoice_calculator.amount)}
            {self._format_value(f'Sales Tax ({self.invoice_calculator.SALES_TAX}%)',
                               self.invoice_calculator.sales_tax)}
            {self._format_value('Card Fees', self.invoice_calculator.card_fees)}
            {self._format_value('Total', self.invoice_calculator.total)}
            {bar}
            """))
