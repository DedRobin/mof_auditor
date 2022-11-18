from django.db import models
from apps.users.models import User
from apps.groups.models import Group

PERMISSION_LIST = (
    ("read", "Read"),
    ("create", "Create"),
    ("update", "Update"),
    ("delete", "Delete")
)


class PermissionType(models.Model):
    name = models.CharField(
        max_length=255,
        choices=PERMISSION_LIST,
    )

    def __str__(self):
        return self.name


class Permission(models.Model):
    types = models.ManyToManyField(
        PermissionType,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.types
