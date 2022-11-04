from django.contrib import admin

from users.models import User
from profiles.models import Profile


class ProfileInline(admin.TabularInline):
    model = Profile


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
        ProfileInline,
    ]
