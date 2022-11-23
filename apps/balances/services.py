import requests
import os

from decimal import Decimal


def get_currency_convert_result(
        from_amount: Decimal,
        from_currency: str,
        to_currency: str) -> Decimal:
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={from_amount}"

    payload = {}
    headers = {
        "apikey": os.environ.get("API_LAYER_KEY")
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    response = response.json()

    return response.get("result")
