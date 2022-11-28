from rest_framework import serializers

from api.profiles.serializers import ProfileSerializer


class UserProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=255)
    profile = ProfileSerializer(read_only=True)


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(min_length=8, style={"input_type": "password"})
