from django.urls import path

from apps.groups.views import create_group, edit_group, invitation_list

urlpatterns = [
    path("create/", create_group, name="create_group"),
    path("<str:pub_id>/settings/", edit_group, name="group_settings"),
    path("invitations/", invitation_list, name="group_invitations"),
]
