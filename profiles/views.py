from django.shortcuts import render

from users.models import User
from profiles.forms import ProfileForm


def edit_profile(request, username):
    user = User.objects.get(username=username)
    form = ProfileForm({
        "username": user.username,
        "first_name": user.profile.first_name,
        "last_name": user.profile.last_name,
        "gender": user.profile.gender,
    })
    return render(request, "edit_profile.html", {"form": form})
