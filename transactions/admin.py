# from django.contrib import admin
#
# from transactions.models import Accounting, AccountingCategory
#
#
# @admin.register(AccountingCategory)
# class AccountingCategoryAdmin(admin.ModelAdmin):
#     list_display = ("name",)
#     fields = ("name",)
#     search_fields = ("name",)
#
#
# @admin.register(Accounting)
# class AccountingAdmin(admin.ModelAdmin):
#     list_display = ("balance", "amount", "type", "category", "comment", "created_at")
#     fields = ("balance", "amount", "type", "category", "comment", "created_at")
#     list_filter = ("type", "category__name")
#     readonly_fields = ("created_at",)
#     search_fields = ("balance__name", "amount", "type", "category", "comment", "created_at")
#
