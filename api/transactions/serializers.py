from rest_framework import serializers

from apps.transactions.models import TransactionCategory


class TransactionSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    category = serializers.PrimaryKeyRelatedField(
        queryset=TransactionCategory.objects.all()
    )
    comment = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(read_only=True)
