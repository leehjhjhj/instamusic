from django.db import models
from accounts.models import User

# Create your models here.
class Song(models.Model):
    user = models.ForeignKey(User,related_name='song_user', on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=20)
    artist = models.CharField(max_length=20)
    thumbnail = models.ImageField(upload_to='music_thumbnails/', null=True)
    url = models.CharField(max_length=256)