from django.contrib import admin

from apps.invitations.models import Invitation


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
