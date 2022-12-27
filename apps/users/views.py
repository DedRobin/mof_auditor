from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from apps.users.forms import RegisterForm, LoginForm
from apps.users.models import User
from apps.groups.models import Group
from apps.profiles.models import Profile
from apps.balances.forms import CurrencyConvertForm
from apps.balances.services import get_currency_convert_result


def login_view(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request=request, **form.cleaned_data)
            if user is None:
                return HttpResponse("BadRequest", status=400)
            login(request, user)
            return redirect("index")
    else:
        form = LoginForm()
        return render(request, "index.html", {"form": form})


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(username=form.cleaned_data["username"])
            user.set_password(form.cleaned_data["password"])
            user.save()
            Profile.objects.create(
                user=user,
                gender=form.cleaned_data["gender"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
            )
            return redirect("login")
    else:
        form = RegisterForm()
        return render(request, "profile/register.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect("login")


@login_required
def index(request):
    user = request.user
    groups = Group.objects.filter(Q(group_info__owner=user) | Q(invited_users=user)).order_by("group_info__name")
    if request.GET:
        form = CurrencyConvertForm(request.GET)
        if form.is_valid():
            from_amount = form.cleaned_data["from_amount"]
            from_currency = form.cleaned_data["from_currency"]
            to_currency = form.cleaned_data["to_currency"]

            convert_result = get_currency_convert_result(
                from_amount=from_amount,
                from_currency=from_currency.codename,
                to_currency=to_currency.codename,
            )

            form_data = {
                "from_amount": from_amount,
                "from_currency": from_currency,
                "to_currency": to_currency,
                "result": convert_result,
            }
            form = CurrencyConvertForm(form_data)
    else:
        form = CurrencyConvertForm()

    data = {
        "user": user,
        "user_groups": groups,
        "form": form,
    }
    return render(request, "index.html", data)
