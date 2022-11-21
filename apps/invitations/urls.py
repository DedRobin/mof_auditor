from django.urls import path

from apps.invitations.views import invitation_list, send_invitation

urlpatterns = [
    path("", invitation_list, name="invitation_list"),
    path("send/", send_invitation, name="send_invitation"),
]
