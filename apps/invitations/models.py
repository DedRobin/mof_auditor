import ulid

from django.db import models

from apps.users.models import User
from apps.groups.models import Group


class Invitation(models.Model):
    pub_id = models.CharField(
        db_index=True,
        max_length=255,
        unique=True,
        blank=True,
        null=True,
    )
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

    def __str__(self):
        return self.to_a_group.group_info.name

    def save(self, **kwargs):
        """Generates a public ID when the instance is saved"""

        if not self.pub_id:
            self.pub_id = ulid.new()
        super().save(**kwargs)
