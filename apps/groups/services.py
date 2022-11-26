from collections import OrderedDict
from django.http.request import QueryDict
from rest_framework.request import Request
from typing import Tuple

from apps.groups.models import GroupInformation, Group


def get_users_and_permission_type(permission_query_dict: QueryDict) -> Tuple[list, str]:
    permission_query_dict = permission_query_dict
    users = []
    permission_type = "read"

    if permission_query_dict.getlist("invited_users_read"):
        users = permission_query_dict.getlist("invited_users_read")
        permission_type = "read"

    elif permission_query_dict.getlist("invited_users_create"):
        users = permission_query_dict.getlist("invited_users_create")
        permission_type = "create"

    elif permission_query_dict.getlist("invited_users_update"):
        users = permission_query_dict.getlist("invited_users_update")
        permission_type = "update"

    elif permission_query_dict.getlist("invited_users_delete"):
        users = permission_query_dict.getlist("invited_users_delete")
        permission_type = "delete"

    return users, permission_type


def create_group(request: Request, validated_data: OrderedDict) -> None:
    group_info = GroupInformation.objects.create(
        owner=request.user,
        name=validated_data["group_info"]["name"],
        description=validated_data["group_info"]["description"],
    )
    group = Group.objects.create(
        group_info=group_info,
    )
    group.invited_users.set(validated_data["invited_users"])


def update_group(group_id: int, validated_data: OrderedDict) -> None:
    group = Group.objects.get(pk=group_id)
    group_info = group.group_info

    # Updates group information
    group_info.name = validated_data["group_info"]["name"]
    group_info.description = validated_data["group_info"]["description"]
    group_info.save()

    # Updates invited users
    group.invited_users.set(validated_data["invited_users"])
