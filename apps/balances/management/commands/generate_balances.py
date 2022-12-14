import ulid
import random
from datetime import datetime
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware

from faker import Faker

from apps.balances.models import Balance, Currency, BALANCE_TYPE_CHOICE
from apps.users.models import User

fake = Faker()


class Command(BaseCommand):
    help = "Generate balances"

    start_datetime = datetime(
        year=2022, month=1, day=1, hour=0, minute=0, second=0, microsecond=0
    )
    start_datetime = make_aware(start_datetime)

    def handle(self, *args, **options):
        Balance.objects.all().delete()

        users = User.objects.all()
        currencies = Currency.objects.all()
        balances = []

        # Create balances
        number = 1
        for user in users:
            for _ in range(3):
                balances.append(
                    Balance(
                        pub_id=ulid.new(),
                        name=f"Wallet №{number}",
                        owner=user,
                        currency=random.choice(currencies),
                        type=random.choice(BALANCE_TYPE_CHOICE)[0],
                        private=False,
                    )
                )
                number += 1

        Balance.objects.bulk_create(balances)

        # Add each balance in some group
        balances = Balance.objects.all()
        for balance in balances:
            for _ in range(2):
                user_groups = balance.owner.user_groups.all()
                balance.groups.add(random.choice(user_groups))

        print("Create balances.")
