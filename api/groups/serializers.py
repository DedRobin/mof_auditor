from rest_framework import serializers

from api.users.serializers import UserProfileSerializer
from api.balances.serializers import MyBalanceSerializer
from apps.balances.models import Balance


class GroupInfoSerializer(serializers.Serializer):
    owner = serializers.StringRelatedField()
    name = serializers.CharField(
        max_length=255,
    )
    description = serializers.CharField(required=False)


class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    group_info = GroupInfoSerializer()
    invited_users = UserProfileSerializer(required=False, many=True, read_only=True)
    balances = MyBalanceSerializer(queryset=Balance.objects.all(), required=False, many=True)


class MyGroupSerializer(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get("request", None)
        queryset = super(MyGroupSerializer, self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(group_info__owner=request.user)
