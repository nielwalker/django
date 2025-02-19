from django.urls import path 
from . import views 
from django.contrib import admin 
from django.urls import include, path 

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]