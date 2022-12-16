from rest_framework import serializers

from apps.groups.models import Group
from api.groups.serializers import MyGroupSerializer


class InvitationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    from_who = serializers.CharField(max_length=255, read_only=True)
    to_who = serializers.CharField(max_length=255, required=True)
    to_a_group = MyGroupSerializer(queryset=Group.objects.all(), required=True)
