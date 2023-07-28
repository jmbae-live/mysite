from django.urls import path
from django.contrib.auth import views as auth_views

from account import views

app_name = 'account'

urlpatterns = [
    # path('login/', views.user_login, name='login')
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.dashboard, name='dashboard'),
]
