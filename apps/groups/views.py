from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.transactions.services import create_transaction, delete_transaction
from apps.users.models import User
from apps.groups.models import GroupInformation, Group
from apps.groups.forms import CreateGroupInformationForm, EditGroupInformationForm
from apps.permissions.models import Permission, PermissionType
from apps.groups.services import (
    get_users_and_permission_type,
    delete_invited_user_from_group,
)
from apps.transactions.forms import TransactionForm


@login_required
def balance_and_transaction_list(request, pub_id):
    group = Group.objects.get(pub_id=pub_id)
    if request.method == "POST":

        if request.method == "POST":
            # Create new transaction
            if request.POST.get("balance_pub_id"):
                create_transaction(request=request)
            # Delete specific transaction
            if request.POST.get("transaction_id"):
                delete_transaction(request=request)

    form = TransactionForm()
    data = {
        "group": group,
        "form": form,
        "pub_id": pub_id,
    }
    return render(request, "groups/balance_list.html", data)


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
            # Added user as invited
            group.invited_users.add(user)

            # Added permissions
            permission_types = PermissionType.objects.all()
            permission = Permission.objects.create(group=group, user=user)
            permission.types.set(permission_types)
            return redirect("index")
    else:
        form = CreateGroupInformationForm()
        return render(request, "groups/create_group.html", {"form": form})


@login_required
def group_settings(request, pub_id):
    group = Group.objects.get(pub_id=pub_id)
    group_name = group.group_info.name
    owner = group.group_info.owner

    if request.method == "POST":
        action = request.POST.get("action", None)
        if action == "leave":
            # Leaving from current group

            group.invited_users.remove(request.user)
            return redirect("index")
        elif action == "delete":
            # Delete current group

            group.delete()
            return redirect("index")

    # Checks update permission
    update_is_allowed = False
    delete_is_allowed = False
    permissions = group.permissions.filter(user=request.user)
    if len(permissions):
        permissions = permissions[0]
        update_type = PermissionType.objects.get(name="update")
        delete_type = PermissionType.objects.get(name="delete")
        if update_type in permissions.types.all():
            update_is_allowed = True
        if delete_type in permissions.types.all():
            delete_is_allowed = True

    data = {
        "group_name": group_name,
        "update_is_allowed": update_is_allowed,
        "delete_is_allowed": delete_is_allowed,
        "owner": owner,
    }
    return render(request, "groups/settings/settings.html", data)


@login_required
def edit_group(request, pub_id):
    """Updates data for particular group"""

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

    if request.method == "POST":
        # Delete invited user
        delete_invited_user_from_group(request=request, group=group)

    data = {
        "group_name": group_name,
        "invited_users": invited_users,
    }
    return render(request, "groups/settings/members/members.html", data)


@login_required
def group_privacy(request, pub_id):
    """Gets privacy settings for each group member"""

    group = Group.objects.get(pub_id=pub_id)

    if request.method == "POST":
        users, permission_name = get_users_and_permission_type(
            permission_query_dict=request.POST
        )

        permission_type = PermissionType.objects.get(name=permission_name)
        permissions_for_add = Permission.objects.filter(
            user__username__in=users, group=group
        )
        permissions_for_delete = Permission.objects.filter(group=group).exclude(
            user__username__in=users
        )

        for p_for_add in permissions_for_add:
            p_for_add.types.add(permission_type)
        for p_for_del in permissions_for_delete:
            p_for_del.types.remove(permission_type)

    permission_types = PermissionType.objects.all()
    permission_list = [permission_type for permission_type in permission_types]

    group_name = group.group_info.name
    invited_users = group.invited_users.all().order_by("profile__first_name")
    permissions = group.permissions.all()

    data = {
        "group_name": group_name,
        "invited_users": invited_users,
        "permissions": permissions,
        "permission_list": permission_list,
    }

    return render(request, "groups/settings/privacy/privacy.html", data)
