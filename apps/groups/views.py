from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.users.models import User
from apps.groups.models import GroupInformation, Group, Permission
from apps.groups.forms import CreateGroupInformationForm, EditGroupInformationForm


@login_required
def create_group(request):
    if request.method == "POST":
        form = CreateGroupInformationForm(request.POST)
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
        form = CreateGroupInformationForm()
        return render(request, "groups/create_group.html", {"form": form})


@login_required
def edit_group(request, pub_id):
    group = Group.objects.get(pub_id=pub_id)
    group_info = group.group_info
    permissions = group.permissions.all()
    invited_users = group.invited_users.all()

    group_info_form = EditGroupInformationForm(instance=group_info)

    if request.method == "POST":
        if request.POST.get("invited_user") is not None:
            # Removes a specific invite user

            invited_user = request.POST.get("invited_user")
            user = User.objects.get(username=invited_user)
            group.invited_users.remove(user)

        group_info_form = EditGroupInformationForm(request.POST)
        if group_info_form.is_valid():
            group.group_info.name = group_info_form.cleaned_data["name"]
            group.group_info.description = group_info_form.cleaned_data["description"]
            group.group_info.save()
    return render(
        request,
        "groups/edit_group.html",
        {
            "group_info_form": group_info_form,
            "invited_users": invited_users,
            "permissions": permissions,
        },
    )
