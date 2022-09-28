from __future__ import annotations

from django.contrib.auth.backends import BaseBackend
from django.http import HttpRequest

from users.models import User


class EmailAuthBackend(BaseBackend):
    def authenticate(
            self, request: HttpRequest, email: str = None, password: str = None
    ) -> User | None:
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return

    def get_user(self, user_id: int) -> User | None:
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return
