from django.urls import include, path
from api.invitations.views import InvitationViewSet

actions_for_list = {
    "get": "list",
    "post": "create",
}
actions_for_one_note = {
    "get": "retrieve",
    # "put": "update",
    # "delete": "destroy",
}

urlpatterns = [
    path("", InvitationViewSet.as_view(actions_for_list), name="invitations"),
    path(
        "<int:pk>/",
        InvitationViewSet.as_view(actions_for_one_note),
        name="specific_invitation",
    )
]
