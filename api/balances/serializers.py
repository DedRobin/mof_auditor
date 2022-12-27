from rest_framework import serializers

from apps.balances.models import BALANCE_TYPE_CHOICE
from apps.balances.models import Currency


class BalanceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    pub_id = serializers.StringRelatedField()
    name = serializers.CharField(max_length=255, required=False)
    owner = serializers.StringRelatedField()
    type = serializers.ChoiceField(choices=BALANCE_TYPE_CHOICE)
    currency = serializers.PrimaryKeyRelatedField(queryset=Currency.objects.all())
    private = serializers.BooleanField()
    total = serializers.StringRelatedField()


class MyBalanceSerializer(serializers.PrimaryKeyRelatedField, BalanceSerializer):
    def get_queryset(self):
        request = self.context.get("request", None)
        queryset = super(MyBalanceSerializer, self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(owner=request.user).order_by("name")
