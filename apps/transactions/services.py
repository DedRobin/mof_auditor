from collections import OrderedDict

from apps.balances.models import Balance
from apps.transactions.models import Transaction


def create_transaction_API(balance_id: int, validated_data: OrderedDict) -> None:
    balance = Balance.objects.get(pk=balance_id)
    Transaction.objects.create(
        balance=balance,
        amount=validated_data["amount"],
        category=validated_data["category"],
        comment=validated_data["comment"],
    )


def update_transaction_API(transaction_id: str, validated_data: OrderedDict) -> None:
    transaction = Transaction.objects.filter(pk=transaction_id)
    transaction.update(
        amount=validated_data["amount"],
        category=validated_data["category"],
        comment=validated_data["comment"],
    )
