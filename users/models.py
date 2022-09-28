from __future__ import annotations

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(
            self,
            email,
            password: str = None,
            is_staff: bool = False,
            is_superuser: bool = False,
    ) -> User | None:
        if email is None:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            is_staff=is_staff,
            is_superuser=is_superuser,
        )
        user.set_password(password)
        user.save()
        return user

    def create_staffuser(self, email: str, password: str):
        return self.create_user(email=email, password=password, is_staff=True)

    def create_superuser(self, email: str, password: str):
        return self.create_user(
            email=email, password=password, is_staff=True, is_superuser=True
        )


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, db_index=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, blank=True, null=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    objects = UserManager()
