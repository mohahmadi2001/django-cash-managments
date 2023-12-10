from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db import transaction, models
from .models import Transactions, UserBalance


@receiver(post_save, sender=Transactions)
def update_balance(sender, instance, created, **kwargs):
    """
    A signal handler to update the user's balance when a new transaction is created or updated.
    """
    user = instance.user
    balance_object, created = UserBalance.objects.get_or_create(user=user)

    if instance.trans_type == 'income':
        balance_object.balance += instance.amount
    elif instance.trans_type == 'expense':
        balance_object.balance -= abs(instance.amount)

    balance_object.save()
    balance_object.calculate_balance()
