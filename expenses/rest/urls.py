from django.urls import path, include
from rest_framework.routers import DefaultRouter

from expenses.rest.views import UserViewSet, CategoryViewSet, SpendingViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'spendings', SpendingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
