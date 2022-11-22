from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.permissions.models import PERMISSION_LIST
from apps.users.models import User
from apps.groups.models import GroupInformation, Group
from apps.groups.forms import CreateGroupInformationForm, EditGroupInformationForm
from apps.permissions.models import Permission, PermissionType
from apps.permissions.services import get_users_and_permission_type


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
    """Gets privacy settings for each group member"""
    permission_list = [permission[0] for permission in PERMISSION_LIST]

    group = Group.objects.get(pub_id=pub_id)

    if request.method == "POST":
        users, permission_name = get_users_and_permission_type(
            permission_query_dict=request.POST
        )

        permission_type = PermissionType.objects.get(name=permission_name)
        permissions_for_add = Permission.objects.filter(user__username__in=users, group=group)
        permissions_for_delete = Permission.objects.filter(group=group).exclude(user__username__in=users)

        for p_for_add in permissions_for_add:
            p_for_add.types.add(permission_type)
        for p_for_del in permissions_for_delete:
            p_for_del.types.remove(permission_type)

    group_name = group.group_info.name
    invited_users = group.invited_users.all().order_by("profile__first_name")
    permissions = group.permissions.all()

    data = {
        "group_name": group_name,
        "invited_users": invited_users,
        "permissions": permissions,
        "permission_list": permission_list,
        "member_number": 4,
    }

    return render(request, "groups/settings/privacy/privacy.html", data)
