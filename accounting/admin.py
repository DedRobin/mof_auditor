from django.contrib import admin

from accounting.models import Accounting


@admin.register(Accounting)
class AccountingAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "type", "accounting_category", "comment", "created_at")
    fields = ("user", "amount", "type", "accounting_category", "comment", "created_at")
    list_filter = ("type", "accounting_category")
    readonly_fields = ("created_at",)
    search_fields = ("user__email", "amount", "type", "accounting_category", "comment", "created_at")
