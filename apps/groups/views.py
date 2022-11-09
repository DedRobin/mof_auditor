from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.users.models import User
from apps.groups.models import GroupInformation, Group, Permission
from apps.groups.forms import CreateGroupForm, EditGroupForm, EditGroupInformationForm


@login_required
def create_group(request):
    if request.method == "POST":
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user)
            group_info = GroupInformation.objects.create(
                owner=user,
                name=form.cleaned_data["name"],
                description=form.cleaned_data["description"],
            )
            group = Group.objects.create(
                group_info=group_info,
            )
            group.invited_users.add(user)
            return redirect("index")
    else:
        form = CreateGroupForm()
        return render(request, "create_group_page.html", {"form": form})


@login_required
def edit_group(request, pub_id):
    group = Group.objects.get(pub_id=pub_id)
    group_info = group.group_info
    group_form = EditGroupForm(instance=group)
    group_info_form = EditGroupInformationForm(instance=group_info)
    return render(request, "edit_group.html", {"group_form": group_form, "group_info_form": group_info_form })
