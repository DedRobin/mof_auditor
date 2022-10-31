from django.contrib import admin

from transactions.models import Transaction, TransactionCategory


@admin.register(TransactionCategory)
class TransactionCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "type")
    fields = ("name", "type")
    search_fields = ("name", "type")


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("balance", "amount", "category", "comment", "who_made", "created_at")
    fields = ("balance", "amount", "category", "comment", "who_made")
    list_filter = ("category__name", "balance__name")
    readonly_fields = ("created_at",)
    search_fields = ("balance__name", "amount", "category", "comment", "created_at")
