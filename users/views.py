from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate

from users.forms import RegisterForm, LoginForm
from users.models import User
from profiles.models import Profile


def index(request):
    username = request.user.username
    if request.user.is_authenticated:
        return redirect(f"/{username}")
    else:
        redirect("login")


def login_view(request):
    if request.user.is_authenticated:
        return redirect(f"/{request.user.username}")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request=request, **form.cleaned_data)
            if user is None:
                return HttpResponse("BadRequest", status=400)
            login(request, user)
            return redirect(f"/{user.username}")
    else:
        form = LoginForm()
        return render(request, "index.html", {"form": form})


def register_user(request):
    if request.user.is_authenticated:
        return redirect(f"/{request.user.username}")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(username=form.cleaned_data["username"])
            user.set_password(form.cleaned_data["password"])
            user.save()
            Profile.objects.create(user=user,
                                   gender=form.cleaned_data["gender"],
                                   first_name=form.cleaned_data["first_name"],
                                   last_name=form.cleaned_data["last_name"])
            return redirect("login")
    else:
        form = RegisterForm()
        return render(request, "register.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect("login")


def user_page(request, username):
    user = User.objects.filter(username=username)
    return render(request, "index.html", {"user": user[0].username})
