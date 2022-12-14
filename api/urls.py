from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()

app_name = "mof_auditor_api"

urlpatterns = [
    # Routers
    path("", include(router.urls)),
    # Swagger
    path("", include("api.yasg")),
    # Urls
    path("auth/", include("api.auth.urls")),
    path("balances/", include("api.balances.urls")),
    path("groups/", include("api.groups.urls")),
    path("profile/", include("api.profiles.urls")),
    path("invitations/", include("api.invitations.urls")),
]
