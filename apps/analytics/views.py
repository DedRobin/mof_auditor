from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def get_charts(request):
    return render(request, "analytics/charts.html")
