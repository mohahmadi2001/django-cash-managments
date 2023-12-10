from django.contrib import admin
from reports.models import TransactionReport, TransactionReportType

admin.site.register(TransactionReport)
admin.site.register(TransactionReportType)
