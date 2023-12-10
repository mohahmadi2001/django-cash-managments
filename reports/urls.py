from django.urls import path
from .views import (
    MonthlySummaryAPIView,
    CategoryExpenseReportAPIView,
    TransactionReportCreateAPIView,
    TransactionReportTypeCreateAPIView, TransactionReportDeleteAPIView, TransactionReportTypeDeleteAPIView
)


urlpatterns = [
    path('type/create/', TransactionReportTypeCreateAPIView.as_view(), name='report-type-create-api'),
    path('create/', TransactionReportCreateAPIView.as_view(), name='transaction-report-create-api'),
    path('delete/<int:pk>/', TransactionReportDeleteAPIView.as_view(), name='transaction-report-delete-api'),
    path('report-type/delete/<int:pk>/', TransactionReportTypeDeleteAPIView.as_view(), name='report-type-delete-api'),
    path('monthly-summary/', MonthlySummaryAPIView.as_view(), name='monthly-summary-api'),
    path('category-expense-report/', CategoryExpenseReportAPIView.as_view(), name='category-expense-report-api'),
]