from collections import OrderedDict
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from apps.invitations.models import Invitation
from apps.users.models import User
from apps.groups.models import Group


def create_invitation_or_404_api(request: Request, validated_data: OrderedDict) -> Response:
    invited_user = validated_data.get("to_who")

    # to_a_group = Group.objects.get(pk=validated_data.get("to_a_group"))
    if User.objects.filter(username=invited_user).exists():
        invited_user = User.objects.get(username=invited_user)
        Invitation.objects.create(
            from_who=request.user,
            to_who=invited_user,
            to_a_group=validated_data.get("to_a_group"),
        )
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
