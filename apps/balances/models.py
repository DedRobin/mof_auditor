import ulid
from django.db import models

from apps.users.models import User
from apps.groups.models import Group

BALANCE_TYPE_CHOICE = (("cash", "Cash"), ("card", "Card"), ("bank", "Bank account"))

BALANCE_PRIVATE_CHOICE = ((False, "Public"), (True, "Private"))


class BalanceCurrency(models.Model):
    name = models.CharField(
        max_length=255,
    )
    codename = models.CharField(
        max_length=255,
        unique=True,
    )

    def __str__(self):
        return f"{self.name} ({self.codename})"


class Balance(models.Model):
    pub_id = models.CharField(
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="balances"
    )

    type = models.CharField(
        max_length=255,
        choices=BALANCE_TYPE_CHOICE
    )
    currency = models.ForeignKey(
        BalanceCurrency,
        related_name="balances",
        on_delete=models.CASCADE
    )
    private = models.BooleanField(
        choices=BALANCE_PRIVATE_CHOICE
    )
    groups = models.ManyToManyField(
        Group,
        related_name="balances",
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return f"{self.name}"

    def save(self, **kwargs):
        if not self.pub_id:
            self.pub_id = ulid.new()
        super().save(*kwargs)

    def total(self):
        transactions = self.transactions.all()
        if len(transactions):
            total = sum(transactions.amount for transactions in transactions)
            return total
        return 0

    def all_groups(self):
        return ", ".join(group.group_info.name for group in self.groups.all())
