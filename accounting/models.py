from django.db import models

from balance.models import Balance

ACCOUNTING_TYPE_CHOICE = (
    ("income", "Income"),
    ("expense", "Expense"),
)


class AccountingCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Accounting(models.Model):
    balance = models.ForeignKey(
        Balance,
        on_delete=models.CASCADE,
        related_name="accounting",
        blank=True,
        null=True
    )
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    type = models.CharField(max_length=255, choices=ACCOUNTING_TYPE_CHOICE)
    accounting_category = models.ForeignKey(
        AccountingCategory,
        on_delete=models.CASCADE,
        related_name="accounting_category",
        blank=True,
        null=True
    )
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
