from django.http.request import QueryDict
from typing import Tuple


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
