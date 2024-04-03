from functools import lru_cache


class CurrencyError(Exception):
    pass

class FxProviderError(Exception):
    pass


CONVERSIONS = {
    "USD": 1,
    "GBP": 1.34,
    "EUR": 1.21,
    "YEN": 0.0096,
    "RMB": 0.15,
    "CAD": 0.77,
}

PROVIDER_BIAS = {
  'www.fx.com': 1,
  'www.forexr.us': 1.03,
  'www.cashforforeigncash.biz': 0.97,
}


def get_provider_bias(provider):
    bias = PROVIDER_BIAS.get(provider)
    if bias is None:
        raise FxProviderError(f"Unrecognised FX provider {provider}")
    return bias


def get_conversion_to_usd(currency):
    rate = CONVERSIONS.get(currency)
    if rate is None:
        raise CurrencyError(f"No rates available for currency: {currency}")

    return rate


@lru_cache()
def get_conversion_rate(from_currency, to_currency, provider):
    from_rate = get_conversion_to_usd(from_currency)
    to_rate = get_conversion_to_usd(to_currency)
    provider_bias = get_provider_bias(provider)
    return (from_rate / to_rate) * provider_bias


class FxService:
    def __init__(self, provider):
        self.provider = provider

    def convert(self, from_currency, to_currency, amount):
        rate = get_conversion_rate(from_currency, to_currency, self.provider)
        converted_amount = amount * rate
        return round(converted_amount, 2)
