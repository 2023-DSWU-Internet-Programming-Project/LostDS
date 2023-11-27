from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required   # 아이디와 이메일 마이페이지에 가져오기 위해 사용했음
# from django.views.generic import ListView

# Create your views here.
def mypage_view(request):
    # 사용자 정보를 세션에서 가져와서 전달함
    username = request.user.username
    email = request.user.email

    return render(request, 'mypage/mypage.html', {'username':username, 'email':email, })

