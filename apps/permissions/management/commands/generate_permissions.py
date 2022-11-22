from django.core.management.base import BaseCommand

from apps.permissions.models import Permission, PermissionType
from apps.groups.models import Group


class Command(BaseCommand):
    help = "Generate permissions"

    def handle(self, *args, **options):
        Permission.objects.all().delete()

        groups = Group.objects.all()
        permission_types = PermissionType.objects.all()
        for group in groups:
            invited_users = group.invited_users.all()
            for user in invited_users:
                permission = Permission.objects.create(
                    user=user,
                    group=group,
                )
                permission.types.set(permission_types)
        print("Create user permissions.")
