from django.urls import include, path

from api.users.views import UserViewSet

actions_for_list = {
    "get": "list",
}
actions_for_one_note = {
    "get": "retrieve",
}

urlpatterns = [
    path("", UserViewSet.as_view(actions_for_list), name="invited_users"),
    path("<int:user_id>/", UserViewSet.as_view(actions_for_one_note), name="specific_invited_user"),
    path("<int:user_id>/permissions/", include("api.permissions.urls")),
]
