from django.urls import path
from . import views
from .views import *

from django.conf import settings
from django.conf.urls.static import static

# 아래 주석은 확인 시 삭제 부탁드려요!
# message/find/ 및 message/ask url은 이미 message 앱 내의 urls.py에서 정의되었기 때문에 여기서 다시 등록하게 되면 중복 url 패턴을 갖게 됩니다!
# 중복된 url 패턴을 가지면 어떤 views를 불러와야 하는지 혼동이 발생해 오류가 생겨 정상 출력되지 않습니다.
# includes를 사용하여 타 앱의 url을 불러오거나 html 파일의 href 속성에 직접 url을 입력해주는 방법이 있습니다!
# 오류로 인해 우선 후자의 방식을 써서 제가 임의로 수정했는데 편하신대로 수정해주세요!

urlpatterns = [
    path('', views.connect),
    path('login/', views.login, name='login'),
    # path('message/', views.found, name='found'),
    # path('message/ask/', views.find, name='find'),
    # path('mypage/', views.mypage, name='mypage')
    path('signup/', views.info, name='info')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
