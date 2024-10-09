from django.contrib import admin
from django.urls import path, include

from expenses.rest.views import CustomObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', CustomObtainAuthToken.as_view(), name='api_token_auth'),
    path('core/api/', include('expenses.rest.urls')),
]
