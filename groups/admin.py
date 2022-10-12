from django.contrib import admin

from groups.models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    fields = ("name",)
    readonly_fields = ("created_at",)
    search_fields = ("name", "created_at")
