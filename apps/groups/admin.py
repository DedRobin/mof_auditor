from django.contrib import admin

from apps.groups.models import Group, GroupInformation, Permission


class GroupInline(admin.TabularInline):
    model = Group


@admin.register(GroupInformation)
class GroupInformationAdmin(admin.ModelAdmin):
    list_display = ("owner", "name", "description")
    fields = ("owner", "name", "description")
    search_fields = ("owner__username", "name", "description")

    inlines = [
        GroupInline,
    ]


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ("name", "codename", "applied_to_users")
    fields = ("name", "codename", "users")
    search_fields = ("name", "codename")


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        "group_info",
        "pub_id",
        "all_invited_users",
        "all_permissions",
        "created_at"
    )
    fields = (
        "group_info",
        "pub_id",
        "invited_users",
        "permissions")
    readonly_fields = (
        "created_at",
    )
    search_fields = (
        "group_info__name",
        "created_at",
        "pub_id"
    )
