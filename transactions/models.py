from django.db import models

from balances.models import Balance

TRANSACTION_TYPE_CHOICE = (
    ("required", "Required"),
    ("optional", "Optional"),
)


class TransactionCategoryType(models.Model):
    name = models.CharField(max_length=255)
    codename = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class TransactionCategory(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(
        TransactionCategoryType,
        on_delete=models.CASCADE,
        related_name="transaction_categories",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.name}"


class Transaction(models.Model):
    balance = models.ForeignKey(
        Balance,
        on_delete=models.CASCADE,
        related_name="transactions",
        blank=True,
        null=True
    )
    income = models.DecimalField(max_digits=19, decimal_places=2)
    expense = models.DecimalField(max_digits=19, decimal_places=2)
    type = models.CharField(max_length=255, choices=TRANSACTION_TYPE_CHOICE)
    category = models.ForeignKey(
        TransactionCategory,
        on_delete=models.CASCADE,
        related_name="transactions",
        blank=True,
        null=True
    )
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
