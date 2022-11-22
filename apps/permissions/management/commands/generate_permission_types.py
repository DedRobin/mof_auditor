from django.core.management.base import BaseCommand

from apps.permissions.models import PermissionType
from apps.permissions.models import PERMISSION_LIST


class Command(BaseCommand):
    help = "Generate permission types"

    def handle(self, *args, **options):
        PermissionType.objects.all().delete()

        for permission_type in PERMISSION_LIST:
            PermissionType.objects.create(
                name=permission_type[0],
            )
        print("Create user permission types.")
