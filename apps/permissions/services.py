from collections import OrderedDict
from rest_framework.request import Request

from apps.permissions.models import Permission


def create_permission_api(request: Request, validated_data: OrderedDict) -> None:
    Permission.objects.create(user=request.user, group=validated_data.get("group"))


def update_permission_api(permission_id: int, validated_data: OrderedDict) -> None:
    permission = Permission.objects.get(pk=permission_id)
    permission.types.set(validated_data.get("types"))
