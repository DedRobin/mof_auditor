from django.contrib import admin

from accounting.models import Accounting


@admin.register(Accounting)
class AccountingAdmin(admin.ModelAdmin):
    list_display = ("balance", "amount", "type", "accounting_category", "comment", "created_at")
    fields = ("balance", "amount", "type", "accounting_category", "comment", "created_at")
    list_filter = ("type", "accounting_category__name")
    readonly_fields = ("created_at",)
    search_fields = ("balance__name", "amount", "type", "accounting_category", "comment", "created_at")
