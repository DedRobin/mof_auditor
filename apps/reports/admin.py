from django.contrib import admin
from apps.reports.models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "balance",
        "total",
        "created_at",
    )
    fields = (
        "balance",
        "total",
    )
    readonly_fields = ("created_at",)

    search_fields = (
        "balance__name",
        "total",
        "created_at",
    )
