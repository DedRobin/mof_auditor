from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.balances.models import Balance


@login_required
def get_charts(request):
    balances = Balance.objects.filter(owner=request.user).order_by("name")
    test = balances[0].get_total_by_each_category()
    data = {
        "balances": balances,
    }
    return render(request, "analytics/charts.html", data)
