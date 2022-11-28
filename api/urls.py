from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()

app_name = "mof_auditor_api"

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("api.auth.urls")),
    path("balances/", include("api.balances.urls")),
    path("groups/", include("api.groups.urls")),
    path("profile/", include("api.profiles.urls")),
    path("permissions/", include("api.permissions.urls")),
]
