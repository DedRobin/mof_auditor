from django.urls import path

from apps.balances.views import (
    get_balance_list,
    edit_balance,
    balance_settings,
    get_specific_balance,
)

urlpatterns = [
    path("", get_balance_list, name="get_balance_list"),
    path("<str:pub_id>/", get_specific_balance, name="get_specific_balance"),
    path("<str:pub_id>/settings/", balance_settings, name="balance_settings"),
    path("<str:pub_id>/settings/editing/", edit_balance, name="edit_balance"),
]
