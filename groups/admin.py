from django.contrib import admin

from groups.models import Group, GroupID


@admin.register(GroupID)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    fields = ("name",)
    search_fields = ("name",)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("group_id", "user", "balance", "permission", "created_at")
    fields = ("group_id", "user", "balance", "permission")
    readonly_fields = ("created_at",)
    search_fields = ("group_id", "group_id__name", "created_at")
