from rest_framework import serializers

from apps.transactions.models import TransactionCategory


class TransactionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    amount = serializers.IntegerField()
    category = serializers.PrimaryKeyRelatedField(
        queryset=TransactionCategory.objects.order_by("-type")
    )
    comment = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(read_only=True)
