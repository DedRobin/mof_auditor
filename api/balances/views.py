from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.balances.models import Balance
from api.balances.serializers import BalanceSerializer


class BalanceViewSet(viewsets.ModelViewSet):
    serializer_class = BalanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Balance.objects.filter(owner=self.request.user).order_by("-created_at")
