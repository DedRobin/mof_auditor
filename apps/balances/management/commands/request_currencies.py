import os
import requests
from django.core.management.base import BaseCommand

from apps.balances.models import BalanceCurrency


class Command(BaseCommand):
    help = "Request currencies"

    def handle(self, *args, **options):
        BalanceCurrency.objects.all().delete()

        url = "https://api.apilayer.com/exchangerates_data/symbols"

        payload = {}
        headers = {
            "apikey": os.environ.get("API_LAYER_KEY")
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        result = response.json()
        currencies = []
        for codename, name in result.get("symbols").items():
            currencies.append(
                BalanceCurrency(
                    name=name,
                    codename=codename
                )
            )
        BalanceCurrency.objects.bulk_create(currencies)
        print("Received current currencies")
