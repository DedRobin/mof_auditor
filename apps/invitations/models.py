from django.db import models
from apps.users.models import User
from apps.groups.models import Group


class Invitation(models.Model):
    from_who = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="invitation_from",
    )
    to_who = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="invitation_to"
    )
    to_a_group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        blank=True,
        null=True,
    )
