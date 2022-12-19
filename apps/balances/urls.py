from django.urls import path, include

from apps.balances.views import balance_list, edit_balance, balance_settings

urlpatterns = [
    path("", balance_list, name="balance_list"),
    path("<str:pub_id>/", balance_list, name="balance"),
    path("<str:pub_id>/settings/", balance_settings, name="balance_settings"),
    path("<str:pub_id>/settings/editing/", edit_balance, name="edit_balance"),
]
