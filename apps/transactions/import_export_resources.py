from import_export import resources
from apps.transactions.models import Transaction


class TransactionResource(resources.ModelResource):
    class Meta:
        model = Transaction
        fields = (
            "balance__name",
            "amount",
            "category__name",
            "category__type",
            "comment",
            "created_at",
        )
        export_order = (
            "balance__name",
            "amount",
            "category__name",
            "category__type",
            "comment",
            "created_at",
        )
