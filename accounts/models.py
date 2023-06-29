from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

class User(AbstractUser):
    first_name = None
    last_name = None
    username = models.CharField(max_length=20, unique=True, verbose_name="아이디",)
