import boto3
from django.views import View
from django.http import JsonResponse
from .models import Song
from pytube import YouTube
import io
from decouple import config
from django.shortcuts import redirect

s3 = boto3.client('s3',
          aws_access_key_id=config('AWS_ACCESS_KEY_ID'),
          aws_secret_access_key= config('AWS_SECRET_ACCESS_KEY'))
bucket_name = 'tuaz'

class SongUploadView(View):
    def post(self, request):
        user = self.request.user
        thumbnail_file = request.FILES.get('thumbnail')
        name = request.POST.get('name')
        artist = request.POST.get('artist')
        youtube_url = request.POST.get('youtube_url')

        yt = YouTube(youtube_url)
        stream = yt.streams.filter(only_audio=True).first()

        # mp3 스트림을 메모리 버퍼로 변환
        buffer = io.BytesIO()
        stream.stream_to_buffer(buffer)
        buffer.seek(0)

        # S3에 mp3 파일 업로드
        s3_key = f'music/{self.request.user.username}/' + stream.default_filename.replace('mp4', 'mp3')
        s3.upload_fileobj(buffer, bucket_name, s3_key)

        # 업로드된 파일의 URL 설정
        mp3_url = f'https://{bucket_name}.s3.amazonaws.com/{s3_key}'

        # 모델에 저장
        song = Song(user=user, thumbnail=yt.thumbnail_url, name=name, artist=artist, url=mp3_url)
        song.save()

        return redirect('set')
    
