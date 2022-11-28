from rest_framework import serializers

from apps.permissions.models import PermissionType
from apps.groups.models import Group
from apps.users.models import User
from api.groups.serializers import CustomGroupSerializer


class PermissionSerializer(serializers.Serializer):
    types = serializers.PrimaryKeyRelatedField(
        queryset=PermissionType.objects.all(), many=True
    )
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    group = CustomGroupSerializer(queryset=Group.objects.all(), required=False)
