from django.db import models
# from django.contrib.auth.models import User
from message.models import FindItem, AskItem, CompleteItem, Comment
#
from django.conf import settings
#
#
# # Create your models here.
# class UserProfile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     nickname = models.CharField(max_length=20, blank=True)
#     profile_photo = models.ImageField(upload_to='mypage/profiles/', blank=True)
#
#     def __str__(self):
#         return self.user.username
#
class UserPost(models.Model):       # message 앱의 FindItem, AskItem, CompleteItem 모델과 관련이 있음
    # 사용자(user)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # 게시글 제목
    title = models.CharField(max_length=30)

    # 게시글에서 사용된 이미지
    head_image = models.ImageField(upload_to='message/images/find/%Y/%m/%d/', blank=True)

    # 게시글 내용
    content = models.TextField()

    # 게시글 생성일
    created_at = models.DateTimeField()

    def __str__(self):
        return f'{self.user.username}::{self.title}'

class UserComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    find_post = models.ForeignKey(FindItem, on_delete=models.CASCADE, null=True, blank=True)
    ask_post = models.ForeignKey(AskItem, on_delete=models.CASCADE, null=True, blank=True)
    complete_post = models.ForeignKey(CompleteItem, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}::{self.content}'