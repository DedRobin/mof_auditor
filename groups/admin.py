from django.contrib import admin

from groups.models import Group, GroupInformation, Permission


class GroupInline(admin.TabularInline):
    model = Group


@admin.register(GroupInformation)
class GroupInformationAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    fields = ("name", "description")
    search_fields = ("name", "description")

    inlines = [GroupInline, ]


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ("name", "codename", "get_users")
    fields = ("name", "codename", "users")
    search_fields = ("name", "codename")


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    # list_display = ("group_id", "user", "balance", "permission", "created_at")
    list_display = ("group_info", "get_users", "get_permissions", "created_at")
    fields = ("group_info", "users", "permissions")
    readonly_fields = ("created_at",)
    search_fields = ("group_info", "group_info__name", "created_at")
