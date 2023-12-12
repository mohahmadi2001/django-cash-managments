from datetime import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Transactions, UserBalance, TransactionCategories
from decimal import Decimal


class TransactionsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = TransactionCategories.objects.create(name='Test Category')
        self.client.force_login(self.user)

    def test_update_balance_income(self):
        Transactions.objects.create(
            user=self.user,
            amount=100,
            trans_type='income',
            category=self.category,
            date=datetime.now()
        )

        user_balance = UserBalance.objects.get(user=self.user)
        self.assertEqual(user_balance.balance, Decimal(100.00))

    def test_update_balance_expense(self):
        Transactions.objects.create(
            user=self.user,
            amount=-50,
            trans_type='expense',
            category=self.category,
            date=datetime.now()
        )

        user_balance = UserBalance.objects.get(user=self.user)
        self.assertEqual(user_balance.balance, -50.00)

    def test_update_balance_combined(self):
        Transactions.objects.create(
            user=self.user,
            amount=200,
            trans_type='income',
            category=self.category,
            date=datetime.now()
        )

        Transactions.objects.create(
            user=self.user,
            amount=-50,
            trans_type='expense',
            category=self.category,
            date=datetime.now()
        )

        user_balance = UserBalance.objects.get(user=self.user)
        self.assertEqual(user_balance.balance, 150.00)

    def test_calculate_balance(self):
        Transactions.objects.create(
            user=self.user,
            amount=100,
            trans_type='income',
            category=self.category,
            date=datetime.now()
        )

        Transactions.objects.create(
            user=self.user,
            amount=-50,
            trans_type='expense',
            category=self.category,
            date=datetime.now()
        )

        Transactions.objects.create(
            user=self.user,
            amount=200,
            trans_type='income',
            category=self.category,
            date=datetime.now()
        )

        user_balance = UserBalance.objects.get(user=self.user)
        user_balance.calculate_balance()

        self.assertEqual(user_balance.balance, 250.00)