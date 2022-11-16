from django.urls import path

from apps.groups.views import \
    create_group, \
    edit_group, \
    invitation_list, \
    group_settings, \
    group_members, \
    group_privacy

urlpatterns = [
    path("create/", create_group, name="create_group"),
    path("<str:pub_id>/settings/", group_settings, name="group_settings"),
    path("<str:pub_id>/settings/editing/", edit_group, name="group_editing"),
    path("<str:pub_id>/settings/privacy/", group_privacy, name="group_privacy"),
    path("<str:pub_id>/settings/members/", group_members, name="group_members"),
    path("invitations/", invitation_list, name="group_invitations"),
]
