import ulid
import random
from datetime import datetime
from decimal import Decimal
from django.core.management.base import BaseCommand
from faker import Faker

from apps.balances.models import Balance, BalanceCurrency, BALANCE_TYPE_CHOICE
from apps.transactions.models import (
    Transaction,
    TransactionCategory,
)
from apps.users.models import User

fake = Faker()


class Command(BaseCommand):
    help = "Request currencies"

    start_datetime = datetime(
        year=2022, month=8, day=1, hour=0, minute=0, second=0, microsecond=0
    )

    def handle(self, *args, **options):
        Balance.objects.all().delete()

        users = User.objects.all()
        currencies = BalanceCurrency.objects.all()
        balances = []

        # Create balances
        number = 1
        for user in users:
            for _ in range(3):
                balances.append(
                    Balance(
                        pub_id=ulid.new(),
                        name=f"Balance №{number}",
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

        # Create transactions
        transaction_cat = TransactionCategory.objects.all()
        transactions = []
        for balance in balances:
            for _ in range(10):
                # Random datetime and transaction category
                random_datetime = fake.date_time_between_dates(
                    datetime_start=self.start_datetime, datetime_end="now"
                )
                random_transaction_cat = random.choice(transaction_cat)

                if random_transaction_cat.type == "income":
                    amount = Decimal(str(random.uniform(0.00000, 999.99999)))
                else:
                    amount = Decimal(str(random.uniform(-999.99999, -0.00001)))
                transactions.append(
                    Transaction(
                        balance=balance,
                        amount=amount,
                        category=random_transaction_cat,
                        comment=fake.sentence(),
                        created_at=random_datetime,
                    )
                )
        Transaction.objects.bulk_create(transactions)
        print("Create balances and transactions.")
