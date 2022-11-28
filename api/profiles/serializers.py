from rest_framework import serializers

from apps.profiles.models import GENDER_CHOICE


class ProfileSerializer(serializers.Serializer):
    gender = serializers.ChoiceField(required=False, choices=GENDER_CHOICE)
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(max_length=255, required=False)
    last_name = serializers.CharField(max_length=255, required=False)


class UserProfileSerializer(ProfileSerializer):
    username = serializers.CharField(max_length=255)
