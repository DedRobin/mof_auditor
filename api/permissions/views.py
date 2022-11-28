from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.permissions.models import Permission
from api.permissions.serializers import PermissionSerializer
from apps.permissions.services import update_permission_API


class PermissionsViewSet(viewsets.ModelViewSet):
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "permission_id"

    def get_queryset(self):
        group_id = self.kwargs.get("pk")
        user_id = self.kwargs.get("user_id")
        permission_id = self.kwargs.get("permission_id")
        permissions = Permission.objects.filter(user=user_id, group=group_id)
        if permission_id:
            permission = Permission.objects.filter(pk=permission_id)
            return permission
        return permissions

    def get(self):
        return Response(status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        permission_id = kwargs.get("permission_id")

        update_permission_API(
            permission_id=permission_id, validated_data=serializer.validated_data
        )
        return Response(status=status.HTTP_200_OK)
