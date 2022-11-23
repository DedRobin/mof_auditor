from django.urls import include, path
from rest_framework import routers

# from api.groups.views import GroupViewSet

app_name = "api"

router = routers.DefaultRouter()
# router.register(r"groups", GroupViewSet, basename="pk")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("api.auth.urls")),
]
