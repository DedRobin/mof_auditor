import requests
from django.core.management.base import BaseCommand

from apps.balances.models import BalanceCurrency


class Command(BaseCommand):
    help = "Request currencies"

    def handle(self, *args, **options):
        BalanceCurrency.objects.all().delete()


