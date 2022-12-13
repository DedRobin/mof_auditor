from django.urls import include, path
from api.groups.views import GroupViewSet

actions_for_list = {"get": "list", "post": "create"}
actions_for_one_note = {"get": "retrieve", "put": "update", "delete": "destroy"}

urlpatterns = [
    path("", GroupViewSet.as_view(actions_for_list), name="groups"),
    path(
        "<int:pk>/",
        GroupViewSet.as_view(actions_for_one_note),
        name="specific_group",
    ),
    path("<int:pk>/permissions/", include("api.permissions.urls")),
    path("<int:pk>/invited_users/", include("api.users.urls")),
]
