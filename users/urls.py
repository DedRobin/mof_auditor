from django.urls import path

from users.views import register_user, logout_user

urlpatterns = [
    path("register/", register_user, name="register"),
    path("logout/", logout_user, name="logout_view"),
]
