from django.contrib import admin

from apps.groups.models import Group, GroupInformation


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


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        "group_info",
        "pub_id",
        "all_invited_users",
        "all_linked_balances",
        "created_at",
    )
    fields = (
        "group_info",
        "invited_users",
        "balances",
    )
    readonly_fields = ("created_at",)
    search_fields = (
        "group_info__name",
        "created_at",
        "pub_id",
    )
    list_filter = ("group_info__owner",)
