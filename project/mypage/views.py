from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import *

# Create your views here.
def mypage_view(requset):
    return render(requset, 'mypage/mypage.html')

# def user_view(requset):
#     return render(requset, 'mypage/user.html')

# class postList(ListView):
#     model = Post
#     ordering = '-pk'
#     template_name = 'mypage/my-post.html'

def mypost_view(requset):   # 회원가입을 했을때 로그인한 그 유저가 쓴 글만 불러오도록..
    posts = Post.objects.all().order_by('-pk')  # 데이터베이스에 있는 내용들 가져옴
    return render(
        requset,
        'mypage/my-post.html',
        {
            'posts': posts,
        }
    )

# class commentList(ListView):
#     model = Post
#     ordering = '-pk'
#     template_name = 'mypage/comment.html'

def comment_view(requset):
    return render(requset, 'mypage/comment.html')