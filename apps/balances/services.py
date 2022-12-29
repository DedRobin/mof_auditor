import requests
import os
from django.forms import Form
from decimal import Decimal
from collections import OrderedDict
from django.core.handlers.wsgi import WSGIRequest
from rest_framework.request import Request

from apps.balances.forms import CurrencyConvertForm
from apps.balances.models import Balance, Currency


def get_currency_form(request: WSGIRequest) -> Form:
    form = CurrencyConvertForm(request.GET)
    if form.is_valid():
        from_amount = form.cleaned_data["from_amount"]
        from_currency = form.cleaned_data["from_currency"]
        to_currency = form.cleaned_data["to_currency"]
        convert_result = _get_convert_result(
            from_amount=from_amount,
            from_currency=from_currency.codename,
            to_currency=to_currency.codename,
        )

        form_data = {
            "from_amount": from_amount,
            "from_currency": from_currency,
            "to_currency": to_currency,
            "result": convert_result,
        }
        form = CurrencyConvertForm(form_data)
    else:
        form = CurrencyConvertForm()
    return form


def _get_convert_result(
        from_amount: Decimal, from_currency: str, to_currency: str
) -> Decimal:
    url = "https://api.apilayer.com/exchangerates_data/convert?to={0}&from={1}&amount={2}".format(
        to_currency, from_currency, from_amount
    )

    payload = {}
    headers = {"apikey": os.environ.get("API_LAYER_KEY")}

    response = requests.request("GET", url, headers=headers, data=payload)

    response = response.json()

    return response.get("result")


def create_balance(request: WSGIRequest) -> None:
    Balance.objects.create(
        name=request.POST.get("name"),
        owner=request.user,
        type=request.POST.get("type"),
        currency=Currency.objects.get(pk=request.POST.get("currency")),
        private=request.POST.get("private"),
    )


def create_balance_api(request: Request, validated_data: OrderedDict) -> None:
    Balance.objects.create(
        name=validated_data["name"],
        owner=request.user,
        type=validated_data["type"],
        currency=validated_data["currency"],
        private=validated_data["private"],
    )


def update_balance_api(balance_id: int, validated_data: OrderedDict) -> None:
    balance = Balance.objects.filter(pk=balance_id)
    balance.update(
        name=validated_data["name"],
        type=validated_data["type"],
        currency=validated_data["currency"],
        private=validated_data["private"],
    )
