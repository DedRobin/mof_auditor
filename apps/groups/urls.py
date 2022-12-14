from django.urls import path

from apps.groups.views import (
    create_group,
    edit_group,
    group_settings,
    group_members,
    group_privacy,
    balance_and_transaction_list,
    get_linked_balances,
)

urlpatterns = [
    path("create/", create_group, name="create_group"),
    path(
        "<str:pub_id>/",
        balance_and_transaction_list,
        name="balance_and_transaction_list",
    ),
    path("<str:pub_id>/settings/", group_settings, name="group_settings"),
    path("<str:pub_id>/settings/editing/", edit_group, name="group_editing"),
    path("<str:pub_id>/settings/privacy/", group_privacy, name="group_privacy"),
    path("<str:pub_id>/settings/members/", group_members, name="group_members"),
    path(
        "<str:pub_id>/settings/linked_balances/",
        get_linked_balances,
        name="linked_balances",
    ),
]
