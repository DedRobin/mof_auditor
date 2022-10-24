from django.db import models

from users.models import User


# PERMISSION_CHOICE = (
#     ("create", "Creating"),
#     ("read", "Reading"),
#     ("update", "Updating"),
#     ("delete", "Deleting"),
# )


class GroupInformation(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Permission(models.Model):
    name = models.CharField(max_length=255)
    codename = models.CharField(max_length=255, default="read_only")
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f"{self.name}"

    def get_users(self):
        queryset = self.users.all()
        if not len(queryset):
            return "No users"
        return ", ".join(user.username for user in queryset)


class Group(models.Model):
    group_info = models.OneToOneField(
        GroupInformation,
        on_delete=models.CASCADE
    )
    users = models.ManyToManyField(User)
    permissions = models.ManyToManyField(Permission)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, blank=True, null=True)

    def get_users(self):
        return ", ".join(user.username for user in self.users.all())

    def get_permissions(self):
        return ", ".join(permission.name for permission in self.permissions.all())
