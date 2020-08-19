from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/inventory/', include('inventory.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
