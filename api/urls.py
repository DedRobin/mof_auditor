from django.urls import include, path
from rest_framework import routers

from api.auth.views import RegisterView, LoginView, LogoutView

app_name = "api"

router = routers.DefaultRouter()
# router.register(r"posts", PostViewSet, basename="pk")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/register/", RegisterView.as_view(), name="api_register"),
    path("auth/login/", LoginView.as_view(), name="api_login"),
    path("auth/logout/", LogoutView.as_view(), name="api_logout"),
]
