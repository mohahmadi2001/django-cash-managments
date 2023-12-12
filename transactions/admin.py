from django.contrib import admin
from .models import Transactions, TransactionCategories, UserBalance


class TransactionCategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(TransactionCategories, TransactionCategoriesAdmin)


class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'amount', 'trans_type', 'category', 'date')
    list_filter = ('trans_type', 'category', 'date')


admin.site.register(Transactions, TransactionsAdmin)


class UserBalanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')


admin.site.register(UserBalance, UserBalanceAdmin)