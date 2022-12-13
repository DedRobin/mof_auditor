from django.urls import path
from api.profiles.views import ProfileUpdateAPI

urlpatterns = [
    path("", ProfileUpdateAPI.as_view(), name="profile"),
]
