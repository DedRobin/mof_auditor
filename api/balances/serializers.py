from rest_framework import serializers

from apps.balances.models import BALANCE_PRIVATE_CHOICE, BALANCE_TYPE_CHOICE
from api.auth.serializers import UsernameSerializer
from api.groups.serializers import GroupSerializer


class BalanceCurrencySerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=255,
    )
    codename = serializers.CharField(
        max_length=255,
    )


class BalanceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    pub_id = serializers.CharField(
        max_length=255,
        required=False,
    )
    name = serializers.CharField(
        max_length=255,
        required=False,
    )
    owner = UsernameSerializer()
    type = serializers.ChoiceField(
        choices=BALANCE_TYPE_CHOICE,
    )
    currency = BalanceCurrencySerializer()
    private = serializers.BooleanField()
    groups = GroupSerializer(
        many=True,
    )
