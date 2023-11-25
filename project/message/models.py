from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=10, unique=True)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)
    head_image = models.ImageField(upload_to='message/images/category/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url_find(self):
        return f'/message/find/category/{self.slug}/'

    def get_absolute_url_complete(self):
        return f'/message/complete/category/{self.slug}/'

    def get_absolute_url_ask(self):
        return f'/message/ask/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories'


class FindItem(models.Model):
    # 포스트 제목
    title = models.CharField(max_length=20)

    # 작성자
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    # 포스트 생성일
    created_at = models.DateTimeField(auto_now_add=True)

    # 포스트 카테고리
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    # 사진 업로드
    head_image = models.ImageField(upload_to='message/images/find/%Y/%m/%d/', blank=True)

    # 포스트 내용
    content = models.TextField()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'/message/find/{self.pk}/'


class AskItem(models.Model):
    # 포스트 제목
    title = models.CharField(max_length=20)

    # 작성자
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    # 포스트 생성일
    created_at = models.DateTimeField(auto_now_add=True)

    # 포스트 카테고리
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    # 사진 업로드
    head_image = models.ImageField(upload_to='message/images/ask/%Y/%m/%d/', blank=True)

    # 포스트 내용
    content = models.TextField()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'/message/ask/{self.pk}/'


class CompleteItem(models.Model):
    # 포스트 제목
    title = models.CharField(max_length=20)

    # 작성자
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    # 포스트 생성일
    created_at = models.DateTimeField()

    # 포스트 카테고리
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    # 사진 업로드
    head_image = models.ImageField(upload_to='message/images/complete/%Y/%m/%d/', blank=True)

    # 포스트 내용
    content = models.TextField()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'/message/complete_post/{self.pk}/'

class Comment(models.Model):
    findPost = models.ForeignKey(FindItem, on_delete=models.CASCADE, null=True, blank=True)
    askPost = models.ForeignKey(AskItem, on_delete=models.CASCADE, null=True, blank=True)
    completePost = models.ForeignKey(CompleteItem, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url_find(self):
        return f'{self.findPost.get_absolute_url()}#comment-{self.pk}'

    def get_absolute_url_ask(self):
        return f'{self.askPost.get_absolute_url()}#comment-{self.pk}'
