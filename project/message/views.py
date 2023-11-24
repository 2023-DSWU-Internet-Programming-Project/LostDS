from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import CommentForm
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
        context['comment_form'] = CommentForm
        return context


# 습득물 페이지 게시글 생성 뷰
class FindPostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = FindItem
    fields = ['title', 'category', 'head_image', 'content']
    template_name = 'message/findItem_form.html'
    context_object_name = 'find'

    def test_func(self):
        return self.request.user.is_authenticated

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
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
        if (request.user.is_authenticated and
                (request.user == self.get_object().author or request.user.is_superuser or request.user.is_staff)):
            return super(FindPostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


# 습득물 페이지 게시글 삭제 뷰
class FindPostDelete(LoginRequiredMixin, DeleteView):
    model = FindItem
    success_url = '/message/find/'
    context_object_name = 'find'

    def dispatch(self, request, *args, **kwargs):
        if (request.user.is_authenticated and
                (request.user == self.get_object().author or request.user.is_superuser or request.user.is_staff)):
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
        context['comment_form'] = CommentForm
        return context


# 분실물 페이지 게시글 생성 뷰
class AskPostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = AskItem
    fields = ['title', 'category', 'head_image', 'content']
    template_name = 'message/askItem_form.html'
    context_object_name = 'ask'

    def test_func(self):
        return self.request.user.is_authenticated

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

    def dispatch(self, request, *args, **kwargs):
        if (request.user.is_authenticated and
                (request.user == self.get_object().author or request.user.is_superuser or request.user.is_staff)):
            return super(AskPostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


# 분실물 페이지 게시글 삭제 뷰
class AskPostDelete(LoginRequiredMixin, DeleteView):
    model = AskItem
    success_url = '/message/ask/'
    context_object_name = 'ask'

    def dispatch(self, request, *args, **kwargs):
        if (request.user.is_authenticated and 
            (request.user == self.get_object().author or request.user.is_superuser or request.user.is_staff)):
            return super(AskPostDelete, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


# 완료 처리된 페이지 리스트 뷰
class completeList(ListView):
    model = CompleteItem
    ordering = '-pk'
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
    success_url = '/message/complete_post/'
    context_object_name = 'complete'

    def dispatch(self, request, *args, **kwargs):
        if (request.user.is_authenticated and
                (request.user == self.get_object().author or request.user.is_superuser or request.user.is_staff)):
            return super(CompletePostDelete, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


# 완료 버튼을 누를 시 FindItem 모델의 데이터가 CompleteItem 모델로 이동
def complete_post(request, pk):
    post = get_object_or_404(FindItem, pk=pk)

    # 권한이 있는 사람만 완료 버튼을 누를 수 있도록 수정 예정
    completed_post = completeList.model(
        title=post.title,
        author=post.author,
        created_at=post.created_at,
        category=post.category,
        head_image=post.head_image,
        content=post.content
    )

    completed_post.save()

    comments = Comment.objects.filter(findPost=post)
    for comment in comments:
        Comment.objects.create(
            completePost=completed_post,
            author=comment.author,
            content=comment.content,
            created_at=comment.created_at
        )

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


def new_comment_find(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(FindItem, pk=pk)

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.findPost = post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url_find())
        else:
            return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied


def new_comment_ask(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(AskItem, pk=pk)

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.askPost = post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url_ask())
        else:
            return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied

# 댓글 삭제
def delete_comment_find(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.findPost
    if request.user.is_authenticated:
        if request.user == comment.author or request.user.is_superuser or request.user.is_staff:
            comment.delete()
            return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied
    

def delete_comment_ask(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.askPost
    if request.user.is_authenticated and request.user == comment.author:
        comment.delete()
        return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied
    

def delete_comment_complete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.completePost
    if request.user.is_authenticated and request.user == comment.author:
        comment.delete()
        return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied

