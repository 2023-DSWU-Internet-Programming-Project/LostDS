from django.urls import path
from . import views

urlpatterns = [
    path('', views.findList.as_view()),
    path('<int:pk>/', views.findDetail.as_view()),
    path('ask/', views.askList.as_view()),
    path('ask/<int:pk>/', views.askDetail.as_view()),
    path('complete_post/', views.completeList.as_view()),
    path('complete_post/<int:pk>/', views.complete_post, name='complete_post'),
]
