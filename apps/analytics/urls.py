from django.urls import path

from apps.analytics.views import get_charts

urlpatterns = [
    path("", get_charts, name="get_charts"),
]
