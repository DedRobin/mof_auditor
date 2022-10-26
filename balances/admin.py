from django.contrib import admin

from balances.models import Balance


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "currency", "created_at")
    fields = ("name", "type", "currency")
    list_filter = ("type", "currency")
    readonly_fields = ("created_at",)
    search_fields = ("name", "type", "currency", "created_at")
    radio_fields = {"type": admin.VERTICAL}

