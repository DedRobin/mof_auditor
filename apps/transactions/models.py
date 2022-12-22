from django.db import models
from django.conf import settings
from django.utils import timezone

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

    class Meta:
        verbose_name_plural = "Transaction Categories"

    def __str__(self):
        return f"{self.type.capitalize()} --> {self.name}"


class Transaction(models.Model):
    balance = models.ForeignKey(
        Balance,
        on_delete=models.CASCADE,
        related_name="transactions",
        blank=True,
        null=True,
    )
    amount = models.DecimalField(
        max_digits=settings.MAX_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
        default=0,
    )
    category = models.ForeignKey(
        TransactionCategory,
        on_delete=models.CASCADE,
        related_name="transactions",
        blank=True,
        null=True,
    )
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now(), db_index=True)

    def __str__(self):
        return (
            f"Amount={self.amount}, Category={self.category.name}({self.category.type})"
        )
