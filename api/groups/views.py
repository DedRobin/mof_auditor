from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.groups.models import Group
from api.groups.serializers import GroupSerializer
from apps.groups.services import create_group, update_group


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Group.objects.filter(
            group_info__owner__username=self.request.user
        ).order_by("-created_at")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        create_group(request=request, validated_data=serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        group_id = kwargs.get("pk", None)

        update_group(group_id=group_id, validated_data=serializer.validated_data)

        return Response(status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        group_id = kwargs.get("pk", None)

        Group.objects.get(pk=group_id).delete()

        return Response(status=status.HTTP_200_OK)
