import factory.fuzzy
from factory.django import DjangoModelFactory

from apps.balances.models import (
    Balance,
    Currency,
    BALANCE_TYPE_CHOICE,
)
from apps.users.factories import UserFactory


class CurrencyFactory(DjangoModelFactory):
    class Meta:
        model = Currency
        exclude = ("currency",)

    currency = factory.Faker("currency")
    name = factory.LazyAttribute(lambda x: x.currency[1])
    codename = factory.LazyAttribute(lambda x: x.currency[0])


class BalanceFactory(DjangoModelFactory):
    class Meta:
        model = Balance

    name = factory.Faker("word")
    owner = factory.SubFactory(UserFactory)
    type = factory.fuzzy.FuzzyChoice(dict(BALANCE_TYPE_CHOICE).keys())
    currency = factory.Iterator(Currency.objects.all())
    private = factory.Faker("pybool")
    created_at = factory.Faker("date_time")
