from django.contrib import admin
from apps.permissions.models import Permission, PermissionType


@admin.register(PermissionType)
class PermissionTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    fields = ("name",)
    search_fields = ("name",)


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "group",
        "all_types",
    )
    fields = (
        "user",
        "group",
        "types",
    )
    search_fields = (
        "user__username",
        "group__group_info__name",
    )
