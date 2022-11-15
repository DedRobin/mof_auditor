import random
from django.core.management.base import BaseCommand

from apps.users.models import User
from apps.groups.models import Invitation, Group


class Command(BaseCommand):
    help = "Generate invitations"

    def handle(self, *args, **options):
        Invitation.objects.all().delete()

        admin = User.objects.get(username="dedrobin")
        users = User.objects.exclude(username="dedrobin")
        groups = Group.objects.exclude(group_info__owner=admin)

        i = 0
        while i < 10:
            random_group = random.choice(groups)
            owner = random_group.group_info.owner
            Invitation.objects.create(
                from_who=owner,
                to_who=admin,
                to_a_group=random_group,
            )
            i += 1
        print("Create invitations.")
