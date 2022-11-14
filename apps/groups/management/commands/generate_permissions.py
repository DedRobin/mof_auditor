from django.core.management.base import BaseCommand

from apps.groups.models import Permission


class Command(BaseCommand):
    help = "Generate permissions"

    def handle(self, *args, **options):
        Permission.objects.all().delete()

        default_permissions = (
            ("All users | Can create the data", "all_create"),
            ("All users | Can read the data", "all_read"),
            ("All users | Can update the data", "all_update"),
            ("All users | Can delete the data", "all_delete"),
        )
        for name, codename in default_permissions:
            Permission.objects.create(name=name, codename=codename)
        print("Create default permissions.")
