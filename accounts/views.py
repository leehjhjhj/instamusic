from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .models import *
import re
from django.http import JsonResponse

def login_view(request):
  if request.method == 'GET':
    return render(request, 'login.html')
  
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(
        request=request,
        username=email,
        password=password
    )
    if user is not None:
        login(request, user)
        return redirect('index')
    return render(request, 'login.html', {'message': '이메일이나 비밀번호를 다시 한번 확인해주십시오.'})


def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        errors = {}
        if not re.match(r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+$', email):
            errors['email'] = '이메일은 영문 대소문자, 숫자, 언더바(_), ".", "@"만 가능합니다.'
        if password != password2:
           errors['password'] = '비밀번호가 일치하지 않습니다.'

        if errors:
            return render(request, 'register.html', {'errors': errors})
        

        user = User.objects.create(username=email)
        user.set_password(password)
        user.save()

        return render(request, 'login.html', {'message': '가입을 축하합니다. 로그인해주세요!'})
    else:
        return render(request, 'register.html', {'error': 'Invalid request method.'})

def logout_view(request):
	logout(request)
	return render(request, 'login.html')

def check_email_duplication(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not re.match(r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+$', email):
            return JsonResponse({'duplicated': 'error'})
        
        if User.objects.filter(username=email).exists():
            return JsonResponse({'duplicated': True})
        else:
            return JsonResponse({'duplicated': False})
    else:
        return render(request, 'register.html', {'error': 'Invalid request method.'})