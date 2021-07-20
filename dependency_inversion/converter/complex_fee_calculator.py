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
