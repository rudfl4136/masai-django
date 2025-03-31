from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    ## �ʱ� ����
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('masai/', include('masai.urls')),
    path('admin/', admin.site.urls),
]
