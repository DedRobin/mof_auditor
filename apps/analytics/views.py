from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.balances.models import Balance


@login_required
def get_charts(request):
    balance = Balance.objects.filter(owner=request.user).first()
    transactions = balance.transactions.all()
    data = {
        "transactions": transactions,
        "balance": balance,
    }
    return render(request, "analytics/charts.html", data)
