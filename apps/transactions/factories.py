import factory.fuzzy
from factory.django import DjangoModelFactory

from apps.transactions.models import TransactionCategory, Transaction, TRANSACTION_TYPE_CHOICE
from apps.balances.factories import BalanceFactory
from apps.users.factories import UserFactory


class TransactionCategoryFactory(DjangoModelFactory):
    class Meta:
        model = TransactionCategory

    name = factory.Faker("word")
    type = factory.fuzzy.FuzzyChoice(dict(TRANSACTION_TYPE_CHOICE))


class TransactionFactory(DjangoModelFactory):
    class Meta:
        model = Transaction

    balance = factory.SubFactory(BalanceFactory)
    amount = factory.Faker("pydecimal", left_digits=5, right_digits=2)
    category = factory.SubFactory(TransactionCategoryFactory)
    comment = factory.Faker("sentence")
