from django.core.management.base import BaseCommand

from apps.users.models import User
from apps.groups.models import Permission
from apps.groups.models import PERMISSION_LIST


class Command(BaseCommand):
    help = "Generate permissions"

    def handle(self, *args, **options):
        Permission.objects.all().delete()
        permissions = []

        users = User.objects.all()
        for user in users:
            for permission in PERMISSION_LIST:
                permissions.append(
                    Permission.objects.create(
                        permission_type=permission[0],
                        user=user,
                    )
                )
        Permission.objects.bulk_create(permissions)
        print("Create user permissions.")
