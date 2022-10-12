from django.contrib import admin

from permissions.models import Permission


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ("name", "codename")
    fields = ("name", "codename")
    list_filter = ("name",)
    search_fields = ("name", "codename")
