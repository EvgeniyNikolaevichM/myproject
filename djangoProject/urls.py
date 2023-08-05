from django.contrib import admin
from django.urls import path, include
from lawAPI.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('systemStewartPlatform.urls')),
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls')), # http://127.0.0.1:8000/api/auth/login/ авторизация через cookies
]