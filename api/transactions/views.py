from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.transactions.models import Transaction

from api.transactions.serializers import TransactionSerializer
from apps.transactions.services import create_transaction_API, update_transaction_API


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "transaction_id"

    def get_queryset(self):
        balance_id = self.kwargs.get("pk")
        transaction_id = self.kwargs.get("transaction_id")
        transaction = Transaction.objects.filter(balance=balance_id).order_by(
            "-created_at"
        )
        if transaction_id:
            transaction = Transaction.objects.filter(pk=transaction_id)
        return transaction

    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        create_transaction_API(
            balance_id=kwargs.get("pk"), validated_data=serializer.validated_data
        )

        return Response(status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        transaction_id = kwargs.get("transaction_id")

        update_transaction_API(
            transaction_id=transaction_id,
            validated_data=serializer.validated_data,
        )

        return Response(status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        transaction_id = kwargs.get("transaction_id")

        Transaction.objects.get(pk=transaction_id).delete()

        return Response(status=status.HTTP_200_OK)
