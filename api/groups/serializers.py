from django.db.models import Q
from rest_framework import serializers

from apps.users.models import User


class GroupInfoSerializer(serializers.Serializer):
    owner = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.order_by("username"),
    )
    name = serializers.CharField(
        max_length=255,
    )
    description = serializers.CharField()


class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    pub_id = serializers.CharField(max_length=255, read_only=True)
    group_info = GroupInfoSerializer()
    invited_users = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.order_by("username"), many=True, required=False
    )


class CustomGroupSerializer(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get("request", None)
        queryset = super(CustomGroupSerializer, self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(Q(group_info__owner=request.user) | Q(invited_users=request.user))
