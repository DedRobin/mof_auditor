from rest_framework import serializers

from apps.profiles.models import GENDER_CHOICE


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(min_length=8, style={"input_type": "password"})


class ProfileSerializer(serializers.Serializer):
    gender = serializers.ChoiceField(required=False, choices=GENDER_CHOICE)
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(max_length=150, required=False)
    last_name = serializers.CharField(max_length=150, required=False)


class RegisterSerializer(UserSerializer, ProfileSerializer):
    pass


class LoginSerializer(UserSerializer):
    pass
