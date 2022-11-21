import ulid
from django.db import models

from apps.users.models import User


class GroupInformation(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="group_info", blank=True, null=True
    )
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} (Owner: {self.owner})"


class Group(models.Model):
    group_info = models.OneToOneField(
        GroupInformation,
        on_delete=models.CASCADE
    )
    pub_id = models.CharField(
        max_length=255,
        unique=True,
        blank=True,
        null=True,
    )
    invited_users = models.ManyToManyField(
        User,
        related_name="user_groups",
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True, blank=True, null=True
    )

    def __str__(self):
        return f"{self.group_info.name} (Owner: {self.group_info.owner})"

    def save(self, **kwargs):
        """Generates a public ID when the instance is saved"""

        if not self.pub_id:
            self.pub_id = ulid.new()
        super().save(**kwargs)

    def all_invited_users(self):
        """Method for displaying all invited users in admin"""

        return ", ".join(user.username for user in self.invited_users.all())


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
