from rest_framework import serializers

from apps.balances.models import BALANCE_TYPE_CHOICE
from apps.balances.models import BalanceCurrency
from apps.groups.models import Group


class CustomGroupSerializer(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super(CustomGroupSerializer, self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(group_info__owner=request.user)


class BalanceSerializer(serializers.Serializer):
    id = serializers.IntegerField(
        read_only=True
    )
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
    total = serializers.IntegerField()
    groups = CustomGroupSerializer(
        queryset=Group.objects.all(),
        many=True,
        required=False
    )
