from collections import OrderedDict
from django.db.models import QuerySet
from django.http import QueryDict

from apps.balances.models import Balance
from apps.transactions.models import Transaction


def get_sorted_transactions(queryset: QuerySet, query_param: QueryDict) -> QuerySet:
    # Query param
    amount = query_param.get("amount")
    amount_sign = query_param.get("amount_sign")
    category_type = query_param.get("category_type")
    category_name = query_param.get("category_name")

    if category_type:
        if category_type == "income":
            queryset = queryset.filter(amount__gt=0)
        elif category_type == "expense":
            queryset = queryset.filter(amount__lte=0)
    if amount:
        if amount_sign == "gt":
            queryset = queryset.filter(amount__gt=amount)
        elif amount_sign == "gte":
            queryset = queryset.filter(amount__gte=amount)
        elif amount_sign == "lt":
            queryset = queryset.filter(amount__lt=amount)
        elif amount_sign == "lte":
            queryset = queryset.filter(amount__lte=amount)
    if category_name:
        queryset = queryset.filter(category__name__contains=category_name)
    return queryset


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
