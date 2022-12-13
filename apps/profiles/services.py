from collections import OrderedDict

from apps.profiles.models import Profile


def update_profile_api(user: str, validated_data: OrderedDict) -> None:
    Profile.objects.filter(user=user).update(**validated_data)
