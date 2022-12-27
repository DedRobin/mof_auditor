import ulid
import random
from datetime import datetime
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware

from faker import Faker

from apps.balances.models import Balance, Currency, BALANCE_TYPE_CHOICE
from apps.balances.factories import BalanceFactory
from apps.users.models import User

fake = Faker()


class Command(BaseCommand):
    help = "Generate balances"

    start_datetime = datetime(
        year=2022, month=1, day=1, hour=0, minute=0, second=0, microsecond=0
    )
    start_datetime = make_aware(start_datetime)

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete all balance records",
        )

    def handle(self, *args, **options):
        if options["clear"]:
            Balance.objects.all().delete()

        users = User.objects.all()
        size = 0
        try:
            size = int(input("How much would you like create balances for each user?\n"))
            if size <= 0:
                print("Size must be greater than 0.")
                return
        except ValueError:
            print("The value is incorrect.")
        else:
            for user in users:
                BalanceFactory.create_batch(owner=user, size=size)

        print(f"{size * len(users)} balances has been created.")
