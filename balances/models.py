from django.db import models

from users.models import User


# PRIVATE_CHOICE = ((True, "True"),
#                   (False, "False"),
#                   )
# TYPE_CHOICE = (
#     ("cash", "Cash"),
#     ("card", "Card"),
#     ("bank", "Bank account"),
#     # ("deposit", "Deposit"),
#     # ("credit", "Credit"),
# )


class BalanceType(models.Model):
    name = models.CharField(max_length=255)
    codename = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


#
#
# CURRENCY_CHOICE = (
#     ("BYN", "Belorussian (BYN)"),
#     ("RUS", "Russian (RUS)"),
#     ("USD", "American Dollar (USD)"),
#     ("EUR", "Euro (EUR)"),
#     ("CNY", "Chinese yan (CNY)"),
# )


class BalanceCurrency(models.Model):
    name = models.CharField(max_length=255)
    codename = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Balance(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    type = models.ForeignKey(
        BalanceType,
        related_name="balances",
        on_delete=models.CASCADE
    )
    currency = models.ForeignKey(
        BalanceCurrency,
        related_name="balances",
        on_delete=models.CASCADE
    )
    private = models.BooleanField(default=False, choices=(True, False))
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.name}"
