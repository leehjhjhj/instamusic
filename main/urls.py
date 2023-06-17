from .upload import *
from django.contrib import admin
from django.urls import path, include
from main import views
app_name = 'main'

urlpatterns = [
    path('upload/', SongUploadView.as_view(), name='upload'),
]
