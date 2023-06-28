from .views import *
from django.urls import path
app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('duplicate/', check_email_duplication, name='duplicate')
]