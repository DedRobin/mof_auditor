from django.db import models

from users.models import User
from balance.models import Balance
from permissions.models import Permission


class Group(models.Model):
    name = models.CharField(max_length=255)
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
        null=True)

    def __str__(self):
        return self.name
