from django.db import models

# Create your models here.
class User(models.Model):
    # 유저 이름
    name = models.CharField(max_length=10)

    # 유저가 설정한 닉네임
    nickname = models.CharField(max_length=10)

    # 유저의 이메일
    email = models.CharField(max_length=40)

    # 유저의 프로필 사진(필수x)
    profile_photo = models.ImageField(blank=True)

class Post(models.Model):
    # Post 제목
    title = models.CharField(max_length=30)

    # 물건 사진
    head_image = models.ImageField(upload_to='message/images/find/%Y/%m/%d/', blank=True)

    # Post 내용
    content = models.TextField()

    # 댓글창
