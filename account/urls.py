from django.urls import path, include
from django.contrib.auth import views as auth_views

from account import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
]
