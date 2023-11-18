from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

class findList(ListView):
    model = FindItem
    ordering = '-pk'
    template_name = 'message/findItem_list.html'

class findDetail(DetailView):
    model = FindItem
    template_name = 'message/findItem_detail.html'
    # 컨텍스트 객체 이름 지정
    context_object_name = 'find'
class askList(ListView):
    model = AskItem
    ordering = '-pk'
    template_name = 'message/askItem_list.html'

class askDetail(DetailView):
    model = AskItem
    template_name = 'message/askItem_detail.html'

class completeList(ListView):
    model = CompleteItem
    template_name = 'message/completeItem.html'

def complete_post(request, pk):
    post = get_object_or_404(FindItem, pk=pk)
    
    # author 속성을 만들었을 때 추후 추가할 if문. 현재 로그인 유저 == 작성자일 경우 버튼을 누를 수 있게하기 위함.
    # if post.user == request.user:
    completed_post = completeList.model(title=post.title, content=post.content)
    completed_post.save()

    post.delete()

    # '완료' 버튼 클릭 시 완료 처리된 게시글들의 목록을 보여주기 위함
    return redirect('../')
