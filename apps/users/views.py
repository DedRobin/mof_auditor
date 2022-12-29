from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from apps.groups.services import get_filter_groups
from apps.users.forms import RegisterForm, LoginForm
from apps.users.models import User
from apps.groups.models import Group
from apps.groups.forms import GroupFilterForm
from apps.profiles.models import Profile
from apps.balances.forms import CurrencyConvertForm
from apps.balances.services import get_currency_form


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
    form = CurrencyConvertForm()
    group_filter_form = GroupFilterForm()

    if request.GET:
        if request.GET.get("group_filter", None):
            groups = get_filter_groups(request, groups)
            group_filter_form = GroupFilterForm(request.GET)
        elif request.GET.get("converter", None):
            form = get_currency_form(request)

    data = {
        "user": user,
        "user_groups": groups,
        "form": form,
        "group_filter_form": group_filter_form,
    }
    return render(request, "index.html", data)
