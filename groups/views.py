from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from users.models import User
from groups.models import GroupInformation, Group
from groups.forms import CreateGroupForm


@login_required
def create_group(request):
    if request.method == "POST":
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user)
            group_info = GroupInformation.objects.create(
                name=form.cleaned_data["name"],
                description=form.cleaned_data["description"]
            )
            group = Group.objects.create(
                group_info=group_info
            )
            group.users.add(user)
            return redirect("index")
    else:
        form = CreateGroupForm()
        return render(request, "create_group_page.html", {"form": form})
