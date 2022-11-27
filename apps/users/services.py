from apps.users.models import User
from apps.profiles.models import Profile


def create_user_and_profile(
    username: str,
    password: str,
    gender: str = None,
    email: str = None,
    first_name: str = None,
    last_name: str = None,
):
    user = User(
        username=username,
    )
    user.set_password(password)
    user.save()

    Profile.objects.create(
        user=user,
        gender=gender,
        email=email,
        first_name=first_name,
        last_name=last_name,
    )
