from .router import *
from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('<str:username>/', main, name='main'),
    path('<str:username>/set/', set, name='set')
]
