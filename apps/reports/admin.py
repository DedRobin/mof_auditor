from django.contrib import admin
from apps.reports.models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
        "balance",
        "date_from",
        "date_to",
        "total",
        "created_at",
    )
    fields = (
        "balance",
        "date_from",
        "date_to",
        "total",
    )
    readonly_fields = ("created_at",)

    search_fields = (
        "balance__name",
        "date_from",
        "date_to",
        "total",
        "created_at",
    )
