from api.profiles.serializers import ProfileSerializer
from api.users.serializers import UserSerializer


class RegisterSerializer(UserSerializer, ProfileSerializer):
    ...


class LoginSerializer(UserSerializer):
    ...
