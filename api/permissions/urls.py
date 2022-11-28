from django.urls import include, path
from api.permissions.views import PermissionsViewSet

actions_for_list = {"get": "list", "post": "create"}
actions_for_one_note = {"get": "retrieve", "put": "update", "delete": "destroy"}

urlpatterns = [
    path("", PermissionsViewSet.as_view(actions_for_list), name="permissions"),
    path(
        "<int:permission_id>/",
        PermissionsViewSet.as_view(actions_for_one_note),
        name="particular_permission",
    ),
]
