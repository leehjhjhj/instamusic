from django.shortcuts import render, get_object_or_404
from .models import *
from django.views import View
from django.core.serializers import serialize

class SetView(View):
    def get(self, request):
        playlist = Song.objects.filter(user=self.request.user)
        context = {
            'playlist': playlist,
        }
        return render(request, 'set.html', context)
    
class MainView(View):
    def get(self, request, username):
        playlist = Song.objects.filter(user__username=username)
        playlist_data = serialize('json', playlist)
        context = {
            'playlist': playlist_data,
        }
        return render(request, 'main.html', context)