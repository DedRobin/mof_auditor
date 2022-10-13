from django.db import models

from users.models import User
from balance.models import Balance
from permissions.models import Permission


class GroupID(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return f"{self.name}(ID={self.id})"


class Group(models.Model):
    group_id = models.ForeignKey(
        GroupID,
        on_delete=models.CASCADE,
        related_name="group_ids",
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="users",
        blank=True,
        null=True
    )
    balance = models.ForeignKey(
        Balance,
        on_delete=models.CASCADE,
        related_name="balances",
        blank=True,
        null=True
    )
    permission = models.ForeignKey(
        Permission,
        on_delete=models.CASCADE,
        related_name="permissions",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.group_id}"
