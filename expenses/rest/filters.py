import django_filters
from expenses.models import Category, Spending


class CategoryFilter(django_filters.FilterSet):
    user_id = django_filters.NumberFilter(field_name='user__id')

    class Meta:
        model = Category
        fields = ['user_id']


class SpendingFilter(django_filters.FilterSet):
    user_id = django_filters.NumberFilter(field_name='user__id')
    category_id = django_filters.NumberFilter(field_name='category__id')

    class Meta:
        model = Spending
        fields = ['user_id', 'category_id']
