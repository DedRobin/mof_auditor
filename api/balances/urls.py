from django.urls import path
from api.balances.views import BalanceViewSet

actions_for_list = {"get": "list", "post": "create"}
actions_for_value = {"get": "retrieve", "put": "update", "delete": "destroy"}

urlpatterns = [
    path("", BalanceViewSet.as_view(actions_for_list), name="balances"),
    path("<int:pk>/", BalanceViewSet.as_view(actions_for_value),
         name="RUD_particular_balances"),
]
