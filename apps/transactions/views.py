from django.shortcuts import render

from apps.transactions.models import (
    Transaction,
    TransactionCategory,
    TRANSACTION_TYPE_CHOICE,
)
from apps.transactions.forms import TransactionFilterForm
from apps.transactions.services import get_sorted_transactions


def get_transactions(request):
    transactions = Transaction.objects.filter(balance__owner=request.user)
    if request.GET:
        query_param = request.GET
        transactions = get_sorted_transactions(
            queryset=transactions, query_param=query_param
        )
        form = TransactionFilterForm(request.GET)
    else:
        form = TransactionFilterForm()

    data = {
        "transactions": transactions,
        "form": form,
    }
    return render(request, "operations/operation_list.html", data)
