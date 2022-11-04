import random
from faker import Faker
from django.core.management.base import BaseCommand

from users.models import User
from profiles.models import Profile, GENDER_CHOICE

fake = Faker()
gender_choice = [gender[0] for gender in GENDER_CHOICE]


class Command(BaseCommand):
    help = "Generate users"

    def handle(self, *args, **options):
        i = 0
        number = int(input("How much users do you want to create?\nEnter number: "))
        while i < number:
            random_gender = random.choice(gender_choice)

            user = User.objects.create(username=fake.user_name())
            user.set_password("password")
            user.save()
            Profile.objects.create(
                user=user,
                gender=random_gender,
                first_name=fake.first_name(),
                last_name=fake.last_name(),
            )
            i += 1
        print(f"Create {number} users.")
