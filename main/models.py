from django.db import models
from accounts.models import User

# Create your models here.
class Song(models.Model):
    user = models.ForeignKey(User,related_name='song_user', on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=128)
    artist = models.CharField(max_length=128)
    thumbnail = models.CharField(max_length=256, null=True)
    url = models.CharField(max_length=256)