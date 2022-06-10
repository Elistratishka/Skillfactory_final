from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import News
from django.contrib.auth.models import User
from .forms import PostForm, CommentForm
# from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
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


class UserView(DetailView):
    model = User
    context_object_name = 'User'


class PostAdd(CreateView):
    permission_required = ('news.add_post',)
    model = News
    form_class = PostForm
    template_name = 'ads/News_update.html'


class PostEdit(UpdateView):
    permission_required = ('news.change_post',)
    model = News
    form_class = PostForm

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return News.objects.get(pk=pk)


class PostDelete(DeleteView):
    permission_required = ('news.delete_post',)
    model = News
    queryset = News.objects.all()
    success_url = '/news/'


def comment_add(request):
    pass
