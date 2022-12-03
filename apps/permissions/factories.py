import factory.fuzzy
from factory.django import DjangoModelFactory

from apps.groups.factories import GroupFactory
from apps.permissions.models import Permission, PermissionType
from apps.users.factories import UserFactory


class PermissionTypeFactory(DjangoModelFactory):
    class Meta:
        model = PermissionType

    # name = factory.fuzzy.FuzzyChoice(dict(PERMISSION_LIST).keys())
    name = None


class PermissionFactory(DjangoModelFactory):
    class Meta:
        model = Permission

    user = factory.SubFactory(UserFactory)
    group = factory.SubFactory(GroupFactory)

    @factory.post_generation
    def types(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for p_type in extracted:
                self.types.add(p_type)
