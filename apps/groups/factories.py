import factory.fuzzy
from factory.django import DjangoModelFactory

from apps.groups.models import Group, GroupInformation
from apps.users.factories import UserFactory


class GroupInformationFactory(DjangoModelFactory):
    class Meta:
        model = GroupInformation

    owner = factory.SubFactory(UserFactory)
    name = factory.Faker("word")
    description = factory.Faker("sentence")


class GroupFactory(DjangoModelFactory):
    class Meta:
        model = Group

    group_info = factory.SubFactory(GroupInformationFactory)
    # invited_users = factory.SubFactory(UserFactory)
    # permissions = factory.SubFactory(PermissionFactory)
