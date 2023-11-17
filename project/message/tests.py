from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_findItem_list(self):
        # 포스트 페이지 로드
        response = self.client.get('/message/')
        # 페이지 정상 동작 확인
        self.assertEqual(response.status_code, 200)
        # 페이지 타이틀 == "분실물 찾아가세요!"
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, '분실물 찾아가세요!')
        # 게시물 1개 생성
        post = Post.objects.create(
            title='첫 분실물',
            content='찾아가세요'
        )
        # 포스트가 1개 존재하는지
        self.assertEqual(Post.objects.count(), 1)
