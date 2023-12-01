from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required   # 아이디와 이메일 마이페이지에 가져오기 위해 사용했음
from message.models import AskItem, FindItem, Comment
from django.views.generic import ListView

# Create your views here.
def mypage_view(request):
    # 사용자 정보를 세션에서 가져와서 전달
    username = request.user.username
    email = request.user.email

    return render(request, 'mypage/mypage.html', {'username':username, 'email':email, })

def mypost_view(requset):   # 게시글 리스트 페이지

    return render(
        requset,
        'mypage/my-post.html',
    )

def comment_view(requset):   # 댓글 리스트 페이지

    return render(
        requset,
        'mypage/comment.html',
    )