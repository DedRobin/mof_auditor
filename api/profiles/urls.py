from django.urls import include, path
from api.profiles.views import ProfileUpdateAPI

# actions_for_list = {"get": "list", "post": "create"}
actions_for_one_note = {
    "get": "retrieve",
    "put": "update"
    # "delete": "destroy",
}

urlpatterns = [
    path("", ProfileUpdateAPI.as_view(), name="profile"),
]
