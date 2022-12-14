from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.balances.forms import BalanceForm
from apps.balances.models import Balance, Currency
from apps.balances.services import create_balance
from apps.transactions.forms import TransactionForm
from apps.transactions.services import create_transaction, delete_transaction


@login_required
def get_balance_list(request):
    balances = Balance.objects.filter(owner=request.user)

    if request.method == "POST":
        # Create new balance
        if request.POST.get("create_balance_pub_id"):
            create_balance(request=request)
        # Create new transaction
        if request.POST.get("balance_pub_id"):
            create_transaction(request=request)
        # Delete specific transaction
        if request.POST.get("transaction_id"):
            delete_transaction(request=request)

    form = TransactionForm()
    balance_form = BalanceForm()
    data = {
        "balances": balances,
        "form": form,
        "balance_form": balance_form,
    }
    return render(request, "balances/balance_list.html", data)


@login_required
def get_specific_balance(request, pub_id):
    balance = Balance.objects.get(pub_id=pub_id)
    if request.method == "POST":
        # Create new transaction
        if request.POST.get("balance_pub_id"):
            create_transaction(request=request)
        # Delete specific transaction
        if request.POST.get("transaction_id"):
            delete_transaction(request=request)

    form = TransactionForm()
    data = {"balance": balance, "form": form}
    return render(request, "balances/specific_balance.html", data)


@login_required
def balance_settings(request, pub_id):
    balance = Balance.objects.get(pub_id=pub_id)
    if request.method == "POST":
        action = request.POST.get("action", None)
        if action == "delete":
            balance.delete()
            return redirect("balance_list")
    data = {
        "balance": balance,
        "pub_id": pub_id,
    }
    return render(request, "balances/settings/settings.html", data)


@login_required
def edit_balance(request, pub_id):
    balance = Balance.objects.get(pub_id=pub_id)
    if request.method == "POST":
        balance.name = request.POST.get("name")
        balance.owner = request.user
        balance.type = request.POST.get("type")
        balance.currency = Currency.objects.get(pk=request.POST.get("currency"))
        balance.private = request.POST.get("private")
        balance.save()
    balance_form = BalanceForm(instance=balance)
    data = {
        "balance_form": balance_form,
        "balance": balance,
        "pub_id": pub_id,
    }
    return render(request, "balances/settings/editing/edit_balance.html", data)
