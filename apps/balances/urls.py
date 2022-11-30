from django.urls import path, include

from apps.balances.views import balance_list

urlpatterns = [
    path("", balance_list, name="balance_list"),
]
