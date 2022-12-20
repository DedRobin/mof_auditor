from django.core.management.base import BaseCommand

from apps.users.models import User
from apps.users.factories import UserFactory
from apps.profiles.factories import ProfileFactory


class Command(BaseCommand):
    help = "Create random users with their profiles."

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete all user records",
        )

    def handle(self, *args, **options):
        if options["clear"]:
            User.objects.all().exclude(is_superuser=True).delete()
        try:
            size = int(input("How much would you like create users?\n"))
            if size <= 0:
                print("Size must be greater than 0.")
                return
        except ValueError:
            print("The value is incorrect.")
        else:
            for _ in range(size):
                user = UserFactory()
                ProfileFactory(user=user)
            print(f"The {size} users has been created.")
