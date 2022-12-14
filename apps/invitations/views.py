from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.users.models import User
from apps.permissions.models import Permission, PermissionType
from apps.invitations.models import Invitation
from apps.invitations.forms import SendInvitationForm

from django import forms
from apps.groups.models import Group


@login_required
def invitation_list(request):
    """Gets all invitations for current user"""

    username = request.user.username
    current_user = User.objects.get(username=username)

    if request.method == "POST":
        if request.POST.get("incoming_invitation_pub_id"):
            # For incoming invitations

            invitation_pub_id = request.POST.get("incoming_invitation_pub_id")
            invitation = Invitation.objects.get(pub_id=invitation_pub_id)

            if request.POST.get("to_accept") == "True":
                # Adds current user in invited group if invitation is accepted
                # Then it is deleted

                invited_group = invitation.to_a_group
                invited_group.invited_users.add(current_user)
                invitation.delete()

                # Adds read-only permission for current user
                readonly_permission = PermissionType.objects.get(name="read")
                permission_by_default = Permission.objects.create(
                    user=current_user, group=invited_group
                )
                permission_by_default.types.add(readonly_permission)

            elif request.POST.get("to_delete") == "True":
                # If user refused invitation then it is removed

                invitation.delete()
        elif request.POST.get("outgoing_invitation_pub_id"):
            # For outgoing invitations (only remove)

            invitation_pub_id = request.POST.get("outgoing_invitation_pub_id")
            invitation = Invitation.objects.get(pub_id=invitation_pub_id)
            invitation.delete()

    # All invitations are displayed but not the current user

    incoming_invitations = Invitation.objects.filter(to_who__username=username).exclude(
        from_who__username=username
    )
    outgoing_invitations = Invitation.objects.filter(from_who__username=username)
    data = {
        "incoming_invitations": incoming_invitations,
        "outgoing_invitations": outgoing_invitations,
    }

    return render(request, "invitations/invitations.html", data)


@login_required
def send_invitation(request):
    """Sends invitation some user"""

    username = request.user.username
    current_user = User.objects.get(username=username)

    form = SendInvitationForm()
    form.fields["to_a_group"] = forms.ModelChoiceField(
        Group.objects.filter(group_info__owner=current_user)
    )

    if request.method == "POST":
        form = SendInvitationForm(request.POST)
        form.fields["to_a_group"] = forms.ModelChoiceField(
            Group.objects.filter(group_info__owner=current_user)
        )
        if form.is_valid():
            try:
                to_who = User.objects.get(username=form.data.get("to_who"))
            except:
                message = "Such user does not existed"
                return render(
                    request,
                    "invitations/send_invitation.html",
                    {"message": message, "form": form},
                )

            to_a_group = Group.objects.get(pk=form.data.get("to_a_group"))
            Invitation.objects.create(
                from_who=current_user,
                to_who=to_who,
                to_a_group=to_a_group,
            )
            return redirect("invitation_list")
    data = {
        "form": form,
    }
    return render(request, "invitations/send_invitation.html", data)
