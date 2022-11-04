import requests
from django.core.management.base import BaseCommand

from balances.models import BalanceCurrency


class Command(BaseCommand):
    help = "Request currencies"

    def handle(self, *args, **options):
        BalanceCurrency.objects.all().delete()
        response = requests.get("https://www.nbrb.by/api/exrates/rates?periodicity=0")
        response = response.json()
        currencies = [
            {
                "name": currency.get("Cur_Name"),
                "codename": currency.get("Cur_Abbreviation"),
            }
            for currency in response
        ]
        for currency in currencies:
            name = currency.get("name")
            codename = currency.get("codename")
            BalanceCurrency.objects.create(name=name, codename=codename)
        BalanceCurrency.objects.create(name="Белорусский рубль", codename="BYN")

        print(f"Update currencies.")
