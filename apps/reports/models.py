from django.db import models
from apps.balances.models import Balance


class Report(models.Model):
    balance = models.ForeignKey(
        Balance, on_delete=models.CASCADE, related_name="reports"
    )
    total = models.DecimalField(max_digits=19, decimal_places=7)
    difference = models.DecimalField(max_digits=19, decimal_places=7, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
