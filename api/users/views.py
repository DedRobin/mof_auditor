from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.users.models import User
from api.users.serializers import UserProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "user_id"

    def get_queryset(self):
        group_id = self.kwargs.get("pk")
        user_id = self.kwargs.get("user_id")
        users = User.objects.filter(user_groups=group_id).order_by("username")
        if user_id:
            user = User.objects.filter(pk=user_id)
            return user
        return users

    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)
    #
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     create_transaction_API(
    #         balance_id=kwargs.get("pk"), validated_data=serializer.validated_data
    #     )
    #
    #     return Response(status=status.HTTP_201_CREATED)
    #
    # def update(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     transaction_id = kwargs.get("transaction_id")
    #
    #     update_transaction_API(
    #         transaction_id=transaction_id,
    #         validated_data=serializer.validated_data,
    #     )
    #
    #     return Response(status=status.HTTP_200_OK)
    #
    # def destroy(self, request, *args, **kwargs):
    #     transaction_id = kwargs.get("transaction_id")
    #
    #     Transaction.objects.get(pk=transaction_id).delete()
    #
    #     return Response(status=status.HTTP_200_OK)
