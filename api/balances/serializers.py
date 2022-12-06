from rest_framework import serializers
from django.conf import settings

from apps.balances.models import BALANCE_TYPE_CHOICE
from apps.balances.models import BalanceCurrency
from apps.groups.models import Group
from api.groups.serializers import CustomGroupSerializer


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
        queryset=BalanceCurrency.objects.all(),
    )
    private = serializers.BooleanField()
    total = serializers.DecimalField(
        max_digits=settings.MAX_DIGITS,
        decimal_places=settings.DECIMAL_PLACES, )
    groups = CustomGroupSerializer(
        queryset=Group.objects.all(), many=True, required=False
    )
