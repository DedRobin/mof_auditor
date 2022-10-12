from django.db import models

from users.models import User
from balance.models import Balance
from permissions.models import Permission


class Group(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User)
    balances = models.ManyToManyField(Balance)
    permissions = models.ManyToManyField(Permission)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, blank=True, null=True)
