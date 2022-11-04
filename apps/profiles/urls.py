from django.urls import path

from apps.profiles.views import edit_profile

urlpatterns = [
    path("", edit_profile, name="edit_profile"),
]
