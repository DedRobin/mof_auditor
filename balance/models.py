from django.db import models

from users.models import User

TYPE_CHOICE = (
    ("cash", "Cash"),
    ("iban", "Bank account"),
)

CURRENCY_CHOICE = (
    ("BYN", "Belorussian (BYN)"),
    ("RUS", "Russian (RUS)"),
    ("USD", "American Dollar (USD)"),
    ("EUR", "Euro (EUR)"),
    ("CNY", "Chinese yan (CNY)"),
)


class Balance(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    type = models.CharField(max_length=255, choices=TYPE_CHOICE)
    currency = models.CharField(max_length=255, choices=CURRENCY_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return {self.name}
