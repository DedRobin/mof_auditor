from rest_framework import status, viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.balances.serializers import BalanceSerializer
from apps.balances.models import Balance
from apps.balances.services import create_balance_api, update_balance_api


class BalanceViewSet(viewsets.ModelViewSet):
    serializer_class = BalanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Balance.objects.filter(owner=self.request.user).order_by("-created_at")

    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        create_balance_api(request=request, validated_data=serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        balance_id = kwargs.get("pk", None)

        update_balance_api(
            balance_id=balance_id, validated_data=serializer.validated_data
        )

        return Response(status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        balance_id = kwargs.get("pk", None)

        Balance.objects.get(pk=balance_id).delete()

        return Response(status=status.HTTP_200_OK)
