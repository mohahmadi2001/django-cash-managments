from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase

from reports.models import TransactionReportType, TransactionReport
from transactions.models import Category, Transactions


class TransactionReportTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", password="testpassword")
        self.category = Category.objects.create(name="TestCategory")
        self.report_type = TransactionReportType.objects.create(name="TestReportType")

    def test_generate_monthly_summary_no_transactions(self):
        report = TransactionReport.generate_monthly_summary(self.user, date.today().year, date.today().month)

        self.assertEqual(report.user, self.user)
        self.assertIn("Monthly Summary", report.title)
        self.assertIn("Income: 0", report.content)

    def test_generate_category_expense_report_no_expense(self):
        report = TransactionReport.generate_category_expense_report(self.user, date.today().year, date.today().month)

        self.assertEqual(report.user, self.user)
        self.assertIn("Category-wise Expense Report", report.title)
        self.assertIn("TestCategory: 0", report.content)

    def test_generate_monthly_summary_with_income_and_expense(self):
        Transactions.objects.create(user=self.user, amount=100, trans_type='income',
                                    category=self.category, date=date.today())
        Transactions.objects.create(user=self.user, amount=50, trans_type='expense',
                                    category=self.category, date=date.today())

        report = TransactionReport.generate_monthly_summary(self.user, date.today().year, date.today().month)

        self.assertEqual(report.user, self.user)
        self.assertIn("Monthly Summary", report.title)
        self.assertIn("Income: 100", report.content)
        self.assertIn("Expense: 50", report.content)
        self.assertIn("Net Balance: 50", report.content)

    def test_generate_category_expense_report_with_expense(self):
        Transactions.objects.create(user=self.user, amount=75, trans_type='expense',
                                    category=self.category, date=date.today())

        report = TransactionReport.generate_category_expense_report(self.user, date.today().year, date.today().month)

        self.assertEqual(report.user, self.user)
        self.assertIn("Category-wise Expense Report", report.title)
        self.assertIn("TestCategory: 75", report.content)
