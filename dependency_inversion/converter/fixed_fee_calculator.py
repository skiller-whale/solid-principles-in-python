class FixedFeeCalculator:
    def __init__(self, fx_service, fee_amount=5, fee_currency="USD"):
        self.fee_amount = fee_amount
        self.fee_currency = fee_currency
        self.fx_service = fx_service

    def calculate(self, target_currency):
        return self.fx_service.convert(
            self.fee_currency,
            target_currency, self.fee_amount
         )
