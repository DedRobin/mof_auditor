from django.urls import include, path
from rest_framework import routers

from api.groups.views import GroupViewSet
from api.balances.views import BalanceViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r"groups", GroupViewSet, basename="groups")
router.register(r"balances", BalanceViewSet, basename="balances")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("api.auth.urls")),
]
