import factory.fuzzy
from factory.django import DjangoModelFactory

from apps.profiles.models import Profile, GENDER_CHOICE
from apps.users.factories import UserFactory


class ProfileFactory(DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    email = factory.Faker("email")
    gender = factory.fuzzy.FuzzyChoice(dict(GENDER_CHOICE).keys())
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
