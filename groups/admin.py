from django.contrib import admin

from groups.models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("group_id", "user", "balance", "permission", "created_at")
    fields = ("group_id", "user", "balance", "permission")
    readonly_fields = ("created_at",)
    search_fields = ("group_id", "created_at")
