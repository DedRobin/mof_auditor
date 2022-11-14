from django.contrib import admin
from apps.invitations.models import Invitation


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = (
        "from_who",
        "to_who",
        "to_a_group",
        "created_at",
    )
    fields = (
        "from_who",
        "to_who",
        "to_a_group",
    )
    search_fields = (
        "from_who__username",
        "to_who__username",
        "to_a_group__name",
    )
