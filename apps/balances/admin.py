from django.contrib import admin

from apps.balances.models import Balance, BalanceCurrency
from apps.transactions.admin import TransactionInline


class BalanceInline(admin.TabularInline):
    model = Balance


@admin.register(BalanceCurrency)
class BalanceCurrencyAdmin(admin.ModelAdmin):
    list_display = ("name", "codename")
    fields = ("name", "codename")
    search_fields = ("name", "codename")


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
        "pub_id",
        "total",
        "type",
        "currency",
        "private",
        "created_at",
        "all_groups",
    )
    fields = (
        "name",
        "owner",
        "pub_id",
        "type",
        "currency",
        "private",
        "groups",
    )
    list_filter = (
        "type",
        "currency",
        "private",
    )
    readonly_fields = ("created_at",)
    search_fields = (
        "owner__username",
        "name",
        "pub_id",
        "type",
        "currency__name",
        "private",
    )
    radio_fields = {"type": admin.VERTICAL, "private": admin.VERTICAL}

    inlines = [
        TransactionInline,
    ]
