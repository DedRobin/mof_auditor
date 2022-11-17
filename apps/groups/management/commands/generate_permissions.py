from django.core.management.base import BaseCommand

from apps.users.models import User
from apps.groups.models import Permission

PERMISSION_LIST = ["read", "create", "update", "delete"]


class Command(BaseCommand):
    help = "Generate permissions"

    def handle(self, *args, **options):
        Permission.objects.all().delete()
        permissions = []

        users = User.objects.values("username").all()
        for user in users:
            for permission in PERMISSION_LIST:
                permissions.append(
                    Permission.objects.create(
                        name=f"{user.get('username')} | Can {permission} the data",
                        codename=f"{user.get('username')}_{permission}"
                    )
                )
        Permission.objects.bulk_create(permissions)
        print("Create user permissions.")
