from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView

from apps.profiles.models import Profile
from api.profiles.serializers import ProfileSerializer
from apps.profiles.services import update_profile_api


class ProfileUpdateAPI(UpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.all()

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def get(self, request):
        obj = self.get_object()
        serializer = self.serializer_class(obj)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        update_profile_api(user=self.request.user, validated_data=serializer.data)

        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
