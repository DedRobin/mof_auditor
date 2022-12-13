from django.urls import include, path
from api.balances.views import BalanceViewSet

actions_for_list = {"get": "list", "post": "create"}
actions_for_one_note = {"get": "retrieve", "put": "update", "delete": "destroy"}

urlpatterns = [
    path("", BalanceViewSet.as_view(actions_for_list), name="balances"),
    path(
        "<int:pk>/",
        BalanceViewSet.as_view(actions_for_one_note),
        name="specific_balance",
    ),
    path("<int:pk>/transactions/", include("api.transactions.urls")),
]
