from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required

from apps.users.forms import RegisterForm, LoginForm
from apps.users.models import User
from apps.profiles.models import Profile
from apps.balances.forms import CurrencyConvertForm


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
    user = User.objects.get(username=request.user)
    user_groups = user.user_groups.all()
    form = CurrencyConvertForm()
    data = {
        "user": user,
        "user_groups": user_groups,
        "form": form,
    }
    return render(request, "index.html", data)
