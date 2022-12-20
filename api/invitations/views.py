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
        return Invitation.objects.filter(from_who=self.request.user).order_by(
            "-created_at"
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = create_invitation_or_404_api(
            request=request, validated_data=serializer.validated_data
        )

        return response

    def destroy(self, request, *args, **kwargs):
        invitation_id = kwargs.get("pk", None)

        Invitation.objects.get(pk=invitation_id).delete()

        return Response(status=status.HTTP_200_OK)
