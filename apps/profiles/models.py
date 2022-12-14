from django.db import models

from apps.users.models import User

GENDER_CHOICE = (
    (None, "Empty"),
    ("male", "Male"),
    ("female", "Female"),
)


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        blank=True,
        null=True,
    )
    email = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default="",
    )
    gender = models.CharField(
        max_length=255,
        choices=GENDER_CHOICE,
        blank=True,
        null=True,
    )
    first_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default="",
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default="",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )

    def __str__(self):
        return f"Profile for {self.user}"
