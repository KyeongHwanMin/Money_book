from django.contrib import admin
from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    search_fields = ['memo']
    list_display = ['pk', 'memo', 'user']



