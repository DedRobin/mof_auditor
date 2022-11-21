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
        unique=True,
        db_index=True,
        choices=PERMISSION_LIST,
    )

    def __str__(self):
        return self.name


class Permission(models.Model):
    types = models.ManyToManyField(
        PermissionType,
        blank=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="permissions",
        blank=True,
        null=True,
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="permissions",
        blank=True,
        null=True,
    )

    def all_types(self):
        """Method for displaying all permissions in admin"""

        return ", ".join(p_type.name for p_type in self.types.all())

    def __str__(self):
        return f"{self.user.username} | {self.group.group_info.name} | {self.all_types()}"
