from django.db import models
from django.contrib.auth.models import User


class TransactionCategories(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Transactions(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    trans_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    category = models.ForeignKey(TransactionCategories, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.date}"


class UserBalance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Balance for {self.user.username} is {self.balance}"

    def calculate_balance(self):
        """
        Calculate the user's balance based on transactions.
        """
        transactions = Transactions.objects.filter(user=self.user)
        income = transactions.filter(trans_type='income').aggregate(models.Sum('amount'))['amount__sum'] or 0
        expense = transactions.filter(trans_type='expense').aggregate(models.Sum('amount'))['amount__sum'] or 0

        self.balance = income - abs(expense)
        self.save()




