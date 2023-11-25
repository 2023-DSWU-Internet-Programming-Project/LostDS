from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.conf import settings

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')  
        password = request.POST.get('password')  
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'user/login.html', {'error_message': '아이디 또는 비밀번호가 일치하지 않습니다.'})
    else: 
        return render(request, 'user/login.html')


def logout_view(request):
    auth.logout(request)
    return redirect('/')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        password = request.POST.get('password')  
        password2 = request.POST.get('password2')  
        email = request.POST.get('email')

        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'user/signup.html', {'error_message': '이미 존재하는 아이디입니다.'})

        if password == password2:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, get_verification_token=get_random_string(length=32), is_active=False)
            user.save()
            send_verification_email(email, user.get_verification_token) 
            return render(request, 'user/verification.html')
        else:
            return render(request, 'user/signup.html', {'error_message': '비밀번호를 동일하게 입력해주세요.'})

    return render(request, 'user/signup.html')

def send_verification_email(email, verification_token):
    subject = '이메일 인증'
    message = f'회원가입을 완료하기 위해 이메일을 인증해주세요. 인증 토큰: {verification_token}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)

def verification_view(request):
    if request.method == 'POST':
        verification_token = request.POST.get('verification_token')
        try:
            user = CustomUser.objects.get(get_verification_token=verification_token)
            user.is_active = True
            user.save()
            return redirect('user:login')
        except CustomUser.DoesNotExist:
            return render(request, 'user/verification.html', {'error_message': '인증 토큰이 잘못되었습니다.'})
    else: 
        return render(request, 'user/verification.html')
