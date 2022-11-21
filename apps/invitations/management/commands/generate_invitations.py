import random
from django.core.management.base import BaseCommand

from apps.users.models import User
from apps.groups.models import Group
from apps.invitations.models import Invitation


class Command(BaseCommand):
    help = "Generate invitations"

    def handle(self, *args, **options):
        """Generates a unique invitation from each user"""

        Invitation.objects.all().delete()

        admin = User.objects.get(username="dedrobin")
        checked_users = [admin]
        groups = Group.objects.exclude(group_info__owner__in=checked_users)
        if not groups:
            print("Groups not found. Create it.")
            return None
        i = 0
        while i < len(groups):
            groups = Group.objects.exclude(group_info__owner__in=checked_users)
            random_group = random.choice(groups)
            owner = random_group.group_info.owner
            Invitation.objects.create(
                from_who=owner,
                to_who=admin,
                to_a_group=random_group,
            )
            checked_users.append(owner)
            i += 1
        print("Create invitations.")
