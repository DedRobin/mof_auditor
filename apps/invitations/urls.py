from django.urls import path

from apps.invitations.views import invitation_list

urlpatterns = [
    path("", invitation_list, name="invitation_list"),
]
