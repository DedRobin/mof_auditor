import os
import requests
from django.core.management.base import BaseCommand
from django.conf import settings

from apps.balances.models import Currency


class Command(BaseCommand):
    help = "Getting actual currency rates"

    def handle(self, *args, **options):
        if settings.OTHER_CURRENCIES:
            symbols = "".join(f"%20{s}%2C" for s in settings.OTHER_CURRENCIES)
        else:
            symbols = ""

        url_rates = "https://api.apilayer.com/exchangerates_data/latest?symbols={0}&base={1}"
        url_rates = url_rates.format(symbols, settings.BASE_CURRENCY)
        url_symbols = "https://api.apilayer.com/exchangerates_data/symbols"

        payload = {}
        headers = {"apikey": os.environ.get("API_LAYER_KEY")}

        response_rates = requests.request("GET", url_rates, headers=headers, data=payload).json()
        response_symbols = requests.request("GET", url_symbols, headers=headers, data=payload).json()

        currencies = []
        for codename, rate in response_rates.get("rates").items():
            name = response_symbols["symbols"].get(codename)
            currencies.append(Currency(name=name, codename=codename, rate=rate))
        Currency.objects.bulk_create(currencies)

        print("Updates currency rates.")
