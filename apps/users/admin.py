from django.contrib import admin

from apps.users.models import User
from apps.profiles.admin import ProfileInline
from apps.balances.admin import BalanceInline
from import_export.admin import ImportExportModelAdmin


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    list_display = ("username", "password", "is_staff", "is_superuser", "created_at")
    fields = ("username", "password", "is_staff", "is_superuser",)
    list_filter = ("is_staff", "is_superuser")
    readonly_fields = ("created_at",)
    search_fields = ("username", "is_staff", "is_superuser")

    inlines = [ProfileInline, BalanceInline]
