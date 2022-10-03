from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate

from users.forms import RegisterForm, LoginForm
from users.models import User


# def index(request):
#     return render(request, "index.html")


def login_view(request):
    if request.user.is_authenticated:
        # return redirect("login_view")
        return render(request, "index.html")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request=request, **form.cleaned_data)
            if user is None:
                return HttpResponse("BadRequest", status=400)
            login(request, user)
            return redirect("login_view")
    else:
        form = LoginForm()
        return render(request, "index.html", {"form": form})


def register_user(request):
    if request.user.is_authenticated:
        return redirect("login_view")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(email=form.cleaned_data["email"])
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("login_view")
    else:
        form = RegisterForm()
        return render(request, "register.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect("login_view")
