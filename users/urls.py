from django.urls import path

from users.views import register_user, logout_user, login_view

urlpatterns = [
    path("register/", register_user, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_user, name="logout"),
]
