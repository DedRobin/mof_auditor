import csv
import tablib
from django.core.management.base import BaseCommand
from import_export import resources

from apps.users.import_export_resources import UserResource


class Command(BaseCommand):
    help = "Import all user data"

    def handle(self, *args, **options):
        dataset = UserResource().export()
        print(dataset.csv)
        with open("example.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerows(dataset)
        print()
