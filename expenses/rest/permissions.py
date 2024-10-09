from rest_framework import permissions


class IsRootOrAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        # Проверяем, является ли пользователь root
        if request.user.is_superuser:
            return True
        # Проверяем, авторизован ли пользователь
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Проверяем, является ли пользователь root
        if request.user.is_superuser:
            return True
        # Проверяем, авторизован ли пользователь
        return request.user and request.user.is_authenticated
