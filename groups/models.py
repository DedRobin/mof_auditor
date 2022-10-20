from django.db import models

from users.models import User

PERMISSION_CHOICE = (
    ("create", "Creating"),
    ("read", "Reading"),
    ("update", "Updating"),
    ("delete", "Deleting"),
)


class GroupInformation(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class GroupPermission(models.Model):
    name = models.CharField(max_length=255)
    codename = models.CharField(max_length=255, choices=PERMISSION_CHOICE)

    def __str__(self):
        return f"{self.name}"


class Group(models.Model):
    group_info = models.ForeignKey(
        GroupInformation,
        on_delete=models.CASCADE,
        related_name="groups"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="groups"
    )
    group_permission = models.ForeignKey(
        GroupPermission,
        on_delete=models.CASCADE,
        related_name="groups"
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, blank=True, null=True)
