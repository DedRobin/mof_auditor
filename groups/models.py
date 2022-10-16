from django.db import models

from users.models import User
from balance.models import Balance
from permissions.models import Permission


class GroupDescription(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}(ID={self.id})"


class Group(models.Model):
    group_description = models.ForeignKey(
        GroupDescription,
        on_delete=models.CASCADE,
        related_name="group_description",
        blank=True,
        null=True
    )
    user = models.ManyToManyField(User)
    balance = models.ManyToManyField(Balance)
    permission = models.ManyToManyField(Permission)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, blank=True, null=True)

    def get_users(self):
        return ", ".join(user.username for user in self.user.all())

    def get_balances(self):
        return ", ".join(balance.name for balance in self.balance.all())

    def get_permission(self):
        return ", ".join(permission.name for permission in self.permission.all())

    def __str__(self):
        return f"{self.group_description}"
