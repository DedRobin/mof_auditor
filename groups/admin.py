# from django.contrib import admin
#
# from groups.models import Group, GroupInformation
#
#
# @admin.register(GroupInformation)
# class GroupInformationAdmin(admin.ModelAdmin):
#     list_display = ("id", "name", "description")
#     fields = ("name", "description")
#     search_fields = ("name", "description")
#
#
# @admin.register(Group)
# class GroupAdmin(admin.ModelAdmin):
#     # list_display = ("group_id", "user", "balance", "permission", "created_at")
#     list_display = ("group_info", "get_users", "get_balances", "get_permission", "created_at")
#     fields = ("group_info", "user", "balance", "permission")
#     readonly_fields = ("created_at",)
#     search_fields = ("group_info", "group__name", "created_at")
