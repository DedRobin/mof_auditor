from django.db import models

PERMISSION_CHOICE = (
    ("read", "User can read data"),
    ("edit", "User can write data"),
)


class Permission(models.Model):
    name = models.CharField(max_length=255)
    codename = models.CharField(max_length=255, choices=PERMISSION_CHOICE)

    def __str__(self):
        return self.name
