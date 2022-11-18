from django.contrib import admin

from apps.groups.models import Group, GroupInformation, Invitation


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
        "created_at",
    )
    fields = (
        "group_info",
        "invited_users",
    )
    readonly_fields = ("created_at",)
    search_fields = (
        "group_info__name",
        "created_at",
        "pub_id",
    )


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = (
        "pub_id",
        "to_a_group",
        "from_who",
        "to_who",
        "created_at",
    )
    fields = (
        "pub_id",
        "to_a_group",
        "from_who",
        "to_who",
    )
    search_fields = (
        "pub_id",
        "to_a_group__group_info__name",
        "from_who__username",
        "to_who__username",
    )
