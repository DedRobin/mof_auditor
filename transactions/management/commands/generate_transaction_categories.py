from django.core.management.base import BaseCommand

from transactions.models import TransactionCategory


class Command(BaseCommand):
    help = "Generate transaction categories by default"

    def handle(self, *args, **options):
        default_transaction_categories = (
            # Income
            ("Salary", "income"),
            ("Business", "income"),
            ("Perquisite", "income"),
            ("Gift", "income"),
            ("Pension", "income"),
            ("Social allowance", "income"),
            # Expense
            ("Food", "expense"),
            ("Home", "expense"),
            ("Clothes", "expense"),
            ("Health", "expense"),
            ("Credits", "expense"),
            ("Saving", "expense")
        )

        TransactionCategory.objects.all().delete()

        for name, type_category in default_transaction_categories:
            TransactionCategory.objects.create(
                name=name,
                type=type_category
            )
        print("Create default transaction categories.")
