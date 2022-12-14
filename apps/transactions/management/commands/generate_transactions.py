import random
from datetime import datetime
from decimal import Decimal
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware

from faker import Faker

from apps.balances.models import Balance
from apps.transactions.models import (
    Transaction,
    TransactionCategory,
)

fake = Faker()


class Command(BaseCommand):
    help = "Generate transactions"

    start_datetime = datetime(
        year=2022, month=1, day=1, hour=0, minute=0, second=0, microsecond=0
    )
    start_datetime = make_aware(start_datetime)

    def handle(self, *args, **options):
        Transaction.objects.all().delete()

        transaction_cat = TransactionCategory.objects.all()
        balances = Balance.objects.all()
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
        print("Create transactions.")
