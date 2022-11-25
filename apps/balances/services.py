import requests
import os

from decimal import Decimal
from collections import OrderedDict
from rest_framework.request import Request

from apps.balances.models import Balance


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


def create_balance(request: Request, validated_data: OrderedDict) -> None:
    Balance.objects.create(
        name=validated_data["name"],
        owner=request.user,
        type=validated_data["type"],
        currency=validated_data["currency"],
        private=validated_data["private"],
    )
