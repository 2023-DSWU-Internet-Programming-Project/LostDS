from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", mypage_view),
    path("my-post/", mypost_view, name='my-post'),                                  # '내가 쓴 게시글' 눌렀을 때 넘어가는 페이지
    path("comment/", comment_view, name='my-comment'),                              # '내가 쓴 댓글' 눌렀을 때 넘어가는 페이지
]