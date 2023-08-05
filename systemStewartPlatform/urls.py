from django.urls import path,  include

from .views import *


urlpatterns = [
    # path('create_system', views.create_system, name='create_system'),
    # path('read_system', views.read_system, name='read_system'),
    path('systemListView', systemListView.as_view(), name='systemListView'),
    path('systemDetailView/<int:pk>/', systemDetailView.as_view(), name='systemDetailView'),
    path('systemNewView', systemCreateView.as_view(), name='systemCreateView'),
    path('systemDetailView/<int:pk>/edit/', systemEditView.as_view(), name='systemEditView'),
    path('systemDeleteView/<int:pk>/delete/', systemDeleteView.as_view(), name='systemDeleteView'),

    path('platformListView', platformListView.as_view(), name='platformListView'),
    path('platformDetailView/<int:pk>/', platformDetailView.as_view(), name='platformDetailView'),
    path('platformNewView', platformCreateView.as_view(), name='platformCreateView'),
    path('platformDetailView/<int:pk>/edit/', platformEditView.as_view(), name='platformEditView'),
    path('platformDeleteView/<int:pk>/delete/', platformDeleteView.as_view(), name='platformDeleteView'),

    path('LawListView', LawListView.as_view(), name='LawListView'),
    path('LawDetailView/<int:pk>/', LawDetailView.as_view(), name='LawDetailView'),
    path('LawNewView', LawCreateView.as_view(), name='LawCreateView'),
    path('LawDetailView/<int:pk>/edit/', LawEditView.as_view(), name='LawEditView'),
    path('LawDeleteView/<int:pk>/delete/', LawDeleteView.as_view(), name='LawDeleteView'),
]