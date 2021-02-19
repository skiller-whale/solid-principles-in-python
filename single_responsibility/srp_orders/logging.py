import pathlib


save_directory = pathlib.Path(__file__).parent / '_invoices'


def get_invoice_filename(order):
    return "INV-" + order.order_id.replace('_', '-')


def format_order(order):
    return f"{order.order_id} | {order.item_name} | {order.amount}"


def log_order(order):
    filename = save_directory / get_invoice_filename(order)
    with open(filename, 'w') as file:
        file.write(format_order(order))
