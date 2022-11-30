from django.urls import path, include

from apps.balances.views import balance_list, edit_balance

urlpatterns = [
    path("", balance_list, name="balance_list"),
    path("<str:pub_id>/", edit_balance, name="balance_settings"),
]
