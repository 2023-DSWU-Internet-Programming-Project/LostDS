from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", mypage_view),
    path("comment-detail/<int:pk>", views.comment_detail, name='comment-detail'),   # 댓글의 상세 페이지
    path("my-post/", mypost_view, name='my-post'),                                  # 내가 쓴 게시글 눌렀을 때 넘어가는 페이지
    path("comment/", comment_view, name='my-comment'),                              # 내가 쓴 댓글 눌렀을 때 넘어가는 페이지
    path("ask-detail/<int:pk>", views.ask_detail, name='ask-detail'),               # 게시글 눌렀을 때 해당 게시글로 넘어감
    path("find-detail/<int:pk>/", views.find_detail, name='find-detail'),
]