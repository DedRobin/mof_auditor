from django.db import models


class AccountingCategory(models.Model):
    name = models.CharField(max_length=255)
