from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),    
    path('ai_request/',views.ai_request, name='ai_request'),    
] 