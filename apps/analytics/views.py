import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.groups.models import Group
from apps.balances.models import Balance


@login_required
def get_charts(request):
    plt.style.use("seaborn-whitegrid")  # plot style

    # data
    balance = Balance.objects.all().first()
    transactions = [x.amount for x in balance.transactions.order_by("created_at")]
    dates = [x.created_at for x in balance.transactions.order_by("created_at")]

    # plot axes
    x = np.array(dates)
    y = np.array(transactions)

    # create plot
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()

    # save figure as picture
    fig.savefig("static/plots/test_plot.png")

    return render(request, "analytics/charts.html")
