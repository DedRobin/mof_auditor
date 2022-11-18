from django.contrib import admin
from apps.permissions.models import Permission


# @admin.register(Permission)
# class PermissionAdmin(admin.ModelAdmin):
#     list_display = ("permission_type", "user")
#     fields = ("permission_type", "user")
#     search_fields = ("permission_type", "user__username")
