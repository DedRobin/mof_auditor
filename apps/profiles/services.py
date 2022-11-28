from collections import OrderedDict

from apps.profiles.models import Profile


def update_profile_API(user: str, validated_data: OrderedDict) -> None:
    Profile.objects.filter(user=user).update(
        email=validated_data["email"],
        gender=validated_data["gender"],
        first_name=validated_data["first_name"],
        last_name=validated_data["last_name"],
    )
