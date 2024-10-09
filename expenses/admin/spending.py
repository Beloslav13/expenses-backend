from django.contrib import admin

from expenses.models import Spending


@admin.register(Spending)
class SpendingAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'category', 'cost', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'user', 'category')
    search_fields = ('name', 'user__username', 'category__name')
    ordering = ('id',)
