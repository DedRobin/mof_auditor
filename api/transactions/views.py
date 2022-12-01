from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.transactions.import_export_resources import TransactionResource
from apps.transactions.models import Transaction

from api.transactions.serializers import TransactionSerializer
from apps.transactions.services import (
    create_transaction_api,
    update_transaction_api,
    get_sorted_transactions,
)


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "transaction_id"

    def get_queryset(self):
        balance_id = self.kwargs.get("pk")
        transaction_id = self.kwargs.get("transaction_id")
        transactions = Transaction.objects.filter(balance_id=balance_id).order_by(
            "-created_at"
        )
        query_param = self.request.query_params

        transactions = get_sorted_transactions(
            queryset=transactions, query_param=query_param
        )

        if transaction_id:
            transaction = Transaction.objects.filter(pk=transaction_id)
            return transaction
        return transactions

    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        create_transaction_api(
            balance_id=kwargs.get("pk"), validated_data=serializer.validated_data
        )

        return Response(status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        transaction_id = kwargs.get("transaction_id")

        update_transaction_api(
            transaction_id=transaction_id,
            validated_data=serializer.validated_data,
        )

        return Response(status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        transaction_id = kwargs.get("transaction_id")

        Transaction.objects.get(pk=transaction_id).delete()

        return Response(status=status.HTTP_200_OK)


class DownloadTransactionAPI(XLSXFileMixin, TransactionViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    renderer_classes = (XLSXRenderer,)
    filename = "transactions.xlsx"

    column_header = {
        "titles": [
            # "id",
            "amount",
            "category",
            "comment",
            "created_at",
        ],
    }

    xlsx_ignore_headers = ["id"]
