from django.db import models
from django.contrib.auth.models import User

from transactions.models import Transactions, TransactionCategories


class TransactionReportType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class TransactionReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    report_type = models.ForeignKey(TransactionReportType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @staticmethod
    def generate_monthly_summary(user, year, month):
        transactions = Transactions.objects.filter(user=user, date__year=year, date__month=month)

        income = transactions.filter(trans_type='income').aggregate(models.Sum('amount'))['amount__sum'] or 0
        expense = transactions.filter(trans_type='expense').aggregate(models.Sum('amount'))['amount__sum'] or 0

        net_balance = income - abs(expense)

        title = f"Monthly Summary - {year}-{month}"
        content = f"Income: {income}, Expense: {expense}, Net Balance: {net_balance}"

        report_type, created = TransactionReportType.objects.get_or_create(name="Monthly Summary")

        report = TransactionReport.objects.create(
            user=user,
            title=title,
            content=content,
            report_type=report_type
        )

        return report

    @staticmethod
    def generate_category_expense_report(user, year, month):
        categories = TransactionCategories.objects.all()
        report_content = ""

        for category in categories:
            category_expense = \
                Transactions.objects.filter(user=user, category=category, trans_type='expense', date__year=year,
                                            date__month=month).aggregate(models.Sum('amount'))['amount__sum'] or 0
            report_content += f"{category.name}: {category_expense}, "

        title = f"Category-wise Expense Report - {year}-{month}"

        report_type, created = TransactionReportType.objects.get_or_create(name="Category-wise Expense Report")

        report = TransactionReport.objects.create(
            user=user,
            title=title,
            content=report_content,
            report_type=report_type
        )

        return report
