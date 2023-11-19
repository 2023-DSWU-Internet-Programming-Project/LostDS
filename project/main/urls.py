from django.urls import path
from . import views
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.connect),
    path('login/', views.login, name='login'),
    path('message/', views.found, name='found'),
    path('message/', views.find, name='find')
    # path('mypage/', views.mypage, name='mypage')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
