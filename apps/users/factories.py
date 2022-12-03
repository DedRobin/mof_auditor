import factory.fuzzy
from factory.django import DjangoModelFactory
from apps.users.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    password = factory.Faker("md5")
