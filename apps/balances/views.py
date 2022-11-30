from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.balances.models import Balance
from apps.transactions.forms import TransactionForm
from apps.transactions.services import create_transaction, delete_transaction


@login_required
def balance_list(request):
    balances = Balance.objects.filter(owner=request.user)

    if request.method == "POST":
        # Create new transaction
        if request.POST.get("balance_pub_id"):
            create_transaction(request=request)
        # Delete specific transaction
        if request.POST.get("transaction_id"):
            delete_transaction(request=request)

    form = TransactionForm()
    data = {
        "balances": balances,
        "form": form,
    }
    return render(request, "balances/balance_list.html", data)
