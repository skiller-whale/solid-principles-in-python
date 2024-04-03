class PercentageFeeCalculator:
    """A calculator class to return a percentage of a monetary fee"""
    def __init__(self, percentage):
        self.fee_ratio = percentage / 100.

    def calculate(self, amount):
        return round(amount * self.fee_ratio, 2)
