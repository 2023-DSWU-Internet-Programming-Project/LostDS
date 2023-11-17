from django.db import models

class FindItem(models.Model):
    # 포스트 제목
    title = models.CharField(max_length=20)

    # 포스트 생성일
    created_at = models.DateTimeField(auto_now_add=True)

    # 포스트 카테고리

    # 사진 업로드

    # 포스트 내용
    content = models.TextField()

    # 댓글

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'/message/{self.pk}/'


class AskItem(models.Model):
    # 포스트 제목
    title = models.CharField(max_length=20)

    # 포스트 생성일
    created_at = models.DateTimeField(auto_now_add=True)

    # 포스트 카테고리

    # 사진 업로드

    # 포스트 내용
    content = models.TextField()

    # 댓글

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'/message/ask/{self.pk}/'

class CompleteItem(models.Model):
    # 포스트 제목
    title = models.CharField(max_length=20)

    # 포스트 생성일
    created_at = models.DateTimeField(auto_now_add=True)

    # 포스트 카테고리

    # 사진 업로드

    # 포스트 내용
    content = models.TextField()

    # 댓글

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'/message/complete/{self.pk}/'
