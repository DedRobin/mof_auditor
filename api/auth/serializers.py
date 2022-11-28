from rest_framework import serializers

from api.profiles.serializers import ProfileSerializer


class UsernameSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(min_length=8, style={"input_type": "password"})


class RegisterSerializer(UserSerializer, ProfileSerializer):
    ...


class LoginSerializer(UserSerializer):
    ...
