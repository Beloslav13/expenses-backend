from django.contrib import admin

from expenses.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'user')
    search_fields = ('name', 'user__username')
    ordering = ('id',)
