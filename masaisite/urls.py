from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    ## �ʱ� ����
    path('masai/', include('masai.urls')),
    path('admin/', admin.site.urls),
]
