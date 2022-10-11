from django.contrib import admin

from balance.models import Balance


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ("name", "amount", "type", "currency", "created_at")
    fields = ("name", "users", "amount", "type", "currency")
    list_filter = ("type", "currency")
    readonly_fields = ("created_at",)
    search_fields = ("users__username", "amount", "type", "currency", "created_at")

