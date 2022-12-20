from django.contrib import admin
from apps.reports.models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
        "balance",
        "total",
        "difference",
        "created_at",
    )
    fields = (
        "balance",
        "total",
        "difference",
    )
    readonly_fields = ("created_at",)

    search_fields = (
        "balance__name",
        "total",
        "difference",
        "created_at",
    )
