from rest_framework import serializers

from apps.profiles.models import GENDER_CHOICE


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(min_length=8, style={"input_type": "password"})
    gender = serializers.ChoiceField(required=False, choices=GENDER_CHOICE)
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(max_length=150, required=False)
    last_name = serializers.CharField(max_length=150, required=False)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(min_length=8, style={"input_type": "password"})
