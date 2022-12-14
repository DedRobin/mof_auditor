from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.invitations.models import Invitation
from apps.invitations.services import create_invitation_or_404_api
from api.invitations.serializers import InvitationSerializer


class InvitationViewSet(viewsets.ModelViewSet):
    serializer_class = InvitationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Invitation.objects.filter(to_who=self.request.user).order_by("-created_at")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = create_invitation_or_404_api(request=request, validated_data=serializer.validated_data)

        return response
    #
    # def update(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     group_id = kwargs.get("pk", None)
    #
    #     update_group_api(group_id=group_id, validated_data=serializer.validated_data)
    #
    #     return Response(status=status.HTTP_200_OK)
    #
    # def destroy(self, request, *args, **kwargs):
    #     group_id = kwargs.get("pk", None)
    #
    #     Group.objects.get(pk=group_id).delete()
    #
    #     return Response(status=status.HTTP_200_OK)
