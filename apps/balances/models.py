import ulid
from decimal import Decimal
from django.db import models
from django.utils import timezone

from apps.users.models import User
from apps.groups.models import Group

BALANCE_TYPE_CHOICE = (("cash", "Cash"), ("card", "Card"), ("bank", "Bank account"))

BALANCE_PRIVATE_CHOICE = ((False, "Public"), (True, "Private"))


class Currency(models.Model):
    name = models.CharField(max_length=255)
    codename = models.CharField(max_length=255, unique=True)
    rate = models.DecimalField(max_digits=9, decimal_places=6, default=1)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Currencies"

    def __str__(self):
        return f"{self.name} ({self.codename})"


class Balance(models.Model):
    pub_id = models.CharField(max_length=255, unique=True, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="balances")

    type = models.CharField(max_length=255, choices=BALANCE_TYPE_CHOICE)
    currency = models.ForeignKey(
        Currency, related_name="balances", on_delete=models.CASCADE
    )
    private = models.BooleanField(choices=BALANCE_PRIVATE_CHOICE)
    groups = models.ManyToManyField(Group, related_name="balances", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, **kwargs):
        """Generates a public ID when the instance is saved"""

        if not self.pub_id:
            self.pub_id = ulid.new()
        super().save(**kwargs)

    def total(self):
        transactions = self.transactions.all()
        if len(transactions):
            total = sum(transactions.amount for transactions in transactions)
            return total
        return Decimal("0")

    def for_groups(self):
        return ", ".join(group.group_info.name for group in self.groups.all())
