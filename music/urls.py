from .router import *
from django.contrib import admin
from django.urls import path, include
from accounts.models import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('accounts/', include('accounts.urls')),
    path('', main, name='index'),
    # path('<str:username>/', main, name='main'),
    path('set/', set, name='set'),
]
