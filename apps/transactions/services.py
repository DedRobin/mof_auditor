from collections import OrderedDict

from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet
from django.http import QueryDict

from apps.balances.models import Balance
from apps.transactions.models import Transaction, TransactionCategory


def get_sorted_transactions(queryset: QuerySet, query_param: QueryDict) -> QuerySet:
    # Query param
    cat_type = query_param.get("category__type")
    cat_name = query_param.get("category__name")
    balance = query_param.get("balance__name")
    from_amount = query_param.get("from_amount")
    to_amount = query_param.get("to_amount")
    comment = query_param.get("comment")
    from_date = query_param.get("from_date")
    to_date = query_param.get("to_date")

    if cat_type:
        if cat_type == "income":
            queryset = queryset.filter(amount__gte=0)
        elif cat_type == "expense":
            queryset = queryset.filter(amount__lte=0)
    if cat_name:
        queryset = queryset.filter(category__name__icontains=cat_name)
    if balance:
        queryset = queryset.filter(balance__name__icontains=balance)
    if from_amount or to_amount:
        if from_amount:
            queryset = queryset.filter(amount__gte=from_amount)
        if to_amount:
            queryset = queryset.filter(amount__lte=to_amount)
        elif from_amount and to_amount:
            queryset = queryset.filter(amount__gte=from_amount, amount__lte=to_amount)
    if comment:
        queryset = queryset.filter(comment__icontains=comment)
    if from_date or to_date:
        if from_date and not to_date:
            queryset = queryset.filter(created_at__gte=from_date)
        elif not from_date and to_date:
            queryset = queryset.filter(created_at__lte=to_date)
        elif from_date and to_date:
            queryset = queryset.filter(
                created_at__gte=from_date, created_at__lte=to_date
            )
    return queryset


def create_transaction(request: WSGIRequest) -> None:
    balance_pub_id = request.POST.get("balance_pub_id")

    # Values
    balance = Balance.objects.get(pub_id=balance_pub_id)
    category = TransactionCategory.objects.get(pk=request.POST.get("category"))
    amount = request.POST.get("amount")
    comment = request.POST.get("comment")

    # Create transaction
    Transaction.objects.create(
        balance=balance,
        category=category,
        amount=amount,
        comment=comment,
    )


def delete_transaction(request: WSGIRequest) -> None:
    pk = request.POST.get("transaction_id")
    Transaction.objects.get(pk=pk).delete()


def create_transaction_api(balance_id: int, validated_data: OrderedDict) -> None:
    balance = Balance.objects.get(pk=balance_id)
    Transaction.objects.create(
        balance=balance,
        amount=validated_data["amount"],
        category=validated_data["category"],
        comment=validated_data["comment"],
    )


def update_transaction_api(transaction_id: str, validated_data: OrderedDict) -> None:
    transaction = Transaction.objects.filter(pk=transaction_id)
    transaction.update(
        amount=validated_data["amount"],
        category=validated_data["category"],
        comment=validated_data["comment"],
    )
