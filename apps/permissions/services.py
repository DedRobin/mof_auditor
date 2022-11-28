from collections import OrderedDict

from apps.permissions.models import Permission, PermissionType, PERMISSION_LIST


def create_permission_API(permission_id: int, validated_data: OrderedDict) -> None:
    permission_type = Permission.objects.get(pk=permission_id)
    permission = Permission.objects.create(
        user=validated_data["user"],
        group=validated_data["group"],
    )
    permission = permission.set(permission_type)
