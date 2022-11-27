from django.urls import include, path

app_name = "mof_auditor_api"

urlpatterns = [
    path("auth/", include("api.auth.urls")),
    path("balances/", include("api.balances.urls")),
    path("groups/", include("api.groups.urls")),
]
