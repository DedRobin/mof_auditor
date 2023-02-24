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
from apps.transactions.factories import TransactionFactory

fake = Faker()


class Command(BaseCommand):
    help = "Generate transactions"

    start_datetime = datetime(
        year=2022, month=1, day=1, hour=0, minute=0, second=0, microsecond=0
    )
    start_datetime = make_aware(start_datetime)

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete all transaction records",
        )

    def handle(self, *args, **options):
        if options["clear"]:
            Transaction.objects.all().delete()

        transaction_cat = TransactionCategory.objects.all()
        balances = Balance.objects.all()
        size = 0

        try:
            size = int(
                input("How much would you like to create transaction for each balance?\n")
            )
            if size <= 0:
                print("Size must be greater than 0.")
                return
        except ValueError:
            print("The value is incorrect.")
        else:
            for balance in balances:
                for _ in range(size):
                    random_transaction_cat = random.choice(transaction_cat)
                    if random_transaction_cat.type == "income":
                        amount = Decimal(str(random.uniform(0.00000, 999.99999)))
                    else:
                        amount = Decimal(str(random.uniform(-999.99999, -0.00001)))
                    TransactionFactory(
                        balance=balance,
                        amount=amount,
                        category=random_transaction_cat,
                    )

        print("Create transactions.")
