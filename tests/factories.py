import factory.fuzzy
from factory.django import DjangoModelFactory

from apps.balances.models import Balance, BalanceCurrency
from apps.users.models import User
from apps.groups.models import Group, GroupInformation
from apps.profiles.models import Profile, GENDER_CHOICE
from apps.permissions.models import Permission
from apps.balances.models import BALANCE_TYPE_CHOICE, BALANCE_PRIVATE_CHOICE


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    password = factory.Faker("md5")


class ProfileFactory(DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    email = factory.Faker("email")
    gender = factory.fuzzy.FuzzyChoice(dict(GENDER_CHOICE).keys())
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")


class BalanceCurrencyFactory(DjangoModelFactory):
    class Meta:
        model = BalanceCurrency

    name = factory.Faker("currency_name")
    codename = factory.Faker("currency_code")


class GroupInformationFactory(DjangoModelFactory):
    class Meta:
        model = GroupInformation

    owner = factory.SubFactory(UserFactory)
    name = factory.Faker("word")
    description = factory.Faker("sentence")


class PermissionFactory(DjangoModelFactory):
    class Meta:
        model = Permission

    name = factory.Faker("word")
    codename = factory.Faker("word")
    users = factory.SubFactory(UserFactory)


class GroupFactory(DjangoModelFactory):
    class Meta:
        model = Group

    group_info = factory.SubFactory(GroupInformationFactory)
    pub_id = factory.Faker("md5")
    invited_users = factory.SubFactory(UserFactory)
    permissions = factory.SubFactory(PermissionFactory)


class BalanceFactory(DjangoModelFactory):
    class Meta:
        model = Balance

    name = f"Balance №{factory.Faker('random_number')}"
    owner = factory.SubFactory(UserFactory)
    type = factory.fuzzy.FuzzyChoice(dict(BALANCE_TYPE_CHOICE).keys())
    private = factory.Faker("pybool")
    # groups =
