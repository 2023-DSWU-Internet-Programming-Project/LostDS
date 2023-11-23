
from django.shortcuts import render, redirect
from .models import *
from . import *
from django.contrib.auth.decorators import login_required


# Create your views here.

def connect(request):
    return render(
        request,
        'main/connect.html'
    )

def login(request):
    return render(
        request, 'user/login.html'
    )

def found(request):
    return render(
        request,'message/findItem_list.html'
    )

def find(request):
    return render(
        request,'message/askItem_list.html'
    )

@login_required
def mypage(request):
    return render(
        request,'mypage/mypage.html'
    )

def info(request):
    return render(
        request,'user/signup.html'
    )