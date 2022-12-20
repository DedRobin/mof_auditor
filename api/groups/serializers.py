from django.db.models import Q
from rest_framework import serializers

from apps.users.models import User
from api.users.serializers import UserProfileSerializer


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


class MyAndInvitedGroupSerializer(serializers.PrimaryKeyRelatedField, GroupSerializer):
    def get_queryset(self):
        request = self.context.get("request", None)
        queryset = super(MyAndInvitedGroupSerializer, self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(
            Q(group_info__owner=request.user) | Q(invited_users=request.user)
        )


class MyGroupSerializer(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get("request", None)
        queryset = super(MyGroupSerializer, self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(group_info__owner=request.user)
