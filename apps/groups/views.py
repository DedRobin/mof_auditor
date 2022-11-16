from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.users.models import User
from apps.groups.models import GroupInformation, Group, Permission, Invitation
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
def group_settings(request, pub_id):
    group = Group.objects.get(pub_id=pub_id)
    group_name = group.group_info.name
    return render(request, "groups/settings/settings.html", {"group_name": group_name})


@login_required
def edit_group(request, pub_id):
    """Updates data for single group"""

    group = Group.objects.get(pub_id=pub_id)
    group_info = group.group_info

    group_info_form = EditGroupInformationForm(instance=group_info)

    if request.method == "POST":
        if request.POST.get("invited_user") is not None:
            # Removes a specific invite user

            invited_user = request.POST.get("invited_user")
            user = User.objects.get(username=invited_user)
            group.invited_users.remove(user)

        group_info_form = EditGroupInformationForm(request.POST)

        if group_info_form.is_valid():
            # Update data for group

            new_name = group_info_form.cleaned_data["name"]
            new_description = group_info_form.cleaned_data["description"]

            group.group_info.name = new_name
            group.group_info.description = new_description
            group.group_info.save()

    data = {
        "group_info_form": group_info_form,
        "group_name": group_info.name,
    }
    return render(
        request,
        "groups/settings/editing/editing.html",
        data,
    )


@login_required
def group_members(request, pub_id):
    group = Group.objects.get(pub_id=pub_id)
    group_name = group.group_info.name
    invited_users = group.invited_users.all()
    data = {
        "group_name": group_name,
        "invited_users": invited_users,
    }
    return render(request, "groups/settings/members/members.html", data)


@login_required
def group_privacy(request, pub_id):
    group = Group.objects.get(pub_id=pub_id)
    group_name = group.group_info.name
    data = {
        "group_name": group_name,
    }
    return render(request, "groups/settings/privacy/privacy.html", data)


@login_required
def invitation_list(request):
    """Gets all invitations for current user"""

    username = request.user.username
    current_user = User.objects.get(username=username)

    if request.method == "POST":
        invitation_pub_id = request.POST.get("invitation_pub_id")
        invitation = Invitation.objects.get(pub_id=invitation_pub_id)

        if request.POST.get("to_accept") == "True":
            # Adds current user in invited group if invitation is accepted
            # Then it is deleted

            invited_group = invitation.to_a_group
            invited_group.invited_users.add(current_user)
            invitation.delete()

        elif request.POST.get("to_delete") == "True":
            # If user refused invitation then it is removed

            invitation.delete()

    # All invitations are displayed but not the current user

    invitations = Invitation.objects.filter(to_who__username=username).exclude(from_who__username=username)
    data = {"invitations": invitations}

    return render(request, "groups/invitations.html", data)
