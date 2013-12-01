__author__ = 'surendra'

from django.contrib import admin
from hisabkitab.models import ExpenseItem,Expense

admin.site.register(Expense)
admin.site.register(ExpenseItem)
