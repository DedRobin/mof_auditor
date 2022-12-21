from faker import Faker
from django.core.management.base import BaseCommand

from apps.groups.factories import GroupFactory
from apps.users.models import User
from apps.groups.models import Group

fake = Faker()


class Command(BaseCommand):
    help = "Generate groups"

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete all group records",
        )

    def handle(self, *args, **options):
        if options["clear"]:
            Group.objects.all().delete()

        users = User.objects.all()
        size = 0
        try:
            size = int(input("How much would you like create groups for each user?\n"))
            if size <= 0:
                print("Size must be greater than 0.")
                return
        except ValueError:
            print("The value is incorrect.")
        else:
            for user in users:
                groups = GroupFactory.create_batch(size=size, group_info__owner=user)
                for group in groups:
                    invited_users = User.objects.exclude(pk=user.id).order_by("?")[:3]
                    group.invited_users.set(invited_users)

        print(f"{size * len(users)} groups have been created.")
