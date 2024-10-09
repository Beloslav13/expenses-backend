from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from expenses.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'external_id')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_bot', 'is_premium')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'external_id', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')
