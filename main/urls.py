from django.urls import path
from .import views
from .views import RegisterUser, LoginUser, logout_user

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', views.admin, name='admin'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
