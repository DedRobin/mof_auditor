from rest_framework import serializers

from apps.balances.models import BALANCE_TYPE_CHOICE
from api.auth.serializers import UsernameSerializer
from apps.balances.models import BalanceCurrency
from apps.groups.models import Group


class BalanceSerializer(serializers.Serializer):
    id = serializers.IntegerField(
        read_only=True
    )
    pub_id = serializers.CharField(
        max_length=255,
        read_only=True
    )
    name = serializers.CharField(
        max_length=255,
        required=False,
    )
    owner = UsernameSerializer(
        read_only=True,
    )
    type = serializers.ChoiceField(
        choices=BALANCE_TYPE_CHOICE,
    )
    currency = serializers.PrimaryKeyRelatedField(
        queryset=BalanceCurrency.objects.order_by("name"),
    )
    private = serializers.BooleanField()
    # groups = serializers.PrimaryKeyRelatedField(
    #     queryset=Group.objects.filter(group_info__owner=),
    #     many=True,
    # )
