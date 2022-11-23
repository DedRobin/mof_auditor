from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, RetrieveAPIView
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.auth.serializers import LoginSerializer, RegisterSerializer
from apps.users.services import create_user_and_profile


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = []

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_user_and_profile(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)


class LoginView(CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = []

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user = authenticate(
            request,
            username=request.data["username"],
            password=request.data["password"],
        )
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        token = Token.objects.get_or_create(user=user)[0].key
        login(request, user)
        return Response(status=status.HTTP_200_OK, data={"token": token})


class LogoutView(RetrieveAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = []

    def get(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        Token.objects.get_or_create(user=request.user)[0].delete()
        logout(request)
        return Response("User logged out successfully")
