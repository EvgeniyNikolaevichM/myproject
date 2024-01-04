from django.urls import path
from .import views

urlpatterns = [
    path('systemLawView/<int:pk>/', views.systemLawView, name='systemLawView'),
    path('ForFullLaw/<int:pk>/', views.ForFullLaw, name='ForFullLaw'),
]