from rest_framework import serializers

from apps.transactions.models import TRANSACTION_TYPE_CHOICE


class TransactionCategorySerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=255
    )
    type = serializers.ChoiceField(
        choices=TRANSACTION_TYPE_CHOICE
    )


class TransactionSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    category = TransactionCategorySerializer()
    comment = serializers.CharField()
    created_at = serializers.DateTimeField(
        read_only=True
    )
