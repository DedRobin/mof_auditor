from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Checks all transactions"

    def handle(self, *args, **options):
        pass
