from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.exceptions import PermissionDenied

# 습득물 페이지 리스트 뷰
class findList(ListView):
    model = FindItem
    ordering = '-pk'
    template_name = 'message/findItem_list.html'

    def get_context_data(self, **kwargs):
        context = super(findList, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context

# 습득물 페이지 디테일 뷰
class findDetail(DetailView):
    model = FindItem
    template_name = 'message/findItem_detail.html'
    # 컨텍스트 객체 이름 지정
    context_object_name = 'find'

    def get_context_data(self, **kwargs):
        context = super(findDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context

# 습득물 페이지 게시글 생성 뷰
class FindPostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = FindItem
    fields = ['title', 'category', 'head_image', 'content']
    template_name = 'message/findItem_form.html'
    context_object_name = 'find'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(FindPostCreate, self).form_valid(form)
        else:
            return redirect('/message/find/')

# 습득물 페이지 게시글 수정 뷰
class FindPostUpdate(LoginRequiredMixin, UpdateView):
    model = FindItem
    fields = ['title', 'category', 'head_image', 'content']
    template_name = 'message/findItem_update_form.html'
    context_object_name = 'find'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(FindPostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

# 습득물 페이지 게시글 삭제 뷰
class FindPostDelete(LoginRequiredMixin, DeleteView):
    model = FindItem
    success_url = '/message/find/'
    context_object_name = 'find'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(FindPostDelete, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

# 분실물 페이지 리스트 뷰
class askList(ListView):
    model = AskItem
    ordering = '-pk'
    template_name = 'message/askItem_list.html'

    def get_context_data(self, **kwargs):
        context = super(askList, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context

# 분실물 페이지 디테일 뷰
class askDetail(DetailView):
    model = AskItem
    template_name = 'message/askItem_detail.html'
    # 컨텍스트 객체 이름 지정
    context_object_name = 'ask'

    def get_context_data(self, **kwargs):
        context = super(askDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context

# 분실물 페이지 게시글 생성 뷰
class AskPostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = AskItem
    fields = ['title', 'category', 'head_image', 'content']
    template_name = 'message/askItem_form.html'
    context_object_name = 'ask'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(AskPostCreate, self).form_valid(form)
        else:
            return redirect('/message/ask/')

# 분실물 페이지 게시글 수정 뷰
class AskPostUpdate(LoginRequiredMixin, UpdateView):
    model = AskItem
    fields = ['title', 'category', 'head_image', 'content']
    template_name = 'message/askItem_update_form.html'
    context_object_name = 'ask'

# 분실물 페이지 게시글 삭제 뷰
class AskPostDelete(LoginRequiredMixin, DeleteView):
    model = AskItem
    success_url = '/message/ask/'
    context_object_name = 'ask'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(AskPostDelete, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

# 완료 처리된 페이지 리스트 뷰
class completeList(ListView):
    model = CompleteItem
    template_name = 'message/completeItem_list.html'

    def get_context_data(self, **kwargs):
        context = super(completeList, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context

# 완료 처리된 페이지 디테일 뷰
class completeDetail(DetailView):
    model = CompleteItem
    template_name = 'message/completeItem_detail.html'
    # 컨텍스트 객체 이름 지정
    context_object_name = 'complete'

    def get_context_data(self, **kwargs):
        context = super(completeDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context

# 완료 처리된 페이지 게시글 삭제 뷰
class CompletePostDelete(LoginRequiredMixin, DeleteView):
    model = CompleteItem
    success_url = '/message/complete/'
    context_object_name = 'complete'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(CompletePostDelete, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

# 완료 버튼을 누를 시 FindItem 모델의 데이터가 CompleteItem 모델로 이동
def complete_post(request, pk):
    post = get_object_or_404(FindItem, pk=pk)
    
    # author 속성을 만들었을 때 추후 추가할 if문. 현재 로그인 유저 == 작성자일 경우 버튼을 누를 수 있게하기 위함.
    # if post.user == request.user:
    completed_post = completeList.model(
        title=post.title,
        author=post.author,
        created_at=post.created_at,
        category=post.category,
        head_image=post.head_image,
        content=post.content
    )
    completed_post.save()

    post.delete()

    return redirect('../../')

def category_page_find(request, slug):
    category = Category.objects.get(slug=slug)

    return render(
        request,
        'message/findItem_list.html',
        {
            'object_list': FindItem.objects.filter(category=category),
            'categories': Category.objects.all(),
            'category': category
        }
    )

def category_page_complete(request, slug):
    category = Category.objects.get(slug=slug)

    return render(
        request,
        'message/completeItem_list.html',
        {
            'object_list': CompleteItem.objects.filter(category=category),
            'categories': Category.objects.all(),
            'category': category
        }
    )

def category_page_ask(request, slug):
    category = Category.objects.get(slug=slug)

    return render(
        request,
        'message/askItem_list.html',
        {
            'object_list': AskItem.objects.filter(category=category),
            'categories': Category.objects.all(),
            'category': category
        }
    )
