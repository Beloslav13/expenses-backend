from django.db.models import Count, Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from expenses.rest.filters import CategoryFilter, SpendingFilter
from expenses.rest.serializers import UserListSerializer, UserDetailSerializer, CategorySerializer, SpendingSerializer
from expenses.models import User, Category, Spending


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserDetailSerializer
        return UserListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(
            category_count=Count('categories'),
            total_spending=Sum('spendings__cost')
        ).select_related('categories', 'spendings')
        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        data['category_count'] = instance.category_count
        data['total_spending'] = instance.total_spending
        return Response(data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(is_active=True).select_related('user').all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = CategoryFilter
    search_fields = ['user__id', 'user__external_id', 'user__username']


class SpendingViewSet(viewsets.ModelViewSet):
    queryset = Spending.objects.filter(is_active=True).select_related('user', 'category').all()
    serializer_class = SpendingSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = SpendingFilter
    search_fields = ['user__id', 'user__external_id', 'user__username']


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'user_id': token.user_id, 'username': token.user.username})
