from django.db import models

PERMISSION_CHOICE = (
    ("Test permission №1", "t_perm_1"),
    ("Test permission №1", "t_perm_2"),
)


class Permission(models.Model):
    name = models.CharField(max_length=255)
    codename = models.CharField(max_length=255, choices=PERMISSION_CHOICE)

    def __str__(self):
        return self.name
