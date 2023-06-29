from .router import *
from django.contrib import admin
from django.urls import path, include
from accounts.models import *
from main.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('accounts/', include('accounts.urls')),
    path('', MainView.as_view(), name='index'),
    path('index/', index, name='dd'),
    path('set/', SetView.as_view(), name='set'),
    path('<str:username>/', MainView.as_view(), name='main'),
]
