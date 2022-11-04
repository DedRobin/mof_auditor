from __future__ import annotations

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(
        self,
        username,
        password: str = None,
        is_staff: bool = False,
        is_superuser: bool = False,
    ) -> User | None:
        if username is None:
            raise ValueError("Users must have an username")

        user = self.model(
            username=username,
            is_staff=is_staff,
            is_superuser=is_superuser,
        )
        user.set_password(password)
        user.save()
        return user

    def create_staffuser(self, username: str, password: str):
        return self.create_user(username=username, password=password, is_staff=True)

    def create_superuser(self, username: str, password: str):
        return self.create_user(
            username=username, password=password, is_staff=True, is_superuser=True
        )


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True, db_index=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True, blank=True, null=True
    )

    USERNAME_FIELD = "username"

    objects = UserManager()
