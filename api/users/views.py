from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

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
