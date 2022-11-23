from rest_framework import serializers

from api.auth.serializers import UsernameSerializer, ProfileSerializer
from apps.profiles.models import GENDER_CHOICE


class GroupInfoSerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=255,
    )
    description = serializers.CharField()


class InvitedUserSerializer(UsernameSerializer):
    profile = ProfileSerializer()


class GroupSerializer(serializers.Serializer):
    group_info = GroupInfoSerializer()
    invited_users = InvitedUserSerializer(many=True, required=False)
