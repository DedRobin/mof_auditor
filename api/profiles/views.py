from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView, get_object_or_404

from apps.profiles.models import Profile
from api.profiles.serializers import ProfileSerializer
from apps.profiles.services import update_profile_API


class ProfileUpdateAPI(UpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = self.serializer_class(profile)

        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        update_profile_API(user=self.request.user, validated_data=serializer.data)

        return Response(status=status.HTTP_200_OK, data=serializer.data)
