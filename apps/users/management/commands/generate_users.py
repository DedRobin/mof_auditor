import random
from faker import Faker
from django.core.management.base import BaseCommand

from apps.users.models import User
from apps.users.factories import UserFactory
from apps.profiles.factories import ProfileFactory
from apps.profiles.models import Profile, GENDER_CHOICE

fake = Faker()
gender_choice = [gender[0] for gender in GENDER_CHOICE]


class Command(BaseCommand):
    help = "Create random users with their profiles."

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            type=bool,
            help="Delete all user records",
        )

    def handle(self, *args, **options):
        if options.get("clear", None):
            User.objects.all().exclude(is_superuser=True).delete()
        # try:
        size = int(input("How much would you like create users?\n"))
        # except:
        # print(f'The value "{size}" is incorrect. Enter a number greater than 0.')
        for _ in range(size):
            user = UserFactory()
            ProfileFactory(user=user)
        print(f"The {size} users has been created.")
