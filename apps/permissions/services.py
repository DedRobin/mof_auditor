from collections import OrderedDict

from apps.permissions.models import Permission


def update_permission_api(permission_id: int, validated_data: OrderedDict) -> None:
    permission = Permission.objects.get(pk=permission_id)
    permission.types.set(validated_data.get("types"))
