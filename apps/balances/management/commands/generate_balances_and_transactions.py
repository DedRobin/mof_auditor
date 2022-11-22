import ulid
import random
from decimal import Decimal
from django.core.management.base import BaseCommand
from faker import Faker

from apps.balances.models import Balance, BalanceCurrency, BALANCE_TYPE_CHOICE
from apps.transactions.models import Transaction, TransactionCategory, TRANSACTION_TYPE_CHOICE
from apps.users.models import User

fake = Faker()


class Command(BaseCommand):
    help = "Request currencies"

    def handle(self, *args, **options):
        Balance.objects.all().delete()

        users = User.objects.all()
        currencies = BalanceCurrency.objects.all()
        balances = []

        for user in users:
            for _ in range(3):
                balances.append(
                    Balance(
                        pub_id=ulid.new(),
                        name=fake.word(),
                        owner=user,
                        currency=random.choice(currencies),
                        type=random.choice(BALANCE_TYPE_CHOICE)[0],
                        private=False
                    )
                )
        Balance.objects.bulk_create(balances)

        balances = Balance.objects.all()
        transaction_cat = TransactionCategory.objects.all()
        transactions = []
        for balance in balances:
            for _ in range(3):
                random_transaction_cat = random.choice(transaction_cat)
                if random_transaction_cat.type == "income":
                    amount = Decimal(str(random.uniform(0.00001, 999.99999)))
                else:
                    amount = Decimal(str(random.uniform(-999.99999, -0.00001)))

                transactions.append(
                    Transaction(
                        balance=balance,
                        amount=amount,
                        category=random.choice(transaction_cat),
                        comment=fake.sentence(),
                    )
                )
        Transaction.objects.bulk_create(transactions)
        print("Create balances and transactions.")
