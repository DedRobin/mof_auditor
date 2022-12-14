from django.shortcuts import render
from django.http import HttpResponse

from apps.transactions.import_export_resources import TransactionResource
from apps.transactions.models import Transaction
from apps.transactions.forms import TransactionFilterForm
from apps.transactions.services import get_sorted_transactions
from django.contrib.auth.decorators import login_required


@login_required
def get_transactions(request):
    transactions = Transaction.objects.filter(balance__owner=request.user).order_by(
        "-created_at"
    )
    query_param = None
    if request.GET:
        query_param = request.GET
        transactions = get_sorted_transactions(
            queryset=transactions, query_param=query_param
        )
        form = TransactionFilterForm(request.GET)
    else:
        form = TransactionFilterForm()

    data = {"transactions": transactions, "form": form, "filter": query_param}
    return render(request, "operations/operation_list.html", data)


@login_required
def export_operations(request):
    filters = request.GET
    filters = filters.dict()
    transactions = Transaction.objects.filter(**filters, balance__owner=request.user)

    transaction_resource = TransactionResource()
    dataset = transaction_resource.export(queryset=transactions)
    response = HttpResponse(dataset.xls, content_type="application/vnd.ms-excel")
    response["Content-Disposition"] = 'attachment; filename="transactions.xls"'
    return response
