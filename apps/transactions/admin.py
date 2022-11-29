from django.contrib import admin

from apps.transactions.models import Transaction, TransactionCategory


class TransactionInline(admin.TabularInline):
    model = Transaction


@admin.register(TransactionCategory)
class TransactionCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "type")
    fields = ("name", "type")
    search_fields = ("name", "type")


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "balance",
        "amount",
        "category",
        "comment",
        "created_at",
    )
    fields = ("balance", "amount", "category", "comment","created_at")
    list_filter = ("category__name", "balance__name")
    # readonly_fields = ("created_at",)
    search_fields = (
        "balance__name",
        "amount",
        "category__name",
        "category__type",
        "comment",
        "created_at",
    )
