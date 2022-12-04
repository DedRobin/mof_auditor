import factory.fuzzy
from factory.django import DjangoModelFactory

from apps.balances.models import (
    Balance,
    BalanceCurrency,
    BALANCE_TYPE_CHOICE,
    BALANCE_PRIVATE_CHOICE,
)
from apps.users.factories import UserFactory


class BalanceCurrencyFactory(DjangoModelFactory):
    class Meta:
        model = BalanceCurrency

    # name = factory.Faker("currency_name")
    # codename = factory.Faker("currency_code")
    name = "Belorussian Ruble"
    codename = "BYN"


class BalanceFactory(DjangoModelFactory):
    class Meta:
        model = Balance

    name = factory.Faker("random_number")
    owner = factory.SubFactory(UserFactory)
    type = factory.fuzzy.FuzzyChoice(dict(BALANCE_TYPE_CHOICE).keys())
    currency = factory.SubFactory(BalanceCurrencyFactory)
    private = factory.Faker("pybool")
    # groups =
