from django.core.management.base import BaseCommand

from groups.models import Permission


class Command(BaseCommand):
    help = "Generate permissions"

    def handle(self, *args, **options):
        default_permissions = (
            ("All users | All groups | Can create the data", "all_all_create"),
            ("All users | All groups | Can read the data", "all_all_read"),
            ("All users | All groups | Can update the data", "all_all_update"),
            ("All users | All groups | Can delete the data", "all_all_delete"),
        )
        for name, codename in default_permissions:
            Permission.objects.create(
                name=name,
                codename=codename
            )
        print("Create default permissions.")
