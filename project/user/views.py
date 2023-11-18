from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def login_view(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("#") # 로그인이 성공하면 리다이렉트할 위치 적기
        else:
            # 로그인에 실패하였을 경우의 처리
            return render(request, 'user/login.html', {'error': '아이디 또는 비밀번호가 일치하지 않습니다.'})

    return render(request, 'user/login.html')

def logout_view(request):
    logout(request)
    return redirect("/login/")