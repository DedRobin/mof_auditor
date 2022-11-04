from django.db import models

from apps.users.models import User
from apps.balances.models import Balance

TRANSACTION_TYPE_CHOICE = (
    ("income", "Income"),
    ("expense", "Expense"),
)


class TransactionCategory(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(
        max_length=255, choices=TRANSACTION_TYPE_CHOICE, blank=True, null=True
    )

    def __str__(self):
        return f"{self.name}"


class Transaction(models.Model):
    balance = models.ForeignKey(
        Balance,
        on_delete=models.CASCADE,
        related_name="transactions",
        blank=True,
        null=True,
    )
    amount = models.DecimalField(max_digits=19, decimal_places=7, default=0)
    category = models.ForeignKey(
        TransactionCategory,
        on_delete=models.CASCADE,
        related_name="transactions",
        blank=True,
        null=True,
    )
    comment = models.TextField(blank=True, null=True)
    who_made = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="transactions",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
