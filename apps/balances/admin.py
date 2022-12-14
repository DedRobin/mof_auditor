from django.contrib import admin

from apps.balances.models import Balance, Currency
from apps.transactions.admin import TransactionInline


class BalanceInline(admin.TabularInline):
    model = Balance


@admin.register(Currency)
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
        "for_groups",
    )
    fields = (
        "name",
        "owner",
        "type",
        "currency",
        "private",
        "groups",
    )
    list_filter = (
        "type",
        "private",
    )
    readonly_fields = ("created_at",)
    search_fields = (
        "owner__username",
        "name",
        "pub_id",
        "type",
        "currency__name",
        "currency__codename",
        "private",
    )
    radio_fields = {"type": admin.VERTICAL, "private": admin.VERTICAL}

    inlines = [
        TransactionInline,
    ]
