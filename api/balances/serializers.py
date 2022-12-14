from rest_framework import serializers

from apps.balances.models import BALANCE_TYPE_CHOICE
from apps.balances.models import Currency
from apps.groups.models import Group
from api.groups.serializers import MyOwnGroupSerializer


class BalanceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    pub_id = serializers.StringRelatedField()
    name = serializers.CharField(
        max_length=255,
        required=False,
    )
    owner = serializers.StringRelatedField()
    type = serializers.ChoiceField(
        choices=BALANCE_TYPE_CHOICE,
    )
    currency = serializers.PrimaryKeyRelatedField(
        queryset=Currency.objects.all(),
    )
    private = serializers.BooleanField()
    total = serializers.StringRelatedField()
    groups = MyOwnGroupSerializer(
        queryset=Group.objects.all(), many=True, required=False
    )
