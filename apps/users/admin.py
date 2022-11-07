from django.contrib import admin

from apps.users.models import User
from apps.profiles.admin import ProfileInline
from apps.balances.admin import BalanceInline


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "is_staff", "is_superuser", "created_at")
    fields = (
        "username",
        "is_staff",
        "is_superuser",
        (
            "groups",
            "user_permissions",
        ),
    )
    list_filter = ("is_staff", "is_superuser")
    readonly_fields = ("created_at",)
    search_fields = ("username", "is_staff", "is_superuser")

    inlines = [
        ProfileInline, BalanceInline
    ]
