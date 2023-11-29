from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required   # 아이디와 이메일 마이페이지에 가져오기 위해 사용했음
from message.models import AskItem, FindItem, Comment
# from django.views.generic import ListView

# Create your views here.
def mypage_view(request):
    # 사용자 정보를 세션에서 가져와서 전달함
    username = request.user.username
    email = request.user.email

    return render(request, 'mypage/mypage.html', {'username':username, 'email':email, })

def mypost_view(requset):   # 회원가입을 했을때 로그인한 그 유저가 쓴 글만 불러오도록..

    return render(
        requset,
        'mypage/my-post.html',
    )

def comment_view(requset):   # 회원가입을 했을때 로그인한 그 유저가 쓴 글만 불러오도록..

    return render(
        requset,
        'mypage/comment.html',
    )

def ask_detail(request, pk):
    ask_item = get_object_or_404(AskItem, pk=pk)
    return render(request, 'message/askItem_detail.html', {'ask': ask_item})

def find_detail(request, pk):
    find_item = get_object_or_404(FindItem, pk=pk)
    return render(request, 'message/findItem_detail.html', {'find': find_item})

def comment_detail(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    # 댓글이 있는 게시물의 종류에 따라 적절한 상세 페이지로 이동할 수 있게함
    if comment.findPost:
        return render(request, 'message/findItem_detail.html', {'find': comment.findPost})
    elif comment.askPost:
        return render(request, 'message/askItem_detail.html', {'find': comment.askPost})
    else:   # 다른 종류의 게시물이 있다면 그에 맞는 상세 페이지로 이동함
        pass