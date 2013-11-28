from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ExpenseItem(models.Model):
    name=models.Charfield(max_length=100)

class Expense(models.Model):
    expenseItem = models.ForeignKey(ExpenseItem)
    expense_date=models.DateTimeField('expense date')
    amount=models.DecimalField(max_digits=6,decimal_places=2)
    comments=models.TextTfield()
    user=models.ForeignKey(User)
    borrower=models.ForeignKey(User)