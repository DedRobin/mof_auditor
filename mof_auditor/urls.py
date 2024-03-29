"""mof_auditor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from apps.transactions.views import get_transactions, export_operations
from apps.users.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls", namespace="api")),
    path("django-rq/", include("django_rq.urls")),
    path("", index, name="index"),
    path("auth/", include("apps.users.urls")),
    path("profile/", include("apps.profiles.urls")),
    path("groups/", include("apps.groups.urls")),
    path("balances/", include("apps.balances.urls")),
    path("invitations/", include("apps.invitations.urls")),
    path("operations/", get_transactions, name="operation_list"),
    path("operations/export", export_operations, name="export_operations"),
    path("analytics/", include("apps.analytics.urls")),
]
