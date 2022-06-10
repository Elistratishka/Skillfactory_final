from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import News, Comment
from django.contrib.auth.models import User
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import logging


logger = logging.getLogger(__name__)


class PostList(ListView):
    model = News
    context_object_name = 'posts'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)


class PostView(DetailView):
    model = News
    context_object_name = 'post'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)


class UserView(DetailView, LoginRequiredMixin):
    model = User
    context_object_name = 'User'


class PostAdd(CreateView, LoginRequiredMixin):
    model = News
    form_class = PostForm
    template_name = 'ads/News_update.html'


class PostEdit(UpdateView, LoginRequiredMixin):
    model = News
    form_class = PostForm

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return News.objects.get(pk=pk)


class PostDelete(DeleteView, LoginRequiredMixin):
    permission_required = ('news.delete_post',)
    model = News
    queryset = News.objects.all()
    success_url = '/news/'


@login_required()
def comment_add(request, pk):
    user = request.user
    post = News.objects.get(pk=pk)
    text = request.POST['text']
    Comment.objects.create(commentator=user, news=post, text=text)
    return redirect('detail', pk)


def comment_commit(request, pk):
    user = request.user
    comment = Comment.objects.get(pk=pk)
    comment.commit = True
    comment.save()
    return redirect('user', user.id)


def comment_delete(request, pk):
    user = request.user
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return redirect('user', user.id)
