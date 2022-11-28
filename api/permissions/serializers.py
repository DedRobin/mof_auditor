from rest_framework import serializers

from apps.permissions.models import PermissionType


class PermissionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    types = serializers.PrimaryKeyRelatedField(
        queryset=PermissionType.objects.all(), many=True
    )
    user = serializers.StringRelatedField()
    group = serializers.StringRelatedField()
