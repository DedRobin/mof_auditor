from django.db import models
from apps.balances.models import Balance


class Report(models.Model):
    balance = models.ForeignKey(
        Balance, on_delete=models.CASCADE, related_name="reports"
    )
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    total = models.DecimalField(max_digits=19, decimal_places=7, default=0)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    pass
