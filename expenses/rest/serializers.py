from rest_framework import serializers
from expenses.models import Category, Spending, User

TMP_ERROR = 'Это поле обязательное'


class CategorySerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(view_name='category-detail')
    user_external_id = serializers.IntegerField(source='user.external_id', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'is_active', 'created_at', 'updated_at', 'detail_url', 'user', 'user_external_id',
                  'user_username']


class SpendingSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(view_name='spending-detail')
    user_external_id = serializers.IntegerField(source='user.external_id', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Spending
        fields = ['id', 'name', 'cost', 'is_active', 'created_at', 'updated_at', 'detail_url', 'user',
                  'user_external_id', 'user_username', 'category', 'category_name']


class UserListSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(view_name='user-detail')
    category_count = serializers.IntegerField(read_only=True)
    total_spending = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'external_id', 'is_bot',
                  'is_premium', 'category_count', 'total_spending', 'detail_url']


class UserDetailSerializer(serializers.ModelSerializer):
    category_count = serializers.IntegerField(read_only=True)
    total_spending = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'external_id', 'is_bot',
                  'is_premium', 'category_count', 'total_spending']
