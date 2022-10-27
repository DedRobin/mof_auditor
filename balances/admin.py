from django.contrib import admin

from balances.models import Balance, BalanceCurrency


@admin.register(BalanceCurrency)
class BalanceCurrencyAdmin(admin.ModelAdmin):
    list_display = ("name", "codename")
    fields = ("name", "codename")
    search_fields = ("name", "codename")


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "type", "currency", "private", "created_at")
    fields = ("name", "owner", "type", "currency", "private")
    list_filter = ("type", "currency", "private",)
    readonly_fields = ("created_at",)
    search_fields = ("owner__username", "name", "type", "currency", "private", "created_at")
    radio_fields = {"type": admin.VERTICAL, "private": admin.VERTICAL}
