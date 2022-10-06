from django.contrib import admin

from accounting_category.models import AccountingCategory


@admin.register(AccountingCategory)
class AccountingCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    fields = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)
