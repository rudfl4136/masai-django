from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    ## 초기 셋팅
    path('masai/', include('masai.urls')),
    path('admin/', admin.site.urls),
]
