from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('',views.index, name='index'),    
    path('ai_request/',views.ai_request, name='ai_request'),    
] 