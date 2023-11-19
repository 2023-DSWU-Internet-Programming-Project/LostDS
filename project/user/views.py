from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import *
from .forms import *

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('#') #health:main, 로그인이 성공하면 리다이렉트할 위치 적기
        else:
            return render(request, 'user/login.html', {'error': '아이디 또는 비밀번호가 일치하지 않습니다.'})
    else: 
        return render(request, 'user/login.html')


def logout_view(request):
    auth.logout(request)
    return redirect('/login/')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            user = User.objects.create_user(username=username, password=password)
            auth.login(request, user)
            return render(request, 'user/login.html')
        else:
            return render(request, 'user/signup.html', {'error': '비밀번호를 동일하게 입력해주세요.'})
    
    return render(request, 'user/signup.html')