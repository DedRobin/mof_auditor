from django.db import models

from accounting_category.models import AccountingCategory
from users.models import User

ACCOUNTING_TYPE_CHOICE = (
    ("income", "Income"),
    ("expense", "Expense"),
)


class Accounting(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="accounting"
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
