from django.urls import path
from . import views

urlpatterns = [
    path('find/', views.findList.as_view()),
    path('find/<int:pk>/', views.findDetail.as_view()),
    path('find/category/<str:slug>/', views.category_page_find),
    path('find/create_post/', views.FindPostCreate.as_view()),
    path('find/update_post/<int:pk>/', views.FindPostUpdate.as_view()),
    path('find/delete_post/<int:pk>/', views.FindPostDelete.as_view()),
    path('find/<int:pk>/new_comment/', views.new_comment_find),
    path('find/delete_comment/<int:pk>/', views.delete_comment_find),
    path('ask/', views.askList.as_view()),
    path('ask/<int:pk>/', views.askDetail.as_view()),
    path('ask/category/<str:slug>/', views.category_page_ask),
    path('ask/create_post/', views.AskPostCreate.as_view()),
    path('ask/update_post/<int:pk>/', views.AskPostUpdate.as_view()),
    path('ask/delete_post/<int:pk>/', views.AskPostDelete.as_view()),
    path('ask/<int:pk>/new_comment/', views.new_comment_ask),
    path('ask/delete_comment/<int:pk>/', views.delete_comment_ask),
    path('complete_post/', views.completeList.as_view()),
    path('complete_post/<int:pk>/', views.completeDetail.as_view()),
    path('complete_post/<int:pk>/add/', views.complete_post, name='complete_post'),
    path('complete/category/<str:slug>/', views.category_page_complete),
    path('complete/delete_post/<int:pk>/', views.CompletePostDelete.as_view()),
    path('complete/delete_comment/<int:pk>/', views.delete_comment_complete),
]
