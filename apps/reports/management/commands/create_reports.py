from django.core.management.base import BaseCommand

from apps.reports.sevices import create_reports


class Command(BaseCommand):
    help = "Checks all balances by transactions"

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete all group records",
        )

    def handle(self, *args, **options):
        clear = options.get("clear", None)
        create_reports.delay(clear)
