from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView

class findList(ListView):
    model = FindItem
    ordering = '-pk'
    template_name = 'message/findItem_list.html'

    def get_context_data(self, **kwargs):
        context = super(findList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = FindItem.objects.filter(category=None).count()
        return context

class findDetail(DetailView):
    model = FindItem
    template_name = 'message/findItem_detail.html'
    # 컨텍스트 객체 이름 지정
    context_object_name = 'find'

class FindPostCreate(CreateView):
    model = FindItem
    fields = ['title', 'content', 'head_image', 'category']

class askList(ListView):
    model = AskItem
    ordering = '-pk'
    template_name = 'message/askItem_list.html'

class askDetail(DetailView):
    model = AskItem
    template_name = 'message/askItem_detail.html'
    # 컨텍스트 객체 이름 지정
    context_object_name = 'ask'

class AskPostCreate(CreateView):
    model = AskItem
    fields = ['title', 'content', 'head_image', 'category']

class completeList(ListView):
    model = CompleteItem
    template_name = 'message/completeItem_list.html'

class completeDetail(DetailView):
    model = CompleteItem
    template_name = 'message/completeItem_detail.html'
    # 컨텍스트 객체 이름 지정
    context_object_name = 'complete'

class CompletePostCreate(CreateView):
    model = CompleteItem
    fields = ['title', 'content', 'head_image', 'category']

def complete_post(request, pk):
    post = get_object_or_404(FindItem, pk=pk)
    
    # author 속성을 만들었을 때 추후 추가할 if문. 현재 로그인 유저 == 작성자일 경우 버튼을 누를 수 있게하기 위함.
    # if post.user == request.user:
    completed_post = completeList.model(
        title=post.title,
        content=post.content,
        created_at=post.created_at)
    completed_post.save()

    post.delete()

    # '완료' 버튼 클릭 시 완료 처리된 게시글들의 목록을 보여주기 위함
    return redirect('../')
