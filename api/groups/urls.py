from django.urls import include, path
from api.groups.views import GroupViewSet

actions_for_list = {"get": "list", "post": "create"}
actions_for_one_note = {"get": "retrieve", "put": "update", "delete": "destroy"}

urlpatterns = [
    path("", GroupViewSet.as_view(actions_for_list), name="groups"),
    path(
        "<int:pk>/",
        GroupViewSet.as_view(actions_for_one_note),
        name="particular_group",
    ),
    # path("<int:pk>/transactions/", include("api.transactions.urls")),
]
