from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from api.balances.serializers import BalanceSerializer
from apps.balances.models import Balance
from apps.balances.services import create_balance, update_balance
from apps.groups.services import Group
from apps.transactions.models import Transaction

from api.transactions.serializers import TransactionSerializer


class BalanceViewSet(viewsets.ModelViewSet):
    serializer_class = BalanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Balance.objects.filter(owner=self.request.user).order_by("-created_at")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        create_balance(
            request=request,
            validated_data=serializer.validated_data
        )

        return Response(status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        balance_id = kwargs.get("pk", None)

        update_balance(
            balance_id=balance_id,
            validated_data=serializer.validated_data
        )

        return Response(status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        balance_id = kwargs.get("pk", None)

        Balance.objects.get(pk=balance_id).delete()

        return Response(status=status.HTTP_200_OK)

    # @action(methods=['get'], detail=True)
    # def groups(self, request, pk):
    #     groups = Group.objects.filter(group_info__owner=request.user, balances=pk)
    #     groups = {"results": [{"name": g.group_info.name} for g in groups]}
    #     return Response(status=status.HTTP_200_OK, data=groups)

    @action(methods=['get'], detail=True)
    def transactions(self, request, pk):
        self.serializer_class = TransactionSerializer
        transactions = Transaction.objects.filter(balance=pk)

        page = self.paginate_queryset(transactions)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(transactions, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
