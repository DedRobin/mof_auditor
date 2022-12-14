from rest_framework import serializers

from apps.groups.models import Group
from api.groups.serializers import MyOwnGroupSerializer


class InvitationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    to_who = serializers.CharField(max_length=255, required=True)
    # to_a_group = MyOwnGroupSerializer(
    #     queryset=Group.objects.all(), required=True
    # )
    to_a_group = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(), required=True
    )
