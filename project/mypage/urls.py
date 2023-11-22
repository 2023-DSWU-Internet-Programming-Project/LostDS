from django.urls import path
from .views import *

urlpatterns = [
    path("", mypage_view),
    # path("user/", user_view),
    path("my-post/", mypost_view),
    path("comment/", comment_view),
    # path("my-post/", views.postList.as_view),
    # path("comment/", views.commentList.as_view),
]
