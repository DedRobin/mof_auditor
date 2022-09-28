from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "is_staff", "is_superuser", "created_at")
    fields = ("email", "is_staff", "is_superuser")
    list_filter = ("is_staff", "is_superuser")
    readonly_fields = ("created_at",)
    search_fields = ("email", "is_staff", "is_superuser")
