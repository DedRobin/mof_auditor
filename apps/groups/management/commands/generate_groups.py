import random
from copy import deepcopy
from faker import Faker
from django.core.management.base import BaseCommand

from apps.users.models import User
from apps.groups.models import GroupInformation, Group

fake = Faker()


class Command(BaseCommand):
    help = "Generate groups"

    def handle(self, *args, **options):
        Group.objects.all().delete()

        users = User.objects.all()

        i = 0
        while i < 10:
            copy_users = deepcopy(users)
            group_info = GroupInformation.objects.create(
                owner=random.choice(users),
                name=fake.word(),
                description=fake.sentence(),
            )
            group = Group.objects.create(
                group_info=group_info,
            )
            for _ in range(5):
                checked_users = []
                invited_user = random.choice(copy_users)
                group.invited_users.add(invited_user)
                checked_users.append(invited_user.username)
                copy_users = copy_users.exclude(username__in=checked_users)
            i += 1
        print("Create groups")
