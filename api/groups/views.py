from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.groups.models import Group
from api.groups.serializers import GroupSerializer
from apps.groups.services import create_group


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Group.objects.filter(group_info__owner__username=self.request.user).order_by("-created_at")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        create_group(
            request=request,
            validated_data=serializer.validated_data
        )

        return Response(status=status.HTTP_201_CREATED)
