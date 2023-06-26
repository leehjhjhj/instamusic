import os
import boto3
import youtube_dl
from django.core.files.base import ContentFile
from django.views import View
from django.http import JsonResponse
from .models import Song
from pytube import YouTube
import io
from decouple import config

s3 = boto3.client('s3',
         aws_access_key_id=config('AWS_ACCESS_KEY_ID'),
         aws_secret_access_key= config('AWS_SECRET_ACCESS_KEY'))
bucket_name = 'tuaz'

class SongUploadView(View):
    def post(self, request):
        user = request.user
        thumbnail_file = request.FILES.get('thumbnail')
        name = request.POST.get('name')
        artist = request.POST.get('artist')
        youtube_url = request.POST.get('youtube_url')

        yt = YouTube(youtube_url)
        stream = yt.streams.filter(only_audio=True).first().download(output_path='main')
        mp3_file_path = stream.replace('mp4', 'mp3')
        os.rename(stream, mp3_file_path)
        # S3에 mp3 파일 업로드
        file_name = os.path.basename(mp3_file_path)
        s3_key = 'music/' + file_name
        s3.upload_file(mp3_file_path, bucket_name, s3_key)


        # 업로드된 파일의 URL 설정
        mp3_url = f'https://{bucket_name}.s3.amazonaws.com/{file_name}'

        # 모델에 저장
        song = Song(thumbnail=thumbnail_file, name=name, artist=artist, url=mp3_url)
        song.save()

        # mp3 파일 삭제
        os.remove(mp3_file_path)

        return JsonResponse({'status': 'success'})
