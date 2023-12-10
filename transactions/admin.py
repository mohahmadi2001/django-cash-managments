from django.contrib import admin
from .models import Transactions, Category, UserBalance


admin.site.register(Transactions)
admin.site.register(Category)
admin.site.register(UserBalance)
