from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

class User(AbstractUser):
    first_name = None
    last_name = None
    email = None
    username = models.EmailField(unique=True, verbose_name="이메일",)
