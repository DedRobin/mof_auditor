import factory.fuzzy
from factory.django import DjangoModelFactory

from apps.invitations.models import Invitation
from apps.users.factories import UserFactory
from apps.groups.factories import GroupFactory


class InvitationFactory(DjangoModelFactory):
    class Meta:
        model = Invitation

    from_who = factory.SubFactory(UserFactory)
    to_who = factory.SubFactory(UserFactory)
    to_a_group = factory.SubFactory(GroupFactory)
