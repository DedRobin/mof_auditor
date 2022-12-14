from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.users.models import User
from apps.profiles.models import Profile
from apps.profiles.forms import ProfileForm


@login_required
def edit_profile(request):
    user = User.objects.get(username=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data["username"]
            user.save()

            profile = Profile.objects.get(user=user)
            profile.gender = form.cleaned_data["gender"]
            profile.first_name = form.cleaned_data["first_name"]
            profile.last_name = form.cleaned_data["last_name"]
            profile.save()

    else:
        current_user_data = {
            "username": user.username,
            "first_name": user.profile.first_name,
            "last_name": user.profile.last_name,
            "gender": user.profile.gender,
        }
        form = ProfileForm(current_user_data)

    return render(request, "profile/edit_profile.html", {"form": form, "user": user})
