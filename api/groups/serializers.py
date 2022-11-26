from rest_framework import serializers

from apps.users.models import User


class GroupInfoSerializer(serializers.Serializer):
    owner = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.order_by("username"),
    )
    name = serializers.CharField(
        max_length=255,
    )
    description = serializers.CharField(
    )


class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(
        read_only=True
    )
    pub_id = serializers.CharField(
        max_length=255,
        read_only=True
    )
    group_info = GroupInfoSerializer()
    invited_users = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.order_by("username"),
        many=True,
        required=False
    )
