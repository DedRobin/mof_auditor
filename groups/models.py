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
    users = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.name}"


class Group(models.Model):
    group_info = models.OneToOneField(
        GroupInformation,
        on_delete=models.CASCADE
    )
    users = models.ManyToManyField(User)
    group_permissions = models.ManyToManyField(GroupPermission)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, blank=True, null=True)
