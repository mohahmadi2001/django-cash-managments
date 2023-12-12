from django.contrib import admin
from reports.models import TransactionReport, TransactionReportType


@admin.register(TransactionReportType)
class TransactionReportTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


# admin.site.register(TransactionReportType, TransactionReportTypeAdmin)



class TransactionReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'report_type', 'created_at')
    list_filter = ('report_type', 'created_at')


admin.site.register(TransactionReport, TransactionReportAdmin)