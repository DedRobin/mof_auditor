from django.contrib import admin

from apps.profiles.models import Profile


class ProfileInline(admin.TabularInline):
    model = Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "email", "gender", "first_name", "last_name", "created_at")
    fields = ("user", "email", "gender", "first_name", "last_name")
    list_filter = ("gender",)
    readonly_fields = ("created_at",)
    search_fields = (
        "user__username",
        "email",
        "first_name",
        "last_name",
        "gender",
        "created_at",
    )
