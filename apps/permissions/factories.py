import factory.fuzzy
from factory.django import DjangoModelFactory

from apps.permissions.models import Permission
from apps.users.factories import UserFactory


class PermissionFactory(DjangoModelFactory):
    class Meta:
        model = Permission

    name = factory.Faker("word")
    codename = factory.Faker("word")
    users = factory.SubFactory(UserFactory)
