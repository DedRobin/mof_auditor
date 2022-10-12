from django.contrib import admin

from groups.models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "balance", "permission", "created_at")
    fields = ("name", "user", "balance", "permission")
    readonly_fields = ("created_at",)
    search_fields = ("name", "created_at")
