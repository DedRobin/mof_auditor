from django.urls import path
from api.transactions.views import TransactionViewSet, DownloadTransactionAPI

actions_for_list = {"get": "list", "post": "create"}
actions_for_one_note = {"get": "retrieve", "put": "update", "delete": "destroy"}

urlpatterns = [
    path("", TransactionViewSet.as_view(actions_for_list), name="transactions"),
    path(
        "<int:transaction_id>/",
        TransactionViewSet.as_view(actions_for_one_note),
        name="particular_transaction",
    ),
    path("download/", DownloadTransactionAPI.as_view({"get": "list"}), name="download"),

]
