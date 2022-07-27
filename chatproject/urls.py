
from django.contrib import admin
from django.urls import  include, path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_one.urls'))
]