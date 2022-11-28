from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.permissions.models import Permission
from api.permissions.serializers import PermissionSerializer
from apps.groups.services import create_group_API, update_group_API
from apps.permissions.services import create_permission_API


class PermissionsViewSet(viewsets.ModelViewSet):
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Permission.objects.filter(user=self.request.user)

    def get(self):
        return Response(status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        create_permission_API(
            permission_id=kwargs.get("pk"), validated_data=serializer.validated_data
        )

        return Response(status=status.HTTP_201_CREATED)

    # def update(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     transaction_id = kwargs.get("transaction_id")
    #
    #     update_transaction_API(
    #         transaction_id=transaction_id,
    #         validated_data=serializer.validated_data,
    #     )
    #
    #     return Response(status=status.HTTP_200_OK)
    #
    # def destroy(self, request, *args, **kwargs):
    #     transaction_id = kwargs.get("transaction_id")
    #
    #     Transaction.objects.get(pk=transaction_id).delete()
    #
    #     return Response(status=status.HTTP_200_OK)
