from django.db import models

from users.models import User


class Permission(models.Model):
    name = models.CharField(max_length=255)
    codename = models.CharField(max_length=255)
    users = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.name}"

    def applied_to_users(self):
        queryset = self.users.all()
        if not len(queryset):
            return None
        return ", ".join(user.username for user in queryset)


class GroupInformation(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="group_info", blank=True, null=True
    )
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Group(models.Model):
    group_info = models.OneToOneField(GroupInformation, on_delete=models.CASCADE)
    invited_users = models.ManyToManyField(User, related_name="user_groups")
    permissions = models.ManyToManyField(Permission, related_name="user_groups")
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True, blank=True, null=True
    )

    def __str__(self):
        return f"{self.group_info.name}"

    def all_invited_users(self):
        return ", ".join(user.username for user in self.invited_users.all())

    def all_permissions(self):
        return ", ".join(permission.name for permission in self.permissions.all())
