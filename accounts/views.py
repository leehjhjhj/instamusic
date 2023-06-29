from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .models import *
import re
from django.http import JsonResponse

def login_view(request):
  if request.method == 'GET':
    return render(request, 'login.html')
  
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(
        request=request,
        username=username,
        password=password
    )
    if user is not None:
        login(request, user)
        return redirect('main', username=username)
    return render(request, 'login.html', {'message': '아이디나 비밀번호를 다시 한번 확인해주십시오.'})


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        errors = {}
        if not re.match(r'^[a-zA-Z0-9_.]', username):
            errors['email'] = '아이디는 영어와 숫자만 가능합니다.'
        if password != password2:
           errors['password'] = '비밀번호가 일치하지 않습니다.'

        if errors:
            return render(request, 'register.html', {'errors': errors})
        

        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()

        return render(request, 'login.html', {'message': '가입을 축하합니다. 로그인해주세요!'})
    else:
        return render(request, 'register.html', {'error': 'Invalid request method.'})

def logout_view(request):
	logout(request)
	return redirect('main')

def check_email_duplication(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        if not re.match(r'^[a-zA-Z0-9_.]', username):
            print('형식 에러')
            return JsonResponse({'duplicated': 'error'})
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'duplicated': True})
        else:
            return JsonResponse({'duplicated': False})
    else:
        return render(request, 'register.html', {'error': 'Invalid request method.'})